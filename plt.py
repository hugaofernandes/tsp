
# coding: utf-8
# python 2.7

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plotar(populacao, n):
	populacao.sort(key=lambda x: x.distance, reverse=True)
	cidades = populacao[-1].cidades
	distance = populacao[-1].distance
	print cidades
	print distance
	plt.title("Algoritmo Genetico - " + str(n) + ' geracoes')
	plt.plot(pd.DataFrame(np.array(cidades))[0], pd.DataFrame(np.array(cidades))[1], 'o', c='red', label='Distancia: ' + str(distance))
	#plt.plot(cidades[0][0], cidades[0][1], 'o', c='green')
	for i in range(len(cidades)-1):
		plt.arrow(cidades[i][0], cidades[i][1], cidades[i+1][0]-cidades[i][0], cidades[i+1][1]-cidades[i][1], length_includes_head=True, head_width=0.6, head_length=0.6, color='black')
	plt.arrow(cidades[-1][0], cidades[-1][1], cidades[0][0]-cidades[-1][0], cidades[0][1]-cidades[-1][1], length_includes_head=True, head_width=0.6, head_length=0.6, color='black')
	plt.legend(loc='upper left', shadow=True, fontsize='small')
	plt.show()


def plotar2(cidades, distance, n):
	print np.array(cidades)
	print distance
	plt.title("Algoritmo da Colonia de Formigas - " + str(n) + ' iteracoes')
	plt.plot(pd.DataFrame(np.array(cidades))[0], pd.DataFrame(np.array(cidades))[1], 'o', c='red', label='Distancia: ' + str(distance))
	#plt.plot(cidades[0][0], cidades[0][1], 'o', c='green')
	for i in range(len(cidades)-1):
		plt.arrow(cidades[i][0], cidades[i][1], cidades[i+1][0]-cidades[i][0], cidades[i+1][1]-cidades[i][1], length_includes_head=True, head_width=0.6, head_length=0.6, color='black')
	plt.arrow(cidades[-1][0], cidades[-1][1], cidades[0][0]-cidades[-1][0], cidades[0][1]-cidades[-1][1], length_includes_head=True, head_width=0.6, head_length=0.6, color='black')
	plt.legend(loc='upper left', shadow=True, fontsize='small')
	plt.show()

