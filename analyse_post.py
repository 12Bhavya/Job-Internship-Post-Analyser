#!/usr/bin/python

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
   posts = "Not entered"

posts=posts.lower()
s=posts
if re.search(r'internship',posts)!=None or re.search(r'salary',posts)!=None or re.search(r'\w+@\w+.com',s)!=None or re.search(r'\w+@\w+.co.in',s)!=None or re.search(r'\w+@\w+.in',s)!=None or re.search(r'http://\w',s)!=None or re.search(r'https://\w',s)!=None or re.search(r'www.\w',s)!=None :
  sp=0
else:
  sp=1

phno=0
ph=re.compile(r'(\d{4})-(\d{7})')
phno=ph.search(s)
if phno==None:
  ph=re.compile(r'(\d{3})-(\d{8})')
  phno=ph.search(s)
  if phno==None:
    ph=re.compile(r'(\d{2})-(\d{10})')
    phno=ph.search(s)
    if phno==None:
      ph=re.compile(r'(\d{10})')
      phno=ph.search(s)
      if phno==None:
        ph=re.compile(r'(\d{11})')
        phno=ph.search(s)
        if phno==None:
          ph=re.compile(r'(\d{12})')
          phno=ph.search(s)     

if phno!=None:
  sp=0

if sp == 0:
  pid = random.uniform(4, 9)
else:
  pid = 0
def text_cleaning(text):
  text = text.encode('ascii', 'ignore').decode('ascii')
  text=text.replace('\\','BSL')
  text=text.replace('\'','SIC')
  text=text.replace('\n','NLC')
  text=text.replace(',','COM')
  return text

np = text_cleaning(posts)

if not os.path.isfile('./group.csv'):
	outfile=open("group.csv","w")
	outfile.write("post"+","+"score")
	outfile.write("\n")
else:
	outfile=open("group.csv","a")

outfile.write(np+","+"0")
outfile.write("\n")

#algo here

