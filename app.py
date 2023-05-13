# Importamos el módulo hashlib para poder hacer uso de las funciones de hash.
import hashlib

# archivo hashes.txt es el archivo PASSWORD.md (solo se cambio el nombre y extension para la conversion)
# Abrimos el archivo "hashes.txt" en modo de lectura "r" y lo asignamos a la variable f utilizando un contexto with, lo que nos garantiza que el archivo será cerrado automáticamente al salir del bloque with.
with open("hashes.txt", "r") as f:
    # Leemos todas las líneas del archivo f y creamos una lista md5_hashes que contiene todas las líneas leídas, eliminando el salto de línea al final de cada una de ellas.
    md5_hashes = [line.strip() for line in f]

# Abrimos el archivo "rockyou.txt" en modo de lectura "r" y lo asignamos a la variable f utilizando un contexto with, lo que nos garantiza que el archivo será cerrado automáticamente al salir del bloque with.
with open("rockyou.txt", "r", errors='ignore') as f:
    # Abrimos el archivo "rockyou.txt" en modo de lectura "r" y lo asignamos a la variable f utilizando un contexto with, lo que nos garantiza que el archivo será cerrado automáticamente al salir del bloque with.
    rockyou_words = {line.strip() for line in f}

# Abrimos el archivo "passwords.txt" en modo de lectura "r" y lo asignamos a la variable f utilizando un contexto with, lo que nos garantiza que el archivo será cerrado automáticamente al salir del bloque with.
with open("passwords.txt", "r", errors='ignore') as f:
    # Leemos todas las líneas del archivo f y creamos un conjunto password_words que contiene todas las palabras leídas, eliminando el salto de línea al final de cada una de ellas. También ignoramos cualquier error de codificación que pueda ocurrir durante la lectura.
    password_words = {line.strip() for line in f}

# Abrimos el archivo "darkc0de.txt" en modo de lectura "r" y lo asignamos a la variable f utilizando un contexto with, lo que nos garantiza que el archivo será cerrado automáticamente al salir del bloque with.
with open("darkc0de.txt", "r", errors='ignore') as f:
    # Leemos todas las líneas del archivo f y creamos un conjunto darks0de_words que contiene todas las palabras leídas, eliminando el salto de línea al final de cada una de ellas. También ignoramos cualquier error de codificación que pueda ocurrir durante la lectura.
    darks0de_words = {line.strip() for line in f}

# Abrimos el archivo "plain.txt" en modo de escritura "w" y lo asignamos a la variable f utilizando un contexto with, lo que nos garantiza que el archivo será cerrado automáticamente al salir del bloque with.
with open("plain.txt", "w") as f:
    # Iteramos a través de cada uno de los hashes en la lista md5_hashes.
    for hash in md5_hashes:
        # Inicializamos la variable reversed a False.
        reversed = False
        # Para cada palabra en el conjunto "rockyou_words"
        for word in rockyou_words:
            # Si el hash MD5 de la palabra coincide con el hash actual
            if hashlib.md5(word.encode()).hexdigest() == hash:
                # Escribir la palabra en el archivo "plain.txt"
                f.write(word + "\n")
                # Establecer "reversed" en True para indicar que se encontró una coincidencia
                reversed = True
                # Salir del bucle for actual
                break
        # Si no se encontró una coincidencia en "rockyou_words"
        if not reversed:
            # Para cada palabra en el conjunto "password_words"
            for word in password_words:
                # Si el hash MD5 de la palabra coincide con el hash actual
                if hashlib.md5(word.encode()).hexdigest() == hash:
                    # Escribir la palabra en el archivo "plain.txt"
                    f.write(word + "\n")
                    # Establecer "reversed" en True para indicar que se encontró una coincidencia
                    reversed = True
                    # Salir del bucle for actual
                    break
        # Si no se encontró una coincidencia en "password_words"
        if not reversed:
            # Para cada palabra en el conjunto "darks0de_words"
            for word in darks0de_words:
                # Si el hash MD5 de la palabra coincide con el hash actual
                if hashlib.md5(word.encode()).hexdigest() == hash:
                    # Escribir la palabra en el archivo "plain.txt"
                    f.write(word + "\n")
                     # Establecer "reversed" en True para indicar que se encontró una coincidencia
                    reversed = True
                     # Salir del bucle for actual
                    break
        if not reversed:
            # Si no se encontró ninguna coincidencia, escribir una línea en blanco en el archivo "plain.txt"
            f.write("\n")

#Abrir un nuevo archivo llamado "new_passwords.txt" en modo escritura ("w")
with open("new_passwords.txt", "w") as f:
    # Para cada línea en el archivo "plain.txt"
    for line in open("plain.txt", "r"):
        # Eliminar el carácter de salto de línea al final de la línea y asignarla a la variable "word"
        word = line.strip()
        # Si la línea es una línea en blanco, escribir otra línea en blanco en el archivo "new_passwords.txt"
        if not word:
            f.write("\n")
        # De lo contrario, calcular el hash SHA-256 de la palabra y escribirlo en el archivo "new_passwords.txt"
        else:
            sha256_hash = hashlib.sha256(word.encode()).hexdigest()
            f.write(sha256_hash + "\n")
