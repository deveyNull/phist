import urllib.request
import re
import os
from os.path import basename
from posixpath import basename, dirname

# function that processes url, if there are any spaces it replaces with '%20' ##


url = 'http://www.facebook.com'
dirname2 = url.split("//")[1] #awkward overwrite rename
if not os.path.exists('images'):
    os.makedirs("images", exist_ok=True)
os.makedirs("images/" + dirname2, exist_ok=True)
os.chdir("images/" + dirname2)

urlcontent = urllib.request(url).read()
imgurls = re.findall('img .*?src="(.*?)"', urlcontent)
for imgurl in imgurls:
    try:
        imgurl = process_url(imgurl)
        imgdata = urllib2.urlopen(imgurl).read()
        filname = basename(urlsplit(imgurl)[2])
        output = open(filname, 'wb')
        output.write(imgdata)
        output.close()
        os.remove(filename)
    except:
        pass
