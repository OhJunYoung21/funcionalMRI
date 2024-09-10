import numpy as np
from nilearn import datasets
from nilearn.maskers import NiftiMapsMasker
from nilearn.connectome import ConnectivityMeasure
from nilearn import plotting
from nilearn import datasets
import os
from nilearn import image
from nilearn import input_data
from nilearn.regions import RegionExtractor

# Download the Shen atlas
atlas_path = '/Users/oj/Downloads/shen_2mm_268_parcellation.nii'

file_path = '/Users/oj/Desktop/Yoo_Lab/post_fMRI/confounds_regressed_RBD/sub-01_confounds_regressed.nii.gz'


def FC_extraction(file_path, atlas_path):
    shen_atlas = input_data.NiftiLabelsMasker(labels_img=atlas_path, standardize=True)

    data = image.load_img(file_path)

    time_series = shen_atlas.fit_transform(data)

    correlation_measure = ConnectivityMeasure(kind='correlation')
    correlation_matrix = correlation_measure.fit_transform([time_series])[0]

    return correlation_matrix


def Reho_extraction(file):
    func_img = image.load_img(file)

    extractor = RegionExtractor(func_img,
                                min_region_size=1,  # 최소 영역 크기 설정
                                extractor='local_regions',  # ReHo 계산을 위한 지역 추출 방법
                                standardize=True,  # ReHo 계산 전에 시계열 표준화
                                verbose=True)

    extractor.fit()
    timeseries_img = extractor.transform(func_img)

    return timeseries_img


plotting.plot_img(Reho_extraction(file_path))
plotting.show()
