# bmrcli

Command-line utility for managing BMR HC64 heating controller configuration.

Features:

- save controller configuration into a YAML file
- load controller configuration from a YAML file

Product page: https://www.bmr.cz/produkty/regulace-topeni/rnet

## Install

```
pip install bmrcli
```

## Usage

To get the current config from the heating controller:

```
bmrcli http://username@password:192.168.1.32 dump > bmr-config.yaml
```

To load configuration into the heating controller:

```
bmrcli http://username@password:192.168.1.32 load < bmr-config.yaml
```

# License

MIT
