__author__ = 'Reid'

from distutils.core import setup
import py2exe

setup(console=['StandAloneApp.py'],
      options = {
          'py2exe': {
              'packages': ['Project']
          }
      })

#python setup.py py2exe
#cd dist
#____.exe