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
            $ bugbounty.py unique
        (c) clone all repos (dryrun)
            $ bugbounty.py unique clone 
        (d) clone all repos (actually do it)
            $ bugbounty.py unique clone no-dryrun


        # NOTE: default output folder is $(pwd)/bugbounty_repos/<project>

    (2) run your fancy tools/code-smell rules on it
    (3) profit $$
    
Consider donating if you win a $mm 🥳
"""

import requests
import re
import json
import os


##### CONFIG THIS
MAX_REWARD_CUTOFF = 100_000   # only check out projects with max bounty >= 100_000 $$ 
OUTPATH = os.path.abspath("./bugbounty_repos")   # abspath to main repo checkout dir
##### NO CHANGES BEYOND THIS LINE


class ImmunefiCompanion(object):
    REX_VALID_PROJECT = re.compile(r'[a-zA-Z0-9\_\-]+')

    def __init__(self, repofile="immunefi_repos.json"):
        self.repofile = repofile
        self.data = []

    def loadRepo(self):
        with open(self.repofile, 'r') as f:
            self.data = json.load(f)
        return self

    def _saveRepo(self):
        with open(self.repofile, 'w') as f:
            f.write(json.dumps(self.data))
        return self

    def getRepos(self):
        all_projects = re.findall("href=\"/bounty/([^\"]+)\"", requests.get("https://immunefi.com/explore/?filter=immunefi").text)
        print("found %d projects"%len(all_projects))

        results = self.data

        for nr,p in enumerate(all_projects):
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

    def getUniqeRepos(self, repos):
        return sorted(set([ "/".join(r.split("/")[0:5]) for r in repos]))


    def gitClone(self, basedir, project, giturl):
        assert(self.REX_VALID_PROJECT.match(project))
        cmd = "mkdir -p %s/%s; cd %s/%s && git clone --depth=1 %s"%(basedir, project, basedir, project, giturl)
        
        if "no-dryrun" in sys.argv:
            os.system(cmd)
        print(cmd)

if __name__ == "__main__":
    import sys

    ic = ImmunefiCompanion()

    if "sync" in sys.argv:
        bounties = ic.getRepos().data
    else:
        bounties = ic.loadRepo().data
    
    num_repos = 0  
    num_bounties_selected = 0 
     

    for bounty in reversed(sorted(bounties, key=lambda x: int(x['max_reward']))):
        if int(bounty["max_reward"]) < MAX_REWARD_CUTOFF: continue
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
    print("total bounties: %d"%len(bounties))
    print("")
    print("min_reward: %d"%MAX_REWARD_CUTOFF)
    print(" - selected bounties: %d"%num_bounties_selected)
    print(" - selected repos: %d"%num_repos)
    
