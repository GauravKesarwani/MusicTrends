#!/usr/bin/env python

import sys

idRating = {}
idName = {}
average = {}

#file containing artistId and artistNames
file1 = open("/home/swap/artistname.txt")

# split the line into artistId and artist name
for line1 in file1:
	artistId, artistName1 = line1.split("	", 1)
	artistName, newLine = artistName1.split("\n", 1)
	idName[artistId] = artistName

file1.close()	

# Create a Dictionary with artistId as the key and list of artist ratings as the values 
for line in sys.stdin:
	
	artistId, rating  = line.split()
	if(rating == "255"):
		rating = "0"
		
	if(idRating.has_key(artistId)):
		idRating[artistId].append(rating)		
	
	else:
		idRating[artistId] = [rating]

#Compute the Average value of Rating given to each user
for key in idRating:
	sum1 = 0.0
	avgValue = 0.0
	ratingValues =[]
	ratingValues = idRating[key]
	for j in ratingValues:
		sum1+=int(j)
	
	length = len(idRating[key])
	avgValue = (sum1/length)
	avgValue = round(avgValue,2)
	average[key] = avgValue

#Display artistId, Rating and ArtistName  	
for key in average:
	name = "Unknown"
	if(idName.has_key(key)):
		artistName = idName[key]
		artistId = key
		avgValue = average[key]
		print "%s\t%s" %(avgValue, artistName)

	
	



		
