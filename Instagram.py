import re
import os
fo = open("instagram", "rw+")
f =  open("url", "rw+")
#t = fo.read(100000000)
#print t
out=[]
url = " "
import urllib
count = 0 
k = []
for i in fo:
#	print i
#	k =  re.findall(r"\bhttps://scontent.cdninstagram.com/t51.2885-19/s150x150/1[\w]*", i) 
#	k = re.findall(r'[w.-]https[w.-]+', i)
#	k =  re.findall(r'[\w\.-]+://s[\w\.-]+', i)
	k =  re.findall("(?P<url>https?://[^\s]+)", i)
	print k
	for i in k:
		i = i[:-2]
#		url = str("wget") + " " + "-O" + " " + str(count) + " " +  i 
		url = str("wget") + " " + "-P" + " " + "fashion" + " " +  i 
#		print url
		count = count + 1
	for item in k:
		ite = item[:-2]		
		print item
  		f.write(ite)
		f.write('\n')
	#i#	print url
#		os.system(url)
"""	if len(url) > 65 :
		testfile = urllib.URLopener()
		testfile.retrieve(url, count)
		count = count + 1
"""	
	
"""for m in re.finditer("href=profile_picture", t):
	print t
	temp=t[m.end():m.start()+100]
	print temp
        lnk=(t[m.end():m.end()+temp.find("\"")])
        if lnk in names and lnk not in out:
            out.append(lnk)
print (out)"""

