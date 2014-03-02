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
