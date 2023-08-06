# -*- coding: utf-8 -*-
import numpy as np

class MSE:
    
    def __init__(self):
        pass
    
    
    def recon(self,s_matrix,y,weight):
        weighted_s_matrix = s_matrix.T @ np.diag(weight)
        return np.linalg.pinv(weighted_s_matrix.dot(s_matrix)).dot(weighted_s_matrix.dot(y)) 
