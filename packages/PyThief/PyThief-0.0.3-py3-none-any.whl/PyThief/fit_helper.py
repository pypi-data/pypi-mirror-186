# -*- coding: utf-8 -*-

from PyThief.models.naive import NaiveModel
from PyThief.models.snaive import NaiveSeasonal
from PyThief.models.arima import ArimaModel
from PyThief.models.theta import ThiefThetaModel
from PyThief.models.ets import ETSModel
from PyThief.models.mean import MeanModel
from PyThief.aggregation import Aggregation

class Fit_Helper:
    
    def __init__(self,method,
                 stat,
                 annual_agg,
                 semiannual_agg,
                 fourmonth_agg,
                 threemonth_agg,
                 damped:bool=False,
                 seasonality:str='additive'):
        self.method = method
        self.stat = stat
        self.annual_agg = annual_agg
        self.semiannual_agg = semiannual_agg
        self.fourmonth_agg = fourmonth_agg
        self.threemonth_agg = threemonth_agg
        self.damped = damped
        self.seasonality = seasonality
        
    def trim(self,y,annual_agg,semiannual_agg,fourmonth_agg=True,threemonth_agg=True):
        y_len = len(y)
        if annual_agg:
            y_mod = y_len % 12
            y_len -= y_mod
        elif semiannual_agg:
            y_mod = y_len % 6
            y_len -= y_mod
        elif fourmonth_agg:
            y_mod = y_len % 4
            y_len -= y_mod
        elif threemonth_agg:
            y_mod = y_len % 3
            y_len -= y_mod
        else:
            y_mod = y_len % 2
            y_len -= y_mod
        return y.iloc[-y_len:].reset_index()
        
    def fit_helper(self,y):
        fitted_values = []
        predict_values = []
        res_values = []
        if self.method == 'naive':
            y_len = len(y)
            if len(y) >=12:
                self.annual_agg = True
                self.semiannual_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            elif y_len >= 6 and y_len < 12:
                self.annual_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            elif y_len >=4 and y_len <6:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg)
                y = y_t
            elif y_len == 3:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = False
                self.threemonth_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
                y = y_t
            else:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = False
                self.threemonth_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
                y = y_t
            agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
            y_t = y_t.set_index('period')['y']
            aggs = {1:y_t}
            aggs.update(agg.get_aggs(y))
            model = NaiveModel()
            for key,val in aggs.items():
                if val is not None:
                    fitted = model.fit(val)
                    fitted_values.append(fitted)
                    res_values.append((val-fitted).to_numpy())
                    forecast_horizon = int(24/key)
                    predict_values.append(model.predict(forecast_horizon))
        elif self.method  == 'snaive':
            y_len = len(y)
            if len(y) >=12:
                self.annual_agg = True
                self.semiannual_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            elif y_len >= 6 and y_len < 12:
                self.annual_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            elif y_len >=4 and y_len <6:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg)
                y = y_t
            elif y_len == 3:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = False
                self.threemonth_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
                y = y_t
            else:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = False
                self.threemonth_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
                y = y_t
            agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
            y_t = y_t.set_index('period')['y']
            aggs = {1:y_t}
            aggs.update(agg.get_aggs(y))
            for key,val in aggs.items():
                if val is not None:
                    model = NaiveSeasonal(int(12/key))
                    fitted = model.fit(val)
                    fitted_values.append(fitted)
                    res_values.append((val-fitted).to_numpy())
                    forecast_horizon = int(24/key)
                    predict_values.append(model.predict(forecast_horizon))
        elif self.method == 'theta':
            y_len = len(y)
            if y_len < 36 and y_len >=18:
                self.annual_agg = False
                self.semiannual_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
                agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            elif y_len < 18:
                self.annual_agg = False
                self.semiannual_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
                agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            else:
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
                agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            y_t = y_t.set_index('period')['y']
            aggs = {1:y_t}
            aggs.update(agg.get_aggs(y))
            for key,val in aggs.items():
                if val is not None:
                    model = ThiefThetaModel(int(12/key),self.seasonality)
                    fitted = model.fit(val,key)
                    fitted_values.append(fitted)
                    res_values.append((val-fitted).to_numpy())
                    forecast_horizon = int(24/key)
                    predict_values.append(model.predict(forecast_horizon))
        elif self.method == 'ets':
            y_len = len(y)
            self.annual_agg = False
            if y_len < 18:
                self.semiannual_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            else:
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            y_t = y_t.set_index('period')['y']
            aggs = {1:y_t}
            aggs.update(agg.get_aggs(y))
            for key,val in aggs.items():
                if val is not None:
                    model = ETSModel(int(12/key),self.seasonality,self.damped)
                    fitted = model.fit(val,key)
                    fitted_values.append(fitted)
                    res_values.append((val-fitted).to_numpy())
                    forecast_horizon = int(24/key)
                    predict_values.append(model.predict(forecast_horizon))
        elif self.method == 'arima':
            y_len = len(y)
            if y_len < 36 and y_len >=18:
                self.annual_agg = False
                self.semiannual_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
                agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            elif y_len < 18:
                self.annual_agg = False
                self.semiannual_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
                agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            else:
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
                agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg)
            y_t = y_t.set_index('period')['y']
            aggs = {1:y_t}
            aggs.update(agg.get_aggs(y))
            for key,val in aggs.items():
                if val is not None:
                    model = ArimaModel(int(12/key))
                    fitted = model.fit(val,key)
                    fitted_values.append(fitted)
                    res_values.append((val-fitted).to_numpy())
                    forecast_horizon = int(24/key)
                    predict_values.append(model.predict(forecast_horizon))
        elif self.method == 'mean':
            y_len = len(y)
            if len(y) >=12:
                self.annual_agg = True
                self.semiannual_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            elif y_len >= 6 and y_len < 12:
                self.annual_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg)
                y = y_t
            elif y_len >=4 and y_len <6:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg)
                y = y_t
            elif y_len == 3:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = False
                self.threemonth_agg = True
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
                y = y_t
            else:
                self.annual_agg = False
                self.semiannual_agg = False
                self.fourmonth_agg = False
                self.threemonth_agg = False
                y_t = self.trim(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
                y = y_t
            agg = Aggregation(y_t,self.annual_agg,self.semiannual_agg,self.fourmonth_agg, self.threemonth_agg)
            y_t = y_t.set_index('period')['y']
            aggs = {1:y_t}
            aggs.update(agg.get_aggs(y))
            model = MeanModel(self.stat)
            for key,val in aggs.items():
                if val is not None:
                    fitted = model.fit(val)
                    fitted_values.append(fitted)
                    res_values.append((val-fitted).to_numpy())
                    forecast_horizon = int(24/key)
                    predict_values.append(model.predict(forecast_horizon))
        return predict_values, fitted_values, res_values, self.semiannual_agg, self.annual_agg,self.fourmonth_agg, self.threemonth_agg