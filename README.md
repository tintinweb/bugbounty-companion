# BugBounty Companion 

<sup>
Up your game by being more efficient than others! 🤓
</sup>


Checkout high-reward yielding bug bounty projects, run your scripts to find bugs before others do, submit reports for bounties, win! Scale your bug bounty hunting efforts.

The BugBounty companion is a script that lets you quickly check out source-code from bug bounty programs on various platforms. Currently supporting [Immunefi](https://immunefi.com/explore/) and [C4](https://code4rena.com/) 🙌 

<br>

**TLDR;** clones **Immunefi/C4** Repositories filtered by the highest rewards.

<sup>
⚠️ HACKY SCRIPT! - shell-executes stuff without checking! USE AT OWN RISK. dry-run first! 
</sup>

## Supported Platforms

* [Immunefi](https://immunefi.com/explore/)

<a href="https://immunefi.com/explore/"><img width="400" alt="image" src="https://user-images.githubusercontent.com/2865694/171031969-2e62159b-788d-4a9d-b240-af20982c0b09.png"></a>

* [C4](https://code4rena.com/)

<a href="https://code4rena.com/"><img width="400" alt="image" src="https://user-images.githubusercontent.com/2865694/171032003-99fc1ca6-e178-49be-8e69-008d2895a530.png"></a>


## Usage

```
$ bugbounty.py (code4rena|immunefi) [sync|unique|clone|no-dryrun|noask]
```

**default output folder** is `$(pwd)/bugbounty_repos/<project>`

### Examples

* sync with c4 website and dump results to json file
```
$ bugbounty.py code4rena sync [unique]
```

* alternatively sync with all supported websites and dump results to json file
```
$ bugbounty.py sync [unique]
```

* show unique repos in cache
```
$ bugbounty.py unique
```

* (dry-run) clone all unique repos (optionally only projects with >100_000 rewards)
```
$ bugbounty.py unique clone [maxReward=100000]
```

* (actually) clone all unique repos (optionally only projects with >100_000 rewards)
```
$ bugbounty.py unique clone no-dryrun [maxReward=100000]
```

#### Demo


```
tintin@takeshii:~/workspace/solidity/bugbounty-companion|main⚡ 
⇒  python3 bugbounty.py unique minReward=1000
⚠️ You are about to run this script on ALL bug bounty platforms (currently: C4 AND Immunefi)!
Continue? [yN]y
1000
OpenSea Seaport contest        : $$ 1000000                       
   ➡️ https://github.com/code-423n4/2022-05-opensea-seaport
Notional x Index Coop          : $$ 75000                         
   ➡️ https://github.com/code-423n4/2022-06-notional-coop
Backd Tokenomics contest       : $$ 75000                         
   ➡️ https://github.com/code-423n4/2022-05-backd
veToken Finance contest        : $$ 75000                         
   ➡️ https://github.com/code-423n4/2022-05-vetoken
Velodrome Finance contest      : $$ 75000                         
   ➡️ https://github.com/code-423n4/2022-05-velodrome
ChainSafe contest              : $$ 70000                         
   ➡️ https://github.com/code-423n4/2022-05-chainsafe
=============================
total bounties: 6

min_reward: 1000
 - selected bounties: 6
 - selected repos: 6
wormhole/                      : $$ 10000000                      
   ➡️ https://github.com/certusone/wormhole
makerdao/                      : $$ 10000000                      
   ➡️ https://github.com/dapphub/ds-weth
   ➡️ https://github.com/makerdao/arbitrum-dai-bridge
   ➡️ https://github.com/makerdao/clipper-mom
   ➡️ https://github.com/makerdao/dss
   ➡️ https://github.com/makerdao/dss-auto-line
   ➡️ https://github.com/makerdao/dss-cdp-manager
   ➡️ https://github.com/makerdao/dss-chain-log
   ➡️ https://github.com/makerdao/dss-exec-lib
   ➡️ https://github.com/makerdao/dss-gem-joins
   ➡️ https://github.com/makerdao/dss-interfaces
   ➡️ https://github.com/makerdao/dss-proxy-actions
   ➡️ https://github.com/makerdao/dss-psm
   ➡️ https://github.com/makerdao/dss-vest
   ➡️ https://github.com/makerdao/esm
   ➡️ https://github.com/makerdao/exchange-callees
   ➡️ https://github.com/makerdao/ilk-registry
   ➡️ https://github.com/makerdao/median
   ➡️ https://github.com/makerdao/optimism-dai-bridge
   ➡️ https://github.com/makerdao/osm
aurora/                        : $$ 6000000                       
   ➡️ https://github.com/aurora-is-near/aurora-engine
   ➡️ https://github.com/aurora-is-near/near-erc20-connector
   ➡️ https://github.com/aurora-is-near/rainbow-bridge
   ➡️ https://github.com/aurora-is-near/rainbow-token-connector
   ➡️ https://github.com/aurora-is-near/sputnikvm
   ➡️ https://github.com/near-daos/sputnik-dao-contract
chain/                         : $$ 5000000                       
   ➡️ https://github.com/chain/chain-token
   ➡️ https://github.com/chain/governance
   ➡️ https://github.com/chain/staking
gmx/                           : $$ 5000000                       
   ➡️ https://github.com/gmx-io/gmx-contracts
olympus/                       : $$ 3333333                       
   ➡️ https://github.com/OlympusDAO/olympus-contracts
thegraph/                      : $$ 2500000                       
   ➡️ https://github.com/graphprotocol/agora
   ➡️ https://github.com/graphprotocol/graph-node
   ➡️ https://github.com/graphprotocol/indexer
balancer/                      : $$ 2400000                       
   ➡️ https://github.com/balancer-labs/balancer-v2-monorepo
tribedao/                      : $$ 2200000                       
   ➡️ https://github.com/Rari-Capital/compound-protocol
   ➡️ https://github.com/fei-protocol/fei-protocol-core
zksync/                        : $$ 2100000                       
   ➡️ https://github.com/matter-labs/zksync
optimism/                      : $$ 2000042                       
   ➡️ https://github.com/ethereum-optimism/optimism
   ➡️ https://github.com/ethereum/devp2p
lidoonpolygon/                 : $$ 2000000                       
   ➡️ https://github.com/Shard-Labs/PoLido
zodiac/                        : $$ 2000000                       
   ➡️ https://github.com/gnosis/zodiac
multichain/                    : $$ 2000000                       
   ➡️ https://github.com/anyswap/Anyswap-Audit
celer/                         : $$ 2000000                       
   ➡️ https://github.com/celer-network/sgn-v2-contracts
polygon/                       : $$ 2000000                       
   ➡️ https://github.com/fx-portal/contracts
   ➡️ https://github.com/maticnetwork/contracts
   ➡️ https://github.com/maticnetwork/genesis-contracts
   ➡️ https://github.com/maticnetwork/pos-portal
arbitrum/                      : $$ 2000000                       
   ➡️ https://github.com/OffchainLabs/arb-os
   ➡️ https://github.com/OffchainLabs/arbitrum
...
=============================
total bounties: 288

min_reward: 1000
 - selected bounties: 214
 - selected repos: 365
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
  * e.g. [semgrep](https://semgrep.dev/) - semgrep now supports solidity! write patterns, find bugs, at scale 
* Submit Bugs for Bounties
* 👉 Lambo 🏎️ $$ 🥳🥳
    
# Donate

Got rich? Consider giving back by supporting the eth security community and [my projects](https://github.com/sponsors/tintinweb)  ❤️ 🙏

<sup>
Be a Hero, tip a 🍺 🙂 ⟶ Ƀ: 1AZMeGVfCBbYwVYyG9s79pJDyocTZgiApa | Ξth: 0x438B38E30eF117C15fBfF833f9C2c70182925815
</sup>
