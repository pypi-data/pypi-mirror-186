# -*- coding: utf-8 -*-

import unittest
from PyThief.recon_methods.ols import OLS
from PyThief.recon_methods.wls import WLS
from PyThief.recon_methods.mse import MSE
from PyThief.utils import Utilities
import numpy as np

def testing_data():
    y = [np.array([23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079,
                  23079]),
         np.array([53973,
             53973,
             53973,
             53973,
             53973,
             53973,
             53973,
             53973,
             53973,
             53973,
             53973,
             53973]),
         np.array([69587,
             69587,
             69587,
             69587,
             69587,
             69587,
             69587,
             69587]),
         np.array([96256,
                  96256,
                  96256,
                  96256,
                  96256,
                  96256]),
         np.array([348565,
                  348565,
                  348565,
                  348565]),
         np.array([522803,
                  522803])]
    return y

def weight_data():
    y = np.array([1,
              3,
              3,
              4,
              4,
              4,
              5,
              5,
              5,
              5,
              6,
              6,
              6,
              6,
              6,
              6,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              1,
              3,
              3,
              4,
              4,
              4,
              5,
              5,
              5,
              5,
              6,
              6,
              6,
              6,
              6,
              6,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7,
              7])
    return y

class ReconTest():
    def setUp(self):
        self.recon_obj = None
    
    def set_recon_obj(self, child_recon_obj):
        self.recon_obj = child_recon_obj
    
    def test_recon_series(self):
        y = testing_data()
        s_matrix = Utilities().build_smatrix(True,True,True,True)
        y_recon = Utilities().build_y_hat(y,True,True,True,True)
        weight = weight_data()
        if isinstance(self.recon_obj, MSE):
            beta = self.recon_obj.recon(s_matrix,y_recon,weight)
        else:
            beta = self.recon_obj.recon(s_matrix,y_recon)
        self.assertTrue(isinstance(beta, np.ndarray))
              
    def test_recon_null(self):
        y = testing_data()
        s_matrix = Utilities().build_smatrix(True,True,True,True)
        y_recon = Utilities().build_y_hat(y,True,True,True,True)
        weight = weight_data()
        if isinstance(self.recon_obj, MSE):
            beta = self.recon_obj.recon(s_matrix,y_recon,weight)
        else:
            beta = self.recon_obj.recon(s_matrix,y_recon)
        self.assertFalse(np.isnan(np.min(beta)))
        
class OLSTest(ReconTest, unittest.TestCase):
    def setUp(self):
        self.set_recon_obj(OLS())

class WLSTest(ReconTest, unittest.TestCase):
    def setUp(self):
        self.set_recon_obj(WLS())
        
class MSETest(ReconTest, unittest.TestCase):
    def setUp(self):
        self.set_recon_obj(MSE())
        
if __name__ == '__main__':
    unittest.main()
    

    