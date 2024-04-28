import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import time
from genrate_data_from_today import GenerateData

gd = GenerateData()
df = gd.generateSingleRow()
while True:
   gd.generateSingleRow()
   time.sleep(5)


