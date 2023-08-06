# Jupyter Custom Sort

This module provides both a Jupyter server extension an a (classic) notebook extension that allow custom sorting of files in the directory views in Jupyter.  This is useful for ordering notebooks, without adjusting their file names to be alphabetical.

## Installation

The module can be installed with pip:
```
pip install jupytercustomsort
```

Then, both the server and notebook extensions need to be installed and enabled:
```
jupyter serverextension enable --py jupytercustomsort
jupyter nbextension install --py jupytercustomsort
jupyter nbextension enable --py jupytercustomsort
```
You may wish to add the `--user` flag to these commands to install and enable the extensions for the current user only.

## Usage

To cause a directory to be specially sorted, add to it a JSON file named `.custom_order` like so:
```json
{
  "order": [
    "First.ipynb",
    "Second.ipynb",
    "Third.ipynb"
  ]
}
```

When this directory is viewed in Jupyter, the custom sort will be automatically applied.  The different types of files (directories / notebooks / other files) will still be segregated, but within each group, files specified in the _order_ list will appear in that relative order.  Any files not specified will appear following these files, in alphabetical order.

## License

Jupyter Custom Sort is copyright 2023 Pragmatic Institute, released under the BSD 3-clause license.  See the LICENSE file for details.  The source is available at https://github.com/thedataincubator/jupytercustomsort.
