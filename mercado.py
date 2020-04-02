#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:31:45 2020

@author: rafael
"""

from apyori import apriori
import pandas as pd

dados = pd.read_csv('/home/rafael/git/regras_associacao_python/datasets/mercado.csv', header=None)
transacoes = []


for i in range(0, 10):
    transacoes.append([str(dados.values[i, j]) for j in range(0,4)])

regras = list(apriori(transacoes, min_support = 0.3, min_confidence=0.8, min_lift=2, min_lenght=2))
regras

result = [list(x) for x in regras]
result

result_for = []
for j in range(0, 3):
    result_for.append([list(x) for x in result[j][2]])
result_for
