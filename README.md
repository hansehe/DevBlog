# DevBlog

## Website
- Please visit [northerncoding.com](https://northerncoding.com)!

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
1. Build solution as container images:
    - `dbm -build`
2. Create default certificates:
    - `chmod +x init-letsencrypt`
    - `sudo ./init-letsencrypt`
3. Develop with Hugo:
    - Install Hugo: 
        - https://gohugo.io/getting-started/installing/
    - `cd src/` 
    - `hugo serve -D`
    - http://localhost:1313
4. Run solution as containers, and see results in browser:
    - `dbm -run`
    - https://localhost
5. Publish solution as container images:
    - `dbm -publish`
