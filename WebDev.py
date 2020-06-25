# flake8: noqa
*VENV*
    Virtual env is needed to create a separate python setup with modules for each project
    Linux:
        python3.8 -m venv env #creates a new dir
        #on Ubuntu you may need to install first if python-venv is not available
            sudo apt-get install python3.8-venv
    Windows:
        python -m venv C:\Users\50000700\Python\Python_repos\python_web_dev\env
        or with relative path standing in the python_web_dev folder:
            python -m venv ./env
    
    ACTIVATE
    In VSCode by selecting the interpreter Python 3.8.x 64-bit ('env':venv) will automatically activate the env. 
    Linux:
        source env/bin/activate #will activate the virtual env
        #This will activate the virtual env and the cursor changes
        (env) ls@LS-LINUX:~/Python/python_web_dev$ --> (env) shows you are in the venv
    Windows:
        PowerShell PS C:\> <env>\Scripts\Activate.ps1
        #In CMD it is cmd.exe C:\> <venv>\Scripts\activate.bat
    
    REQUIREMENTS.TXT
    #For each virtual env set up a requirements.txt, which contains the packages installed by pip
    #when env is activated run (only needed at creating env):
        pip3 freeze > requirements.txt #can be done later as well

    #This is good, because on another machine you don't need to install every package one by one
    First activate <env> !
        Linux:
        $ pip3 install -r requirements.txt  #will install all requirments
        Windows: BEHIND PROXY:
            pip --proxy https://148.64.11.164:8080 install -r requirements.txt
        

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

    VSCode:
        https://code.visualstudio.com/docs/python/tutorial-flask
        Click on debug and create a launch.json file for running FLASK_APP
        in the launch.json you may need to add the relative path to app.py if it is saved in subfolder
        "FLASK_APP": "flask_quick_start/app.py",

    @app.route decorator
        @app.route("/test/<search_query>")
        def search(search_query):
            return search_query

    @app.route("/integer/<int:value>")
    def int_type(value):
        print (value + 1)
        return "correct"

    @app.route("/name/<name>")
    def index(name):
        if name.lower() == "michael":
            # return "Hello, {}".format(name), 200
            return f"Hello, {name}", 200
        else:
            return "Not found", 404

    
    Flask converters
        <value> --> unicode string
        <int:value> --> int
        <float:value>  --> float
        <path:some/cool/path>  --> path

    Response object
        The response is a tuple: (response, status, headers)
        By default the status is 200 and the headers is "document" when a string is returned

    Enable debug in browser add this line to the code
        # error handling
        app.config["DEBUG"] = True   

        Open VSCode launch.json which is holding the debugging info and make sure, that your settings are:
            "env": {
                "FLASK_APP": "flask_quick_start/app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"   # set it to "1" by default is "0"
            },

            "args": [
                "run",
                "--no-debugger",  #delete this line
                "--no-reload"   #delete this line
            ],




