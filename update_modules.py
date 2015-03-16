# update_modules.py
# run this whenever a git repo is cloned in

import os, subprocess

potential_repos = os.listdir('../ommod/node_modules')
missing_repos = []
for repo in potential_repos:
	if not os.path.exists('../ommod/' + repo + '.sig'):
		missing_repos.append(repo)
		os.system('mkdir ../ommod/' + repo)

for repo in missing_repos:
	print(repo)
	process = subprocess.Popen(['keybase', 'dir', 'verify', '../ommod/node_modules/' + repo + '/'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
	out, err = process.communicate()
	if err or out.find('Could not open') > -1 or out.find('error') > -1:
		print("didn't work")
		# os.system('rm -rf ../ommod/node_modules/' + repo)
	else:
		print("adding")
		fingerprint = out.split("fingerprint: ")[1].split("\n")[0][:-5].replace(" ", "")
		sigfile = open('../ommod/' + repo + '.sig', 'w')
                sigfile.write(fingerprint + "\n")
                sigfile.close()
