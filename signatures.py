# signatures.py

import gnupg

gpg = gnupg.GPG()
gpg.encoding = 'utf-8'

def get_key_from_message(message):
	return gpg.verify(message)
