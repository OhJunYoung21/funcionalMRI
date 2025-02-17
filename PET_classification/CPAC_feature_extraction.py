import glob
import os
from Comparison_features.rsfmri import static_measures
import re
import numpy as np
from Static_Feature_Extraction.Shen_features.Classification_feature import FC_extraction, region_reho_average, \
    region_alff_average
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

PET_data = pd.read_pickle('PET_shen_static.pkl')

print(PET_data.shape)
