import requests,json,sys,re,os
from datetime import datetime

from saveYouTubeAnnotations import retrieveAnnotation
from saveYouTubeCreatorCredits import retrieveCredits
from saveYouTubeShows import retrieveShows
from VideoIDHelper import *

#if you intend to extend this module
#simply call
#saveYouTubeAnnotations.retrieveAnnotation
#
#arg is either an ID, link or shortened link
#and location is the location the XML file is to be saved in

def main():
	first = True
	argument = ""
	print( "Hello today is: " + str(datetime.now().month) + "/" + str(datetime.now().day))
	print( "Remember that we have time until: " + "1/15" + "for Annotations and Credits; and until " + "1/31" +" for Episodes (presumably PST 0:00) " )
	while first or argument == "":
		#argument ="horse"
		argument = input("Type in a URL to video or its ID: ")
		try:
			if argument == "":
				print("Program Terminated")
				break
			results = [retrieveAnnotation(argument,"saved/annotations/"),retrieveCredits(argument,"saved/creatorCredits/"),retrieveShows(argument,"saved/episodeInfos/")]
			if results != None and len(results) !=0:
				print("Loaded Succesfully.")
			else:
				print("Unable to Load, Some Files not Generated.")
		except:
			print("Unable to recognize {}".format(argument))
			print("Program Terminated")
			break
		#argument = ""
		#first = False


if __name__== "__main__":
	main()