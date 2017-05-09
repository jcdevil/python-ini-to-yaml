#!/usr/bin/env python

import Confi2gParser
import yaml
import argparse

def process_ini(inifile,ymlfile):
    config = ConfigParser.ConfigParser()
    config.read(inifile)
   
    datamap = {} 
    for section in config.sections():
        datamap[section] = {}
        for name,value in config.items(section):
            datamap[section].update({name:value})

    with open(ymlfile,"w") as ymlfile:
        yaml.dump(datamap,ymlfile,default_flow_style=False)     

def main():
    parser = argparse.ArgumentParser(description="Convert a basic ini file to yml")
    parser.add_argument('--in',action="store",dest="ini",required=True,help="Input ini file")
    parser.add_argument('--out',action="store",dest="yml",required=True,help="Output yml file")
    args = vars(parser.parse_args())
    inifile = args['ini']
    ymlfile = args['yml']

    process_ini(inifile,ymlfile) 

if __name__ == '__main__':
    main()
