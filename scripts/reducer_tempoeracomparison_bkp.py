#!/usr/bin/env python

#the script takes the input from the mapper and from the track_metadata.db file which contains the era's for all the tracks. Using this the script lists out total no of tracks, categorizing on the basis of tempo and era 
import sys
import os
import glob
import time
import datetime

trackrepository = {}
eracategorytrack = {}

for line in sys.stdin:	
  line = line.strip()
  category, trackid  = line.split(",")
  trackrepository[trackid] = category

try:
    import sqlite3
except ImportError:
    print 'you need sqlite3 installed to use this program'
    sys.exit(0)

dbfile = '/home/saru/cmpe272/Project/scripts/track_metadata.db'
conn= sqlite3.connect(dbfile)
c=conn.cursor()

q = "select era, track_id from songs where era!=0 order by era"
c.execute(q)
rows = c.fetchall()

for row in rows:
  key = row[0] + "," + trackrepository[row[1]]
  if(eracategorytrack.has_key(key)):
    eracategorytrack[key].append(row[1])		
  else:
    eracategorytrack[key] = [row[1]]
  
for key in eracategorytrack:
  print "%s\t\t%s" %(key,eracategorytrack[key])

c.close()
conn.close()

