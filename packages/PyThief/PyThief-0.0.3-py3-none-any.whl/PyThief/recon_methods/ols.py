# -*- coding: utf-8 -*-
import numpy as np

class OLS:
    
    def __init__(self):
        pass
    
    
    def recon(self,s_matrix,y):
        return np.linalg.pinv(s_matrix.T.dot(s_matrix)).dot(s_matrix.T.dot(y))