import os
import json
import glob
import argparse
from mutagen.easyid3 import EasyID3

def updateAudioMetaData(directory_path, file_extension, metadata_json_path):

    if not os.path.exists(directory_path):
        print("Directory does not exist")
        return
    if file_extension is None:
        print("File extension was not provided")
        return
    if metadata_json_path is None:
        print("JSON file path was not provided")
        return

    success_count = 0
    fail_count = 0
    total_count = 0
    fail_list = []

    # Get a list of all files in the directory
    print("Getting list of files...")
    # Check if the directory path ends with a slash
    if not directory_path.endswith("/"):
        directory_path += "/"
    files = glob.glob(directory_path + "*" + file_extension)

    total_count = len(files)
    if total_count == 0:
        print("No files found")
        return

    print(f"Available files found: {len(files)}")
    print("Updating meta data for the following files:")
    for file in files:
        print(file)

    # Get JSON Metadata
    print("Getting metadata from JSON file...")
    with open(metadata_json_path) as json_file:
        metadata = json.load(json_file)
        if (metadata == None):
            print("No metadata found in JSON file")
            return

    # Update the metadata for each file
    for file in files:
        print(f"Updating metadata for {file}")
        try:
            # Open an MP3 file for editing
            audio = EasyID3(file)

            # Get the file name without extension
            file_name = os.path.basename(file)
            file_name_without_extension = file_name.replace(file_extension, "")

            audio_metadata = metadata[file_name_without_extension]
            if (audio_metadata == None):
                print(f"No metadata found for {file}")
                fail_count += 1
                continue

            # Access and modify tags
            try:
                title = audio_metadata['Title']
                if title is not None:
                    print("Updating title...")
                    audio['title'] = title
            except KeyError:
                print("Could not retrieve Title")
            try:
                artist = audio_metadata['Artist']
                if artist is not None:
                    print("Updating artist...")
                    audio['artist'] = artist
            except KeyError:
                print("Could not retrieve Artist")
            try:
                album = audio_metadata['Album']
                if album is not None:
                    print("Updating album...")
                    audio['album'] = album
            except KeyError:
                print("Could not retrieve Album")
            try:
                tracknumber = audio_metadata['Tracknumber']
                if tracknumber is not None:
                    print("Updating tracknumber...")
                    audio['tracknumber'] = tracknumber
            except KeyError:
                print("Could not retrieve Tracknumber")
            try:
                composer = audio_metadata['Composer']
                if composer is not None:
                    print("Updating composer...")
                    audio['composer'] = composer
            except KeyError:
                print("Could not retrieve Composer")
            try:
                albumartist = audio_metadata['Albumartist']
                if albumartist is not None:
                    print("Updating albumartist...")
                    audio['albumartist'] = albumartist
            except KeyError:
                print("Could not retrieve Albumartist")
            try:
                discnumber = audio_metadata['Discnumber']
                if discnumber is not None:
                    print("Updating discnumber...")
                    audio['discnumber'] = discnumber
            except KeyError:
                print("Could not retrieve Discnumber")
            try:
                copyright = audio_metadata['Copyright']
                if copyright is not None:
                    print("Updating copyright...")
                    audio['copyright'] = copyright
            except KeyError:
                print("Could not retrieve Copyright")
            # Save the changes
            audio.save()
            success_count += 1
            print(f"{file} Successfully Updated")
            print("--------------------------------------------------")

        except Exception as e:
            fail_count += 1
            fail_list.append(file)
            print(f"Error updating metadata: {str(e.__cause__)}")
            print("--------------------------------------------------")
            continue

    print("--------------------------------------------------")
    print("Update complete")
    print(f"Total files found: {total_count}")
    print(f"Total files updated: {success_count}")
    print(f"Total files failed: {fail_count}")
    for file in fail_list:
        print(file)
    print("--------------------------------------------------")


# Call the function
# Uncomment the following lines to run the script directly when debugging
# directory_path = input("Enter the directory path: ")
# file_extension = input("Enter the file extension: ")
# metadata_json_path = input("Enter the JSON file path: ")
# updateAudioMetaData(directory_path, file_extension, metadata_json_path)

# Comment the following lines when debugging
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update audio file metadata.')
    parser.add_argument('directory_path', type=str,
                        help='Path to directory containing audio files.')
    parser.add_argument('file_extension', type=str,
                        help='File extension of audio files to update.')
    parser.add_argument('metadata_json_path', type=str,
                        help='Path to JSON file containing metadata.')
    args = parser.parse_args()

updateAudioMetaData(args.directory_path,
                    args.file_extension, args.metadata_json_path)
