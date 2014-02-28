
python setup.py py2app --resources icon.PNG,chars6x8,chars12x16,introscreen.PNG,selected.PNG,thumbnail.PNG --iconfile thumbnail.icns --packages PIL,pygame,wx

rm -rf dist/*.dmg

hdiutil create -srcfolder dist/ChadTech.app/ dist/ChadTech.dmg
