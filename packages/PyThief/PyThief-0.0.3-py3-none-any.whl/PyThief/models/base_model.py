# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class BaseModel(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def fit(self, y, **kwargs):
        pass
    
    @abstractmethod
    def predict(self, forecast_horizon):
        pass