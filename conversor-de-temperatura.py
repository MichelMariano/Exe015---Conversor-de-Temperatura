# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('Informe a temperatura Cº: '))
f = ((9*c)/5)+32  #Essa é a equação de Cº "Celsius" para Fº (fahrenheit), 9xCelsius / 5 + 32

print('A temperatura de {} ºC corresponde a {} ºF '.format(c, f))
