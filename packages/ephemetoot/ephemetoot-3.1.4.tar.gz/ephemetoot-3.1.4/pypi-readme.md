# 🥳 ==> 🧼 ==> 😇

## Prior work
The initial `ephemetoot` script was based on [this tweet-deleting script](https://gist.github.com/flesueur/bcb2d9185b64c5191915d860ad19f23f) by [@flesueur](https://github.com/flesueur)

`ephemetoot` relies heavily on the [Mastodon.py](https://pypi.org/project/Mastodon.py/) package by [@halcy](https://github.com/halcy)

## Usage

You can use `ephemetoot` to delete [Mastodon](https://github.com/tootsuite/mastodon) toots that are older than a certain number of days (default is 365). Toots can optionally be saved from deletion if:
* they are pinned; or
* they include certain hashtags; or
* they have certain visibility; or
* they are individually listed to be kept

There are various options controlling timing, scheduling, and output.

Run from the command line with `ephemetoot`.

Run `ephemetoot --help` or read the docs for all options.

## Contributing

ephemetoot is packaged using `poetry` and tested using `pytest`.

For all bugs, suggestions, pull requests or other contributions, please check the [contributing guide](https://github.com/hughrun/ephemetoot/blob/master/docs/contributing.md).
