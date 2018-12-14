# Urban Sound 8k dataset conformer

The [Urban Sound 8k Dataset](https://urbansounddataset.weebly.com/urbansound8k.html) is great! But it stores the `.wav` files in `fold1`, `fold2`, `fold3` etc folders unrelated to class. If you want to create a simple classifier which works using folder structures, run this python code.

### before:

```
fold1/randomsoundsfromallclasses
fold2/randomsoundsfromallclasses
etc
```

### after:

```
0_air_conditioner/allairconditionersounds
1_car_horn/allcarhornsounds
etc
```

## How to use

1. Download the Urban Sound 8k dataset from https://urbansounddataset.weebly.com or https://serv.cusp.nyu.edu/files/jsalamon/datasets/UrbanSound8K.tar.gz and save it into a folder, e.g. `/username/Downloads/UrbanSound8k`
2. Run this python script using python3, e.g. `python3 collate_dataset.py`

Note that this file copies each file into a new location, so you need a spare 7Gb of disk space. 