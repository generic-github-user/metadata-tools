import os
import subprocess
from lxml import etree
import json
import datetime
import glob
import xmltodict

# Directory to scan for files
directory = 'C:\\My Files\\Memes'
# counter
c = 0
#metadata = dict()
metadata = {}
# Keep XML formatting characters (only useful if convert_to_json is False)
keep_formatting = False
# Limit of files to check for metadata
max_files = 10
# Save exported data to a timstamped JSON file
save_to_file = True
# Convert XML data to JSON
# Otherwise, the output will be a JSON object with file paths corresponding to XML strings
convert_to_json = True
# Wait for user input after running program
wait = False

# List of extensions that should be exported
extensions = ('.png', '.pdn')

# https://stackoverflow.com/a/40755802
allfiles = glob.glob(directory + '/**/*', recursive=True)
#filelist = list(filter(lambda x: x.endswith(extensions), os.listdir(directory)))
filelist = list(filter(lambda x: x.endswith(extensions), allfiles))

#k = metadata.keys()
parser = etree.XMLParser(remove_blank_text=True)

#metadata[k[0]]
# Remove formatting characters (\n, etc.) from XML string
def cleanXML(xml):
      # Parse XML with lxml library
      elem = etree.XML(xml, parser=parser)
      # Convert back to string
      return etree.tostring(elem)

for i, filename in enumerate(filelist[:max_files]):
      # https://stackoverflow.com/a/18776536
      path = os.path.join(directory, filename).replace("\\","/")
      #path = os.path.normpath(path)
      print(path)
      data = subprocess.check_output(['FileMeta', '-ec', path], shell=True)
      if not keep_formatting:
            data = cleanXML(data)
      data = data.decode('utf-8')
      if convert_to_json:
            data = xmltodict.parse(data)
      #metadata[path] = data
      metadata[path] = data
      print('metadata from %s of %s files exported'%(i+1, len(filelist)))
      
            #c += 1
            #continue
      #else:
            #continue

#len(metadata.keys())
print(metadata)

# If this option is enabled, save the JSON data to a JSON file in the same directory as the program
# The file will be named 'filemeta_metadata_export_' along with a timestamp including the current date and time
if save_to_file:
      # Generate timestamp
      timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
      # Create filename string
      filename = 'filemeta_metadata_export_' + timestamp + '.json'
      #jsondata = json.loads(json.dumps(metadata))

      # Sanity checks
      print(type(metadata))
      print(filename)
      # Open placeholder file in write mode
      with open(filename, 'w') as f:
            # Dump JSON data into file and close
            # Indent with tabs, better than spaces
            #json.dump(metadata, f, ensure_ascii=False, indent='\t')
            json.dump(metadata, f, indent='\t')

# wait
if wait:
      input()

