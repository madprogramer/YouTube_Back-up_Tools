def idExtractor(s):
	#URL?
	if isURL(s):
		return getIDfromURL(s)
	#Short URL?
	elif isShortURL(s):
		return getIDfromShortURL(s)
	#Assume ID
	else:
		return s

def isURL(s): 
	return (s.find("www.youtube.com") != -1)
def isShortURL(s):
	return (s.find("youtu.be") != -1)


def getIDfromURL(s): 
	if(s.find("&")!=-1):
		return  s[ s.find("v=")+2 :  s.find("&")] 
	return  s[ s.find("v=")+2 :  ] 
def getIDfromShortURL(s):
	if(s.find("?")!=-1):
		return  s[ s.find("/", s.find("/")+2)+1 :  s.find("?")] 
	return  s[ s.find("/", s.find("/")+2)+1  :  ]