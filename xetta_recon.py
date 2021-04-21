# -*- coding: utf-8 -*-
#all in one recon tool installer
#coded by Ariful Anik(xetta_byte)
#you can install all those with this automation script
#!/usr/bin/env python3

import os
import sys
import time


print("▀▄▀ █▀▀ ▀█▀ ▀█▀ ▄▀█ ▄▄ █▀█ █▀▀ █▀▀ █▀█ █▄░█ ▀█▀ █▀█ █▀█ █░░ █▀ ▄▄ █ █▄░█ █▀ ▀█▀ ▄▀█ █░░ █░░ █▀▀ █▀█")
print("█░█ ██▄ ░█░ ░█░ █▀█ ░░ █▀▄ ██▄ █▄▄ █▄█ █░▀█ ░█░ █▄█ █▄█ █▄▄ ▄█ ░░ █ █░▀█ ▄█ ░█░ █▀█ █▄▄ █▄▄ ██▄ █▀▄")
time.sleep(2.3)
print("\n")
print("\n\n\tThis script will install those following tools globally.........\n\n\n \t [+]assetfinder \n \t [+]gau \n \t [+]wildcheck \n \t [+]hakrawler \n \t [+]httpprobe \n \t [+]qsreplace \n \t [+]dirdar \n \t [+]dalfox \n \t [+]ffuf ")
time.sleep(1.5)


def install_golang_module(module):
    ''' Install the specified Golang module '''
    modulename = module.split("/")[-1].lower()
    if not os.path.exists("/opt/" + modulename):
        print("Installing go module " + modulename)
        cmdseries = ["sudo -E go get -u " + module,
                     "sudo ln -s /opt/" + modulename + "/bin/" + \
		     modulename + " /usr/local/bin/" + modulename]
        os.environ["GOPATH"] = "/opt/" + modulename
        for cmdstring in cmdseries:
            os.system(cmdstring)
    
        
if __name__ == '__main__':
    ''' These go tools will be installed globally. '''
    
    golang_modules_to_install = ['github.com/tomnomnom/assetfinder',
                                 'github.com/lc/gau',
                                 'github.com/theblackturtle/wildcheck',
                                 'github.com/tomnomnom/httprobe',
                                 'github.com/hakluke/hakrawler',
                                 'github.com/tomnomnom/qsreplace',
                                 'github.com/hahwul/dalfox',
                                 'github.com/M4DM0e/DirDar',
                                 '']

          				
    for module in golang_modules_to_install:
        install_golang_module(module)

        
