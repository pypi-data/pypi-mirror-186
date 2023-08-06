import os
import numpy as np

def get_weight():

    if(os.path.isfile('/tmp/matrices/mat_CNN_1conv1_b.npy')):
        pass
    else:
        try: os.system('rm matrices.zip')
        except: pass
        try: os.system('rm -r matrices')
        except: pass
        os.system('wget -q https://github.com/YeongHyeon/NeuralFilter/raw/main/misc/matrices.zip')
        os.system('unzip matrices.zip')
        os.system('rm matrices.zip')
        os.system('mv matrices /tmp/matrices')

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
