# Ink Wizard

Ink Wizard is a CLI tool used to scaffold Flipper, PSP-22, PSP-34, PSP-37 smart contracts. CLI will ask user on what kind of functionality user needs. It will scaffold smart contracts based on user options.

Ink Wizard uses [OpenBrush](https://openbrush.io) smart contracts. Once you scaffold smart contracts, you can go to the Open Brush docs: https://docs.openbrush.io/ for further steps.


# Installation

You can install `ink-wizard` either via pip or via homebrew(recommended).
If you want to install using pip, it is recommended to use virtualenv.

```sh
virtualenv .venv
source .venv/bin/activate
pip install ink-wizard
```

It you want to install it using homebrew, run the following commands:

```sh
brew tap avirajkhare00/homebrew-ink-wizard
brew install ink-wizard
```

Just type `ink-wizard`, you are good to go.

# Usage

In order to use ink-wizard, you should have `cargo-contract` installed. Run the following command to install it:
```sh
cargo install cargo-contract --version 2.0.0-beta
```

When a smart contract is scaffolded, you can go to the directory and can run `cargo-contract contract build`. It will generate .contract, wasm and metadata.json file that you can use.

# Testing

You can test it either via running `./test.sh` file or you can run tests inside a docker container via `docker build .`
To run tests locally:
```sh
virtualenv .venv
pip install -r requirements.txt
./test.sh
```

Or you can run `docker build .` to run the tests.
