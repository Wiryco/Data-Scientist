import numpy as np
import pandas as pd

base = pd.read_csv('iris.csv')

np.random.seed(2345) #Mantem o mesmo valor dos resultados

amostra = np.random.choice(a = [0, 1], size = 150, replace = True,
                           p = [0.5, 0.5])

len(amostra)
len(amostra[amostra == 0])
len(amostra[amostra == 1])