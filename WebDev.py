*VENV*
    Virtual env is needed to create a separate python setup with modules for each project
    python3.8 -m venv env #creates a new dir
    #on Ubuntu you may need to install first if python-venv is not available
        sudo apt-get install python3.8-venv
    
    ACTIVATE
    source env/bin/activate #will activate the virtual env
    #This will activate the virtual env and the cursor changes
    (env) ls@LS-LINUX:~/Python/python_web_dev$ --> (env) shows you are in the venv
    
    REQUIREMENTS.TXT
    #For each virtual env set up a requirements.txt, which contains the packages installed by pip
    #when env is activated run (only needed at creating env):
        pip freeze > requirements.txt

    DEACTIVATE
    # to deactivate, just run the deactivate command

    #Everytime you create a project, create a venv for it!

*MVC*
    Explained with legos: https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/

*FLASK Quick Start*
    python3.8 -m pip install FLASK
    

