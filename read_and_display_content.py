from bs4 import BeautifulSoup
import urllib
import urllib2
from urllib2 import HTTPError,URLError
try:
   req=urllib2.Request('http://www.rrgroup.com.pk/')
except HTTPError as e:
   print('HTTPError:'+str(e))
except URLError as i:
   print('URLError:'+str(i))
else:
   res=urllib2.urlopen(req)

b=BeautifulSoup(res,"html5lib")
nl=b.findAll("div",{"id":"text_text"})
f=open('downloaded_text_content.txt','w+')
for n in nl:
	p=n.get_text()
f.write(p)
f.close()
    
f=open('parsed_and_downloaded_html_content.txt','w+')
f.write(str(b))
f.close()

