from sfctools.gui import Gui
from importlib.metadata import version
import sys
import os

if len(sys.argv) > 1 and sys.argv[1] == "attune":
    g = Gui()
    g.run()

elif len(sys.argv) > 1 and sys.argv[1] == "mamba-convert":
    # convert MAMBA source to Python and overwrite python_code folder

    source_folder = os.path.join(os.getcwd(),"mamba_code")
    dest_folder = os.path.join(os.getcwd(),"python_code")

    if not os.path.isdir(source_folder):
        print("ERROR: Could not detect source folder in %s" % source_folder)
    if not os.path.isdir(dest_folder):
        print("ERROR: COuld not detect destination folder in %s" % dest_folder)

    from sfctools.gui.attune.src.mamba_interpreter2 import convert_code

    # convert all files
    sub_names = next(os.walk(source_folder), (None, None, []))[2]

    k = 0
    for fname in sub_names:
        k+= 1
        try:

            all_code = None
            source_file = os.path.join(source_folder,fname)
            print("[%03i] %s" % (k,fname))
            with open(source_file,"r") as file:
                codelines = file.readlines()
                all_code,_ = convert_code(codelines)

            if all_code is not None:
                name = os.path.basename(fname)
                dest_file = os.path.join(dest_folder, name).lower()
                with open(dest_file,"w") as file:
                    file.write(all_code)

        except Exception as e:
            print("Error: Could not convert %s: %s" % (fname,str(e)))

    print("done.")

else:
    print("""
============= WELCOME TO SFCTOOLS ============================
ver %s
Main corresponding author: Thomas, thomas.baldauf@dlr.de
Institute of Networked Energy Systems (DLR-VE)
German Aerospace Center, 2020

Sfctools is a lightweight and easy-to-use Python framework
for stock-flow consistent agent-based macroeconomic (SFC-ABM) modeling.
It concentrates on agents in economics and helps you to construct agents,
helps you to manage and document your model parameters,
assures stock-flow consistency, and facilitates basic economic
data structures (such as the balance sheet).

Become part of the community! ;-)

See https://sfctools-framework.readthedocs.io/en/latest/ for the latest documentation
See https://gitlab.com/dlr-ve/esy/sfctools for the latest version on gitlab
==============================================================

Type 'python -m sfctools attune' to start the graphcial user interface 'attune'
Type 'python -m sfctools mamba-convert' to build a Python project from the MAMBA code folder
""" % version('sfctools'))
