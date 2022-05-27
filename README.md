# BugBounty Companion 

<sup>
Up your game by being more efficient than others! 🤓
</sup>


A BugBounty companion script for [Immunefi](https://immunefi.com/explore/) 🙌 Checkout high-reward yielding bug bounty projects and scale your bug bounty hunting.

<br>

**TLDR;** clones **Immunefi** Repositories filtered by the highest rewards.

<sup>
⚠️ HACKY SCRIPT! - shell-executes stuff without checking! USE AT OWN RISK :D 
</sup>

## Usage

```
$ bugbounty.py [sync|unique|clone|no-dryrun]
```

**default output folder** is `$(pwd)/bugbounty_repos/<project>`

## Examples

* sync with immunefi website and dump results to json file
```
$ bugbounty.py sync [unique]
```

* show unique repos in cache
```
$ bugbounty.py unique
```

* (dry-run) clone all unique repos
```
$ bugbounty.py unique clone 
```

* (actually) clone all unique repos 
```
$ bugbounty.py unique clone no-dryrun
```

### I don't know what to do?!

<sup>
⚠️ PSA: Reminder, this script is an ugly hack but it works :D USE AT OWN RISK. 
</sup>

```
$ bugbounty.py sync unique      # 1) download bounty info and cache it; filter unique repos
$ bugbounty.py unique clone     # 2) dry-run clone - dblcheck if this is what you do
$ bugbounty.py unique clone no-dryrun    # 3) actually checkout all the repos to $(pwd)/bugbounty_repos/<project>
```
            
## Cool, but when Lambo 🏎️?

* Check for similar issues in all code-bases
* Run your tools, code-smell detectors
  * e.g. [🐞 semgrep](https://semgrep.dev/)
* Submit Bugs for Bounties
* 👉 Lambo 🏎️ $$ 🥳🥳
    
# Donate

Got rich? Consider giving back by supporting the eth security community and [my projects](https://github.com/sponsors/tintinweb)  ❤️ 🙏

<sup>
Be a Hero, tip a 🍺 🙂 ⟶ Ƀ: 1AZMeGVfCBbYwVYyG9s79pJDyocTZgiApa | Ξth: 0x438B38E30eF117C15fBfF833f9C2c70182925815
</sup>
