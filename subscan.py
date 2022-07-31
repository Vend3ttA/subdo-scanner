#Philippine CyberMafia
#Subdomain scanner coded by ~Kr4k3n
#Greetings SkidSec, COD3X CyberArmy, HCA, Phantom Hackers.PH
import os
import requests

class color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
 
os.system('clear')
def team_banner():
    print(color.BLUE + """
╔═╗┬ ┬┌┐ ┌─┐┬─┐╔╦╗┌─┐┌─┐┬┌─┐  ═╗ ╦  ╔═╗┬┌─┬┌┬┐╔═╗┌─┐┌─┐
║  └┬┘├┴┐├┤ ├┬┘║║║├─┤├┤ │├─┤  ╔╩╦╝  ╚═╗├┴┐│ ││╚═╗├┤ │  
╚═╝ ┴ └─┘└─┘┴└─╩ ╩┴ ┴└  ┴┴ ┴  ╩ ╚═  ╚═╝┴ ┴┴─┴┘╚═╝└─┘└─┘
        Be aware, we are awake.
          """ + color.PURPLE)
def web_scan():
        team_banner()
        target = str(input(color.CYAN + "ENTER TARGET SITE: " + color.CYAN))
        wordlist = open("subscan.txt")
        content = wordlist.read()
        subdomains = content.splitlines()
        extracted_sites = []
        for subdomain in subdomains:
            url = f"https://{subdomain}.{target}"
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(color.GREEN + "[INFO]:Extracted url:", url + color.RED)
                extracted_sites.append(url)


web_scan()
        
 




