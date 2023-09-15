# audio-metadata-updater

- Add songs files to a given directory
- Generate / create a .json file that contains all the metadata you want to update
<b>
Note: File name will be used as the key in the metadata.json file and must be configured accordingly
- Certain special characters (?, >, <, etc) can't be added to file names and will need to be taken out of the .json file to account for this
- However you can still add them in the metadata info
</b>
 
# Execution
<b>Debugging:</b>
- ![debugmodeexecution](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/44482a26-188e-401a-9982-776453dbc391)
  - uncomment following lines and comment lines after
- ![debug_mode](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/dfe15604-ac83-4158-b80f-f4eaaa1180a1)
  - this will allow you to input the arguments

<b>Terminal:</b>
- ![image](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/c6f5e9fc-92bf-462d-9406-f832e655b44b)
  - uncomment following lines and comment lines before
- Using python, execute as such:
  <div>
    <code>python amdu.py /path/to/song/directory .mp3 /path/to/metadata.json</code>
  </div>
  - you can use any audio file extensions supported by mutagen (see documentation)
- This will grab all *.mp3 files (or any other specified extensions) in the given directory and parse the metadata.json file and match them accordingly

# Results
<b>Before:</b>
  ![before](https://github.com/gitchrishan/audio-metadata-updater/assets/43588713/ac1e12e8-477f-4126-90db-f79dbdce7600)

<b>After:</b>

