import webbrowser
import urllib2
from BeautifulSoup import BeautifulSoup

def make_search_string(l):
	st = '';
	for value in l:
		st+=value+'+';
	return st;
	
def find_top_result(search_result):
	b = BeautifulSoup(search_result)
	a = b.find('li', {'class':'g'})
	c = a.find('a');
	return c['href'][7:]
	
search = raw_input("\nPlease tell me your problem?\n").split();
headers = {'User-Agent': 'Mozilla',}
req = urllib2.Request("http://www.google.co.in/search?q="+make_search_string(search)+"+site:stackoverflow.com", None, headers)
resp = urllib2.urlopen(req)


headers = {'User-Agent': 'Mozilla',}
urlad = find_top_result(resp.read())
req = urllib2.Request(urlad, None, headers)
resp = urllib2.urlopen(req)
f = open('stack.html', 'w')
a = BeautifulSoup(resp.read())
st ='';
x = a.find('td', {"class":"answercell"})
for i in x:
	st += str(i)+'\n'

f.write(st)
f.close()
webbrowser.get('google-chrome').open_new('stack.html')

print resp.read()
