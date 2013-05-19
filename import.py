#!/usr/bin/env python

# import os for file system functions
import os
# import json
import json
# shutil for file renaming
import shutil
import sys
import time
import logging

# import flickrapi
# `easy_install flickrapi` or `pip install flickrapi`
from openphoto import OpenPhoto

from os.path import join, getsize


# main program
def import_into_openphoto(client):


  for root, dirs, files in os.walk('fetched/'):
    total = len(files)
    current = 1
    processed = 0
    errored = 0
    start_time = time.time()
    print "Found a total of %d files to process" % total
    for i in files:
      print "Processing %d of %d %s ..." % (current, total, i),
      sys.stdout.flush()
      current = current + 1
      infile = "fetched/%s" % i
      f = open(infile, 'r')
      json_str = f.read()
      f.close()

      shutil.move(infile, "errored/%s" % i)

      params = json.loads(json_str)
      resp = client.post('/photo/upload.json', params)
      result = json.loads(resp)
      if result['code'] == 201:
        print "OK"
        processed = processed + 1
        shutil.move("errored/%s" % i, "processed/%s" % i)
      else:
        code = result['code']
        message = result['message']
        print "FAILED: %d - %s" % (code, message)
        if code == 409 :
          shutil.move("errored/%s" % i, "duplicates/%s" % i)
        else:
          print params
        errored = errored + 1
      sys.stdout.flush()

    end_time = time.time()
    total_time = (end_time - start_time) / 60.0
    photos_minute = int(total / total_time)

    if total > 0:
      print "Results. Processed: %d. Errored: %d." % (processed, errored)
      print "Imported %d photos at %d photos/minute." % (total, photos_minute)
  
# create a directory only if it doesn't already exist
def createDirectorySafe( name ):
  if not os.path.exists(name):
    os.makedirs(name)


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Import photos into an OpenPhoto instance')
  parser.add_argument('--config', help="Configuration file to use")
  parser.add_argument('--host', help="Hostname of the OpenPhoto server (overrides config_file)")
  parser.add_argument('--consumer-key')
  parser.add_argument('--consumer-secret')
  parser.add_argument('--token')
  parser.add_argument('--token-secret')
  parser.add_argument('--debug', help="Print extra debug information", action="store_true")
  config = parser.parse_args()

  if config.debug:
    logging.basicConfig(level=logging.DEBUG)

# Host option overrides config file settings
  if config.host:
    client = OpenPhoto(host=config.host, consumer_key=config.consumer_key,
                       consumer_secret=config.consumer_secret,
                       token=config.token, token_secret=config.token_secret)
  else:
    try:
      client = OpenPhoto(config_file=config.config)
    except IOError as error:
      print error
      print
      print "You must create a configuration file with the following contents:"
      print "    host = your.host.com"
      print "    consumerKey = your_consumer_key"
      print "    consumerSecret = your_consumer_secret"
      print "    token = your_access_token"
      print "    tokenSecret = your_access_token_secret"
      print
      print "To get your credentials:"
      print " * Log into your Trovebox site"
      print " * Click the arrow on the top-right and select 'Settings'."
      print " * Click the 'Create a new app' button."
      print " * Click the 'View' link beside the newly created app."
      print
      print error
      sys.exit(1)

  # check if a processed and errored directories exist else create them
  createDirectorySafe('processed')
  createDirectorySafe('errored')
  createDirectorySafe('duplicates')

  import_into_openphoto(client)
