"""This file contains tools and recicle functions :)"""

def clean_and_uppercase(value:str)->str: #validar, limpiar espacios y convertir a upperCase
    value = value.replace(" ","")
    return value.upper()