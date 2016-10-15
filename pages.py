# Code to remove duplicate pages &
# Code to remove pages with no posts

import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import pandas

access_token=" " #Access token here
outfile=open("pages.csv","a")
outfile.write("page_id"+","+"page_name")
outfile.write("\n")
data= pandas.read_csv('page_list.csv',sep=',',na_values='.')

def search():
        
        s = data['id']  
	a= data['name']
        for i in range(0,1000): # no. of rows in page_list csv        
                if (s[i]!=s[i-1]):
			w=str(int(s[i]))
			b=a[i]
		        print(w)
		        base_url = "https://graph.facebook.com/v2.6/"+w+"/feed?access_token="+access_token
		        results_json=json.loads(requests.get(base_url).text) 

		        if 'error' in results_json:
		                print "some error occurred"
		                return

		        if 'paging'in results_json:
				outfile.write(w+","+b)
				outfile.write("\n")

search()
