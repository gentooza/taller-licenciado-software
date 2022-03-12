#
#    Copyright 2022 Joaquín Cuéllar.
#    
#    This file is part of Hola Mundo Especial.
#
#    Hola Mundo Especial is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#    Hola Mundo Especial is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with Hola Mundo Especial. If not, see <https://www.gnu.org/licenses/>.


CC=gcc
CFLAGS=-I.

holamundo: main.o
	$(CC) -o hola_mundo main.o

all: clean hola_mundo

.PHONY: clean

clean:
	rm -f hola_mundo *.o
