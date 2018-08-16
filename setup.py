import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Khanh Huynh\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Khanh Huynh\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

executables = [cx_Freeze.Executable('game.py')]

cx_Freeze.setup(
    name = '64-bit Ninja',
    version = '1.05',
    author = 'Khanh H',
    options = {'build_exe': {'packages': ['pygame'], 'include_files': ['icon.png', 'idle1.png']}},
    executables = executables 
)