# reverse-MD5
 Este es un script de Python para crackear hashes MD5 utilizando diccionarios de palabras comunes. El script utiliza los diccionarios "RockYou", "passwords" y "darkc0de" para crackear los hashes.
 
## Requisitos
El script requiere la librería hashlib para funcionar correctamente. Esta librería viene incluida en la instalación de Python y no requiere de instalación adicional.

## Uso
1. Coloca los hashes MD5 que se desean crackear en el archivo hashes.txt. Cada hash debe estar en una línea separada.
2. Coloca las palabras del diccionario "RockYou" en el archivo rockyou.txt. Cada palabra debe estar en una línea separada.
3. Coloca otras palabras comunes en los archivos passwords.txt y darkc0de.txt. Cada palabra debe estar en una línea separada.
4. Ejecuta el script desde la línea de comandos de Python con el comando python crack.py.
5. Los resultados se guardarán en el archivo new_passwords.txt. Este archivo contendrá los hashes SHA256 de las contraseñas descifradas.

## Contribución
Este proyecto es OpenSource, por lo que cualquier persona puede contribuir y mejorarlo. Si deseas contribuir, simplemente haz un fork del proyecto y envía tus cambios a través de un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.
