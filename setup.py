<<<<<<< HEAD
#*********************************************
#        Auto-Generated With py2Nsis
#*********************************************

import warnings 
#ignore the sets DeprecationWarning
warnings.simplefilter('ignore', DeprecationWarning) 
import py2exe
warnings.resetwarnings() 
from distutils.core import setup
		
target = {
'script' : "C:\\HFNPPSF\\code\\ChadTech-v0\\ChadTech.py",
'version' : "0.30",
'company_name' : "ChadTech",
'copyright' : "",
'name' : "ChadTech_Installer", 
'dest_base' : "ChadTech_Installer", 
'icon_resources': [(1, "C:\\HFNPPSF\\code\\ChadTech-v0\\thumbnail.ico")]
}		



setup(

	data_files = [(u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\dist', [u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\ChadTech.py']), (u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\dist', [u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\introscreen.PNG']), (u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\dist', [u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\readme.PNG']), (u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\dist', [u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\selected.PNG']), (u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\dist', [u'C:\\\\HFNPPSF\\\\code\\\\ChadTech-v0\\\\thumbnail.PNG'])],
    
    zipfile = None,

	options = {"py2exe": {"compressed": 0, 
						  "optimize": 0,
						  "includes": ['', '', ''],
						  "excludes": ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl', 'Tkconstants', 'Tkinter'],
						  "packages": [],
						  "bundle_files": 2,
						  "dist_dir": "C:\\HFNPPSF\\code\\ChadTech-v0\\dist",
						  "xref": False,
						  "skip_archive": False,
						  "ascii": False,
						  "custom_boot_script": '',                          
						 }
			  },
	console = [],
	windows = [target],
	service = [],
	com_server = [],
	ctypes_com_server = []
)
		
=======
"""
 py2app/py2exe build script for MyApplication.

 Will automatically ensure that all build prerequisites are available
 via ez_setup

 Usage (Mac OS X):
     python setup.py py2app

 Usage (Windows):
     python setup.py py2exe
 """

import sys

mainscript = 'ChadTech.py'

PACKAGES = ['PIL','pygame']
RESOURCES =['chars6x8','chars12x16','introscreen.PNG','selected.PNG','thumbnail.PNG']
WINRESOURCES =['chars6x8/*','chars12x16/*','introscreen.PNG','selected.PNG','thumbnail.PNG']


if sys.platform == 'darwin':
     from setuptools import setup    
     extra_options = dict(
         setup_requires=['py2app'],
         app=[mainscript],
         options={'py2app':
         {
             'packages': PACKAGES,
             'resources': RESOURCES,
             'iconfile': 'thumbnail.icns',
             'plist': {
                 'CFBundleName': 'ChadTech',
                 'CFBundleShortVersionString':'0.3.0', # must be in X.X.X format
                 'CFBundleVersion': '0.3.0',
                 'CFBundleIdentifier':'com.chadtech.chadtechv0', #optional
                 'NSHumanReadableCopyright': '@ ChadTech ChadTech 2014', #optional
                 'CFBundleDevelopmentRegion': 'English', #optional - English is default
                 'CFBundleDocumentTypes':[
                 dict(
                 CFBundleTypeExtensions=['png'],
                 CFBundleTypeIconFile='thumbnail.icns',
                 CFBundleTypeRole='Editor',
                 )
                 ],
             }
         }
     },
     )
elif sys.platform == 'win32':
     from distutils.core import setup
     import py2exe, os, glob
     
     def find_data_files(source,target,patterns):
        """Locates the specified data-files and returns the matches
        in a data_files compatible format.

        source is the root of the source data tree.
            Use '' or '.' for current directory.
        target is the root of the target data tree.
            Use '' or '.' for the distribution directory.
        patterns is a sequence of glob-patterns for the
            files you want to copy.
        """
        if glob.has_magic(source) or glob.has_magic(target):
            raise ValueError("Magic not allowed in src, target")
        ret = {}
        for pattern in patterns:
            pattern = os.path.join(source,pattern)
            for filename in glob.glob(pattern):
                if os.path.isfile(filename):
                    targetpath = os.path.join(target,os.path.relpath(filename,source))
                    path = os.path.dirname(targetpath)
                    ret.setdefault(path,[]).append(filename)
        return sorted(ret.items())

     extra_options = dict(
     windows=[mainscript],
     data_files=find_data_files('','',WINRESOURCES),
     options={
         'py2exe':{
             'compressed': True,
             'bundle_files': 1,
             'packages': PACKAGES,
             'dist_dir':'dist/windows',
         }
     },
     )
else:
     extra_options = dict(
         # Normally unix-like platforms will use "setup.py install"
         # and install the main script as such
         scripts=[mainscript],
     )

setup(
    **extra_options
)
>>>>>>> fb7a032c506c4170df54478f23d2a6499a5269d0
