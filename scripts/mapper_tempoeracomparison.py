#!/usr/bin/env python

#The script reads each track from the input file, uses bubble sort to find out its tempo category and maps it to its respective category
import sys

def read_input(file):
    for line in file:
        # split the line into words
	track, tempo, loudness = line.split()
        yield track, tempo

#bubble sort
def sort_bubble(tempo):
    tempoRange =    [19, 40, 45, 50, 55, 65, 69, 72, 77, 83, 85, 97, 109, 132, 140, 150, 167, 177]
    tempocategory = ['Larghissimo','Grave','Lento','Largo','Larghetto','Adagio','Adagietto','Andante_moderato','Andante','Andantino','Marcia _moderato','Moderato','Allegretto', 'Allegro', 'Vivace', 'Vivacissimo','Allegrissimo', 'Presto', 'Prestissimo']
    min_index=0
    max_index=len(tempoRange)-1
    
    while(min_index<=max_index):
      #determining midvalue
      midindex=min_index+((max_index-min_index)/2)
                       
      #comparison
      if(tempoRange[midindex]==tempo):
	return tempocategory[midindex]
      elif(tempoRange[midindex] > tempo):
	max_index=midindex-1
      elif(tempoRange[midindex]<tempo):
	min_index=midindex+1
    return tempocategory[max_index+1]


def main():
    # input comes from STDIN (standard input) and theen prints the values of trackid and the category of track's tempo 
    data = read_input(sys.stdin)
    for trackid, tempo in data:
      tempo = float(tempo)
      category = sort_bubble(tempo)
      print "%s,%s" %(category, trackid)
	
	
if __name__ == "__main__":
    main()

