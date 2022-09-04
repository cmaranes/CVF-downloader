# Computer Vision Foundation Paper Downloader (CVPR, ICCV, WACV)

This repo consists of a script that scraps from the [CVF webpage](https://openaccess.thecvf.com/menu)
the papers of the selected conference (CVPR, ICCV, WACV).
This can be useful for offline reading and annotating them.

## Installation
**Python 3.9** is required since the argparse uses booleans. For installing the libraries,
run the following command:

`$ pip install -r requirements.txt`

## Usage
For example, if you would like to download the CVPR 2022 articles,
and enumerate the pdf file to keep track of what you have read, run the following command:

`$ python main.py --conference CVPR --year 2022 --enumerate`
