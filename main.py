# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

def arithmetic_arranger(problems, show_answers=False):
#viendo longitud problems, no mas de 5
    if len(problems) > 5:
        return 'Error: Too many problems.'

#solo suma y resta
    operadores = []
    for problem in problems:
        lista = problem.split()
        operadores.append(lista[1])
    
    for operador in operadores:
        if operador in ['*','/','//']:
            return "Error: Operator must be '+' or '-'." 

#operandos solo digitos 
    numeros = []
    for problem in problems:
        lista = problem.split()
        numeros.append(lista[0])
        numeros.append(lista[2])

    for numero in numeros:
        if not numero.isdigit():
            return 'Error: Numbers must only contain digits.'
#maximo numeros de cuatro digitos
        elif len(numero) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
#evaluacion
    respuestas = []
    arriba = ''
    abajo = ''
    respuesta = ''
    guiones = ''

    for i in range(0, len(numeros), 2):

        num1 = int(numeros[i])
        num2 = int(numeros[i+1])
        operador = operadores[i // 2]

        if operador == '+':
            resultado = num1 + num2
        else:
            resultado = num1 - num2
        respuestas.append(resultado)

#formando composicion de operaciones (columnas)

        espacio = max(len(numeros[i]), len(numeros[i + 1])) + 2
        arriba += numeros[i].rjust(espacio)
        abajo += operador + numeros[i + 1].rjust(espacio - 1)
        guiones += '-' * espacio
          
#espacios entre problemas
        if i != len(numeros) - 2:
            arriba += ' ' * 4 
            abajo += ' ' * 4 
            guiones += ' ' * 4 

#fomateo el valor de respuestas
    for i in range(len(respuestas)):
        espacio = max(len(numeros[2 * i]), len(numeros[2 * i +1])) + 2
        respuesta += str(respuestas[i]).rjust(espacio)

#espacio entre respuestas
        if i != len(respuestas) - 1:
            respuesta += ' ' * 4

#arreglo final y retorno
    if show_answers:
        arren_problems = '\n'.join((arriba, abajo, guiones, respuesta))
    else:
        arren_problems = '\n'.join((arriba, abajo, guiones))
    

    return arren_problems

print(f'\n{arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')





# Run unit tests automatically
main(module='test_module', exit=False)
