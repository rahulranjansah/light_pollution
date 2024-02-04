import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv("filtered_data.csv")

date_time = data["UT_datetime"]
brightness = data[" Brightness"]