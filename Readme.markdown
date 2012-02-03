Open Photo API / Import companion for export- tools
=======================
#### OpenPhoto, a photo service for the masses

----------------------------------------

<a name="overview"></a>
### Overview

This tool processes the files generated from the `export-*` tools such as `export-flickr` ([repository on GitHub](https://github.com/openphoto/export-flickr)).

<a name="setup"></a>
### Running an export tool

Before you run an import you'll have to first run an export. If you haven't done this already pick the appropriate one below.

* https://github.com/openphoto/export-flickr

<a name="dependencies"></a>
### Getting dependencies

The only dependency you need the `openphoto` module ([repository on Github](https://github.com/openphoto/openphoto-python)).

    git clone git://github.com/openphoto/openphoto-python.git
    cd openphoto-python
    sudo python setup.py install
    # you can leave this directory now that it's been installed
    cd ..

<a name="download"></a>
### Downloading the script

#### Using git

    git clone git@github.com:openphoto/import.git

#### Using wget

    mkdir export-flickr
    wget -O import/import.py https://raw.github.com/openphoto/import/master/import.py --no-check-certificate

#### Using file->save

Click the link below and save the file into a directory named `import`.

https://raw.github.com/openphoto/import/master/import.py

<a name="running"></a>
### Running the script

Start a terminal and enter the following.

    cd import
    # assuming you ran the export script from flickr copy the fetched files into this repository
    cp -R ../export-flickr/fetched ./
    python import.py

You'll be prompted for your key and secret which you took note of in step 4 above.

    Enter your OpenPhoto host:  ********************
    Enter your consumer key:  ********************
    Enter your consumer secret:  ********************
    Enter your token:  ********************
    Enter your token secret:  ********************
    
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

### YAY

You can go to your OpenPhoto site and see all of your Flickr photos with tags, title and description all in tact.

<a name="knownissues"></a>
### Known issues

1. Should we try to fetch these in parallel?
