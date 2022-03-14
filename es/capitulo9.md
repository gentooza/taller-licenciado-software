# 9 Mantenenimiento del licenciado, gestionar forks, obras derivadas, reutilizaciones, etc. [<<](../README.md)

## Mantenimiento de la licencia.

Para mantener la licencia al día, lo único que habrá que hacer es actualizar el año del copyright de cada archivo que se vaya actualizando.

Si el código ya se publicó lo podemos considerar como registrado, no hay que hacer más.

## Si hacemos un fork de una aplicación para devolver una mejora.

Si no hemos firmado acuerdo de cesión del copyright, lo suyo a efectos legales es *marcar* el archivo de código modificado añadiendo una nueva línea de copyright holder, con el año de la modificación y nuestros datos.

Cuando hay muchos Copyright Holders se suele usar archivos externos como AUTHORS, etc.

## Si hacemos un fork para llevar un proyecto paralelo o para reutilizarlo en otros proyectos.

Igual que en el punto anterior, sólo que ahora habrá modificaciones que no devolveremos al proyecto original.

Deberemos renombrar el proyecto, y dependiendo de la licencia del proyecto original deberemos mantener los copyright originales o no:

+ En licencias sin copyleft no hará falta.
+ En licencias con copyleft seguramente sí.

A su vez podremos decidir si relicenciamos la aplicación o no:

+ En licencias sin copyleft podremos *absorver* el código en un proyecto con copyleft sin problema
+ En licencias con copyleft, deberemos ver la compatibilidad de licencias, varios ejemplos:
    - un código bajo la GPLv3+ se podrá convertir en otro bajo la AGPLv3+ sin problema.
    - un código bajo la GPLv2 **no** se podrá convertir en otro bajo la GPLv3+.
+ Nunca podremos pasar de licencias con un copyleft fuerte a licencias más laxas (sin copyleft).

