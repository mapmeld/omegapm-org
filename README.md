# omegapm-org

Central website for Ωpm (omega package manager)

### Submit packages

Go to <a href="http://omegapm.org/packages">the packages page</a> and submit a public git repo.

### Send messages

Go to <a href="http://omegapm.org/sign">the messages page</a> and paste in a clearsigned message
signed with the same key ```gpg --clearsign message.txt```

## Security model

OmegaPM.org is built with <a href="http://webpy.org">web.py</a>, a simple Python web framework.
Here's why a Node.js-centric tool has its website written in Python:

- if there's a security issue with Node.js, npm, or Ωpm, we should have a communication channel which does not rely on any of those technologies
- web.py is a secure framework - it was the first choice of the SecureDrop project
- web.py is a simple framework - even if you're not a Python expert or a coder, you should be able to propose changes to content and functionality

Packages are cloned from a public git repo, then keybase verifies the signature. Any unsigned packages are deleted.

Messages are checked for a signature matching their package, and stored as timestamped files.


## Setup and Run

Install dependencies, then run the server continuously on standard port 80:

```
# dependencies
sudo easy_install web.py
pip install python-gnupg gitpython

# installing Node.js and associated packages
sudo apt-get install nodejs nodejs-legacy npm
npm install -g omegapm-require

# using Keybase to verify repos and messages (no need to add your own user)
npm install -g keybase-installer
keybase-installer
keybase config

# repo folders
mkdir ../ommod
mkdir ../ommod/node_modules

# running server
nohup python site.py 80 &
disown
```

## License

GPLv3+
