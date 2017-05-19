# .*- coding: utf-8 *-*
"""Funciones de la calculadora"""

def sumar (num1, num2):
	"""Suma los dos números enviados como parámetro y devuelve el resultado."""
	return num1 + num2

def restar (num1, num2):
	"""Resta los dos números enviados como parámetro y devuelve el resultado."""
	return num1 - num2

def multiplicar (num1, num2):
	"""Multiplica los dos números enviados como parámetro y devuelve el resultado."""
	return num1 * num2

def dividir (num1, num2):
	"""Divide los dos números enviados como parámetro y devuelve el resultado."""
	try:
		resultado = num1 / num2
		return resultado
	except ZeroDivisionError:
		print ': error, no puedes dividir entre cero'
		return -1
	
