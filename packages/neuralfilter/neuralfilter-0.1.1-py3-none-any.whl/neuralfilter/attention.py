import numpy as np

def get_weight():

    dic_mat = {}
    dic_mat['mat_CNN_1conv1_b'] = np.load('/tmp/matrices/mat_CNN_1conv1_b.npy')
    dic_mat['mat_CNN_1conv1_w'] = np.load('/tmp/matrices/mat_CNN_1conv1_w.npy')
    dic_mat['mat_CNN_1conv2_b'] = np.load('/tmp/matrices/mat_CNN_1conv2_b.npy')
    dic_mat['mat_CNN_1conv2_w'] = np.load('/tmp/matrices/mat_CNN_1conv2_w.npy')
    dic_mat['mat_CNN_2conv1_b'] = np.load('/tmp/matrices/mat_CNN_2conv1_b.npy')
    dic_mat['mat_CNN_2conv1_w'] = np.load('/tmp/matrices/mat_CNN_2conv1_w.npy')
    dic_mat['mat_CNN_2conv2_b'] = np.load('/tmp/matrices/mat_CNN_2conv2_b.npy')
    dic_mat['mat_CNN_2conv2_w'] = np.load('/tmp/matrices/mat_CNN_2conv2_w.npy')
    dic_mat['mat_CNN_attn_b'] = np.load('/tmp/matrices/mat_CNN_attn_b.npy')
    dic_mat['mat_CNN_attn_w'] = np.load('/tmp/matrices/mat_CNN_attn_w.npy')

    return dic_mat
