#!/usr/bin/env python

'''
To run this script, please use pipenv, conda, or venv and install the following packages.

$ pip install pandas requests
'''
import gzip
import logging
import os
import pandas
import requests

logger = logging.getLogger('') # <--- Probable a good idea to name your logger. '' is the 'root' logger
sysHandler = logging.StreamHandler()
sysHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(sysHandler)
logger.setLevel(logging.INFO)

CHUNK_SIZE: int = 1024
ENCODING: str = 'utf-8'
OUTPUT_DIR: str = '/tmp/outputs'
if not os.path.exists(OUTPUT_DIR):
  os.makedirs(OUTPUT_DIR)

url: str = 'https://github.com/jbcurtin/noaa-timeseries-dataset/blob/master/dataset/45ad4419-0af8-4044-a65c-3f7fcabb1f19.csv.gz?raw=true'
filename: str = os.path.basename(url.rsplit('?', 1)[0])
filepath: str = os.path.join(OUTPUT_DIR, filename)
with open(filepath, 'wb') as output_stream:
  logger.info(f'Downloading Data[{filename}]')
  response = requests.get(url, stream=True)
  for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
    output_stream.write(chunk)

csv_filename: str = filename.rsplit('.', 1)[0]
csv_filepath: str = os.path.join(OUTPUT_DIR, csv_filename)
with open(csv_filepath, 'w', encoding=ENCODING, newline='\n') as output_stream:
  logger.info(f'Decompressing Data to filepath[{csv_filepath}]')
  with gzip.open(filepath, 'rb') as compressed_stream:
    data: bytes = compressed_stream.read()
    data: str = data.decode('utf-8')
    output_stream.write(data)

data_frame: pandas.core.frame.DataFrame = pandas.read_csv(csv_filepath)
print(data_frame)

