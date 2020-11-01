# your code goes here

alfabeto = {
	'𐌀' : 'A',
	'𐌁' : 'B',
	'𐌂' : 'C',
	'𐌃' : 'D',
	'𐌄' : 'E',
	'𐌅' : 'F',
	'𐌆' : 'Z',
	'𐌇' : 'H',
	'𐌉' : 'I',
	'𐌊' : 'K',
	'𐌋' : 'L',
	'𐌌' : 'M',
	'𐌍' : 'N',
	'𐌏' : 'O',
	'𐌐' : 'P',
	'𐌒' : 'Q',
	'𐌓' : 'R',
	'𐌔' : 'S',
	'𐌕' : 'T',
	'𐌖' : 'V',
	'𐌗' : 'X'
}

texto = input()

def transformar(palabra):
	resultados = ''
	for caracter in palabra:
		if caracter in alfabeto:
			resultados = resultados + alfabeto[caracter]
		else:
			resultados = resultados + caracter
	return resultados
print(transformar(texto))