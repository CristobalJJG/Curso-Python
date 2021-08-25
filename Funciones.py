def saludo(frase):
    if frase == "en":
        return("Hello")
    elif frase == "esp":
        return("Hola")
    elif frase == "fr":
        return("Bonjour")
    else:
        return("Hey")

print("esp, fr, en")
frase = input("Escriba el idioma: ")
nombre = input("Escriba un nombre: ")
print(saludo(frase),nombre)
