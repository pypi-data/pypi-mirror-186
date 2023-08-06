# -*- coding: utf-8 -*-d
class Aggregation:
    
    def __init__(self,
                 y,
                 annual_agg,
                 semiannual_agg,
                 fourmonth_agg=True,
                 threemonth_agg=True
                 ):
        self.y = y
        self.annual_agg = annual_agg
        self.semiannual_agg = semiannual_agg
        self.fourmonth_agg = fourmonth_agg
        self.threemonth_agg = threemonth_agg
        
    def agg_bimonthly(self,y):
        d = {'period': 'last','y': 'sum'}
        y = y.groupby(y.index // 2).agg(d)
        y = y.set_index('period')['y']
        return y

    def agg_quar(self,y):
        d = {'period': 'last','y': 'sum'}
        y = y.groupby(y.index // 3).agg(d)
        y = y.set_index('period')['y']
        return y
    
    def agg_fourmonthly(self,y):
        d = {'period': 'last','y': 'sum'}
        y = y.groupby(y.index // 4).agg(d)
        y = y.set_index('period')['y']
        return y
    
    def agg_semiannual(self,y):
        d = {'period': 'last','y': 'sum'}
        y = y.groupby(y.index // 6).agg(d)
        y = y.set_index('period')['y']
        return y
    
    def agg_year(self,y):
        d = {'period': 'last','y': 'sum'}
        y = y.groupby(y.index // 12).agg(d)
        y = y.set_index('period')['y']
        return y
    
    def get_aggs(self,y):
        if self.annual_agg:
            y_bimonth = self.agg_bimonthly(y)
            y_quar = self.agg_quar(y)
            y_fourmonthly = self.agg_fourmonthly(y)
            y_semiannual = self.agg_semiannual(y)
            y_year = self.agg_year(y)
        elif self.semiannual_agg:
            y_bimonth = self.agg_bimonthly(y)
            y_quar = self.agg_quar(y)
            y_fourmonthly = None
            y_semiannual = self.agg_semiannual(y)
            y_year = None
        elif self.fourmonth_agg:
            y_bimonth = self.agg_bimonthly(y)
            y_quar = None
            y_fourmonthly = self.agg_fourmonthly(y)
            y_semiannual = None
            y_year = None
        elif self.threemonth_agg:
            y_bimonth = None
            y_quar = self.agg_quar(y)
            y_fourmonthly = None
            y_semiannual = None
            y_year = None
        else:
            y_bimonth = self.agg_bimonthly(y)
            y_quar = None
            y_fourmonthly = None
            y_semiannual = None
            y_year = None
        output = {2:y_bimonth,3:y_quar,4:y_fourmonthly,6:y_semiannual,12:y_year}
        return output
    
        
        
        