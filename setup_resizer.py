from distutils.core import setup
import py2exe
setup(console=['resizer.py'],
 options={ 
        'py2exe': 
        { 
            'includes': ['PIL'], 
        } 
    })