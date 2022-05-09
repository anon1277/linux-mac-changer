#/usr/bin/env python

import subprocess
import optparse


def get_argumnets():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="to add new mac address")
    (options, argumnets) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface , use --help for more info")
    elif not options.new_mac: 
        parser.error("[-] please specify an mac adress , use --help for more info")
    return options
    
def change_mac(interface, new_mac):
    print("[+] changeing a mac of " + interface + " address to new mac" + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
      
     

options = get_argumnets()    
change_mac(options.interface, options.new_mac)




#parser.parse_args()

#nterface = input("interface >")

#new_mac =  input("new mac >")

#interface = options.interface

#new_mac =  options.new_mac

#mac_changerr(options.interface, options.new_mac)

subprocess.call("ifconfig",shell=True)


#ubprocess.call(["ifconfig"])



