# Proyecto 1 Análisis y Diseño de Algoritmos

## 1. Máquinas de Turing
### a. Convenciones elegidas
En nuestro programa se utiliza un archivo `.json` para poder cargar una máquina. El estándar es el siguiente:
```json

{
    "estados": "a,b,c,d,e",
    "alfabetoEntrada": "1,2,3,4",
    "alfabetoCinta": "1,3",
    "delta": "(a,0,*,b,R);(a,*,-,g,L)", 
    "estadoInicial": "a",
    "estadoAceptacion": "e",
    "estadoRechazo": "d"
}

```
En donde, `delta` corresponde a la función de transición. Sus elementos son:
* "a" es el estado inicial
* "0" es caracter de entrada
* "*" es el caracter  que se escribe en la cinta
* "b" es el estado al que pasa
* "R" es la dirección a donde se mueve

Tomar nota de que:

* "*" es el caracter que representa un espacio vacío. 
* "-" representa que no se escribe nada (se deja el caracter que ya estaba escrito).
* "R" representa movimiento hacia la derecha, "N" no se realiza un movimiento, "L" movimiento a la izquierda. 


### b. Máquina Fibonacci
#### Generalidades 

Ver `maquinafibo.json` para máquina completa.

Las cadenas de entrada son cadenas de 1s, como `111` que indica que se quiere el 3er número de fibonacci, `11111` que representa el 5to número de fibonacci. 

La máquina devuelve también cadenas de 1s, con espacios vacíos. Para obtener cuál es el número de fibonacci correspondiente a la entrada se deben contar los 1s. 

Para la entrada "111" la respuesta es: 

```python
['1', '1', '*', '*', '*', '*', '*', '*', '*', '*', '*']
``` 

Que nos indica que el 3er número de fibonacci es 2. 

#### Componentes de la máquina 
La configuración de la máquina de Fibonacci ha sido seleccionada de la solución de [Vinokur (s.f.)](https://arxiv.org/pdf/cs/0601050.pdf), en donde se define los elementos de la máquina de la siguiente manera:
|Elemento|Componente|
|------|--------|
|Estados|q0,qf,q101,q102,q103,q104,q105,q106,q107,q108,q109,q201,q202,q203,q204,|
|Estados|q301,q302,q303,q304,q305,q306,q307,q308,q309,q310,q311|
|Estados|q401,q402,q403,q404,q501,q502,q503,q601,q602,q603,q604|
|Estados|q701,q702,q703,q704,q801,q802,q803,q804,q805,q806,q807,q808,q809,g|
|Estado inicial|q0|
|Estado de aceptación|qf|
|Estado de rechazo|g|
|Alfabeto de entrada|{1}|
|Alfabeto de Salida|{b,x,*}|
|Función de transición|Consultar archivo [funcion transicion](./Transiciones.pdf)|

#### Diagrama de la máquina 
<a href="logo github">
<img src="https://github.com/gon21077/proyecto1ADA/blob/main/Diagrama%20Maquina.png" align="middle"></a>

También disponible [aquí](https://lucid.app/lucidchart/67f28186-2fd6-4094-97ea-28c89341747f/edit?invitationId=inv_6db535a5-ceae-40ca-b550-30ddd4cbed00)
## 2. Funcionamiento del Programa

Al iniciar el programa se tiene un menú con las siguientes opciones.

```
Bienvenido al simulador de máquinas de Turing

Escoja una opcion: 
1. Cargar una máquina
2. Evaluar cadena en máquina actual (escribir cadena)
3. Encontrar número de fibonacci (escribir indice a encontrar) 
4. Salir.
¿Que desea hacer? (escriba solo 1, 2, 3 o 4):
``` 
Aquí inicialmente se debe escribir 1 para cargar una máquina cualquiera de Turing. Luego se pide el nombre del archivo, en el caso de la máquina de fibonacci es `maquinafibo.json` lo que se debe escribir. 

Luego se pueden evaluar cadenas de la manera normal, escribiendo la cadena de entrada utilizando la opción 2, o específicamente para la máquina de fibonacci se puede utilizar la opción 3 que nos permite dar un número entero que lo convierte a la cadena de 1s correspondiente y al recibir el output cuenta los 1s automáticamente. 

Para ambas de las opciones anteriores se puede seleccionar si se quiere ver la cinta o no, generalmente si no se ve la cinta es más rápido el programa, pero la funcionalidad es la misma.     

Para salir se puede seleccionar la opción 4. 

## 3. Análisis empírico 
### a. Entrada de pruebas usadas
Para la realización de las pruebas, se utilizó el archivo `test.py` en donde no se realizaba la impresión de cada...
|Entrada| Tiempo (s)|
|-------|----------|
|1| 0.0006389003247022629|
|2| 0.0009689000435173512|
|3| 0.0011298996396362782|
|4| 0.0016446998342871666|
|5| 0.0015742997638881207|
|6| 0.0024096001870930195|
|7| 0.00406099995598197|
|8| 0.006132200360298157|
|9| 0.016594599932432175|
|10| 0.037208099849522114|
|11| 0.07861219998449087|
|12| 0.18795529985800385|
|13| 0.5695588998496532|
|14| 1.8007641998119652|
|15| 5.902582300361246|
|16| 21.537495899945498|
|17| 82.23091450007632|

### b. Diagrama de dispersión
<a href="logo github">
<img src="https://github.com/gon21077/proyecto1ADA/blob/main/Dispersi%C3%B3n.jpg" align="middle"></a>

### c. Ajuste de curva
#### Ajuste polinomial 
El ajuste polinomial presenta un coeficiente de determinación de 92.09%.
<a href="logo github">
<img src="https://github.com/gon21077/proyecto1ADA/blob/main/Ajuste2.jpg" align="middle"></a>

#### Ajuste exponencial 
El ajuste exponencial presenta un coeficiente de determinación de 93.72%.
<a href="logo github">
<img src="https://github.com/gon21077/proyecto1ADA/blob/main/Ajuste.jpg" align="middle"></a>


