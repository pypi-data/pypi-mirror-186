# -*- coding: utf-8 -*-

import unittest
from PyThief.aggregation import Aggregation
import numpy as np
import pandas as pd

def testing_data():
    y = [
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
    periods = [	
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
    return y

class AggTest(unittest.TestCase):
    def test_bimonth(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_bimonthly(y)
        self.assertTrue(len(y_agg) == (len(y)/2))
        
    def test_bimonth_null(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_bimonthly(y)
        self.assertFalse(np.isnan(np.min(y_agg)))
        
    def test_quar(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_quar(y)
        self.assertTrue(len(y_agg) == (len(y)/3))
        
    def test_quar_null(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_quar(y)
        self.assertFalse(np.isnan(np.min(y_agg)))
        
    def test_fourmonth(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_fourmonthly(y)
        self.assertTrue(len(y_agg) == (len(y)/4))
    
    def test_fourmonth_null(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_fourmonthly(y)
        self.assertFalse(np.isnan(np.min(y_agg)))
        
    def test_semiannual(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_semiannual(y)
        self.assertTrue(len(y_agg) == (len(y)/6))
    
    def test_semiannual_null(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_semiannual(y)
        self.assertFalse(np.isnan(np.min(y_agg)))
        
    def test_year(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_year(y)
        self.assertTrue(len(y_agg) == (len(y)/12))
        
    def test_year_null(self):
        y = testing_data()
        agg = Aggregation(y,True,True)
        y_agg = agg.agg_year(y)
        self.assertFalse(np.isnan(np.min(y_agg)))
        
if __name__ == '__main__':
    unittest.main()
