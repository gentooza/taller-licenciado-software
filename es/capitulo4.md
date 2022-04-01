# 4 Como se licencia un programa informático, aquí las guías de referencia de la FSF. [<<](../README.md)
[<< cap3](./capitulo3.md) - [cap5 >>](./capitulo5.md)

## ¿Por donde empezamos?

Tendremos que tener en cuenta varios conceptos, pero lo que hay que hacer veremos que es sencillo y básicamente son dos pasos.

### Qué llamamos código fuente de nuestro programa.

lo compone por supuesto los archivos de código...

Pero también los de configuración (.ini, .json, .yaml...), las imágenes necesarias de la aplicación, las utilidades necesarias (Makefiles, CMakelists, etc.), de información (README, CHANGELOG...)...

Se tiene que licenciar todo lo necesario de la aplicación para poder funcionar tal cual por cualquier persona.

### 1er paso: Añadimos una copia de la licencia con el programa.

En el raíz de nuestro proyecto debe de venir un archivo llamado COPYING con el texto plano de la licencia elegida.

En la guía hay varios ejemplos en la carpeta *ejemplos COPYING*.

### 2o paso: Añadimos *Copyright notices* en cada archivo de código fuente.

El *Copyright notice* es una cabecera que habrá que agregar en cada archivo de código fuente de nuestra aplicación, donde definirá quién posée los derechos de copyright de la obra, el llamado *copyright holder*, a qué proyecto pertenece ese archivo y bajo qué licencia está ese proyecto, lo que se llama *license notice*.

Hay que ser conscientes aquí de que no basta con copiar la licencia al raíz del proyecto, a efectos legales cada documento debe venir marcado con esta cabecera.

[referencia](https://savannah.gnu.org/maintenance/ValidNotices/)

#### A qué llamamos *Copyright Holder*

Copyright holder, es quién tiene el copyright de la obra, a nombre de quién (o qué organización) está licenciado el programa. Más adelante veremos el concepto de copyright y su importancia.

el copyright holder se define así:
```
Copyright (C) _year1_, _year2_, _year3_ _copyright-holder_
```

Los años se recomienda ponerlos individuales, o por rangos. el Coyright-holder debe de ser un nombre real de persona o de entidad.

#### A qué llamamos *license notice*

```
    This file is part of Foobar.

    Foobar is free software: you can redistribute it and/or modify it under the terms
    of the GNU General Public License as published by the Free Software Foundation,
    either version 3 of the License, or (at your option) any later version.

    Foobar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
    PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Foobar.
    If not, see <https://www.gnu.org/licenses/>. 
```

Iría a continuación del *Copyright holder* y viene a explicar que el archivo en concreto de código fuente forma parte del proyecto Foobar (como ejemplo) explica que está licenciado bajo GPLv3 o cualquier versión posterior (GPLv3+) que viene sin garantía, y que el lector debería de haber recibido un archivo con el texto completo de la licencia junto con el proyecto.

Esta nota de licencia variará dependiendo de la licencia que elijamos, con cada licencia habrá que seguir las instrucciones pertinentes. En esta guía vamos a licenciar bajo licencias GPL donde las cabeceras son todas similares.

### referencias y conclusiones

En definitiva es copiarnos la licencia al raíz del proyecto y agregar a cada archivo de código fuente esta cabecera completa. (usamos la GPLv3+ de ejemplo):

```
    Copyright 2022 María de las Mercedes Arjona Pérez.

    This file is part of Foobar.

    Foobar is free software: you can redistribute it and/or modify it under the terms
    of the GNU General Public License as published by the Free Software Foundation,
    either version 3 of the License, or (at your option) any later version.

    Foobar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;                     
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
    PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Foobar.   
    If not, see <https://www.gnu.org/licenses/>. 

```

En los archivos de código fuente pondremos la cabecera en la cabecera (jajaja) de cada documento, pero en el CHANGELOG o el README, **lo podemos agregar al final** para facilitar su lectura.

El portal de código de la GNU, GNU Savannah tiene buenas guías sobre como licenciar correctamente, aunque vienen un poco caóticas, os adjunto las que creo que son fundamentales:

* [https://savannah.gnu.org/maintenance/HowToGetYourProjectApprovedQuickly/](https://savannah.gnu.org/maintenance/HowToGetYourProjectApprovedQuickly/)
* [https://savannah.gnu.org/maintenance/ValidNotices/](https://savannah.gnu.org/maintenance/ValidNotices/)
* [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/)

***

```
copyright 2022 Joaquín Cuéllar

This work is licensed under the Creative Commons Attribution 3.0 Unported License. 
You should have received a copy of the Creative Commons Attribution 3.0 Unported License along with this program.
To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```
