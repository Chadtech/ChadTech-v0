## Download 

Download binary for your operating system from dist folder and run installer (.exe or .dmg, no dependencies needed)

## Or run from source

Click download zip then you will need dependencies:

### Windows:

Download python, pygame, tkinter, and PIL

then run 'python ChadTech.py'

### MAC:

Easiest way to get dependancies is homebrew is the preferred method to get them http://brew.sh/

Open a terminal and type:
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

When its done we need some stuff from it:
brew install python mercurial
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi 

Now we need some more stuff from the python package manager :)
pip install PIL
pip install hg+http://bitbucket.org/pygame/pygame

Now we're finally ready, go to directory with chadtech in it and type
python ChadTech.py




## Building an OSX binary (optional)
You might wish to run a more bleeding edge version of chadtech, but still want it to be a mac .app file. To make the mac .app file you'll need another package if you dont have it:
pip install py2app numpy

Then you can run ./buildosx.sh to create an app and DMG

