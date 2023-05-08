#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# github.com/tintinweb
#
"""
BugBounty Companion
    (1) clone all **Immunefi** Repositories according highest bugbounty payout amount

            $ bugbounty.py [sync|unique|clone]

        (a) sync with immunefi
            $ bugbounty.py sync
        (b) show unique repos
            $ bugbounty.py unique [minReward=100000]
        (c) clone all repos (dryrun)
            $ bugbounty.py unique clone [minReward=100000]
        (d) clone all repos (actually do it)
            $ bugbounty.py unique clone no-dryrun [minReward=100000]


        # NOTE: default output folder is $(pwd)/bugbounty_repos/<project>

    (2) run your fancy tools/code-smell rules on it
    (3) profit $$
    
Consider donating if you win a $mm 🥳
"""

from lib2to3.pytree import Base
import requests
import re
import json
import os

from datetime import datetime
from decimal import Decimal



##### CONFIG THIS
MIN_REWARD_CUTOFF = 100_000   # only check out projects with max bounty >= 100_000 $$ 
OUTPATH = os.path.abspath("./bugbounty_repos")   # abspath to main repo checkout dir
##### NO CHANGES BEYOND THIS LINE


class BaseCompanion(object):
    REX_SUB_FOR_SHELL = re.compile(r'[^a-zA-Z0-9\_\-]')
    REX_DUP_USCORE = re.compile(r'_+')

    def __init__(self, repofile):
        self.repofile = repofile
        self.data = []

    def loadRepo(self):
        try:
            with open(self.repofile, 'r') as f:
                self.data = json.load(f)
        except: pass
        return self

    def _saveRepo(self):
        with open(self.repofile, 'w') as f:
            f.write(json.dumps(self.data))
        return self

    def gitClone(self, basedir, project, giturl):
        project = self.REX_DUP_USCORE.sub("_", self.REX_SUB_FOR_SHELL.sub("_",project.lower()))
        cmd = "mkdir -p %s/%s; cd %s/%s && git clone --depth=1 %s"%(basedir, project, basedir, project, giturl)
        
        if "no-dryrun" in sys.argv:
            os.system(cmd)
        print(cmd)

    def getUniqeRepos(self, repos):
        return sorted(set([ "/".join(r.split("/")[0:5]) for r in repos]))


class ImmunefiCompanion(BaseCompanion):
    

    def __init__(self, repofile="immunefi_repos.json"):
        super().__init__(repofile=repofile)

    def getRepos(self):
        mainPage = requests.get("https://immunefi.com/explore/?filter=immunefi").text
        mainMeta = re.findall('id="__NEXT_DATA__" type="application/json">(.*)</script></body></html>', mainPage)
        if not mainMeta:
            return
        all_projects = json.loads(mainMeta[0])["props"]["pageProps"]["bounties"]
        print("found %d projects"%len(all_projects))
        
        results = self.data

        for nr,pstruct in enumerate(all_projects):
            p= pstruct["id"]
            pmeta = {
                'name': p,
                'max_reward': 0,
                'repos': []
            }
            all_links = set([])

            source = requests.get("https://immunefi.com/bounty/%s/"%p).text
            links = re.findall('id="__NEXT_DATA__" type="application/json">(.*)</script></body></html>', source)
            pmeta['max_reward'] = int(re.findall(';maximum_reward=([0-9]+)', source)[0])

            
            print("#",nr, p, "$$", pmeta["max_reward"])
            for f in links:
                dataJson = json.loads(f)

                if "assets_in_scope" in dataJson["props"]["pageProps"]["bounty"].keys():
                    for target in dataJson["props"]["pageProps"]["bounty"]["assets_in_scope"]:
                        if target["target"].startswith("https://github.com"):
                            all_links.add(target["target"])

                if "mdx" in dataJson["props"]["pageProps"]["bounty"].keys():
                    for mdx in dataJson["props"]["pageProps"]["bounty"]["mdx"].values():    
                        if not mdx: continue
                        alt = re.findall("(https?://github.com/[a-zA-Z_\-0-9\/#]+)", mdx)
                        all_links.update(alt)

                if "assets" in dataJson["props"]["pageProps"]["bounty"].keys():
                    if dataJson["props"]["pageProps"]["bounty"]["assets"]:
                        for ass in dataJson["props"]["pageProps"]["bounty"]["assets"]:    
                            if not ass: continue
                            if not "url" in ass.keys(): continue
                            alt = re.findall("(https?://github.com/[a-zA-Z_\-0-9\/#]+)", ass["url"])
                            all_links.update(alt)

            if len(all_links) == 0:
                # fallback, grep serialized links
                alt = re.findall("(https?://github.com/[a-zA-Z_\-0-9\/#]+)", str(links))
                all_links.update(alt)

            # cleanup

            def filterLinks(l):
                if "#" in l: return False
                if "audit" in l: return False
                if "PublicReports" in l or "Halborn" in l: return False
                if len(l.split("/",5))<5: return False
                if l.split("/",5)[-1]=="": return False
                return True

            all_links = [l for l in all_links if filterLinks(l) ]

            print("found %d repos"%len(all_links))
            if len(all_links)== 0 and False: # debug
                import pprint
                pprint.pprint(dataJson["props"])
                exit()

            pmeta["repos"] = sorted(list(all_links))
            results.append(pmeta)
        # sort results by max bounty

        results = list(reversed(sorted(results, key=lambda x: int(x['max_reward']))))

        print(results)
        self.data = results
        return self



