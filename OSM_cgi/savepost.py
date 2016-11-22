#!/Python27/python

# Import modules for CGI handling 
import cgi, cgitb, os
import codecs, random
import re
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('posts'):
   posts = form.getvalue('posts')
else:
   posts = "No post entered"

def text_cleaning(text):
  text = text.encode('ascii', 'ignore').decode('ascii')
  text=text.replace('\n','NLC')
  text=text.replace(',','COM')
  return text

posts=posts.lower()
np = text_cleaning(posts)

outfile=open("group.csv","w")
outfile.write("post_id"+","+"message")
outfile.write("\n")

outfile.write("1"+","+np)
outfile.write("\n")

#algo here

#markup
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Post Analysis</title>"
print"</head>"
print"</body>"
print """<a href='../../gauge/test/test.php?spam=%s'><h1>Click here to see results!</h1></a>
"""%(0)
print"</body>"
print"</html>"

