# -*- coding: utf-8 -*-

import numpy as np

class WLS:
    
    def __init__(self):
        pass
    
    
    def recon(self,s_matrix,y):
        weight = 1/np.sum(s_matrix,axis=1)
        weighted_s_matrix = s_matrix.T @ np.diag(weight)
        return np.linalg.pinv(weighted_s_matrix.dot(s_matrix)).dot(weighted_s_matrix.dot(y))  