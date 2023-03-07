# zippyshare_parser

Creator: GrowAsguard (https://github.com/GrowAsguard)
Edit: Mo-4 (https://github.com/Mo-4)

All credits & rights to GrowAsguard for initiallly creating the script.
I tried to reach him before working on this, but couldn't find any way to contact him.
I only edited it as it was not updated since 2021 and JDownloader was broken at the time of the update,
So I updated the code to match Zippy's code.
Note: Zippy sometimes change their formula for the file's unique code, this script will not work if they do, unless the script is updated accordingly.

**Description:-**

Parses ZippyShare URLs to get direct links. Written in Python.

This is a script useful for parsing a batch of ZippyShare URLs txt file to get direct links for use in a download manager like IDM.
Made because jDownloader2 will not open source their ZippyShare parser's code. Fuck you jDownloader. I'm gonna use IDM.

Currently only supports getting links from a txt file.
Can output results in a text file as well as in the terminal.

**Note:-**

ZippyShare sometimes updates the webpage source code, which may/will break this script. If this happens, simply raise an issue and I will try my best to update the script. 

Script made and tested on Windows 10 Pro. May work for all versions of Windows. May not work for Linux.

_zippy_parser.py_ contains the whole shebang.

_zippy_parser_base.py_ only contains the necessary code; useful for modifying and testing easily.

**Dependencies:-**

You need Python 3 environment to execute the script. You can get Python 3 from [here](https://www.python.org/downloads/).

You need the following packages installed:-

	pip install requests
	pip install bs4
	
Other needed packages which are already installed with Python 3 are:-

	sys
	tKinter
  
**Usage:-**

1) Create a txt file (with any name). Add one ZippyShare link on each line. Add as many links as you want.
2) Run the script by double clicking it or run it in a terminal (zippy_parser.py).
3) In the opening window, select the txt file where your ZippyShare links are stored.
4) In the next opening window, select path and name for the txt file where the parsed links will be stored.
5) The script will now run. Parsed links will be saved to the txt file and will also be displayed in the terminal.
6) Finish.

**Current known and unfixed issues:-**

- The direct download links stop working after a few hours ( About 3-4 hrs, maybe). Don't know the exact time period. At that point, you can rerun the script to get new download links to the same files which will work without problem.
- The script will run into errors when the file is removed from ZippyShare servers (a.k.a. File Not Found).

**Chaneglog:-**

*v1.2*
adjusted to new web code
7th March 2023

*v1.1*
adjusted to new webpage code
20th March 2021

*v1.0* 
Created the script
14th March 2021
