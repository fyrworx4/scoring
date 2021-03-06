# -*- coding: utf-8 -*-
"""
PulseEngine Scoring Engine

@author: jimmy
"""

import json
import time
import requests
import pollers

from pollers import pollPort, pollHTTP, pollSSH, pollFTP

compId = None
apikey = None
teams = []

def loadConfig():
    global teams
    loadedConfig = {}

    with open("./config.json", "r") as f:
        try:
            loadedConfig = json.load(f)
            teams = loadedConfig["teams"]
        except:
            print("[!] Failed to load config")

"""
def sendStatus(teamName, teamServices):
    r = requests.post('https://ccdcscoring.jimmyli.us/api/competitions/update', json={
        "compId": compId,
        "apikey": apikey,
        "teamname": teamName,
        "services": teamServices
    })
    resp = r.json()
    if resp["status"] != "success":
        print("[!] There was a problem while sending the scores")
"""

def runCheck():
    print("Running checks...")
    for team in teams:
        print(team)
        teamname = team["teamname"]
        print(teamname)
        teamServices = []
        scoreObjects = team["scoredObjects"]
        for scoreObject in scoreObjects:
            if scoreObject["type"] == "port":
                print("Checking port pollers.")
                try:
                    result = pollPort(scoreObject["host"], scoreObject["port"])
                    #scoredServiceObject = {}
                    #scoredServiceObject["name"] = scoreObject["displayName"]
                    #scoredServiceObject["status"] = result
                    #teamServices.append(scoredServiceObject)
                    print("Success")
                except Exception as e:
                    print("[!] Port poll failed, likely fault in parameters")
                    print("Detailed exception: " + str(e))
            elif scoreObject["type"] == "http":
                try:
                    result = pollHTTP(scoreObject["host"], scoreObject["port"], scoreObject["md5"])
                    scoredServiceObject = {}
                    scoredServiceObject["name"] = scoreObject["displayName"]
                    scoredServiceObject["status"] = result
                    teamServices.append(scoredServiceObject)
                except Exception as e:
                    print("[!] HTTP poll failed, likely fault in parameters")
                    print("Detailed exception: " + str(e))
            elif scoreObject["type"] == "ftp":
                try:
                    result = pollFTP(scoreObject["host"], scoreObject["port"], scoreObject["users"]) # users must be an array of strings with format username:password
                    scoredServiceObject = {}
                    scoredServiceObject["name"] = scoreObject["displayName"]
                    scoredServiceObject["status"] = result
                    teamServices.append(scoredServiceObject)
                except Exception as e:
                    print("[!] FTP poll failed, likely fault in parameters")
                    print("Detailed exception: " + str(e))
            elif scoreObject["type"] == "ssh":
                try:
                    result = pollSSH(scoreObject["host"], scoreObject["port"], scoreObject["users"]) # users must be an array of strings with format username:password
                    scoredServiceObject = {}
                    scoredServiceObject["name"] = scoreObject["displayName"]
                    scoredServiceObject["status"] = result
                    teamServices.append(scoredServiceObject)
                except Exception as e:
                    print("[!] SSH poll failed, likely fault in parameters")
                    print("Detailed exception: " + str(e))
            else:
                print("Unknown poll type, service was skipped")

        #sendStatus(teamname, teamServices)

def main():
    loadConfig()
    print("[*] Config loaded, beginning scoring now")
    while True:
        loadConfig() # Reload the config during each run to help with user passwords
        runCheck()
        time.sleep(10)

if __name__ == "__main__":
    main()
