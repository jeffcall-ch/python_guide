*VENV*
    Virtual env is needed to create a separate python setup with modules for each project
    Linux:
        python3.8 -m venv env #creates a new dir
        #on Ubuntu you may need to install first if python-venv is not available
            sudo apt-get install python3.8-venv
    Windows:
        python -m venv C:\Users\50000700\Python\Python_repos\python_web_dev\env
    
    ACTIVATE
    In VSCode by selecting the interpreter Python 3.8.x 64-bit ('env':venv) will automatically activate the env. 
    source env/bin/activate #will activate the virtual env
    #This will activate the virtual env and the cursor changes
    (env) ls@LS-LINUX:~/Python/python_web_dev$ --> (env) shows you are in the venv
    
    REQUIREMENTS.TXT
    #For each virtual env set up a requirements.txt, which contains the packages installed by pip
    #when env is activated run (only needed at creating env):
        pip3 freeze > requirements.txt #can be done later as well

    #This is good, because on another machine you don't need to install every package one by one
        $ pip3 install -r requirements.txt  #will install all requirments
        

    DEACTIVATE
    # to deactivate, just run the deactivate command

    #Everytime you create a project, create a venv for it!

*MVC*
    Explained with legos: https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/

*FLASK Quick Start*
    python3.8 -m pip install FLASK # be in env when running
    #IMPORTANT in VSCode choose Python 3.8.x 64-bit ('env':venv) interpreter on the lef bottom corner!
    Check out flask tutorial of VSCode: https://code.visualstudio.com/docs/python/tutorial-flask

    Start app:
    Make sure you are in the folder where your app is located at.
    Linux:
        $ export FLASK_APP=hello.py
        $ flask run
        * Running on http://127.0.0.1:5000/

    Windows:
        set FLASK_APP=app.py
        flask run

    


