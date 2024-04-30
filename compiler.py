import os

validation = input("In order to compile KnowledgeBase in .exe "
                   "you have to install Nuitka lib. Continue? Y or enter to cancel ")

working_dir = os.getcwd()
if validation == "y" or validation == "Y":
    try:
        import nuitka
        print("Module Nuitka already installed")
    except ModuleNotFoundError:
        print("Installing module Nuitka")
        os.system("pip install nuitka")
        pass

    os.system('nuitka '
              '--file-version=0.0.1.0 '
              '--product-name=KnowledgeBase '
              '--output-filename=KnowledgeBase '
              '--enable-console '
              '--standalone '
              '--windows-icon-from-ico=organizer_ico.ico '
              f'--output-dir=\"{working_dir}\"'
              ' --remove-output main.py')

elif not validation:
    print("compilation canceled")
