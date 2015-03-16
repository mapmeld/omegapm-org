# add dependencies
from datetime import datetime
import string, os, re, subprocess
import web, git
import signatures

# list all of the URLs for the server
urls = (
	'/', 'index',
	'/sign', 'sign',
	'/modules', 'modules'
)

# prepare to render template files
app = None
fingerprints = {}
git_urls = {}
mod_shas = {}
render = web.template.render("templates/")

# homepage
class index:
	# /
	def GET(self):
		return render.index()

# listing and adding modules
class modules:
	# /modules
	def GET(self):
		potential_repos = os.listdir('../ommod/node_modules/')
		repos = []
		for repo in potential_repos:
			if os.path.exists('../ommod/' + repo + '.sig') and os.path.isfile('../ommod/' + repo + '.sig'):
				fingerprint = ""
				if repo in fingerprints:
					fingerprint = fingerprints[repo]
				else:
					fpfile = open('../ommod/' + repo + '.sig', 'r')
					fingerprint = fpfile.read()
					fpfile.close()

				git_url = ""
				if repo in git_urls:
					git_url = git_urls[repo]
				else:
					git_data = git.Repo('../ommod/node_modules/' + repo)
					git_origin = git_data.remotes.origin.url
					git_sha = str(git_data.refs[0].log()[0]).split(" ")[1][:10]
					git_url = git_origin + "#" + git_sha

				sha = ""
				if repo in mod_shas:
					sha = mod_shas[repo]
				else:
					process = subprocess.Popen(['omegapm-hash', repo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, cwd='../ommod/')
        				out, err = process.communicate()
					if (err):
						sha = ""
					else:
						sha = out.split("\n")[0]

				repos.append({ "name": repo, "fingerprint": fingerprint, "git": git_url, "sha": sha })
		return render.modules(repos)

	def POST(self):
		try:
			repo_url = web.input()["repo"]
			repo_url = re.sub(r"\s+", "", repo_url)
			repo_url = re.sub(r"\\", "", repo_url)
			if repo_url.find('github.com') > -1 and repo_url.find('@') == -1 and repo_url.find('.git') == -1:
				repo_url = repo_url + '.git'
			os.system('cd ../ommod/node_modules && git clone ' + repo_url + ' && python ../../omegapm-org/update_modules.py &')
			return "ok, I'm going to try that. Check back on /modules soon."
		except:
			return "couldn't process that module posting =-("

# signing messages
class sign:
	# /sign
	def GET(self):
		return render.messenger()

	def POST(self):
		try:
			msg = web.input()["msg"]
			repo = '../ommod/' + verify_filename(web.input()["repo"])
			verified = signatures.get_key_from_message(msg)
			if verified and verified.valid:
				unix_time = int((datetime.now() - datetime(1970, 1, 1)).total_seconds())
				if verified.expire_timestamp == 0 or verified.expire_timestamp < unix_time:
					# ok, good to go
					# verified.pubkey_fingerprint = HEXCODE
					# verified.signature_id = sample/sample
					# verified.username = Name <email>
					# verified.sig_timestamp = when it was signed
					# verified.trust_text = TRUST_ULTIMATE
					if os.path.exists(repo + ".sig") and os.path.isfile(repo + ".sig"):
						sigs = open(repo + ".sig", 'r')
						sigfile = sigs.read().split("\n")
						sigs.close()
						if sigfile[0] == verified.pubkey_fingerprint:
							# valid signature for this package
							message = open(repo + "/" + str(verified.sig_timestamp), "w")
							message.write(msg)
							message.close()
							return "yay! that was a good message"
						else:
							return "the signature doesn't match the package =-("
					else:
						return "that package doesn't exist =-("
				else:
					return "that signature expired =-("
			else:
				return "that didn't look like a signed message =-("
		except:
			return "couldn't process that message =-("

	def verify_filename(fname):
		valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
		return ''.join(c for c in fname if c in valid_chars)

# this starts the server if you've called "python site.py"
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
