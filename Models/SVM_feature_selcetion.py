import pandas as pd
import ast
import os
from nilearn import plotting
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import KFold, cross_val_score
from Visualization.T_test import check_normality, student_t_test, welch_t_test, mann_whitney_test, check_variance
from sklearn.model_selection import ShuffleSplit

BASC_pkl = pd.read_pickle('../Feature_Extraction/Schaefer_features/non_PCA_features/schaefer_200_non_PCA.pkl')

different_nodes = pd.DataFrame()
different_nodes['nodes'] = None


def avoid_duplication(nested_list):
    unique_elements = set()
    for sublist in nested_list:
        unique_elements.update(sublist)

    # 집합을 다시 리스트로 변환
    result = list(unique_elements)

    return result


def statistic(rbd_data, hc_data):
    mann_whitneyu, welch, student = check_variance(np.array(rbd_data.tolist()),
                                                   np.array(hc_data.tolist()))

    student_test = student_t_test(student, np.array(rbd_data.tolist()),
                                  np.array(hc_data.tolist()))
    welch_test = welch_t_test(welch, np.array(rbd_data.tolist()),
                              np.array(hc_data.tolist()))
    mann_test = mann_whitney_test(mann_whitneyu, np.array(rbd_data.tolist()),
                                  np.array(hc_data.tolist()))

    return np.unique(mann_test + student_test + welch_test).tolist()


accuracy_score_mean = []
feature_difference = []

feature_name = 'FC'

status_1_data = BASC_pkl[BASC_pkl['STATUS'] == 1]
status_0_data = BASC_pkl[BASC_pkl['STATUS'] == 0]
# Select only the REHO and STATUS columns
selected_data_1 = status_1_data[[feature_name, 'STATUS']]
selected_data_0 = status_0_data[[feature_name, 'STATUS']]

shuffle_split_1 = ShuffleSplit(n_splits=100, test_size=0.1, random_state=42)
shuffle_split_0 = ShuffleSplit(n_splits=100, test_size=0.1, random_state=42)

print(selected_data_1[feature_name])

'''
for (train_idx_1, test_idx_1), (train_idx_0, test_idx_0) in zip(
        shuffle_split_1.split(selected_data_1),
        shuffle_split_0.split(selected_data_0)):
    # 라벨 1 데이터의 훈련/테스트 분리
    train_1 = selected_data_1.iloc[train_idx_1]
    test_1 = selected_data_1.iloc[test_idx_1]

    # 라벨 0 데이터의 훈련/테스트 분리
    train_0 = selected_data_0.iloc[train_idx_0]
    test_0 = selected_data_0.iloc[test_idx_0]

    # 훈련 데이터와 테스트 데이터 결합
    train_data = pd.concat([train_1, train_0], axis=0).reset_index(drop=True)
    test_data = pd.concat([test_1, test_0], axis=0).reset_index(drop=True)

    train_data[feature_name] = [item[0] for item in train_data[feature_name]]
    test_data[feature_name] = [item[0] for item in test_data[feature_name]]

    print(train_data[feature_name])


    
    model = svm.SVC(kernel='rbf', C=1, probability=True)
    model.fit(np.array(train_data[feature_name]), train_data['STATUS'])
    accuracy = model.score(np.array(test_data[feature_name].tolist()), test_data['STATUS'])

    print(f"accuracy : {accuracy:.2f}")

accuracy_score_mean.append(accuracy)

print(np.round(np.mean(accuracy_score_mean), 2))
'''

'''
rbd_data = train_data[feature_name][train_data['STATUS'] == 1]
hc_data = train_data[feature_name][train_data['STATUS'] == 0]

result = statistic(rbd_data, hc_data)

feature_difference.append(result)
'''

### 통게적으로 유의미한 차이를 보이는 node들만 고려해서 training을 진행하는 코드###
'''
result = pd.read_pickle('../Feature_Extraction/Shen_features/different_nodes_shen_reho.pkl')['nodes'].tolist()

train_data[feature_name] = train_data[feature_name].apply(lambda x: [x[i] for i in result])
test_data[feature_name] = test_data[feature_name].apply(lambda x: [x[i] for i in result])
'''

'''
different_nodes['nodes'] = avoid_duplication(feature_difference)

different_nodes.to_pickle('different_nodes_shen_falff.pkl')
'''
