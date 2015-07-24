import sys  
  
from cx_Freeze import setup, Executable  
from distutils.core import setup  
import py2exe  
  
options ={ 'py2exe':
                {
                    'dll_excludes':['w9xpopen.exe'] #This file is for win9x platform
                }
        }

# Setup
setup ( options  = options,
        windows = [{
                        'script': 'xmlUI.py'
                  }]
      )




#setup(console=["example.py"]) 
  
