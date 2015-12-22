# omegapm-org

Central website for Ωpm (omega package manager)

### Add a public key to your package

Go to <a href="http://omegapm.org/packages">the packages page</a> and add signed messages.

### Send messages

Go to <a href="http://omegapm.org/sign">the messages page</a> and paste in a clearsigned message
signed with the same key ```gpg --clearsign message.txt```

## Security model (website)

OmegaPM.org is built with <a href="http://webpy.org">web.py</a>, a simple Python web framework.
Here's why a Node.js-centric tool has its website written in Python:

- if there's a security issue with Node.js, npm, or Ωpm, we should have a communication channel which does not rely on any of those technologies
- web.py is a secure framework - it was the first choice of the SecureDrop project
- web.py is a simple framework - even if you're not a Python expert or a coder, you should be able to propose changes

Messages are checked for a signature matching their package, and stored as timestamped files.

## Setup and Run

```
# system dependencies
sudo apt-get install apache2 apache2-dev git python python-pip

# install mod_wsgi module for Apache
sudo apt-get install libapache2-mod-wsgi

# set up your Apache config (this is how Ubuntu does it)
cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/omegapm-mirror.org.conf
# read http://webpy.org/cookbook/mod_wsgi-apache-ubuntu for more info on how to edit the config file

# add the website to Apache
sudo a2ensite omegapm.org
sudo service apache2 reload

# use LetsEncrypt to get HTTPS

# Python dependencies
pip install web.py python-gnupg gitpython
```

## License

GPLv3+
