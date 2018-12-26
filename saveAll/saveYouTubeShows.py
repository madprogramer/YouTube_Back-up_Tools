import requests,json,sys,re,os
from datetime import datetime

from VideoIDHelper import *

#if you intend to extend this module
#simply call
#saveYouTubeAnnotations.retrieveAnnotation
#
#arg is either an ID, link or shortened link
#and location is the location the XML file is to be saved in
def retrieveShows(arg,location="showJSONs/"):
	#print(idExtractor(arg))
	contents=""
	episode ={}
	try:
		vID = idExtractor(arg)
		pars = {"v" : vID, "hl":"en"}
		r = requests.get("https://www.youtube.com/watch", params=pars)
		contents = r.content
		sC = str(contents)
		if(len(contents) != 0):
			#print( str(contents).count("watch-extras-section"))
			#print( sC.find("ul", sC.find("content watch-info-tag-list")) )
			#print(len('<span class="standalone-collection-badge-renderer-text">'))
			c = sC.find('<span class="standalone-collection-badge-renderer-text">') + 56

			splice = sC[c:sC.find('</span>',c)] 
			#print(splice)

			#get title 
			title = splice[:splice.find('</a></b>')]
			title = title[title.rfind('>')+1:]
			#print("T:"+title)
			episode = season = splice[splice.find('</a></b>')+8:]
			#episode = season = splice[season.rfind('>')+1:]
			
			#get season
			season=season[season.find('S')+1:]
			season=season[:season.find(' ')]
			#print("S:"+season)
			#get episode
			episode=episode[episode.find('E')+1:]
			#episode=episode[:episode.find(' ')]
			#episode=episode[episode.find('E')+1:]

			#print(episode)

			episode={"title":title, "season":season, "episode":episode }
			#print (episode)
			try:
				with open( location+"{}.json".format(vID), 'w') as f:
					json.dump(episode, f)

				#with open( (location+"{}.html").format(vID),"wb") as f:
				#	f.write(contents)
			except:
				with open( location+"/{}.json".format(vID), 'w') as f:
					json.dump(episode, f)

				#with open( (location+"/{}.html").format(vID),"wb") as f:
				#	f.write(contents)
		else:
			return None
		return episode
	except:
		return None
	return None

def main():
	first = True
	argument = ""
	print( "Hello today is: " + str(datetime.now().month) + "/" + str(datetime.now().day))
	print( "Remember that we have time until: " + "1/15" + " (presumably PST 0:00) " )
	#retrieveShows("https://www.youtube.com/watch?v=BZLGKFWlRzY&list=PLhyKYa0YJ_5BevK2pZGDi-zUMorOSn2ed")
	#return 
	while first or argument == "":
		#argument ="horse"
		argument = input("Type in a URL to video or its ID: ")
		try:
			if argument == "":
				print("Program Terminated")
				break
			result = retrieveShows(argument)
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