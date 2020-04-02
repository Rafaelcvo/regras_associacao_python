#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:41:50 2020

@author: rafael
"""
from apyori import apriori
import pandas as pd

dados = pd.read_csv('/home/rafael/git/regras_associacao_python/datasets/mercado2.csv', header=None)
quant = len(dados)

trans = []

for i in range(0, quant):
    trans.append([str(dados.values[i,j]) for j in range(0,20)])

regras = list(apriori(trans, min_support = 0.003, min_confidence=0.2, min_lift=3.0, min_lenght=2))

result = [list(x) for x in regras]

result_for = []
for j in range(0, 5):
    result_for.append([list(x) for x in result[j][2]])

result_for
