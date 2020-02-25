import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15

k = populacao / amostra

r = np.random.randint(1, k + 1, 1)

acumulador = r[0]

sorteados = []

for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k
    
base = pd.read_csv('iris.csv')

base_final = base.loc[sorteados]