class Code4renaCompanion(BaseCompanion):

    def __init__(self, repofile="code4rena.json"):
        super().__init__(repofile=repofile)

    def _amountToDecimal(self, amount):
        return int(Decimal(re.sub(r'[^\d.]', '', amount)))

    def getRepos(self):
        now = datetime.now()

        cdata = requests.get("https://code4rena.com/page-data/index/page-data.json").json()["result"]["data"]["contests"]["edges"]
        results = []

        for contest in cdata:
            c = contest["node"]
            end_time = datetime.strptime(c["end_time"],'%Y-%m-%dT%H:%M:%S.%fZ')

            if end_time <= now:
                continue

            c["max_reward"] = self._amountToDecimal(c["amount"])
            c["repos"] = [c["repo"]]
            c["name"] = c["title"]

            results.append(c)

        self.data = results
        return self

    
def getMaxRewardCutoffFromArgs():
    for a in sys.argv:
        if a.startswith("minReward="):
            return int(a[len("minReward="):])
    return MIN_REWARD_CUTOFF

if __name__ == "__main__":
    import sys

    programs = []

    if "immunefi" in sys.argv:
        programs.append(ImmunefiCompanion())
    if "code4rena" in sys.argv or "code4" in sys.argv or "c4" in sys.argv:
        programs.append(Code4renaCompanion())

    if not len(programs):
        if "noask" not in sys.argv:
            print("⚠️ You are about to run this script on ALL bug bounty platforms (currently: C4 AND Immunefi)!")
            yno = input("Continue? [yN] (note: use cmdline arg 'noask' to skip )")
            if yno != "y":
                raise Exception("abort") 

        programs = [Code4renaCompanion(), ImmunefiCompanion()]


    arg_min_reward = getMaxRewardCutoffFromArgs()
    

    for ic in programs:

        if "sync" in sys.argv:
            bounties = ic.getRepos().data
            ic._saveRepo()
        else:
            bounties = ic.loadRepo().data
            
        
        num_repos = 0  
        num_bounties_selected = 0 
        
        for bounty in reversed(sorted(bounties, key=lambda x: int(x['max_reward']))):
            if int(bounty["max_reward"]) < arg_min_reward: continue
            if not len(bounty["repos"]): continue
            num_bounties_selected += 1

            repos = bounty["repos"]
            if "unique" in sys.argv:
                repos = ic.getUniqeRepos(bounty["repos"])

            num_repos += len(repos)
            print("%-30s : $$ %-30s" % (bounty["name"], bounty["max_reward"]))
            for k in repos:
                if "#" in k: continue
                print("   ➡️ %s"%k)

                if "clone" in sys.argv:
                    ic.gitClone(OUTPATH, bounty["name"], k) # TODO: maybe handle path exists; it will just error right now

        print("=============================")
        print(ic.__class__.__name__)
        print("-----------------")
        print("total bounties: %d"%len(bounties))
        print("")
        print("min_reward: %d"%arg_min_reward)
        print(" - selected bounties: %d"%num_bounties_selected)
        print(" - selected repos: %d"%num_repos)
    
