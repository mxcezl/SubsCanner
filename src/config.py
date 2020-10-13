import os
import sys

filename = sys.argv[0]

# PATHS

root_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
python3_path = "python"
dir_out = root_path + "/outputs/"
perl_path = "C:/Perl64/bin/perl.exe"
nikto_path = root_path + "/nikto/program/nikto.pl"