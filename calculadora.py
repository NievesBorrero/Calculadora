# .*- coding: utf-8 *-*
from calculadora import op_bas

opcion=5
num1= int(raw_input("número1:"))
num2= int(raw_input("número2:"))
print '1-sumar'
print '2-restar'
print '3-multiplicar'
print '4-dividir'
while opcion <>0:
	opcion=int(raw_input("Introduce una opción--0 para salir--"))
	if opcion==1:
		print "resultado", op_bas.sumar(num1,num2)
	elif opcion==2:
		print "resultado", op_bas.restar(num1, num2)
	elif opcion==3:
		print "resultado", op_bas.multiplicar(num1,num2)
	elif opcion==4:
		print "resultado", op_bas.dividir(num1,num2)
	elif opcion==0:
		print "Hasta otra!"
	else:
		print "Error, elige una opción del menú"
