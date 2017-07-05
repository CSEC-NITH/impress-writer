#Impress Writer


![screenshot]("./Screenshot new.png")


Objective:

Impress Writer is an application engineered with the aim of helping

its user to enhance their literary creations and embellish them with

the usage of better words.Built entirely using Python, the application

dynamically fetches and suggests synonyms for the text typed in by the

user. Boasting of additional features such as a built in Dictionary,

Spell Check and basic text-editing capabilities, Impress Writer utilises

the Beautiful Soup and GTK Libraries of Python for web scraping and the

implementation of the GUI

Authors:

Kartikeya Sharma

Harsh Tiku

Navanshu Agarwal

Radhika Sood

How to Run:

first install bs4,requests,pygtkspellcheck using pip

also install Gtk 3.0 if not present

then in terminal write the following command and press enter

python3 impressWriter.py

DevGuide:

dataManager.py:

	contains function to manage localData and networkData.

dictScript.py:

	script to fetch meaning of a word from dictionary.com.

impressWriter.py:

	this is the main file which contains all the UI and

	events associated with the application.

localData.py:

	contains functions to manipulate,retrive localData

stringProcessing.py:

	contains functions to manipulate,process strings

	fetched from the internet

thesScript.py:

	script to fetch meaning of a word from thesaurus.com

some code is taken from http://python-gtk-3-tutorial.readthedocs.io/en/latest/textview.html

and https://automatetheboringstuff.com/ was helpful for web scraping.
