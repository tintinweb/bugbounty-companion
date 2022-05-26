# BugBounty Companion 

<sup>
Up your game by being more efficient than others! 🤓
</sup>


A BugBounty companion script for [Immunefi](https://immunefi.com/explore/) to checkout all high-reward bug bounty code-bases (use at own risk). 

<br>

* **TLDR;** clone all **Immunefi** Repositories filtered by the highest bugbounty payout amount.

<sup>
⚠️ shell-executes stuff without checking! USE AT OWN RISK :D 
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
            
## Cool, but when Lambo 🏎️?

* Check for similar issues in all code-bases
* Run your tools, code-smell detectors
* Submit Bugs for Bounties
* 👉 Lambo 🏎️ $$ 🥳🥳
    
# Donate

Got rich? Consider giving back by supporting the community ❤️ thanks 🙏 ([github/sponsor](https://github.com/sponsors/tintinweb))

<sup>
Be a Hero, tip a 🍺 🙂 ⟶ Ƀ: 1AZMeGVfCBbYwVYyG9s79pJDyocTZgiApa | Ξth: 0x438B38E30eF117C15fBfF833f9C2c70182925815
</sup>
