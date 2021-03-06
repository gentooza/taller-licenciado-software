# 6 Concepto de Copyright y qué conlleva.. [<<](../README.md)
[<< cap5](./capitulo5.md) - [cap7 >>](./capitulo7.md)

## No es contradictorio? Lo hacemos libre pero tiene copyright? Qué es?

El concepto legal, parece ser (no soy jurista!) que es que tenemos la propiedad intelectual de nuestra obra (derechos de autor), pero decidimos de qué manera se gestiona su uso, derivación, distribución, etc. (los llamados derechos de explotación)

Cualquier obra intelectual tiene una propiedad intelectual y unos derechos de explotación, por eso hay que establecerlos explícitamente de cara a aspectos legales.

## Creamos algo libre y tiene nuestro copyright, qué podemos hacer y qué no?

### Podemos

Cuando creamos una obra y tiene nuestro copyright, podemos licenciarla bajo multiples licencias.

Podemos tener el mismo código bajo GPLv3, y a la vez bajo apache2. Ó guardarnos una versión cerrada también, es nuestra obra y podemos gestionar sus derechos de explotación como nos venga en gana.

### No podemos

Una vez que se haya publicado bajo una licencia, no podemos evitar que se replique, que sea modificado el trabajo, y que las obras derivadas escapen a nuestro control.

La maravilla del software libre es esa, y cuesta a veces entenderla, en cuanto algo es libre y público, ya pertenece a la humanidad.

## Reutilizamos algo libre y tiene copyright, qué podemos hacer y qué no?

### Podemos

Podemos y **debemos** añadir nuestro copyright a los archivos de código fuente que modifiquemos. Ahora el trabajo tendrá dos o más copyright holders!

Podemos relicenciar el programa bajo licencias compatibles:

+ Podemos reutilizar y relicenciar bajo licencias compatibles. Por ejemplo, código bajo la GPLv3 pasarlo a la AGPLv3.
+ Podemos reutilizar y relicenciar código bajo licencia sin copyleft (MIT, BSD, apache2...) en un programa bajo licencia con copyleft, AGPLv3 por ejemplo.
+ Podemos mantener la misma licencia, por supuesto.

### No podemos

No podemos eliminar las autorías previas. A menos que sean licencias sin copyleft que lo permitan o de dominio público, aunque sería una buena práctica reconocerlas de algún modo.

No podemos, por supuesto, relicenciar el programa bajo licencias incompatibles:

+ No podemos reutilizar código con copyleft en un programa bajo licencia sin copyleft

+ [No podemos relicenciar bajo licencias incompatibles](https://www.gnu.org/licenses/license-list.es.html), por ejemplo un programa bajo la GPLv2 no podemos pasarlo a la GPLv3.

## Los acuerdos de cesión del copyright, porqué se hacen?

Vemos que tener el copyright de un programa es un tema importante, pensad por ejemplo que un programa que habéis desarrollado y que haya recibido aportes de la comunidad. Si algún día queréis relicenciarlo tendréis que poner de acuerdo a **cada una de las personas que tienen el copyright del código** para ese cambio.

Para ceder el copyright existen los acuerdos de cesión de copyright, un documento así tendréis que firmar si realizáis aportes de código a un programa oficial de la GNU (Free Software Foundation)

Si no habéis firmado un documento así y habéis participado en un proyecto, tenéis vuestro copyright sobre el código que habéis aportado, aunque no se haya plasmado en una nota de copyright explícita.

Os comparto el ejemplo de la [FSF](https://www.gnu.org/licenses/why-assign.html)

## El famoso caso Linux, ejemplo de la importancia del copyright:

El núcleo linux posee una anomalía, y es que está licenciado bajo la GPLv2, pero no permite su actualización a versiones posteriores de la GPL (lo que llamaríamos GPLv2+)

El proyecto no contempla la cesión del copyright de quién aporte al proyecto, así que ha recibido aportaciones de multitud de personas que tienen su derecho de copyright en el código.

Para realizar una actualización de la licencia habría que poner a todas las personas participantes de acuerdo en hacer ese cambio de licencia, pero no se ha conseguido. (El propio Linus Torvalds se opone)


***

```
copyright 2022 Joaquín Cuéllar

This work is licensed under the Creative Commons Attribution 3.0 Unported License. 
You should have received a copy of the Creative Commons Attribution 3.0 Unported License along with this program.
To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```

