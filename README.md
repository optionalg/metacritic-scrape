DME

The attached python files demonstrate the requirements for a Coding Assesment from gaikai.
This package should complement my existing application documentation for a Site Reliability Role in their Berlin office.
All code was written by Chris Moser Between May 5 and May 12 2016.
I spend between 8 and 10 hours on this project.


PREREQUISITES


This python applicaiton requires python3 and the following additional modules:
json
requests
flask

Use pip or your OS repository to install them.

To install them on Centos 7 you might try:
$sudo /usr/local/bin/pip3 install lxml flask requests


NOTES


It should be noted that the metacritic Terms of Use forbid 'unauthorized spidering, “scraping,”
data mining or harvesting of Content, or use any other unauthorized automated means to gather datai...'.

[https://cbsi.secure.force.com/CBSi/articles/FAQ/CBSi-Terms-of-Use?template=template_tougl&referer=tougl.com&data=&cfs=default]

Consequently, requests to their site with urllib and requests both return 'forbidden 403'.
I used wget to download a copy of the page and then completed the rest of the tasks from that local copy.
metacritic.py will grab the page and store it locally if it does not exist.


RUNNING


Unzip and change to the directory containing the python files.
Run metacritic.py with:
./metacritic.py

An array of JSON objects containing the 'title' and 'score' of the games will be printed.

Run the flask server in a sepearate window with:
./run.py

This will listen for requests on the localhost on the default port (5000).
If port 5000 is not available, chose a new one by setting it in run.py and tests.py.

Point your browser to:
http://127.0.0.1:5000/games
and
http://127.0.0.1:5000/games/Yakuza 5

to test the funcionality of the API.

Run the unit tests with:
./tests.py

The flask server must be running for the tests to succeed.
Close the flask server when done with crtl-c.
