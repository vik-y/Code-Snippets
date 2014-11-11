import webbrowser
import urllib2
from BeautifulSoup import BeautifulSoup

def make_search_string(l):
	'''
	We have to modify the search string in order to match the correct url format
	'''
	st = '';
	for value in l:
		st+=value+'+';
	return st;
	
def find_top_result(search_result):
	'''
	Fetches the top result from the google search and returns the url from it
	'''
	b = BeautifulSoup(search_result)
	a = b.find('li', {'class':'g'})
	c = a.find('a');
	return c['href'][7:]
	
	
search = raw_input("\nPlease tell me your problem?\n").split();
headers = {'User-Agent': 'Mozilla',}
req = urllib2.Request("http://www.google.co.in/search?q="+make_search_string(search)+"+site:stackoverflow.com", None, headers)
resp = urllib2.urlopen(req) #Searching google with the search string you entered and only looking into stackoverflow.com results.


urlad = find_top_result(resp.read()) #Get the top result from the results returned by google
req = urllib2.Request(urlad, None, headers)
resp = urllib2.urlopen(req) #Opening the top result 
f = open('stack.html', 'w')
a = BeautifulSoup(resp.read())
st ='';
x = a.find('td', {"class":"answercell"}) #Getting the top answer from stackoverflow
for i in x:
	st += str(i)+'\n' #Converting those answers into proper format 

f.write(st) #Saving the top answer into stack.html file
f.close()
webbrowser.get('google-chrome').open_new('stack.html') #Opening the file in web browser
