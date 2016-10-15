# Code to collect list of pages with a specific keyword 

import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = " " #Access token goes here
outfile=open("page_list.csv","a")
outfile.write("id"+","+"name")
outfile.write("\n")

def text_cleaning(text):
        text = text.encode('ascii', 'ignore').decode('ascii')
        text=text.replace('\n','NLC')
        text=text.replace(',','COM')
        return text
                
def search(page_name):
        base_url = 'https://graph.facebook.com/search?type=page&q='+page_name+'&access_token='+access_token
        results = requests.get(base_url)
        results_text = results.text
        results_json = json.loads(results_text)
        while 'next' in results_json['paging']:
            if 'data' in results_json:
                for item in results_json['data']:
                    print item['id']
                    outfile.write(item['id']+","+text_cleaning(item['name']))
                    outfile.write("\n")
                base_url= results_json['paging']['next']
                results_json=json.loads(requests.get(base_url).text)

search(' ') # Keyword for page-search here
