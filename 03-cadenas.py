text1='hola'
text2='mundo'

finalText=text1+' '+text2
print(finalText)

print('El saludo es: %s %s' %(text1,text2))

finalText2='saludo: {x} {y}'.format(x=text1,y=text2)
print(finalText2)

texto='Desarrollo Web Profesional UTL'
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find('al'))
print(texto.count('e'))
print(texto.replace('e','a'))
cadenaSeparada=texto.split(' ')
print(cadenaSeparada)