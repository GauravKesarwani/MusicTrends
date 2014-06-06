#!/usr/bin/env python

import sys
import os
import glob
import time
import datetime

trackrepository = {}
eracategorytrack = {}

# Create a Dictionary with artistId as the key and list of artist ratings as the values 
for line in sys.stdin:	
  line = line.strip()
  category, trackid  = line.split(",")
  trackrepository[trackid] = category

#Import Era, category data from track_metadata using sqlite 3
try:
    import sqlite3
except ImportError:
    print 'you need sqlite3 installed to use this program'
    sys.exit(0)

dbfile = '/home/swap/tempo/track_metadata.db'
conn= sqlite3.connect(dbfile)
c=conn.cursor()

q = "select era, track_id from songs where era!=0 order by era"
c.execute(q)
#data = c.fetchone()
rows = c.fetchall()
c.close()
conn.close()

# Make era and category as a composite key to get the Trackids for that particular Era in a particular category
for row in rows:
  #print "%s,%s" %(row[1], row[0])
  key = row[0] + "," + trackrepository[row[1]]
  if(eracategorytrack.has_key(key)):
    eracategorytrack[key].append(row[1])		
  else:
    eracategorytrack[key] = [row[1]]
  
#print era , category and the No of tracks in the particular era and category
for key in eracategorytrack:
  	era, category = key.split(',')
	trackidsample = eracategorytrack[key]
	trackids = str(trackidsample)
	trackids = trackids.strip('[]')
	trackids = trackids.replace('u'', '')
	trackids = trackids.replace('\'', '')
	print "%s\t%s\t%s" %(era, category, len(eracategorytrack[key]))

  
