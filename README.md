# IA - Backend test

This project was made with Flask, a microframework for Python based on Werkzeug, Jinja 2 and good intentions.

## Development server

For a dev server you need to make:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Build

For a first production build you need to make:

```
ssh -i "ec2-ia-test.pem" ubuntu@ec2-3-18-197-205.us-east-2.compute.amazonaws.com
```

Install necessary packages

```
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
sudo apt install build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
```

In order to make it work, you will need to provide SSH access to the EC2 instance to login and clone the repo.

```
ls -al ~/.ssh
ssh-keygen -t rsa -C "your-email@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```

Then, add a new SSH Key into github. The next step is run the application

```
git clone git@github.com:ransilad/IA-backend-test.git
git pull origin master
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

Create a supervisor file in /etc/supervisor/conf.d/ and configure it according to your requirements.

```
[program:app]
directory=/home/ubuntu/IA-backend-test
command=/home/ubuntu/IA-backend-test/venv/bin/gunicorn app:app -b 0.0.0.0:8001
autostart=true
autorestart=true
# stderr_logfile=/var/log/app/app.err.log
# stdout_logfile=/var/log/app/app.out.log
```

And finally

```
sudo service supervisor restart
```

## Update production env

```
ssh -i "ec2-ia-test.pem" ubuntu@ec2-3-18-197-205.us-east-2.compute.amazonaws.com
cd IA-backend-test/
git pull origin master
sudo service supervisor restart
# For verify all is ok
sudo supervisorctl status
```
