# 7 Nos complicamos un poco más, ejemplo de licenciado de una aplicación con imágenes bajo GPLv3+. [<<](../README.md)

## ¿Qué tenemos?

Partimos de un pograma simple usando python y la librería tkitner para tema de ventanas y demás.

La diferencia respecto al programa en C es que mostramos una imagen.

Seguimos usando la licencia GPLv3.

## ¿Qué hacemos con los iconos y gráficos de nuestro programa?

A ver, se puede usar una licencia GPL para el material gráfico, pues forma parte del codigo fuente, pero para este caso concreto ¿porqué no usar una licencia creative commons?

Es fácil pensar que al ser material gráfico, una de estas licencias nos protege mejor, pues lo querremos usar en programas libres, pero también en guías, materiales didácticos, etc. Y para eso estan las licencias creative commons, no?

### Cuando combinemos licencias hay que estudiar su compatibilidad

Lo primero es ver que si el código es libre y GPL, ¿qué licencias son compatibles con nuestra licencia?

En el caso concreto de las creative commons estás son las que hay y lo que conllevarían junto con el código:

| | |
|---|---|
| [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)	| Creative commons 0, es como una licencia de dominio público, donde cualquier puede hacer cualquier cosa con el trabajo publicado. (venderlo, reutilizarlo en un programa cerrado, etc. |
| [CC-BY](https://creativecommons.org/licenses/by/4.0/)	| Esta licencia da también cualquier libertad de los trabajos derivados, la diferencia es que hay que nombrar al autor original. |
| [CC-BY-SA](https://creativecommons.org/licenses/by-sa/2.0/) | Esta licencia es es como la CC-BY, sólo que además obliga a que los trabajos derivados mantengan la misma licencia CC-BY-SA. **esta licencia es considerada problemática por como está redactada, y no se recomienda con trabajos bajo la GPL** |
| [CC-BY-SA-NC](https://creativecommons.org/licenses/by-nc-sa/2.0/) | Esta licencia es como la CC-BY-SA, sólo que además prohibe sacar beneficio económico con el trabajo publicado. **esta licencia no está considerada libre, y no es compatible con trabajos bajo la GPL**|
| cualquier creative commons sin obra derivada (ND) | Esta licencias prohiben trabajos derivados. **esta licencia no está considerada libre, y no es compatible con trabajos bajo la GPL**|

En la santa biblia de las licencias de la GNU comentan cada una de ellas.

### Como las licenciamos.

Lo ideal es usar además los metadatos de la imagen para incrustarles la licencia y el copyright, pero algo más básico y funcional es:

* Copiar la licencia completa en un COPYING en el raíz del proyecto.
* Editar el README del raíz y definiendo cada una de las imágenes del proyecto, ponerles un copyright y una cabecera de licencia.
* A su vez, en cada carpeta del proyecto dodne haya imágenes, añadir el COPYING de la licencia y un README donde igualmente definamos cada una de las imágenes, sus copyrights y cabeceras de licencia.

## ¡Vamos!

Pensemos como queremos licenciarlas, que queremos que se pueda hacer o no con las imágenes y nuestro programa, y buscar info sobre compatibilidades.

[Qué dice la GNU sobre la CCO](https://www.gnu.org/licenses/license-list.html#CC0)

[Qué dice la GNU sobre la CC-BY](https://www.gnu.org/licenses/license-list.html#ccby)

[Qué dice la GNU sobre la CC-BY-SA](https://www.gnu.org/licenses/license-list.html#ccbysa)

[Qué dice la GNU sobre la CC_BY-SA-NC](https://www.gnu.org/licenses/license-list.html#CC-BY-NC)

[Qué dice la GNU sobre la CC No Derivaties](https://www.gnu.org/licenses/license-list.html#CC-BY-ND)



