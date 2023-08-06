# -*- coding: utf-8 -*-

import unittest
from PyThief.PyThief import PyThief
import pandas as pd
import numpy as np

def testing_data():
    y = [
        69,
        2777,
        17356,
        13972,
        420,
        6774,
        8337,
        7956,
        6430,
        4203,
        5603,
        13586,
        29564,
        17635,
        19174,
        21360,
        4413,
        9010,
        711,
        29031,
        15225,
        13870,
        45360,
        20360,
        75956,
        28474,
        22928,
        77955,
        24161,
        3780,
        15897,
        16898,
        4222,
        14006,
        24484,
        48973,
        21222,
        21322,
        11649,
        9797,
        25350,
        68135,
        7336,
        39371,
        21148,
        59876,
        172433,
        26669,
        15614,
        37894,
        22022]
    periods = ['2017-12-31T00:00:00.000+0000',	
               '2018-01-31T00:00:00.000+0000',	
               '2018-02-28T00:00:00.000+0000',	
               '2018-03-31T00:00:00.000+0000',	
               '2018-04-30T00:00:00.000+0000',	
               '2018-05-31T00:00:00.000+0000',	
               '2018-06-30T00:00:00.000+0000',	
               '2018-07-31T00:00:00.000+0000',	
               '2018-08-31T00:00:00.000+0000',	
               '2018-09-30T00:00:00.000+0000',	
               '2018-10-31T00:00:00.000+0000',	
               '2018-11-30T00:00:00.000+0000',	
               '2018-12-31T00:00:00.000+0000',	
               '2019-01-31T00:00:00.000+0000',	
               '2019-02-28T00:00:00.000+0000',	
               '2019-03-31T00:00:00.000+0000',	
               '2019-04-30T00:00:00.000+0000',	
               '2019-05-31T00:00:00.000+0000',	
               '2019-06-30T00:00:00.000+0000',	
               '2019-07-31T00:00:00.000+0000',	
               '2019-08-31T00:00:00.000+0000',	
               '2019-09-30T00:00:00.000+0000',	
               '2019-10-31T00:00:00.000+0000',	
               '2019-11-30T00:00:00.000+0000',	
               '2019-12-31T00:00:00.000+0000',	
               '2020-01-31T00:00:00.000+0000',	
               '2020-02-29T00:00:00.000+0000',	
               '2020-03-31T00:00:00.000+0000',	
               '2020-04-30T00:00:00.000+0000',	
               '2020-05-31T00:00:00.000+0000',	
               '2020-06-30T00:00:00.000+0000',	
               '2020-07-31T00:00:00.000+0000',	
               '2020-08-31T00:00:00.000+0000',	
               '2020-09-30T00:00:00.000+0000',	
               '2020-10-31T00:00:00.000+0000',	
               '2020-11-30T00:00:00.000+0000',	
               '2020-12-31T00:00:00.000+0000',	
               '2021-01-31T00:00:00.000+0000',	
               '2021-02-28T00:00:00.000+0000',	
               '2021-03-31T00:00:00.000+0000',	
               '2021-04-30T00:00:00.000+0000',	
               '2021-05-31T00:00:00.000+0000',	
               '2021-06-30T00:00:00.000+0000',	
               '2021-07-31T00:00:00.000+0000',	
               '2021-08-31T00:00:00.000+0000',	
               '2021-09-30T00:00:00.000+0000',	
               '2021-10-31T00:00:00.000+0000',	
               '2021-11-30T00:00:00.000+0000',	
               '2021-12-31T00:00:00.000+0000',	
               '2022-01-31T00:00:00.000+0000',	
               '2022-02-28T00:00:00.000+0000']
    data = {'period':periods,'y':y
        }
    y = pd.DataFrame(data)
    y = y.set_index('period')['y']
    return y

class IntegrationTest():
    def setUp(self):
        self.class_obj = None
    
    def set_class_obj(self, child_class_obj):
        self.class_obj = child_class_obj
        
    def test_integration_len(self):
        y = testing_data()
        predict_values,fitted_values,res_values = self.class_obj.fit(y)
        recon_fore = self.class_obj.predict(predict_values)
        self.assertTrue(len(recon_fore) == 24)
        
    def test_integration_null(self):
        y = testing_data()
        predict_values,fitted_values,res_values = self.class_obj.fit(y)
        recon_fore = self.class_obj.predict(predict_values)
        self.assertFalse(np.isnan(np.min(recon_fore)))
        
class NaiveOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='naive', recon='ols'))

class NaiveWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='naive', recon='struc'))
        
class NaiveMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='naive', recon='mse'))
        
class SnaiveOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='snaive', recon='ols'))

class SnaiveWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='snaive', recon='struc'))
        
class SnaiveMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='snaive', recon='mse'))
        
class ThetaAddOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='theta', recon='ols'))

class ThetaAddWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='theta', recon='struc'))
        
class ThetaAddMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='theta', recon='mse'))

class ThetaMultOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='theta', recon='ols',seasonality='multi'))

class ThetaMultWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='theta', recon='struc',seasonality='multi'))
        
class ThetaMultMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='theta', recon='mse',seasonality='multi'))

class ETSAddOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='ets', recon='ols'))

class ETSAddWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='ets', recon='struc'))
        
class ETSAddMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='ets', recon='mse'))

class ETSMultOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='ets', recon='ols',seasonality='multi'))

class ETSMultWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='ets', recon='struc',seasonality='multi'))
        
class ETSMultMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='ets', recon='mse',seasonality='multi'))
        
class ArimaOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='arima', recon='ols'))

class ArimaWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='arima', recon='struc'))
        
class ArimaMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='arima', recon='mse'))
        
class MeanMEANOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='mean', recon='ols'))

class MeanMEANWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='mean', recon='struc'))
        
class MeanMEANMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='mean', recon='mse'))

class MeanMedianOLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='mean', stat ='median', recon='ols'))

class MeanMedianWLSIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='mean', stat ='median', recon='struc'))
        
class MeanMedianMSEIntegrationTest(IntegrationTest, unittest.TestCase):
    def setUp(self):
        self.set_class_obj(PyThief(method='mean', stat ='median', recon='mse'))
 

if __name__ == '__main__':
    unittest.main()