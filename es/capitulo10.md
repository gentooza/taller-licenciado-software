# 10 Buenas prácticas de licenciado y curiosidades varias. [<<](../README.md)

## La FSF posee varias recomendaciones de buenas prácticas, que son interesantes seguir.

### 1. Licenciar con copyleft.

Es recomendable proteger el código libre para que lo siga siendo. Veremos que hay varias recomendaciones polémicas y esta es la que más!

La FSF ofrece una licencia con excepción para programas de software cerrado, la LGPL, pero incluso no recomienda su uso. Pensad que el objetivo de la FSF no es que su código sea el más usado y extendido, su objetivo es que todo el conocimiento que genere en forma de código fuente sea libre, y sirva para mejorar aplicaciones libres.

Hay sin embargo excepciones:

#### A. Considera válidas licencias sin copyleft y sencillas para el desarrollo de programas sencillos.

Pues agiliza mucho el trabajo, y minimiza la gestión de copyrights, etc.

#### B. Si se aporta a un proyecto cuya licencia es sin copyleft.

Para no generar conflicto en la comunidad.

#### C. Para aplicaciones móviles recomienda la Apache 2.0

Es de hecho la única licencia sin copyleft que recomienda si se desea usar una de este tipo, pues posee claúsulas de protección respecto las patentes de software.

### 2. Utilizar la claúsula *[...]either version 3 of the License, or (at your option) any later version.[...]*

Está mal licenciar una aplicación diciendo que está bajo la versión X de la GPL, se prefiere decir:

Bajo la versión X o cualquier otra versión a tu disposición.

Esto permite que un código bajo una versión antigua de la licencia GPL (o cualquier otra) sea fácilmente actualizable a una versión más moderna, que esté más actualizada y al día.

#### Ejemplo del núcleo Linux!

Linux está licenciado bajo la GPLv2 y sólo la versión 2. No tiene la claúsula de o cualquier otra versión de la GPL que se quiera.

La versión 2 de la GPL posee una trampa, que permite un fenómeno llamado [tivoización](https://es.wikipedia.org/wiki/Tivoizaci%C3%B3n). Esto permite que Linux sea incluido en los móviles Android, pero las empresas puedan firmar las compilaciones de manera digital y el arranque del sistema sólo aceptar estas versión firmadas del núcleo.

Esto permite de facto que algunos modelos de teléfono sólo puedan ejecutar el linux en binario de la empresa de turno. (con las modificaciones que le hayan podido hacer, y sin una versión pública del código)

Este fenómeno llevó a la edición de la versión 3 de la GPL, pero exigía que los Copyright Holders aceptaran en su conjunto el cambio de licencia.

[Linus Torvalds se ha negado y ha cargado desde siempre contra la GPLv3](https://www.linux.com/news/torvalds-gplv3-final-draft/).

### 3, etc.

El resto de prácticas es más o menos lo que hemos hecho hasta ahora. Adjuntar las licencias en código fuente, licenciarlo todo (archivos de configuración también), usar notas de copyright estándar, etc.

[referencia](https://savannah.gnu.org/maintenance/HowToGetYourProjectApprovedQuickly/)

[referencia2](https://www.gnu.org/licenses/license-recommendations.html)

***

```
copyright 2022 Joaquín Cuéllar

This work is licensed under the Creative Commons Attribution 3.0 Unported License. 
You should have received a copy of the Creative Commons Attribution 3.0 Unported License along with this program.
To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```


