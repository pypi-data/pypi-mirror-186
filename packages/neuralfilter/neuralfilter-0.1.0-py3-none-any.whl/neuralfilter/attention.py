import numpy as np

def get_weight():

    dic_mat = {}
    dic_mat['mat_CNN_1conv1_b'] = np.load('neuralfilter/matrices/mat_CNN_1conv1_b.py')
    dic_mat['mat_CNN_1conv1_w'] = np.load('neuralfilter/matrices/mat_CNN_1conv1_w.py')
    dic_mat['mat_CNN_1conv2_b'] = np.load('neuralfilter/matrices/mat_CNN_1conv2_b.py')
    dic_mat['mat_CNN_1conv2_w'] = np.load('neuralfilter/matrices/mat_CNN_1conv2_w.py')
    dic_mat['mat_CNN_2conv1_b'] = np.load('neuralfilter/matrices/mat_CNN_2conv1_b.py')
    dic_mat['mat_CNN_2conv1_w'] = np.load('neuralfilter/matrices/mat_CNN_2conv1_w.py')
    dic_mat['mat_CNN_2conv2_b'] = np.load('neuralfilter/matrices/mat_CNN_2conv2_b.py')
    dic_mat['mat_CNN_2conv2_w'] = np.load('neuralfilter/matrices/mat_CNN_2conv2_w.py')
    dic_mat['mat_CNN_attn_b'] = np.load('neuralfilter/matrices/mat_CNN_attn_b.py')
    dic_mat['mat_CNN_attn_w'] = np.load('neuralfilter/matrices/mat_CNN_attn_w.py')

    return dic_mat
