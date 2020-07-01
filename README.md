1- apt-get update && apt-get -y upgrade
2- apt-get install python-pip
3- pip install virtualenv
4- Create Virtualenv:

    virtualenv crawler-env
    
5- Activate Virtualenv:

On windows:

    virtualenv crawler-env\script\activate

On Linux:

    source crawler-env/bin/activate
    
6- Install requirements:

    pip install -r requirements.txt
    
7