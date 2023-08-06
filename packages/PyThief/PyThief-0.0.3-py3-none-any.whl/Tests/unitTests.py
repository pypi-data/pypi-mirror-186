# -*- coding: utf-8 -*-

import unittest
from PyThief.models.naive import NaiveModel
from PyThief.models.snaive import NaiveSeasonal
from PyThief.models.arima import ArimaModel
from PyThief.models.theta import ThiefThetaModel
from PyThief.models.ets import ETSModel
from PyThief.models.mean import MeanModel
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

class BaseModelTest():
    def setUp(self):
        self.model_obj = None
    
    def set_model_obj(self, child_model_obj):
        self.model_obj = child_model_obj
        
    def test_fitted_series(self):
        y = testing_data()
        try:
            fitted_values = self.model_obj.fit(y)
        except:
            fitted_values = self.model_obj.fit(y,1)
        self.assertTrue(isinstance(fitted_values, np.ndarray))
    
    def test_predicted_series(self):
        y = testing_data()
        try:
            fitted_values = self.model_obj.fit(y)
        except:
            fitted_values = self.model_obj.fit(y,1)
        predictions = self.model_obj.predict(24)
        self.assertTrue(isinstance(predictions, np.ndarray))
        
    def test_fitted_null(self):
        y = testing_data()
        try:
            fitted_values = self.model_obj.fit(y)
        except:
            fitted_values = self.model_obj.fit(y,1)
        self.assertFalse(np.isnan(np.min(fitted_values)))
        
    def test_prediction_null(self):
        y = testing_data()
        try:
            fitted_values = self.model_obj.fit(y)
        except:
            fitted_values = self.model_obj.fit(y,1)
        predictions = self.model_obj.predict(24)
        self.assertFalse(np.isnan(np.min(predictions)))
                         
class NaiveModelTest(BaseModelTest, unittest.TestCase):
    def setUp(self):
        self.set_model_obj(NaiveModel())

class NaiveSeasonalTest(BaseModelTest, unittest.TestCase):
    def setUp(self):
        self.set_model_obj(NaiveSeasonal())

class ThiefThetaModelTest(BaseModelTest, unittest.TestCase):
    def setUp(self):
        self.set_model_obj(ThiefThetaModel())

class ArimaModelTest(BaseModelTest, unittest.TestCase):
    def setUp(self):
        self.set_model_obj(ArimaModel())
        
class ETSModelTest(BaseModelTest, unittest.TestCase):
    def setUp(self):
        self.set_model_obj(ETSModel())
        
class MeanModelTest(BaseModelTest, unittest.TestCase):
    def setUp(self):
        self.set_model_obj(MeanModel())
        
if __name__ == '__main__':
    unittest.main()