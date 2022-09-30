import numpy as np
import pandas as pd
from keras.models import load_model


class DataPredication:
    def __init__(self):
        self.path = self.get_path()
        df = pd.read_csv(self.path)
        self.X = df[['BGSM1', 'BGSM2', 'BGSM3', 'BGSE1', 'BGSE2', 'BGSE3']]
        self.X = np.array(self.X).reshape((self.X.shape[0],self.X.shape[1],1))
        self.prediction_model = load_model("predication_model.h5")


    def predict(self):
        self.y = self.prediction_model.predict(self.X)
        output = np.array(np.argmax(self.y)).max()
        return [self.convertToString(output), np.argmax(self.y)]

    def convertToString(self, modelOutput):
        if modelOutput == 0:
            out = "Normal State."
        elif modelOutput == 1:
            out = 'Moderate Storm.'
        else:
            out = "Strong Storm."

        return out
        
        








