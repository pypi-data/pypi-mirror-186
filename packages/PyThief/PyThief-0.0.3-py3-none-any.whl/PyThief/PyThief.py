# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyThief.recon_methods.ols import OLS
from PyThief.recon_methods.wls import WLS
from PyThief.recon_methods.mse import MSE
from PyThief.utils import Utilities
from PyThief.fit_helper import Fit_Helper


class PyThief:
    def __init__(self,
                 method:str='snaive',
                 stat:str='mean',
                 recon:str='ols',
                 seasonality:str='additive',
                 damped:bool=False):
        self.method = method
        self.stat = stat
        self.recon = recon
        self.damped = damped
        self.seasonality = seasonality
        self.annual_agg = True
        self.semiannual_agg = True
        self.fourmonth_agg = True
        self.threemonth_agg = True
        self.res_values = None
        self.res_recon = None
        self.weights = None
        
    def fit(self, y):
        fh = Fit_Helper(self.method,self.stat,self.annual_agg,self.semiannual_agg,self.fourmonth_agg,self.threemonth_agg,self.damped,self.seasonality)
        predict_values, fitted_values, res_values, semiannual_agg, annual_agg,fourmonth_agg ,threemonth_agg = fh.fit_helper(y)
        self.annual_agg = annual_agg
        self.semiannual_agg = semiannual_agg
        self.fourmonth_agg = fourmonth_agg
        self.threemonth_agg = threemonth_agg
        self.res_values = res_values
        return predict_values, fitted_values, res_values
    
    def predict(self, y):
        utl = Utilities()
        s_matrix = utl.build_smatrix(self.annual_agg,self.semiannual_agg,self.fourmonth_agg,self.threemonth_agg)
        y_recon = utl.build_y_hat(y,self.annual_agg,self.semiannual_agg,self.fourmonth_agg,self.threemonth_agg)
        if self.recon == 'ols':
            beta = OLS().recon(s_matrix,y_recon)
        elif self.recon == 'struc':
            beta = WLS().recon(s_matrix,y_recon)
        elif self.recon == 'mse':
            res_values,weights = utl.build_res(self.res_values,self.annual_agg,self.semiannual_agg,self.fourmonth_agg,self.threemonth_agg)
            self.res_recon = res_values
            self.weights = weights
            beta = MSE().recon(s_matrix,y_recon,weights)
        recon_p = s_matrix.dot(beta)
        recon_fore = utl.grab_month(recon_p,self.annual_agg,self.semiannual_agg,self.fourmonth_agg,self.threemonth_agg)
        return recon_fore
