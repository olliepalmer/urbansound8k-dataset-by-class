# Urban Sound 8k dataset conformer

The Urban Sound 8k Dataset is great! But it stores the `.wav` files in `foldX` folders unrelated to class. If you want to create a simple classifier which works using folder structures, run this python code.

1. download the urban sound 8k dataset from https://urbansounddataset.weebly.com and save it into a folder, e.g. `/username/Downloads/UrbanSound8k`
2. run this python script using python3, e.g. `python3 collate_dataset.py`

Note that this file copies each file into a new location, so you need a spare 7Gb of disk space.