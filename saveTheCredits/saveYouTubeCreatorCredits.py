import requests,json,sys,re,os
from datetime import datetime

from VideoIDHelper import *

#if you intend to extend this module
#simply call
#saveYouTubeAnnotations.retrieveAnnotation
#
#arg is either an ID, link or shortened link
#and location is the location the XML file is to be saved in
def retrieveCredits(arg,location="episodeJSONs/"):
	#print(idExtractor(arg))
	contents=""
	credits ={}
	try:
		vID = idExtractor(arg)
		pars = {"v" : vID, "hl":"en"}
		r = requests.get("https://www.youtube.com/watch", params=pars)
		contents = r.content
		sC = str(contents)
		if(len(contents) != 0):
			#print( str(contents).count("watch-extras-section"))
			#print( sC.find("ul", sC.find("content watch-info-tag-list")) )
			c = sC.find('h4 class="title"')
			#print(c)
			#print(sC.count('h4 class="title"'))
			for i in range(0, sC.count('h4 class="title"') ):
				#print(c)
				a = sC.find("ul", c)
				b = sC.find("/ul", c)
				#print( contents[  str(contents).find("watch-extras-section") - 200 : str(contents).find("watch-extras-section") + 4000 ] )
				splice =  sC[ a : b ]

				#print (splice)
	
				title = sC[ sC.find("h4",c-100) : sC.find("/h4",c-100)]
				title = title[title.rfind("      ")+6:title.rfind("\\n")]
				#print (title)
				credits[title] = []
				#print (a,b)
				#print( sC[ a : b ] )

				#Count /li's
				lC = splice.count("/li")
				#print(lC)
				#splice = splice[splice.find('/li')+1:]
				for i in range(lC):
					channelUser = channelLink = splice[:splice.find('/li')]
					#print("::::"+channelLink+":::::")
					channelLink = channelLink[channelLink.find('a href="')+8:channelLink.find('" class')]
					#channelLink = channelLink[channelLink.find('>')+1:]
					#print(channelLink)
					channelUser = channelUser[channelUser.find('a href="')+8:channelUser.find('</a>')]
					channelUser = channelUser[channelUser.find('" >')+3:]
					#print(channelUser)
					#print(credits[title])
					credits[title].append({"name": channelUser, "link": channelLink})
					#print(credits)
					splice = splice[splice.find('/li')+1:]
				c = sC.find('h4 class="title"', c + 1 ) 
			#print (credits)
			try:
				with open( location+"{}.json".format(vID), 'w') as f:
					json.dump(credits, f)

				#with open( (location+"{}.html").format(vID),"wb") as f:
				#	f.write(contents)
			except:
				with open( location+"/{}.json".format(vID), 'w') as f:
					json.dump(credits, f)

				#with open( (location+"/{}.html").format(vID),"wb") as f:
				#	f.write(contents)
		else:
			return None
		return credits
	except:
		return None
	return None


def main():
	first = True
	argument = ""
	print( "Hello today is: " + str(datetime.now().month) + "/" + str(datetime.now().day))
	print( "Remember that we have time until: " + "1/31" + " (presumably PST 0:00) " )
	#retrieveCredits("https://www.youtube.com/watch?v=BZLGKFWlRzY&list=PLhyKYa0YJ_5BevK2pZGDi-zUMorOSn2ed")
	#return 
	while first or argument == "":
		#argument ="horse"
		argument = input("Type in a URL to video or its ID: ")
		try:
			if argument == "":
				print("Program Terminated")
				break
			result = retrieveCredits(argument)
			if result != None:
				print("Loaded Succesfully.")
			else:
				print("Unable to Load, File not Generated.")
		except:
			print("Unable to recognize {}".format(argument))
			print("Program Terminated")
			break
		#argument = ""
		#first = False



if __name__== "__main__":
	main()