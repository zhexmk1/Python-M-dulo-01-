
"""
Introdução ao empacotamento e desempacotamento
"""
'''
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
'''

#CRIA VARIÁVEIS PARA CARA PACOTE DE TUPLAS DENTRO DA LISTA, O "*_" SIGNIFICA QUE NÃO SERA UTILIZADO O RESTO
nome1, nome2, *_ = ['Maria', 'Pedro','João','Marcelo']
print(nome1, nome2)
