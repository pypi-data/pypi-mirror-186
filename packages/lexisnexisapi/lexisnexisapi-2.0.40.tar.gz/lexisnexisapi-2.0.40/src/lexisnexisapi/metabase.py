import requests
import json
import pandas as pd
from datetime import datetime
from lexisnexisapi import credentials
from multipledispatch import dispatch

__version__ = '0.1'
__author__ = "Robert Cuffney & Ozgur Aycan, CS Integration Specialists @ LexisNexis"

#Constants are usually defined on a module level and written in all capital letters with underscores separating words. 
#Examples include MAX_OVERFLOW and TOTAL.

#url = 'http://metabase.moreover.com/api/v10/searchArticles?'

METABASE_SEARCH_URL = 'http://metabase.moreover.com/api/v10/searchArticles?'
METABASE_RATE_CHECK_URL = 'https://metabase.moreover.com/api/v10/rateLimits?key='

##Function names should be lowercase, with words separated by underscores as necessary to improve readability.
##Class names should normally use the CapWords convention.  CapitalizedWords 
class MbSearch:
    '''
    mbSearch class
    returns API response as a python class
    accepts either a string query, or a dictionary of all metabase parameters
    full_dataset = True -- activates the option to create a full dataset of total results 
    '''
    def __init__(self, parameters, full_dataset = False):
        self.parameters = self.set_parameters(parameters)
        if full_dataset:
            print('Full Dataset, this function is under construction')
            data = self.get_fulldataset()
            print(data['totalResults'])
        else:
            data = http_request(self.parameters)
        if type(data)==dict:
            self.__dict__.update(data)
        else:
            print("Something went wrong, No data was returned")
        print(f'Class instance of "{self.__class__.__name__}" has been created!')
        #%notify -m "http request complete"
    @dispatch(object)#if input is a dictionary, ensure the key is present:
    def set_parameters(self,p):
        print('you sent a dictionary')
        if 'key' not in p:
            p['key']= get_mb_search_key()
        p['format']='json'
        return p
    @dispatch(str) #if input is a string, use it as the query"
    def set_parameters(self,s):
        dict = {'format': 'json',
                'query': s,
                'limit':'1000',
                'key':get_mb_search_key()}
        return dict
    def get_dataframe(self,fields = []):
        '''
        returns a data frame of the articles
        optional parameter fields, is a list of desired fields to return
        '''
        df = pd.DataFrame()
        for a in self.articles:
            df = df.append(a, ignore_index=True)
        if fields:
            return df[fields]
        else:
            return df
    def create_file(self):
        '''
        creates a json file
        '''
        if self.totalResults != 0:
            with open("articles.json", "w") as my_file:
                my_file.write(json.dumps(self.articles, indent=4))
                print(
                    self.totalResults,
                    "article(s) successfully written to a file:",
                    "articles.json",
                )
        else:
            print("no articles to write!") 
    def get_indexTerms(self):
        if self.articles:
            df=  pd.concat(
                [
                    pd.DataFrame.from_dict(article["indexTerms"], orient="columns")
                    for article in self.articles
                ]
            )
            df = df['name'].value_counts().rename_axis("IndexTermName").reset_index(name="IndexTermCount")
            df = df.sort_values('IndexTermCount', ascending=False)
            return df
        else:
            print("no indexTerms to show!")
