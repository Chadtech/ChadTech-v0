
python setup.py py2app

rm -rf dist/osx/*

hdiutil create -srcfolder dist/ChadTech.app/ dist/osx/ChadTech.dmg
