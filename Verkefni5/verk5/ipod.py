#!/bin/python
import os
import stagger
import shutil
from stagger.id3 import *


def main():
	print('/Users/BH/Desktop/verk5/ipod')
	#full path to ipod folder
	path_to_ipod = input('Full path to ipod folder: ')

	#step one folder back
	create_target = os.path.normpath(path_to_ipod + os.sep + os.pardir)
	path_to_target = ''

	if not os.path.exists(os.path.join(create_target,'Target')):
		path_to_target = os.path.join(create_target,'Target')
		os.mkdir(os.path.join(create_target,'Target'))
	else:
		path_to_target = os.path.join(create_target,'Target')

	for root,dirs,files in os.walk(path_to_ipod):
		if root != path_to_ipod:
			for f in files:
				#full path to current file
				p = os.path.join(root,f)
				#check if file is empty
				if os.stat(p).st_size != 0:
					tag = stagger.read_tag(p)
					#album field not empty
					if tag.album:
						artist = tag.artist or tag.album_artist
						album = tag.album
						songName = tag.title
						track = tag.track
						songFile = os.path.join(root,f)
						newFilename = str(track) + ' - ' + songName +'.mp3'
						#slash is messing with file path, replace with hyphen
						if '/' in newFilename:
							newFilename = newFilename.replace('/','-')
						path_to_artist = os.path.join(path_to_target,artist)
						path_to_album = os.path.join(path_to_artist,album)
						

						if not os.path.exists(path_to_artist):
							#create dir for artist this is his first item
							os.mkdir(path_to_artist)
					
							os.mkdir(path_to_album)

							shutil.copy(songFile,os.path.join(path_to_album,newFilename))
						else:
							#i'm here if artist exists and i have to check if it is the same album
							if not os.path.exists(path_to_album):
								os.mkdir(path_to_album)
								shutil.copy(songFile,os.path.join(path_to_album,newFilename))
							else:
								shutil.copy(songFile, os.path.join(path_to_album,newFilename))
								
						
					#these are files with no album and description is in tag.title and sometimes there's an author	
					else:
						#these files will go to unsorted album
						path_to_unsorted = os.path.join(path_to_target,'Unsorted')
						if not os.path.exists(path_to_unsorted):
							os.mkdir(path_to_unsorted)
						
						songFile = os.path.join(root,f)
						newFileName = tag.title
						if '/' in newFileName:
							newFileName = newFileName.replace('/','-')
						if not ('.mp3'in newFileName):
							newFileName = newFileName + '.mp3'
						shutil.copy(songFile,os.path.join(path_to_unsorted,newFileName))

	







if __name__ == '__main__':
    main()