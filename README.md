# omegapm-org

Central website for Ωpm (omega package manager)

## Security model

OmegaPM.org is built with <a href="http://webpy.org">web.py</a>, a simple Python web framework.
Here's why a Node.js-centric tool has its website written in Python:

- if there's a security issue with Node.js, npm, or Ωpm, we should have a communication channel which does not rely on any of those technologies
- web.py is a secure framework - it was the first choice of the SecureDrop project
- web.py is a simple framework - even if you're not a Python expert or a coder, you should be able to propose changes to content and functionality

## Setup and Run

Install web.py framework, then run the server continuously on standard port 80:

```
sudo easy_install web.py
nohup python site.py 80 &
disown
```