#markup_test
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Post Analysis</title>"
print """<style>
* {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

html {
  height: 100%;
}

body {
  background: #333;
  position: relative;
  height: 100%;
  margin: 0px;
}

@-webkit-keyframes clockwise {
  0% {
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-moz-keyframes clockwise {
  0% {
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-webkit-keyframes counter-clockwise {
  0% {
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(-360deg);
    -ms-transform: rotate(-360deg);
    -webkit-transform: rotate(-360deg);
    transform: rotate(-360deg);
  }
}
@-moz-keyframes counter-clockwise {
  0% {
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -moz-transform: rotate(-360deg);
    -ms-transform: rotate(-360deg);
    -webkit-transform: rotate(-360deg);
    transform: rotate(-360deg);
  }
}
.container {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -100px;
  height: 150px;
  width: 200px;
  margin-top: -75px;
}

.gearbox {
  background: #111;
  height: 150px;
  width: 200px;
  position: relative;
  border: none;
  overflow: hidden;
  -moz-border-radius: 6px;
  -webkit-border-radius: 6px;
  border-radius: 6px;
  -moz-box-shadow: 0px 0px 0px 1px rgba(255, 255, 255, 0.1);
  -webkit-box-shadow: 0px 0px 0px 1px rgba(255, 255, 255, 0.1);
  box-shadow: 0px 0px 0px 1px rgba(255, 255, 255, 0.1);
}
.gearbox .overlay {
  -moz-border-radius: 6px;
  -webkit-border-radius: 6px;
  border-radius: 6px;
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 10;
  -moz-box-shadow: inset 0px 0px 20px black;
  -webkit-box-shadow: inset 0px 0px 20px black;
  box-shadow: inset 0px 0px 20px black;
  -moz-transition: background 0.2s;
  -o-transition: background 0.2s;
  -webkit-transition: background 0.2s;
  transition: background 0.2s;
}
.gearbox.turn .overlay {
  background: transparent;
}

.gear {
  position: absolute;
  height: 60px;
  width: 60px;
  -moz-box-shadow: 0px -1px 0px 0px #888888, 0px 1px 0px 0px black;
  -webkit-box-shadow: 0px -1px 0px 0px #888888, 0px 1px 0px 0px black;
  box-shadow: 0px -1px 0px 0px #888888, 0px 1px 0px 0px black;
  -moz-border-radius: 30px;
  -webkit-border-radius: 30px;
  border-radius: 30px;
}
.gear.large {
  height: 120px;
  width: 120px;
  -moz-border-radius: 60px;
  -webkit-border-radius: 60px;
  border-radius: 60px;
}
.gear.large:after {
  height: 96px;
  width: 96px;
  -moz-border-radius: 48px;
  -webkit-border-radius: 48px;
  border-radius: 48px;
  margin-left: -48px;
  margin-top: -48px;
}
.gear.one {
  top: 12px;
  left: 10px;
}
.gear.two {
  top: 61px;
  left: 60px;
}
.gear.three {
  top: 110px;
  left: 10px;
}
.gear.four {
  top: 13px;
  left: 128px;
}
.gear:after {
  content: "";
  position: absolute;
  height: 36px;
  width: 36px;
  -moz-border-radius: 36px;
  -webkit-border-radius: 36px;
  border-radius: 36px;
  background: #111;
  top: 50%;
  left: 50%;
  margin-left: -18px;
  margin-top: -18px;
  z-index: 3;
  -moz-box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1), inset 0px 0px 10px rgba(0, 0, 0, 0.1), inset 0px 2px 0px 0px #090909, inset 0px -1px 0px 0px #888888;
  -webkit-box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1), inset 0px 0px 10px rgba(0, 0, 0, 0.1), inset 0px 2px 0px 0px #090909, inset 0px -1px 0px 0px #888888;
  box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1), inset 0px 0px 10px rgba(0, 0, 0, 0.1), inset 0px 2px 0px 0px #090909, inset 0px -1px 0px 0px #888888;
}

.gear-inner {
  position: relative;
  height: 100%;
  width: 100%;
  background: #555;
  -webkit-animation-iteration-count: infinite;
  -moz-animation-iteration-count: infinite;
  -moz-border-radius: 30px;
  -webkit-border-radius: 30px;
  border-radius: 30px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.large .gear-inner {
  -moz-border-radius: 60px;
  -webkit-border-radius: 60px;
  border-radius: 60px;
}
.gear.one .gear-inner {
  -webkit-animation: counter-clockwise 3s infinite linear;
  -moz-animation: counter-clockwise 3s infinite linear;
}
.gear.two .gear-inner {
  -webkit-animation: clockwise 3s infinite linear;
  -moz-animation: clockwise 3s infinite linear;
}
.gear.three .gear-inner {
  -webkit-animation: counter-clockwise 3s infinite linear;
  -moz-animation: counter-clockwise 3s infinite linear;
}
.gear.four .gear-inner {
  -webkit-animation: counter-clockwise 6s infinite linear;
  -moz-animation: counter-clockwise 6s infinite linear;
}
.gear-inner .bar {
  background: #555;
  height: 16px;
  width: 76px;
  position: absolute;
  left: 50%;
  margin-left: -38px;
  top: 50%;
  margin-top: -8px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  border-radius: 2px;
  border-left: 1px solid rgba(255, 255, 255, 0.1);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}
.large .gear-inner .bar {
  margin-left: -68px;
  width: 136px;
}
.gear-inner .bar:nth-child(2) {
  -moz-transform: rotate(60deg);
  -ms-transform: rotate(60deg);
  -webkit-transform: rotate(60deg);
  transform: rotate(60deg);
}
.gear-inner .bar:nth-child(3) {
  -moz-transform: rotate(120deg);
  -ms-transform: rotate(120deg);
  -webkit-transform: rotate(120deg);
  transform: rotate(120deg);
}
.gear-inner .bar:nth-child(4) {
  -moz-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  -webkit-transform: rotate(90deg);
  transform: rotate(90deg);
}
.gear-inner .bar:nth-child(5) {
  -moz-transform: rotate(30deg);
  -ms-transform: rotate(30deg);
  -webkit-transform: rotate(30deg);
  transform: rotate(30deg);
}
.gear-inner .bar:nth-child(6) {
  -moz-transform: rotate(150deg);
  -ms-transform: rotate(150deg);
  -webkit-transform: rotate(150deg);
  transform: rotate(150deg);
}

h1 {
  font-family: "Helvetica";
  text-align: center;
  text-transform: uppercase;
  color: #888;
  font-size: 19px;
  padding-top: 10px;
  text-shadow: 1px 1px 0px #111;
}
</style>"""
print """<a href='../../test.php?number=%s&spam=%s&pos=%s'>
<div class="container">
  <div class="gearbox">
  <div class="overlay"></div>
    <div class="gear one">
      <div class="gear-inner">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
    </div>
    <div class="gear two">
      <div class="gear-inner">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
    </div>
    <div class="gear three">
      <div class="gear-inner">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
    </div>
    <div class="gear four large">
      <div class="gear-inner">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
    </div>
  </div>
  <h1>Click here to see results!</h1>
</div></a>
"""%(pid,sp,posts)

#not used now-
"""
#markup
#print "Content-type:text/html\r\n\r\n"
#print "<html>"
#print "<head>"
#print "<title>Post Analysis</title>"
print """"""<style>
body {
background: #99cfe0;
background: -moz-linear-gradient(left, #f9cfe0 0%, #d6dbbf 100%);
background: -webkit-linear-gradient(left, #99cfe0 0%,#d6dbbf 100%);
background: linear-gradient(to right, #99cfe0 0%,#d6dbbf 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#99cfe0', endColorstr='#d6dbbf',GradientType=1 );
}

.btn {
   background: black;
  -webkit-border-radius: 7;
  -moz-border-radius: 7;
  border-radius: 7px;
  color: white;
  font-size: 12px;
  padding: 8px 13px 8px 13px;
  border: solid black 1px;
  text-decoration: none;
}

.btn:hover {
  color: white;
}
</style>""""""

print "</head>"
print "<body>"
print "<h2>Post '%s' added successfully!</h2>" % (posts)
print """"""<form method=Post action='../../gauge/test/test.php?number=%s&spam=%s&pos=%s'>
      <input style="width:auto" class='btn' type='submit' name ='submit' value='See Result' />
    </form>""""""%(pid,sp,posts)
print """"""<form method=Post action='../../OSM/p1.php?number=%s&spam=%s&pos=%s'>
      <input style="width:auto" class='btn' type='submit' name ='submit' value='See Result' />
    </form>""""""%(pid,sp,posts)
print "<a class='btn' href='../../OSM/p1.html'>Back</a>"
"""
print "</body>"
print "</html>"