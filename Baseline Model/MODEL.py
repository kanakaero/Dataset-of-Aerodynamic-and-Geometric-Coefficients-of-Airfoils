import numpy as np
import torch
import torch.nn as nn


class AIRFOIL_GENERATOR(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(in_features=9, out_features= 12),
            nn.BatchNorm1d(12),
            nn.ReLU(),
            nn.Dropout(p=0.5,inplace=False),
            nn.Linear(in_features= 12, out_features= 6),
            nn.BatchNorm1d(6),
            nn.ReLU(),
            nn.Dropout(p=0.5,inplace=False),
            nn.Linear(in_features= 6, out_features= 2),
        )
        

    def forward(self, x):
        #print(x.shape)
        x = self.network(x)
        return x