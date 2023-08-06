from sys import platform
import requests
import pandas as pd
import os
import json
from urllib.parse import urlparse
from typing import List

# Async
import asyncio
from functools import wraps, partial


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 


class Vv:
    def __init__(self):
        self.vaultURL = None
        self.vaultUserName = None
        self.vaultPassword = None
        self.vaultConnection = None
        self.sessionId = None
        self.vaultId: str = None
        self.vaultDNS: str = None
        self.APIheaders = None
        self.APIversionList = []
        self.LatestAPIversion = 'v21.3'
#         self.vaultObjects = None
#         self.all_references_metadata = None
#         self.all_references_names = None
#         self.vault_references_all = None



    def authenticate(self, 
                     vaultURL=None, 
                     vaultUserName=None, 
                     vaultPassword=None, 
                     sessionId=None,
                     vaultId=None,
                     if_return=False, *args, **kwargs):
        """
        TODO: Docs
        """

        
        self.vaultURL = self.vaultURL if vaultURL is None else vaultURL
        self.vaultUserName = self.vaultUserName if vaultUserName is None else vaultUserName
        self.vaultPassword = self.vaultPassword if vaultPassword is None else vaultPassword
        self.sessionId = self.sessionId if sessionId is None else sessionId
        self.vaultId = self.vaultId if vaultId is None else vaultId
        
        url_parse = urlparse(self.vaultURL)
        if len(url_parse.scheme) == 0:
            self.network_protocol = 'https'
            if len(url_parse.path) > 0:
                self.vaultDNS = url_parse.path
                self.vaultURL = self.network_protocol + '://' + url_parse.path

        if len(url_parse.scheme) > 0:
            self.network_protocol = url_parse.scheme
            if len(url_parse.netloc) > 0:
                self.vaultDNS = url_parse.netloc
                self.vaultURL = url_parse.scheme + '://' + url_parse.netloc

        if (self.vaultURL is None) or (len(self.vaultURL) == 0):
            raise Exception('vaultURL is required')
        
        if (self.vaultUserName and self.vaultPassword and self.vaultURL):
            pload = {'username': self.vaultUserName,'password': self.vaultPassword}
            self.vaultConnection = requests.post(f'{self.vaultURL}/api/{self.LatestAPIversion}/auth',data = pload)
            if self.vaultConnection.json()['responseStatus'] == 'FAILURE':
                exceptionMessage = ""
                exceptionMessage += "Error: " + self.vaultConnection.json()['responseMessage'] + "\n"
                exceptionMessage += self.vaultConnection.json()['errorType'] + "\n"
                for error in self.vaultConnection.json()['errors']:
                    exceptionMessage += error['type'] + ": " + error['message'] + "\n"
                raise Exception(exceptionMessage)
            
            self.sessionId = self.vaultConnection.json()['sessionId']
            self.vaultId = self.vaultConnection.json()['vaultId']
            
        self.APIheaders = {'Authorization': self.sessionId}
        self.APIversionList = []
        
        # Error checking whether the required parameters are passed in
        # The check happens here because this is where all the self assignments has completed
        if (not (self.vaultId and self.sessionId and self.vaultURL)) and (not (self.vaultUserName and self.vaultPassword and  self.vaultURL)):
            raise Exception("Please provide either vaultId, sessionId and vaultURL or vaultUserName, vaultPassword and vaultURL")
        
        for API in requests.get(self.vaultURL +'/api', headers=self.APIheaders).json()['values'].keys():
            self.APIversionList.append(float(API.replace("v", "")))
        self.APIversionList.sort()
        self.LatestAPIversion = "v" + str(self.APIversionList[-1])
        
        if if_return:
            return {'vaultURL':self.vaultURL, 
                    'vaultUserName':self.vaultUserName, 
                    'vaultPassword':self.vaultPassword, 
                    'vaultConnection':self.vaultConnection, 
                    'sessionId':self.sessionId, 
                    'APIheaders':self.APIheaders, 
                    'APIversionList':self.APIversionList, 
                    'LatestAPIversion':self.LatestAPIversion}
            
            
    def query(self, query):
        url = f"{self.vaultURL}/api/{self.LatestAPIversion}/query"
        
        h = {
        "X-VaultAPI-DescribeQuery":"true",
        "Content-Type":"application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Authorization": self.sessionId
        }
        params = {
        "q":query
        }

        r = pd.DataFrame(requests.get(url, headers=h, params=params).json()['data'])
        
        return r
    
    def bulk_query(self, query):
        url = f"{self.vaultURL}/api/{self.LatestAPIversion}/query"
        
        h = {
        "X-VaultAPI-DescribeQuery":"true",
        "Content-Type":"application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Authorization": self.sessionId
        }
        params = {
        "q":query
        }

        r = requests.get(url, headers=h, params=params).json()
        
        output = pd.DataFrame(r['data'])
        
        try:
            next_page_url = r['responseDetails']['next_page'][:-4]
            more_pages = True
            page_count = 1000
            
            while more_pages:
                r = pd.DataFrame(requests.get(f"{self.vaultURL}"+ next_page_url+ str(page_count), headers=h).json()['data'])
                if len(r) == 0:
                    more_pages = False
                else:
                    output = pd.concat([output,r],ignore_index=True).copy()
                    page_count += 1000
        except:
            pass
        
        return output
    
    def object_field_metadata(self, object_api_name):
        url = f"{self.vaultURL}/api/{self.LatestAPIversion}/metadata/vobjects/{object_api_name}"
        r = requests.get(url, headers = self.APIheaders).json()['object']['fields']
        return pd.DataFrame(r)
    
    def describe_objects(self):
        url = f"{self.vaultURL}/api/{self.LatestAPIversion}/metadata/vobjects"
        r = requests.get(url, headers = self.APIheaders).json()['objects']
        return pd.DataFrame(r).sort_values(by='name')
    
    def retrieve_picklist_values(self, picklist_name):
        """
        Note: This is not the picklist field's API name, but the picklist (to which the picklist field looks up to) API name.
        For example, the picklist field "specialty_1__v", "specialty_2__v" and "specialty_3__v" all look up to the picklist "specialty__v".
        """
        url = f"{self.vaultURL}/api/{self.LatestAPIversion}/objects/picklists/{picklist_name}"
        r = requests.get(url, headers = self.APIheaders).json()
        if r['responseStatus'] == 'SUCCESS':
            if 'picklistValues' in r.keys():
                result = pd.DataFrame(r['picklistValues'])
                result['picklist_api_name'] = picklist_name
                return result
            else:
                print(f"Warning: Picklist {picklist_name} does not contain any values.")
                result = pd.DataFrame(columns=['name','label','picklist_api_name'])
                return result
        else:
            raise Exception(r['errors'][0]['type'] + ": " + r['errors'][0]['message'])
    
    async def async_bulk_retrieve_picklist_values(self, queries: List[str]) -> pd.DataFrame:
        """_summary_: This function is the async version of the retrieve_picklist_values function. It is used to retrieve multiple picklist values in parallel.

        Args:
            queries (List[str]): List of picklist API names

        Returns:
            _type_: pd.DataFrame
        """
        async_queries = async_wrap(self.retrieve_picklist_values)
        result_list = await asyncio.gather(*[async_queries(query) for query in queries])
        result_length = 0
        for result in result_list:
            result_length += len(result)
        
        if result_length > 0:
            result = pd.concat(result_list, ignore_index=True)
        else:
            result = pd.DataFrame(columns=['name','label','picklist_api_name'])
            
        return result
        