# Code to collect posts from pages

import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import pandas

access_token=" " #Access token here
outfile=open("posts.csv","a")
outfile.write("post_id"+","+"message")
outfile.write("\n")
data= pandas.read_csv('page_list.csv',sep=',',na_values='.')

def text_cleaning(text):
        text = text.encode('ascii', 'ignore').decode('ascii')
        text=text.replace('\n','NLC')
        text=text.replace(',','COM')
        return text

def search():
        s = data['id']  
        for i in range(0,100):  # no. of rows in page_list.csv        
                w=str(int(s[i]))
                count = 0
                print(w)
                base_url = "https://graph.facebook.com/v2.6/"+w+"/feed?access_token="+access_token
                results_json=json.loads(requests.get(base_url).text) 

                if 'error' in results_json:
                        print "some error occurred"
                        return
                if 'paging'in results_json:
		        while 'next' in results_json['paging'] and count<=100: # Limit no. of posts per page to by count
		                if 'data' in results_json:
		                        for item in results_json['data']:
		                                if 'message' in item:
		                                        a=text_cleaning(item['message'])
		                                        outfile.write(item['id']+","+a)
		                                        outfile.write("\n")
		                                        count=count+1
		                                        
		                        base_url= results_json['paging']['next']
		                        results_json=json.loads(requests.get(base_url).text)
		                        if 'paging'in results_json:
		                                continue
		                        else:
		                                break


search()
