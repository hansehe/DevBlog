# DevBlog

## Get Started
1. Install Docker
2. Install python and pip
    - Windows:  https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/
    - Ubuntu: Python is installed by default
        - Install pip: sudo apt-get install python-pip
3. Install python dependencies:
    - -> pip install -r requirements.txt
4. See available commands:
    - -> python DockerBuild.py help

## Build & Run
1. Create default certificates:
    - `chmod +x init-letsencrypt`
    - `sudo ./init-letsencrypt`
1. Build solution as container images:
    - `dbm -build`
2. Run solution as containers:
    - `dbm -run`
3. Publish solution as container images:
    - `dbm -publish`
4. Open browser to see results!
    - https://localhost