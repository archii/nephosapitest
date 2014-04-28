#!/usr/bin/env python

import requests

myUrl = "http://www.opscode.com/chef/download?p=el&pv=6&m=x86_64&v=latest&prerelease=false&nightlies=false"

def reqUrl(myUrl):
    myReq = requests.get(myUrl)
    return myReq

def saveReq(myReq):
    myFilename = myReq.url.split("/")[-1:][0]
    with open(myFilename, 'wb') as myFH:
        for chunk in myReq.iter_content():
            myFH.write(chunk)
    myFH.close()

def main():
    myReq = reqUrl(myUrl)
    saveReq(myReq)

if __name__ == "__main__":
    main()
