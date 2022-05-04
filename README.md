Morsifier
=========

This project was created for a school project to learn a life skill.  Morse code is fascinating, and it seemed like a good practical application to learn how to convert text to Morse.

After considering options for outputting the Morse code, we settled on a GUI that blinks out the Morse code, and shows the dots and dashes.  After this, we decided that having a "follower" that shows what part of the code is currently playing would be nice.

Setup
-----------
1. Install Git [like this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. Clone this repository
   1. Create a new folder in the location of your choice
   2. Open a command/terminal window and navigate to the folder.  ``cd *folder*``
   3. ``git clone https://github.com/teamgz-projects/Morsifier.git``
   4. ``cd Morsifier``
3. Install python version 3 
   1. Check if python is installed ``python3 --version``
   2. If the version number doesn't appear, install Python [like this](https://realpython.com/installing-python/)
4. Install tkinter (GUI framework)
   1. Check if tkinter is installed ``python3 -m tkinter``
   2. If a window opens up, you have tkinter.  If not, it needs to be installed [like this](https://www.delftstack.com/howto/python-tkinter/install-tkinter/)
5. ``python3 main.py``

Technology
----------
* Language = Python
* IDE = PyCharm
* OS = Ubuntu
* GUI = tkinter

What we did
---------------
We created a dictionary of letters and their Morse equivalents so we could easily look up a letter.
We then looped through the input text and checked to see if it was in the dictionary, and if so, used the Morse equivalent to build up a string, which we displayed in the GUI.
We wanted to play back the Morse code as well, so we ended up using a canvas element and a rectangle that we could color to simulate a blink.  We used the time module to sleep after each blink so we could time the dots and dashes.
Finally, in order to create the "follower" effect, we used the text widget and used tags to identify the part of the code that was "active" so we could color it.

Where we go
------------
It would be fun to go outside the boundary of a GUI to output the Morse code.
One such example would be to use a Raspberry Pi, and use the GPIO pins to turn an LED on and off.  There is also a really nifty USB light called Blink(1) that would be fun to experiment with.  There are so many more ways Morse code can be transmitted.  One other is binary, it might be fun to convert to binary representation.  Finally, we haven't done a lot of error handling or testing of special cases, so we might beef it up at some point.  We also have some spaghetti code that could benefit from encapsulation in classes.