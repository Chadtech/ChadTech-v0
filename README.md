## NOTICE, Chadtech v0 is now outdated. Chadtech v0.5 can be used in browser at ChadCS.github.io/ctjs/Chadtech.html, and found in github.com/ChadCS/Chadtech-v0.5 

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

## Building a Windows binary (optional)

0. Install cxfreeze
1. In the directory 'ChadTech-v0' run 'python intoexe.py build' 
2. A folder named 'build' should now exist, add to it 'thumbnail.png','selected.png','introscreen.png','/chars6x8', and '/chars12x16'.
3. The build file is ChadTech as released. The exe in the build file is the application. Its icon is 'thumbnail.ico'. 
4. To create the installer install NSIS, and look for the NSIS quick setup application online. The NSIS quick setup guide, with particular settings, created 'ChadTech-installer.exe'


----------------------------------------------

Discovered bugs:

* L key in slanty font presents 'K'
* Starts to develop lag ~~after only 5 or so pages(800x800, linegap of 4)~~ after enough pages
* Slanty mode leaves an 'S' when activated or deactivated

Feature ideas:

* Automatic file name generator (if a file exists with that name, name the file [name]1.PNG)
* Search
* ~~Delete key~~ Available in v0.5
* New Document Command
* More Document sizes (1000x200 would be useful)
* ~~Remove gap between pages~~ Available in v0.5
* ~~Title on top of document~~ Available in v0.5
* ~~Lowercase form of Slanty Font~~ Available in v0.5
* Save /Save as distinction
* ~~Space character in small scripts~~ Available in v0.5
