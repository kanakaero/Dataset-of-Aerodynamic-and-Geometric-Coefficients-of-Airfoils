import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split


class AIRFOIL_DATASET(Dataset):
    def __init__(self, MODE):
        self.DATA_PATH = 'COMPILED_AIRFOIL_DATA.csv'
        self.DATA = pd.read_csv(self.DATA_PATH)

        self.DATA_X = self.DATA[['CST Coeff 1', 'CST Coeff 2', 'CST Coeff 3', 'CST Coeff 4', 'CST Coeff 5', 'CST Coeff 6', 'CST Coeff 7', 'CST Coeff 8','AoA']]
        self.DATA_Y = self.DATA[['Cl', 'Cd']]

        # Converting to Numpy Array:
        self.DATA_X_ARRAY = self.DATA_X.values
        self.DATA_Y_ARRAY = self.DATA_Y.values

        # TRAIN-TEST SPLIT:
        self.X_TRAIN, self.X_temp, self.Y_TRAIN, self.Y_temp = train_test_split(self.DATA_X_ARRAY, self.DATA_Y_ARRAY, test_size=0.2, random_state=42)
        self.X_VAL, self.X_TEST, self.Y_VAL, self.Y_TEST = train_test_split(self.X_temp, self.Y_temp, test_size=0.25, random_state=42)

        self.MODE = MODE

    def __getitem__(self, index):
        if self.MODE == 'Train':
            return self.X_TRAIN[index], self.Y_TRAIN[index]
        
        if self.MODE == 'Val':
            return self.X_VAL[index], self.Y_VAL[index]
        
        if self.MODE == 'Test':
            return self.X_TEST[index] , self.Y_TEST[index]
        
    def __len__(self):
        if self.MODE == 'Train':
            return len(self.X_TRAIN)
        
        if self.MODE == 'Val':
            return len(self.X_VAL)
        
        if self.MODE == 'Test':
            return len(self.X_TEST)