#### Below Functions, within this class, used only for FullDataSet
    def get_fulldataset(self):
        self.parameters.pop('sequence_id',"")                 #get rid of 'sequence_id' if it's there
        self.parameters['limit']='1000'                       #This will set the limit to the maximum allowed per their key  
        t_lst =[]                                             #this will be the list of all articles
        x=1                                                   #this will represent the number of articles left
        try:
            i=1                                               #i counts the number of loops occurring
            self.call_counter()  
            while x > 0:                                      #run while x (number of articles remaining)
                self.set_calls()                               #use set_calls object to determine calls left in minute
                myData = http_request(self.parameters)             #call API
                t_lst = t_lst + myData['articles']            #add articles to t_lst  
                s_id = myData['articles'][-1]['sequenceId']   #find the last sequence id available
                self.parameters['sequence_id'] = s_id         #set sequence within parameters for next API call
                t = myData['totalResults']
                print(f'Remaining Results: {t} / sequence_id: {s_id} / number: {i}')   # print progress
                x = int(myData['totalResults'])-len(myData['articles'])  #update number of articles left to pull
                i += 1
            #End of 'while' loop   
            print("all done")                                 #print to notify user of completion  
            #total = len(t_lst)                               #total of all articles pulled, should equal original 'totalResults'
            myData['articles']= t_lst                         #set the total list of articles as the value in the key 'articles'
            myData['totalResults']= len(t_lst)                #make sure the 'totalResults' key is set to the original 'totalResults'
            return myData
        #error handling:
        except Exception as e:
            print(f"error:{e}")
        #self.calls = remaining_in_minute()
        #self.startMin = get_time()
        return (self.calls, self.startMin)
    def wait_for_new_min(self):
        t = get_time()
        print(f"Waiting for a new Minute . . . current minute:{t}")
        while self.startMin == t:
            time.sleep(1)
            t = get_time() 
    def call_counter(self):
        self.calls = remaining_in_minute()
        self.startMin = get_time()
    def set_calls(self):
        self.calls = self.calls - 1
        if self.calls < 1:
            self.endMin = get_time()
            if self.startMin != self.endMin:
                self.calls = remaining_in_minute()
            else:
                self.wait_for_new_min()
                self.calls = remaining_in_minute()
            self.startMin = get_time() 

def http_request(p):
    #url = 'http://metabase.moreover.com/api/v10/searchArticles?'
    url = METABASE_SEARCH_URL 
    r = requests.get(url, params=p) 
    myURL = r.url
    #print(myURL)
    if r.status_code == 200:
        data = r.json()
    else:
        print(r.text)
        print('An error occurred while attempting to retrieve data from the API.')   
        data = None
    data['url']=myURL
    return data

        
def set_mb_search_key(k):
    dict = {'Metabase_Search_Key': k}
    me = credentials.myCredentials().setKey(dict)
def get_mb_search_key(): 
    '''
    Uses myCredentials.json file to determine Metabase Search Key
    '''
    myMBkey = credentials.myCredentials().Metabase_Search_Key
    return myMBkey
class Article:
    '''
    An instance of this class is created using 1 article 
    this class is not for the aggregate http response.
    A sample call: 
    myArticleInstance =article = article(myArticle)    
    '''
    def __init__(self, myArticle):
        '''
        Takes each key from the article dictionary and sets it as an attribute of the class
        '''
        self.__dict__.update(myArticle)
    def get_index_terms_df(self,TypeLst=[],aslist=False):
        '''
        returns the index terms as either a list of dataframe
        '''
        indexterms_lst = self.indexTerms
        for x in indexterms_lst:
            if not 'domains' in x:
                x.remove(x)
        df = pd.DataFrame.from_records(indexterms_lst)
        ## Filter dataframe, if a TypeLst is provided
        if TypeLst:
            lst =[x.upper() for x in TypeLst]
            #x = TypeLst.upper()
            df["INCLUDE"] = df["domains"].apply(lambda v: len(list(set(v).intersection(lst)) )!=0 )
            df =  df[df['INCLUDE']] 
            del df['INCLUDE']
            df
        ## return as a list if aslist = True
        if aslist:
            l = df['name'].tolist()
            return l
        else:
            return df
def rate_check():
    '''
    Calls the Metabase rate limit API and returns the results as a list of dictionaries
    '''
    myMBkey = credentials.myCredentials().Metabase_Search_Key
    #rateCheckUrl = 'https://metabase.moreover.com/api/v10/rateLimits?key='+myMBkey
    rateCheckUrl = METABASE_RATE_CHECK_URL + myMBkey
    r = requests.get(rateCheckUrl)
    if r.status_code == 200:
        data = r.json()
    return data['rateLimits']
    
def remaining_in_minute():
    '''
    uses the rateCheck function to call the Metabase rate limit API
    returns the number of calls remaining in the current minute
    '''
    lst = rate_check()
    for l in  lst:
        if l['unit']=='MINUTE':
            remaining  = int(l['limit'])-int(l['counter'])
    return remaining
    
def get_time():
    '''
    returns the current minute
    '''
    return datetime.now().minute 

