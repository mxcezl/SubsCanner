import sys
import os
import getopt
from config import *
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI


##
#
# Authors (GitHub Profiles) : 
# - @mxcezl
# - @squ3D
#
# Depedencies :
# - DNS-Dumpster : https://github.com/PaulSec/API-dnsdumpster.com
# - Perl         : https://www.perl.org/get.html
# - Nikto        : https://github.com/sullo/nikto
##

if len(sys.argv) <= 1:
	sys.exit("\nUse : " + python3_path + " " + filename +" -u [Domain]\nExemple  : " + python3_path + " " + filename + " example.com")
try:
	opts, args = getopt.getopt(sys.argv[1:],"u:h")

except getopt.GetoptError:
	sys.exit(filename + "-u <www.exemple.com>")

for opt,arg in opts:
	if opt in('-u', '--url'):
		domain = arg
	elif opt in('-h', '--help'):
		print("\nVersion 0.1 made by Maxence Z & Naïm G\n")
		print("Idea of this Script is to be run in a company environment")
		print("goals is to scan for subs and perform a vulnscan throught Nikto\n")
		print("Exemple of Usage :")
		print("\tpython " + filename + " -u example.com")


		sys.exit(0)
	else:
		sys.exit(0)

print("\n[*] Running DNS-Dumpster API (By PaulSec)..\n")

results_json = DNSDumpsterAPI().search(domain)

print("\n[=] Subdomains found :\n")

subs = []
for result in results_json['dns_records']:
	print(result)

for result in results_json['dns_records']['host']:
	subs.append(result['domain'])
	print(result['domain'])

print("\n\n[*] Running WAScan (By m4ll0k)..\n")

if not os.path.exists(dir_out):
    os.makedirs(dir_out)

print("[+] Exporting directory : " + dir_out + "\n")

for link in subs:
	print("Running Nikto on : " + link + " ...")
	try:
		#os.system
		os.system(perl_path + " " + nikto_path +" -h https://" + link + " > " + dir_out + link + ".txt")
	except e:
		sys.exit("\nFailed to launch Nikto. Please check your path variables.")
	print("Done running Nikto on " + link + ".\n")
