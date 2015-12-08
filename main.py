import re
import urllib

fo = open("input.txt", 'r')

username = fo.read().split('\n')

for name in username:
	url = "https://www.codechef.com/users/" + name
	text = urllib.urlopen(url).read()
	regex = '<a href="/COOK64/status/(.*?),(.*?)">(.*?)</a>'
	pattern = re.compile(regex)
	data = re.findall(pattern, text)
	print len(data)
