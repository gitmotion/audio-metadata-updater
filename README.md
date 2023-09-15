# audio-metadata-updater
- Uses <code>mutagen.easyid3</code>
- Add songs files to a given directory
- Generate / create a .json file that contains all the metadata you want to update
- current supported metadata fields: <code>title, artist, album, tracknumber, composer, albumartist, discnumber, copyright</code>
- Comes with error handling and will list out files that failed to update at the end of the log

<b>Note: File name will be used as the key in the metadata.json file and must be configured accordingly</b>
</br>
- Certain special characters (?, >, <, etc) can't be added to file names and will need to be taken out of the .json file keys to account for this
- However you can still add them in the metadata info

![specialcharacterexample](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/9533db9e-ca65-47f3-a808-02494734dfd5)

 
# Execution
<b>Debugging:</b>
</br>
![debugmodeexecution](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/44482a26-188e-401a-9982-776453dbc391)
- uncomment following lines and comment lines after
</br>

![debug_mode](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/d5bf55b1-ee0c-4835-b3d1-d06749708152)
- this will allow you to input the arguments

<b>Terminal:</b>
- ![terminalexecution](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/969a1c47-c934-4141-b5c2-7bd728d44fbf)
  - uncomment following lines and comment lines before
- Using <code>python</code>, execute as such:
  <div>
    <code>python path/to/amdu.py /path/to/song/directory .mp3 /path/to/metadata.json</code>
    </br>
    Or
    </br>
    <code>python .\amdu.py '.\AUDIO_FILE_DIRECTORY\' .mp3 '.\metadata.json'</code> (powershell)
  </div>
  - you can use any audio file extensions supported by mutagen (see documentation)
- This will grab all *.mp3 files (or any other specified extensions) in the given directory and parse the metadata.json file and match them accordingly

# Demo & Results
<b>Demo:</b>
</br>
![amdu demo](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/5cc62b9a-4efd-4e51-8041-35fbb65f9760)

<b>Before:</b>
</br>
![before](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/4c919f56-dcd0-4f24-9209-359f4d24a701)

<b>After:</b>
</br>
![after](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/993da10c-ef44-4dd0-b36d-a03ce8536dc8)

<b>View Log:</b>
</br>
[amdu-demo-log.txt](https://github.com/gitchrishan/audio-metadata-updater/files/12614815/amdu-demo-log.txt)

