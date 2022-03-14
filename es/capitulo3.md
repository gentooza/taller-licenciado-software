# 3 Concepto de Copyleft y qué conlleva. [<<](../README.md)
[<< cap2](./capitulo2.md) - [cap4 >>](./capitulo4.md)

Ya tenemos un glosario interesante de la FSF para poder elegir una licencia que sea libre, pero vemos que hacen muchísima referencia al concepto de copyleft dentro de cada licencia.

Vamos a verlo, porque es clave a la hora de trabajar y decidir como queremos licenciar el software


## El concepto.

[Viva la wikipedia](https://es.wikipedia.org/wiki/Copyleft)

El Copyleft básicamente es, si queremos que las obras derivadas de la nuestra preserven las mismas 4 libertades del software libre, que tenía originalmente nuestro trabajo.

## El debate.

Con todo el respeto del mundo (podemos dejarnos matices en el camino, seguro), este podría ser un resumen corto de los dos puntos de vista que vamos a encontrar.

### A favor del copyleft

Los defensores del software libre, bajo el punto de vista de la FSF, defienden que el software libre debe de protegerse, es decir, que una obra que se ha licenciado como libre jamás pueda ser transformada en un trabajo de software cerrado.

Piensan que el conocimiento generado se debe preservar siempre como libre pues pertenece a la comunidad, y es mejor para el progreso humano.

[Se prefieren las licencias típicas de la FSF: GPL, AGPL, LGPL, etc. ó la MPL, etc.](https://www.gnu.org/licenses/copyleft.es.html)

### En contra del copyleft

Los que están en contra del copyleft, argumentan que se debe ser tan libres, que no se debería decir a nadie como usar un trabajo de software libre.

Piensan que condicionar como alguien debe publicar su trabajo es cohartarle la libertad.

Se prefieren las licencias llamadas permisivas, tipo BSD, apache, etc.

## Posicionamiento de la FSF

La Free Software Foundation, evidentemente, apuesta por licencias con copyleft e incentiva su uso. De hecho para publicar programas en su portal estos deberán utilizar algunas de sus licencias. (de otra forma se debería argumentar muy bien)

Aún así, establece que si se hacen mejoras o aportes a programas que ya estaban licenciados previamente, se siga usando la misma licencia, aunque sea sin copyleft, que se usara, para seguir apostando por el trabajo comunitario y no crear conflicto en la comunidad. [referencia](https://www.gnu.org/licenses/license-recommendations.html) (explicamos porqué en el punto siguiente)

## Es complejo, ¡pensadlo bien!

Pensad que tenéis que usar código libre junto con elementos de software cerrado, si el código fuera tipo GPL estaríais vulnerando la licencia. (se podría usar una LGPL, claro).

O pensad que queréis tener una versión libre de vuestro trabajo, para que sea reutilizada en multitud de proyectos y así poder mejorarla, pero queréis tener la oportunidad de poder recuperar ese trabajo mejorado en algún proyecto que necesitéis que sea cerrado.

Tened en cuenta también que **El copyleft siempre vence al no copyleft**, aquí os dejo el ejemplo del openoffice y el libreoffice:

+ Ambos comparte un origen común.
+ Openoffice tiene una licencia sin copyleft, Apache2.
+ Libreoffice tiene una licencia con copyleft, MPL2
+ **Libreoffice puede coger mejoras que se apliquen al Openoffice, pero Openoffice no puede coger mejoras de Libreoffice!!**
+ no podemos convertir código con copyleft a código sin copyleft, pero sí al revés.
+ Libreoffice siempre será mejor programa. (a menos que su comunidad colapsara, claro)

[repetimos el enlace del punto anterior, una guía de la FSF explicando como elegir nuestra licencia.](https://www.gnu.org/licenses/license-recommendations.html

***

```
copyright 2022 Joaquín Cuéllar

This work is licensed under the Creative Commons Attribution 3.0 Unported License. 
You should have received a copy of the Creative Commons Attribution 3.0 Unported License along with this program.
To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```

