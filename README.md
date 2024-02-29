# Proyecto 1 Análisis y Diseño de Algoritmos

## Maquinas de Turing

En nuestro programa se utiliza un archivo .json para poder cargar una máquina. El estándar es el siguiente:

{
    "estados": "a,b,c,d,e",
    "alfabetoEntrada": "1,2,3,4",
    "alfabetoCinta": "1,3",
    "delta": "(a,0,*,b,R);(a,*,-,g,L)" <- donde "a" es el estado inicial, "0" es caracter de entrada "*" es el caracter que se escribe en la cinta, "b" es el estado al que pasa y "R" es la dirección a donde se mueve
    "estadoInicial": "a",
    "estadoAceptacion": "e"
    "estadoRechazo": "d"
}

Algunas convenciones:

"*" es el carácter que representa un espacio vacío. 
"-" representa que no se escribe nada
"R" Representa movimiento hacia la derecha, "N" no se realiza un movimiento, "L" movimiento a la izqueirda. 


## Maquina Fibonacci

Ver "maquinafibo.json" para máquina completa.

Las cadenas de entrada son cadenas de 1s, como "111" que indica que se quiere el 3er número de fibonacci, "11111" que representa el 5to número de fibonacci. 

La máquina devuelve también cadenas de 1s, con espacios vacíos. Para obtener cual es el número de fibonacci correspondiente a la entrada se deben contar los 1s. 

Para la entrada "111" la respuesta es: 

['1', '1', '*', '*', '*', '*', '*', '*', '*', '*', '*']

Que nos indica que el 3er número de fibonacci es 2. 

## Programa

Al iniciar el programa se tiene un menú con las siguientes opciones.

Bienvenido al simulador de máquinas de Turing

Escoja una opcion: 
1. Cargar una máquina
2. Evaluar cadena en máquina actual (escribir cadena)
3. Encontrar número de fibonacci (escribir indice a encontrar) 
4. Salir.
¿Que desea hacer? (escriba solo 1, 2, 3 o 4):

Aquí inicialmente se debe escribir 1 para cargar una máquina. Luego se pide el nombre del archivo, en el caso de la máquina de fibonacci es "maquinafibo.json" lo que se debe escribir. 

Luego se pueden evaluar cadenas de la manera normal, escribiendo la cadena de entrada utilizando la opción 2, o específicamente para la maquina de fibonacci se puede utilizar la opción 3 que nos permite dar un número entero que lo convierte a la cadena de 1s correspondiente y al recibir el output cuenta los 1s automáticamente. 

Para ambas de las opciones anteriores se puede seleccionar si se quiere ver la cinta o no, generalmente si no se ve la cinta es más rápido el programa, pero la funcionalidad es la misma. 

Para salir se puede seleccionar la opción 4. 
