import re
from validate_docbr import CPF
#pip install validate-docbr

def titulo_valido(titulo):
    return titulo.isalpha()
        
def celular_valido(numero_celular):
    #85 98789-1209
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta=re.findall(modelo, numero_celular)
    return resposta

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)
