# Table of Content

* [Introduction](#introduction)
* [Installation](#installation)
    * [Non-developers](#non-developers)
    * [Developers](#developers)
* [Usage](#usage)
    * [Quick Start](#quick-start)
    * [Config](#config)
    * [Keystore](#keystore)
    * [Whitelist](#whitelist)
    * [Wallet](#wallet)
    * [tons-interactive](#tons-interactive)
    * [Contract](#contract)
    * [Development](#development)
    * [toncli](#toncli)


# Introduction

**tons** (TON Stash) is an Open Source cross-platform wallet application
and command-line interface to maintain any type of wallet on the TON network
on desktops and servers. Works with Windows/Mac/Linux.

*keystore* - is a file encrypted by a user's password.
It is used to store private keys from user's wallets.

*whitelist* - is a file which stores all user's contacts.
User have to use it to transfer coins from their wallets to other addresses.

*dapp* - allows user to connect to TON blockchain.
See [config](#config) section to understand how to set it up properly.


# Installation


## Non-developers

As a non-developer user, you should use **tons-intecractive** version.


### Mac OS

Start a terminal application and enter the following command.

```bash
$ sh -c "$(curl -sSfL https://raw.githubusercontent.com/tonfactory/temp_tons_install/master/install)"
```

To run **tons-interactive** enter 'tons-interactive' in the terminal

```bash
$ tons-interactive
[?] Pick command: Keystores
 > Keystores
   Whitelist
   Config
   Exit
```


## Developers

**tons** is a python package. Use pip (python package manager) to install it

```bash
$ mkdir ~/my-ton-workdir/ && cd ~/my-ton-workdir/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install tons
```


# Usage


## Quick start

Create .tons folder in the current directory

```bash
$ tons init
```

Set TON network

```bash
$ tons config --network testnet
```

Create a keystore and set it as a current keystore

```bash
$ tons keystore new myFirstKeystore
Password []:

$ tons config tons.keystore_name myFirstKeystore
```

Create a wallet

```bash
$ tons wallet create pocketMoney --save-to-whitelist myPocketMoney
```

Add a whitelist contact

```bash
$ tons whitelist add myBestFriend EQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjZWW
```

Transfer coins from the wallet to the contact

```bash
tons transfer pocketMoney myBestFriend 10 --message "Happy birthday!"
```

To get all available subcommands and flags run a command with a '-h' flag

```bash
$ tons -h
Usage: tons [OPTIONS] COMMAND [ARGS]...

Options:
  --version      Show the version and exit.
  -c, --config   Use specific config.yaml file
  -h, --help     Show this message and exit.

Commands:
  config     Control config parameters (check README.md for all fields info)
  contract   Operate with contracts
  dev        Development tools
  init       Initialize .tons workdir in a current directory
  keystore   Operate with keystores
  wallet     Operate with wallets
  whitelist  Operate with whitelist contacts

$ tons wallet -h
...
```


## Config

**tons** uses the following file structure:

```
.tons
├── config.yaml
├── whitelist.json
├── keystores
│   ├── *.keystore
```

Every time **tons** reads settings in the way where a next config alters previous one

1. *global*: `~/.config/tons/`
2. *local*: `./..N/.tons/` (where N {0, inf} any number of subdirectories)
*Note: to init tons locally run 'tons init' command*
3. *env*: `export TONS_CONFIG_PATH=~/your/own/path/.tons/`

All config.yaml parameters

| Name                        | Description                                                 |
|:----------------------------|:------------------------------------------------------------|
| tons.workdir                | directory where whitelist and keystores are stored          |
| tons.keystore_name          | name of the keystore a person wants to use                  |
| tons.provider               | provider to access the TON blockchain                       |
| tons.default_wallet_version | the version that will be used during tons wallet create cmd |
| tons.warn_if_outdated       | every run checks whether there is a new version of tons pkg |
| provider.dapp.api_key       | api key for the dapp (TODO: type bot's name)                |
| provider.dapp.network       | TON network to use (mainnet/testnet)                        |

List parameters of all configs (global/local/env)
```bash
$ tons config --list
...
~/local/path/.tons/config.yaml  tons.keystore_name=dev.keystore
...
~/.config/.tons/config.yaml tons.keystore_name=global.keystore
```

List all values of final altered config
```bash
$ tons config --current-setup
tons.workdir=/Users/username/.config/.tons
tons.keystore_name=dev.keystore
tons.provider=dapp
tons.default_wallet_version=v3r2
tons.warn_if_outdated=True
provider.dapp.api_key=YOUR_API_KEY
provider.dapp.network=testnet
```

Change the network
```bash
$ tons config --network testnet
```

Set value of a parameter
```bash
$ tons config --global tons.keystore_name myKeystore2
```

Unset value of a parameter
```bash
$ tons config --local tons.keystore_name --unset
```

Get value of a parameter
```bash
$ tons config tons.keystore_name
dev.keystore
```


## Keystore

Keystore is encrypted by user's password. 
There are several options to work with a password:
1. Runs a command and enter it through input
```bash
$ tons keystore new
Password []: 
```
2. Runs a command with a --password flag
```bash
$ tons keystore new --password admin123
Password []: 
```
3. Set up environment variable TONS_KEYSTORE_PASSWORD
```bash
$ export TONS_KEYSTORE_PASSWORD=admin123
$ tons keystore new
```

List all keystores in a tons.workdir
```bash
$ tons keystore list
dev.keystore
test.keystore
```

Create a new keystore
```bash
$ tons keystore new myNewKeystore
Password []: 
```

Backup a keystore (password is used to export private keys)
```bash
$ tons keystore backup myNewKeystore ./myNewKeystore.backup
Password []: 
```

Restore a keystore (password is used for a new keystore)
```bash
$ tons keystore restore keystoreFromBackup ./myOldKeystore.backup
Password []: 

# to restore keystore from ton-cli's keystore add flag --from-ton-cli
$ tons keystore restore keystoreFromBackup ./ton-cli.backup --from-ton-cli
Password []: 
```


## Whitelist

List all contacts with verbose information (can be redirected to .md file)

```bash
$ tons whitelist list --verbose --currency nanoton
| Name            |                     Address                      |  State   |        Balance |
|:----------------|:------------------------------------------------:|:--------:|---------------:|
| My Wallet 01    | EQC96BhaxqhdK-pwvcBudu-WCtjBFMjPbAqoL7qMKc6rd2U2 |  Uninit  |            0.0 |
| My Wallet 02    | EQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjZWW |  Uninit  |            0.0 |

$ tons whitelist list --verbose > contacts_info.md
```

Add new contact
```bash
$ tons whitelist add myFriend EQC96BhaxqhdK-pwvcBudu-WCtjBFMjPbAqoL7qMKc6rd2U2
```

Edit contact
```bash
$ tons whitelist edit myFriend --name myBestFriend --address EQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjZWW
```

Delete contact
```bash
$ tons whitelist delete myFriend
```

Get address info of a contact
```bash
$ tons whitelist get myFriend
Raw address: 0:4fe5a10f96614daf8792dc3270db2742e17fe13ae9b0668a827098075524078d
Nonbounceable address: UQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjchT
Bounceable address: EQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjZWW
```


## Wallet

Wallets support same CRUD operations
```bash
$ tons wallet create myMain \
        --version v3r2 \
        --workchain 0 \
        --subwallet-id 698983191 \
        --comment "My main secure wallet" \
        --save-to-whitelist myMain

$ tons wallet edit myMain --name myMainOld

$ tons wallet delete myMain
Are you sure you want to delete v2wallet wallet? [y/N]: y

$ tons wallet get myMain
Raw address: 0:4fe5a10f96614daf8792dc3270db2742e17fe13ae9b0668a827098075524078d
Nonbounceable address: UQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjchT
Bounceable address: EQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjZWW
Version: v3r2
Workchain: 0
Subwallet id: 698983191
Comment: My main secure wallet
--- Verbose wallet information ---
address: EQBP5aEPlmFNr4eS3DJw2ydC4X_hOumwZoqCcJgHVSQHjZWW
contract_type: None
seqno: 1
state: Active
balance: 0.394748632
last_activity: 2022-10-07 08:58:00
code: te6cckEBAQEAcQAA3v8AIN0gggFMl7ohggEznLqxn3Gw7UTQ0x/THzHXC//jBOCk8mCDCNcYINMf0x/TH/gjE7vyY+1E0NMf0x/T/9FRMrryoVFEuvKiBPkBVBBV+RDyo/gAkyDXSpbTB9QC+wDo0QGkyMsfyx/L/8ntVBC9ba0=
data: te6cckEBAQEAKgAAUAAAAAEpqaMXz1s51azqoYZWn7ZR2NlTfwg7FABigSY991WpcgOjOlg2uqR/
```

List all wallets (can be redirected to .md file)
```bash
$ tons wallet list -v -c nanoton
| Name        | Version | WC |                     Address                      | Comment            | State  |            Balance |
|:------------|:-------:|:--:|:------------------------------------------------:|:-------------------|:------:|-------------------:|
| dev         |   v3r2  | 0  | Eaddraddraddraddraddraddraddraddraddraddraddradd | Development wallet | Active |      182.349713128 |
| masterchain |   v3r2  | -1 | Eaddraddraddraddraddraddraddraddraddraddraddradd | None               | Active |        0.328599221 |
| newTest     |   v3r2  | 0  | Eaddraddraddraddraddraddraddraddraddraddraddradd |                    | Active |        0.095227164 |
| testmsg     |   v3r2  | 0  | Eaddraddraddraddraddraddraddraddraddraddraddradd | None               | Active |        0.394748632 |
| v2wallet    |   v2r2  | -1 | Eaddraddraddraddraddraddraddraddraddraddraddradd | None               | Uninit |                0.0 |
| Total       |         |    |                                                  |                    |        | 183.16828814499996 |

$ tons wallet list -v > wallet_info.md
```

Import wallet from mnemonic
```bash
$ tons wallet import-from-mnemonics importedWallet v4r2 0 "your 24 mnemo ... words" \
         --subwallet-id 698983191 \
         --comment "My imported wallet" \
         --save-to-whitelist myImportedWallet
```

Init wallet (address must have some coins to be initialized)
```bash
$ tons wallet init myMain
```

Reveal a wallet mnemonics
```bash
$ tons wallet reveal myMain
Password []: 
guitar border swap border actor history universe wrist width mask unveil again dentist tilt theory risk electric flash hat sentence essence able dice mammal
```

Export wallet to .addr and .pk files (e.g. to use in toncli development tool)
```bash
$ tons wallet to-addr-pk myMain ./destination/path/
```

Transfer coins from a wallet to a contact
```bash
$ tons wallet transfer myMain myFriend 10 \
        --message "Happy Birthday!" \
        --wait \
        --bounceable n \
        --pay-gas-separately y \
        --ignore-errors n \
        --destroy-if-zero n \
        --transfer-all n
```


## tons-interactive

For daily usage user may prefer tons-interactive version

```bash
$ tons-interactive
[✓] Pick command: Keystores
[✓] Pick command: Open keystore
[✓] Choose keystore to use: dev.keystore
[?] Pick command: List wallets
 > List wallets
   Transfer
   Create wallet
   Init wallet
   Get wallet
   Edit wallet
   Delete wallet
   Reveal wallet mnemonics
   Import from mnemonics
   Wallet to .addr and .pk
   Backup keystore
   Back
```


## Contract

Contract allows a user to interact with any contract types in the TON blockchain.

Get balance of a contract
```bash
$ tons contract --wallet myMain balance
182.349713128
```

Get seqno of a contract
```bash
$ tons contract --contact myFriend seqno
5
```

Get full info of a contract
```bash
$ tons contract --address EQAhE3sLxHZpsyZ_HecMuwzvXHKLjYx4kEUehhOy2JmCcHCT info
address: EQAhE3sLxHZpsyZ_HecMuwzvXHKLjYx4kEUehhOy2JmCcHCT
contract_type: None
seqno: 1
state: Active
balance: 531223445.66058564
last_activity: 2022-10-07 06:42:24
code: te6cckECKQEAA/cAART/APSkE/S88sgLAQIBIAIDAgFIBAUE2vIgxwCOgzDbPOCDCNcYIPkBAdMH2zwiwAAToVNxePQOb6Hyn9s8VBq6+RDyoAb0BCD5AQHTH1EYuvKq0z9wUwHwCgHCCAGDCryx8mhTFYBA9A5voSCYDqQgwgryZw7f+COqH1NAufJhVCOjU04eIR8gAgLMBgcCASAMDQIBIAgJAgFmCgsAA9GEAiPymAvHoHN9CYbZ5S7Z4BPHohwfIwAtAKkItdJEqCTItdKlwLUAdAT8ArobBKAATwhbpEx4CBukTDgAdAg10rDAJrUAvALyFjPFszJ4HHXI8gBzxb0AMmACASAODwIBIBQVARW77ZbVA0cFUg2zyCgCAUgQEQIBIBITAXOxHXQgwjXGCD5AQHTB4IB1MTtQ9hTIHj0Dm+h8p/XC/9eMfkQ8qCuAfQEIW6TW3Ey4PkBWNs8AaQBgJQA9rtqA6ADoAPoCAXoCEfyAgPyA3XlP+AXkegAA54tkwAAVrhlXQQDVZnah7EACASAWFwIBSBgZAVG3JVtnhiZGakYQCB6BzfQxwk2EWkAAMxph5i4AWuAmHAtv7hwLd3RuECEBhbVZm2eGq+Bv7bHGiiJwCB6PjfSkEcRgWkAAMcNEEAIa5CS64GT2E5kAOeLKhACQCB6IYFImHFImHFImXEA2YlzNiDAhAgEgGhsCA5k4HB0BEawabZ4vgbYJQCEAFa35QQDMlXah7BhAAQ2pNs8FV8FgIQAVrdws4IBqsztQ9iACINs8AvJl+ABQQ3FDE9s87VQhKAAK0//TBzAEoNs8L65TILDyYhKxAqQls1McubAlgQDhqiOgKLyw8mmCAYag+AEFlwIREAI+PjCOjREQH9s8QNd49EMQvQXiVBZbVHPnVhBT3Ns8VHEKVHq8IiMmJAAg7UTQ0x/TB9MH0z/0BPQE0QBIAY4aMNIAAfKj0wfTB1AD1wEg+QEF+QEVuvKkUAPgbCFwVCATAAwByMv/ywcE1ts87VT4D3AlblOJvrGYEG4QLVDHXwePGzBUJANQTds8UFWgRlAQSRA6SwlTuds8UFQWf+L4AAeDJaGOLCaAQPSWb6UglDBTA7neII4WODk5CNIAAZfTBzAW8AcFkTDifwgHBZJsMeKz5jAGKCUmJwBgcI4pA9CDCNcY0wf0BDBTFnj0Dm+h8qXXC/9URUT5EPKmrlIgsVIDvRShI27mbCIyAH5SML6OIF8D+ACTItdKmALTB9QC+wAC6DJwyMoAQBSAQPRDAvAHjhdxyMsAFMsHEssHWM8BWM8WQBOAQPRDAeIBII6KEEUQNEMA2zztVJJfBuIoABzIyx/LB8sHyz/0APQAyc+7oJU=
data: te6cckEBCwEA5wACHQAAAAEFA2JIYo0AAAAA4AECAgHLAwQAE6AxKLsWAAAAACACASAFBgBD0hjXSLxNT0/5NIH9QcOZRdVYe44qotijXq+Z7uktm6lgBAIBIAcIAgEgCQoAQyyRVFPHNrdpK1tMdvOpDmrux6At6Ydsil7uWJwQRyOhgCAAQwd3bNaR++E+iR7W29FUYcCYsblcgir2Bb6NwzHn1FVxACAAQzgX3I3jBXNLDIo60FJk6XZaBKOdvgPdmXOqYSph92bXwCAAQx+MZxR866FwDTUD5UwIIPll9PguUhDpoyJKd2yPP60YQCCZhU9l
```

## Development
A person can deploy smart-contracts using tons and [tonsdk](https://github.com/tonfactory/tonsdk). 
There are three options: send-boc, send-internal and send-external.

Send internal allows a user to send any internal message using any of their wallets
```bash
$ tons dev send-internal ./scripts/deploy.py deploy_through_internal MY_WALLET_NAME 0.1 --wait
```
```python
# ./scripts/deploy.py example. 
# Function must receive WalletContract and  return (str, Optional[Cell], Optional[Cell]) values.

from typing import Optional

from tonsdk.contract.wallet import WalletContract
from tonsdk.boc import Cell
from tonsdk.contract.token.ft import JettonMinter


def deploy_through_internal(wallet: WalletContract) -> (str, Optional[Cell], Optional[Cell]):
    minter = JettonMinter(admin_address=wallet.address,
                          jetton_content_uri="URL",
                          jetton_wallet_code_hex='CODE')

    return minter.address.to_string(), minter.create_state_init()["state_init"], None
```

Send external allows a user to create an external message using tonsdk and send it to the TON blockchain
```bash
$ tons dev send-external ./scripts/deploy.py deploy_through_external --wait
```
```python
# ./scripts/deploy.py example. 
# Function must receive nothing and return (str, Cell) values.
from tonsdk.contract.wallet import WalletContract, WalletVersionEnum, Wallets
from tonsdk.boc import Cell


def deploy_through_external() -> (str, Cell):
    wallet_workchain = 0
    wallet_version = WalletVersionEnum.v3r2
    wallet_mnemonics = "YOUR 24 ... WORDS".split(" ")

    _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(
        wallet_mnemonics, wallet_version, wallet_workchain)
    return wallet.address.to_string(), wallet.create_init_external_message()["message"]
```

*Note: to deploy a wallet one can use '$ tons wallet init WALLET_NAME'*

Send boc allows to send a .boc file to the TON blockchain
```bash
$ tons dev send-boc ./generated-through-fif.boc --wait
```

### integrations
Example of automatic salary payment, you may use cron to run pay_salary.sh

```bash
$ cat employee.info
employee1 EQDvtizebIVTGYASXgjYX5sHfkGLW8aFTa7wfYCyARIpARB0 10
employee2 EQA-Ri7Oftdjq--NJmuJrFJ1YqxYk6t2K3xIFKw3syhIUgUe 20
employee3 EQCNLRRZkvoqAW6zwYyy_BVwOBcMnwqvyrSpm8WnACdzXuu3 15.5

$ cat pay_salary.sh
cd ~/team_workspace/ton/
source venv/bin/activate
tons config tons.keystore_name myKeystore

input="./employees.info"
while IFS= read -r line
do
    stringarray=($line)
    name=${stringarray[0]}
    addr=${stringarray[1]}
    salary=${stringarray[2]}

    tons wallet transfer salaryWallet $name $salary --wait
done < "$input"
```

## toncli

[toncli](https://github.com/disintar/toncli) uses deploy wallet with the following params:
- version v3r2
- subwallet-id 0
- workchain 0

First a developer should create a tons wallet
```bash
$ tons wallet create toncli-deployer -v v3r2 -w 0 -id 0 --save-to-whitelist toncli-deployer
```

Then get the path of toncli deploy wallet
```bash
$ python
>>> from appdirs import user_config_dir
>>> import os
>>> user_config_dir("toncli")  # output may be different
/Users/username/Library/Application Support/toncli
>>> os.path.join(user_config_dir("toncli"), "wallet", "build")  # output may be different
/Users/username/Library/Application Support/toncli/wallet/build
```

Finally, replace toncli default wallet with the tons one
```bash
$ tons wallet to-addr-pk toncli-deployer '/Users/username/Library/Application Support/toncli/wallet/build'
$ cd '/Users/username/Library/Application Support/toncli/wallet/build'
$ mv contract.pk backup_old.pk && mv contract.addr backup_old.addr
$ mv toncli-deployer.pk contract.pk && mv toncli-deployer.addr contract.addr
```
