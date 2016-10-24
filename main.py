import re
import urllib.request
import urllib.parse
import datetime

def getPage(url):
    '''Function that fakes a Mozilla and gets the page and decodes
    from ISO 8859 7'''

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = None
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, values, headers)
    f = urllib.request.urlopen(req)
    return (f.read().decode('iso-8859-7'))

def returnlines(text_list, key):
    '''return lines containing the key'''
    result = []
    for line in text_list:
        if key in line:
            result.append(line)
    del result[0]
    return result

def returninfo(mlist):
	link_pat = re.compile(r'<a\shref="(.+?)"')
	title_pat = re.compile(r'siteid467">(.+?)<')
	result = []
	c = 0
	for i in mlist:
		if "siteid467" in i:
			try:
				link = re.findall(link_pat, i)[0]
			except:
				link = "no link"
			try:
				text_body = re.findall(title_pat, i)
				text = text_body[1]
				title = text_body[0]
			except:
				text, title = "no text or title"
		result.append([link,title,text])
	return result
	
	
########################################################################
# Main program
########################################################################

# various settings
base_url = "http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/"
month_list = "IAN FEB MAR APR MAY JUN JUL AUG SEPT OCT NOE DEC".split(" ")
sub_page_list = "prok_mel ap_anath arch-comp loipes-anatheseis dwrean-meletes".split(" ")
date_list = datetime.date.today().isoformat().split('-')
url_year = date_list[0]
url_month = month_list[(int(date_list[1])-1)]
url_ref = "http://portal.tee.gr/portal/page/portal/tptee/SERVICES_INFORM_TPTEE/prokhrixeis_meleton/2016/PR_MEL-OCT16/loipes-anatheseis"
url = base_url + url_year + '/' + 'PR_MEL-' + url_month + url_year[2:] + '/'

# construct url list with various subpages
url_list = []
for i in sub_page_list:
	url_list.append(url+i)

# key used to match lines that contain interesting text
key = 'descriptionid16244557siteid467'

# iterate url list and fetch results
c = 0
for u in url_list:
	
	# debug separator
	print ("="*60)
	print (sub_page_list[c])
	c = c + 1
	print ("")
	
	# get page and split it at new lines
	try:
		page = getPage(u).split('\n')
	except:
		print("Problem while downloading url:")
		print(u)
		
	# delete lines that do not contain our key
	match_lines = returnlines(page,key)
	
	# regex lines and get final info
	m = returninfo(match_lines)
	
	# print results
	for result in m:
		# separator
		print ("."*60)
		for el in result:
			print (el)
