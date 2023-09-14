# audio-metadata-updater
- Download songs files / playlist and add to a given directory
- In that same directory add a "metadata.json" file that contains any/all tags available from mutagen.easyid3
  - Note: File name will be used as the key in the metadata.json file and must be configured as such
  - To be continued..
 

# Executing Command
- Debugging: uncomment lines towards the end of the file and this will allow you to add the commands from an input
- Terminal: Using python, execute as such:
  - python amdu.py /path/to/song/directory .mp3
  - you can use any audio file extensions supported by mutagen
- This will grab all *.mp3 files (or any other specified extensions) in the given directory and parse the metadata.json file and match them accordingly
