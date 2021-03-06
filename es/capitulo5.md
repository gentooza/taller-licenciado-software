# 5 Ejemplo básico de licenciado de un 'Hola mundo' bajo GPLv3+. [<<](../README.md)
[<< cap4](./capitulo4.md) - [cap6 >>](./capitulo6.md)

## ¿Qué tenemos?

Para el primer ejemplo partimos de un programa sencillo, el típico hola mundo en C.

Para complejizarlo con poco le añadimos un Makefile que nos facilite la compilación y la limpieza de los binarios, y un típico README y un CHANGELOG.

Tenéis el ejemplo licenciado en la carpeta de ejemplos del raíz de esta guía.

## ¿Qué licencia elegimos y qué conlleva?

¡Lo primero es elegir qué licencia queremos utilizar!

Analizamos varias licencias de ejemplo que podríamos plantearnos cara a licenciar nuestro pequeño programa, razonamos su utilidad y conveniencia cara a elegir la más adecuada.

### LGPLv3?

Con la [LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.en.html) nuestro programa será software libre, y estará protegido con copyleft, por lo que, como hemos visto ya, si alguién lo modifica tendrá que seguir publicando el código como software libre.

Lo único es que tiene una llamada excepción en trabajos combinados, viene del concepto de linkado en C / C++, Eso es que se puede usar como librería en un programa de código cerrado.

Esto se ha pensado para la programación de librerías de software, donde la quieres libre, pero no quieres desincentivar su uso en programas cerrados.

En nuestro caso, como es un programa y no una librería, podemos decidimos desechar esta licencia.

### AGPLv3?

Con la [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html) nuestro programa será software libre, y estará protegido con copyleft también, por lo que, como hemos visto ya, si alguién lo modifica tendrá que seguir publicando el código como software libre.

Lo único es que tiene una claúsula especial **para aplicaciones web** donde obliga a publicar un enlace con el código fuente que sea visible a los usuarios de dichas aplicaciones.

En nuestro caso no es una aplicación web! es una aplicación local, así que la desechamos por que no lo vemos necesario.

### GPLv3?

Con la [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) nuestro programa será software libre, y estará protegido con copyleft también, además está pensada para aplicaciones de escritorio.

Es nuestra opción!

### Apache2?

Podríamos plantearnos usar una **licencia sin copyleft**, en ese caso la que siempre recomiendo la FSF es la apache2, porque posee protección contra patentes. (de hecho para aplicaciones móviles es activamente recomendada)

Licenciar nuestra aplicación con Apache2, significa que cualquier persona u organización podría coger nuestro código, modificarlo, y publicarlo como software cerrado.

Por otro lado, las licencias sin copyleft suelen ser más fáciles de gestionar, tienen menos exigencias de licenciado (normalmente es agregar la cabecera igual, pero facilita la gestión del copyright como veremos más adelante) y los trabajos derivados son más fáciles de licenciar también.

En los ejemplos vamos a usar sólamente licencias con copyleft. (el autor tampoco tiene experiencia con licencias sin copyleft :-S)

## ¿Qué tenemos qué hacer con la GPLv3?

### Copiar el texto completo de la licencia

Ea, en la web de la [GNU (brazo informático de la FSF)](https://www.gnu.org/licenses/gpl-3.0.en.html) tenemos versiones en HTML, PDF, etc. y en [texto plano](https://www.gnu.org/licenses/gpl-3.0.txt), basta con descargar la versión en [texto plano](https://www.gnu.org/licenses/gpl-3.0.txt) y pegarla en el raíz del proyecto bajo el nombre COPYING.

En la carpeta *ejemplos COPYING* de esta guía hay igualmente varias licencias de ejemplo.

### Establecer la cabecera de copyright.

Definamos como será nuestra cabecera de copyright.

El copyright es fácil de definir pues nadie más va a programar esto, podemos poner nuestro nombre que somos quienes están desarrollando la aplicación.

El año el actual, y hay que decidir como se va a llamar nuestra aplicación. En este caso le vamos a poner *Hola Mundo Especial*.

Quedaría así:

```
    Copyright 2022 Joaquín Cuéllar.
    
    This file is part of Hola Mundo Especial.

    Hola Mundo Especial is free software: you can redistribute it and/or modify it under 
    the terms of the GNU General Public License as published by the Free Software Foundation,
    either version 3 of the License, or (at your option) any later version.

    Hola Mundo Especial is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
    PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Hola Mundo Especial.
    If not, see <https://www.gnu.org/licenses/>.

```

#### En código fuente .c

Introducirlo en los archivos de código fuente es fácil, será utilizando comentarios. Todos los lenguajes de programación nos lo permiten, no?

En C usaremos por bloques (/\* \*/) o por líneas (//), como lo prefiramos.

#### En archivos de información README, CHANGELOG.

Los archivos de información son fáciles también, además que podemos ponerlo de forma más o menos estética.

Como ya hemos comentado se puede poner también al final para facilitar la lectura.

#### En utilidades como el Makefile.

En un Makefile haremos como con el código fuente, ¿como se puede comentar en un Makefile? Lo investigamos y vemos que es con corchetes (#)

Pues ya está.


***

```
copyright 2022 Joaquín Cuéllar

This work is licensed under the Creative Commons Attribution 3.0 Unported License. 
You should have received a copy of the Creative Commons Attribution 3.0 Unported License along with this program.
To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```
