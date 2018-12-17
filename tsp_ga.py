
# python 2.7

import numpy as np
import pandas as pd
import math
import plt

class Ant():

	def __init__(self, cidades, rate_mutation, rate_crossover):
		self.cidades = np.array(cidades)
		self.distance = 0
		self.rate_mutation = rate_mutation
		self.rate_crossover = rate_crossover
		self.mutacao()

	def evaluate(self):
		self.distance = 0
		for i in range(len(self.cidades) - 1):
			self.distance += math.sqrt(pow(self.cidades[i + 1][0]-self.cidades[i][0], 2) + pow(self.cidades[i + 1][1]-self.cidades[i][1], 2))
		self.distance += math.sqrt(pow(self.cidades[0][0]-self.cidades[-1][0], 2) + pow(self.cidades[0][1]-self.cidades[-1][1], 2))

	def mutacao(self):
		if np.random.rand() <= self.rate_mutation:
			i = np.random.randint(1, len(self.cidades))
			j = np.random.randint(1, len(self.cidades))
			gen1 = self.cidades[i].tolist()
			gen2 = self.cidades[j].tolist()
			self.cidades[i] = gen2
			self.cidades[j] = gen1
		self.evaluate()

	def crossover(self, cromossomo):
		crossover = int(len(self.cidades) * self.rate_crossover)
		cidades1 = self.cidades[:crossover].tolist()
		cidades2 = self.cidades[crossover:].tolist()
		for x in [i for i in cromossomo if not any(i[0] == k for k, _ in cidades1)]:
			cidades1.append(x)
		count = 0
		for x in [i for i in cromossomo if not any(i[0] == k for k, _ in cidades2)]:
			cidades2.insert(count, x)
			count += 1
		ant1 = Ant(cidades1, self.rate_mutation, self.rate_crossover)
		ant2 = Ant(cidades2, self.rate_mutation, self.rate_crossover)
		if ant1.distance <= ant2.distance:
			return ant1
		return ant2

def populacao(name, n, ncidades, rate_mutation, rate_crossover):
	#cidades = np.random.permutation(ncidades*2).reshape(ncidades, 2)
	#cidades = np.random.randint(ncidades*10,  size=(ncidades, 2))
	#file = pd.DataFrame(cidades)
	#file.to_csv('out3.txt', sep=',', encoding='utf-8', header=None, index=None)
	cidades = pd.read_csv(name, header=None).values
	populacao = []
	for i in range(n):
		np.random.shuffle(cidades[1:])
		ant = Ant(cidades, rate_mutation, rate_crossover)
		populacao.append(ant)
	return populacao

def roleta(populacao):
	roleta = []
	score_total = sum(ant.distance for ant in populacao)
	print score_total/len(populacao)
	for ant in populacao:
		lucky = int(1/ant.distance * score_total)
		for i in range(lucky):
			roleta.append(ant)
	return roleta

def selecao(populacao, roleta):
	ant = 0
	for i in range(int(len(roleta) * 0.1)):
		ant = roleta[np.random.randint(0, len(roleta))]
		if ant not in populacao:
			return ant
	return ant

def geracoes(n, populacao):
	geracao = populacao
	for i in range(n):
		new_geracao = []
		_roleta = roleta(geracao)
		for j in range(len(geracao) - int(len(geracao) * geracao[0].rate_crossover)):
			new_geracao.append(selecao(new_geracao, _roleta))
		for x in range(int(len(geracao) * geracao[0].rate_crossover)):
			ant1 = selecao(new_geracao, _roleta)
			ant2 = selecao(new_geracao, _roleta)
			new_geracao.append(ant1.crossover(ant2.cidades))
		geracao = new_geracao
	return geracao


#populacao(100, 30, 0.1, 0.5)
plt.plotar(geracoes(100, populacao('out2.txt', 100, 30, 0.1, 0.5)), 100)

