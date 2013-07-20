Trovebox API / Import companion for export- tools
=======================
#### Trovebox, a photo service for the masses

----------------------------------------

<a name="overview"></a>
### Overview

This tool processes the files generated from the `export-*` tools such as `export-flickr` ([repository on GitHub](https://github.com/photo/export-flickr)).

<a name="setup"></a>
### Running an export tool

Before you run an import you'll have to first run an export. If you haven't done this already pick the appropriate one below.

* https://github.com/photo/export-flickr
* https://github.com/photo/export-openphoto

<a name="dependencies"></a>
### Getting dependencies

The only dependency you need the `trovebox` module ([repository on Github](https://github.com/photo/openphoto-python)).

    sudo pip install trovebox

<a name="download"></a>
### Downloading the script

#### Using git

    git clone git://github.com/photo/import.git

#### Using wget

    mkdir import
    wget -O import/import.py https://raw.github.com/photo/import/master/import.py --no-check-certificate

#### Using file->save

Click the link below and save the file into a directory named `import`.

https://raw.github.com/photo/import/master/import.py

<a name="credentials"></a>
### Credentials

For full access to your photos, you need to create the following config file in ``~/.config/trovebox/default``

    # ~/.config/trovebox/default
    host = your.host.com
    consumerKey = your_consumer_key
    consumerSecret = your_consumer_secret
    token = your_access_token
    tokenSecret = your_access_token_secret

The ``config`` switch lets you specify a different config file.

To get your credentials:
 * Log into your Trovebox site
 * Click the arrow on the top-right and select 'Settings'
 * Click the 'Create a new app' button
 * Click the 'View' link beside the newly created app

<a name="running"></a>
### Running the script

Start a terminal and enter the following. 

    cd import
    # assuming you ran the export script from flickr copy the fetched files into this repository
    cp -R ../export-flickr/fetched ./
    # See above for instructions to get your credentials. The import script reads the config file by default.
    python import.py 
    

Now the script will start processing your files.
    
    Found a total of 6 files to process
    Processing 1 of 6 6065502023.json ... OK
    Processing 2 of 6 6109694637.json ... OK
    Processing 3 of 6 6109694841.json ... OK
    Processing 4 of 6 6109695003.json ... OK
    Processing 5 of 6 6110240222.json ... OK
    Processing 6 of 6 6110240318.json ... OK
    Results. Processed: 6. Errored: 0.

The last line shows how many were processed and how many errors there were. If you quit the script while it's running you can simply rerun the `python import.py` command again and it will resume where it left off.

The processed files will be moved from `fetched/` to `processed/` unless
there's an error, and in that case, they will endup in `errored/`. In
case you try to import a duplicate, the file will instead be moved in `duplicates/`.

### YAY

You can go to your Trovebox site and see all of your Flickr photos with tags, title and description all in tact.

<a name="knownissues"></a>
### Known issues

1. Should we try to fetch these in parallel?
