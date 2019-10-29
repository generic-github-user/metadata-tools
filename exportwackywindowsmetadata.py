import os
import subprocess
from lxml import etree
import json
import datetime
import glob
import xmltodict

directory = 'C:\\My Files\\Memes'
# counter
c = 0
#metadata = dict()
metadata = {}
keep_formatting = False
max_files = 10
save_to_file = True
convert_to_json = True

extensions = ('.png', '.pdn')

# https://stackoverflow.com/a/40755802
allfiles = glob.glob(directory + '/**/*', recursive=True)
#filelist = list(filter(lambda x: x.endswith(extensions), os.listdir(directory)))
filelist = list(filter(lambda x: x.endswith(extensions), allfiles))

#k = metadata.keys()
parser = etree.XMLParser(remove_blank_text=True)

#metadata[k[0]]
def cleanXML(xml):
      elem = etree.XML(xml, parser=parser)
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

if save_to_file:
      timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
      filename = 'filemeta_metadata_export_' + timestamp + '.json'
      #jsondata = json.loads(json.dumps(metadata))

      print(type(metadata))
      print(filename)
      with open(filename, 'w') as f:
            #json.dump(metadata, f, ensure_ascii=False, indent='\t')
            json.dump(metadata, f, indent='\t')

      #input()

