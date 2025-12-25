#Crear una función que: reciba una contraseña (string), devuelva True si tiene 8 o + caracteres, False si no.


def tiene_longitud_segura(password):
    if len(password) >= 8:
        return True
    else:
        return False
    
clave = input("Ingrese una contraseña: ")
print("Tiene longitud segura: " ,tiene_longitud_segura(clave))

#Crear una función que: reciba la contraseña, devuelva True si contiene al menos un nº, False si no.

def tiene_numero(password):
    for i in password:
        if i.isdigit():
            return True
    return False
print("Tiene numero: ", tiene_numero(clave))

#Crear una funcion que: Reciba la contraseña y devuelva True si tiene al menos una mayuscula, False si no.

def tiene_mayusculas(password):
    for i in password:
        if i.isupper():
            return True
    return False

print("Contiene alguna mayuscula: ", tiene_mayusculas(clave))

#Crear una funcion que: Reciba la contraseña, devuelva True si contiene al menos un simbolo, False si no.

def tiene_simbolo(password):
    for i in password:
        if not i.isalnum():
            return True
    return False

print("Contiene algún simbolo: ", tiene_simbolo(clave))


def analizar_contraseña(password):
    puntos = 0

    print("\nResultado del análisis:")

    if tiene_longitud_segura(password):
        print("✔ Longitud segura")
        puntos += 1
    else:
        print("❌ Longitud insuficiente")

    if tiene_numero(password):
        print("✔ Contiene número")
        puntos += 1
    else:
        print("❌ No contiene número")

    if tiene_mayusculas(password):
        print("✔ Contiene mayúscula")
        puntos += 1
    else:
        print("❌ No contiene mayúscula")

    if tiene_simbolo(password):
        print("✔ Contiene símbolo")
        puntos += 1
    else:
        print("❌ No contiene símbolo")

    print("\nNivel de seguridad:", end=" ")

    if puntos == 4:
        print("FUERTE 🔐")
    elif puntos >= 2:
        print("MEDIA ⚠️")
    else:
        print("DÉBIL ❌")

analizar_contraseña(clave)