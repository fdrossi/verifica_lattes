import xml.etree.ElementTree as et
import csv 
import glob

path = 'lattes'
for data in glob.glob(path + '/*.xml'):
	lista_issn = [ ]
	tree = et.parse(data)
	root = tree.getroot()

	for producao in root.iter('DETALHAMENTO-DO-ARTIGO'):
		lista_issn.append(producao.attrib["ISSN"])

	file = 'base/qualis.csv'
	with open(file, 'r') as base:
		tupla = csv.reader(base, delimiter=";")
		tupla_base = list(tuple(line) for line in tupla)

	resultado = [ ]
	for elemento in lista_issn:
		for i in tupla_base:
			if elemento in i:
				resultado.append(i[2])

	valor = 0
	for x in resultado:
		if x == 'A1':
			valor += 100
		elif x == 'A2':
			valor += 87
		elif x == 'A3':
			valor += 75
		elif x == 'A4':
			valor += 60
		elif x == 'B1':
			valor += 30
		elif x == 'B2':
			valor += 20
		elif x == 'B3':
			valor += 10
		elif x == 'B4': 
			valor += 5 

	for nome in root.iter('DADOS-GERAIS'):
		print(nome.attrib['NOME-COMPLETO'])
	print(valor/10)

