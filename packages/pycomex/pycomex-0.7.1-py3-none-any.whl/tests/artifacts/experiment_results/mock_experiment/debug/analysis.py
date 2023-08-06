#! /usr/bin/env python3
import os
import json
import pathlib
from pprint import pprint
from typing import Dict, Any

# Useful imports for conducting analysis
import numpy as np
import matplotlib.pyplot as plt

# Importing the experiment
from snapshot import *

# List of experiment parameters
# - MEAN
# - STANDARD_DEVIATION
# - NUM_VALUES
# - NUM_BINS
# - COLOR_PRIMARY
# - PATH
# - BASE_PATH
# - NAMESPACE
# - DEBUG

PATH = pathlib.Path(__file__).parent.absolute()
DATA_PATH = os.path.join(PATH, 'experiment_data.json')
# Load the all raw data of the experiment
with open(DATA_PATH, mode='r') as json_file:
    DATA: Dict[str, Any] = json.load(json_file)


if __name__ == '__main__':
    print('RAW DATA KEYS:')
    pprint(list(DATA.keys()))

    # The analysis template from the experiment file
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 10))
    ax.hist(e['values'], bins=NUM_BINS, color=COLOR_PRIMARY)
    e.commit_fig('values.pdf', fig)