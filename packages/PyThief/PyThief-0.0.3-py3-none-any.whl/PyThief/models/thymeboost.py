import numpy as np
from PyThief.models.base_model import BaseModel


class ThymeBoostModel(BaseModel):
    model = 'thymeboost'
    
    def __init__(self):
        self.model_params = None
        self.fitted = None
        self._online_steps = 0

    def fit(self, y, **kwargs):
        return None
    
    def predict(self, forecast_horizon):
        return None

