#Comandos para encotrar letras e seus posicionamentos.
frase = str(input('\033[33m Digite uma frase:')).upper().strip()
#O método upper transforma as letras minusculas em maiusculas.
#O método strip retira todos os espaços.
# \033[33m modifica a cor da letra.
print(('#'*50))
print('Nesta frase exitem {} letras :a'.format(frase.count('A')))# para contar quantas letras 'A' tem na frase.
print('E também há nesta frase {} letras :i'.format(frase.count('I')))#para contar quantas letras 'i' tem na frase.
print('A letra A aparece primeiro na posição: {}'.format(frase.find('A')+1))#para mostrar em qual posição esta a letra'a'.
print('A letra A aparece por ultimo na posição: {}'.format(frase.rfind('A')+1))# para mostrar a ultima posição da letra 'a' na frase
print('#'*50)