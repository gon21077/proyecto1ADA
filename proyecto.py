
import json
import timeit

# Formato de ingresar una maquina de turing:

# * representa espacio
# - representa que no escribe nada
""""

"*" representa espacio
"-" representa que no escribe nada

{
    "estados": "a,b,c,d,e",
    "alfabetoEntrada": "1,2,3,4",
    "alfabetoCinta": "1,3",
    "delta": "(a,0,*,b,R);(a,*,,g,R)" ------ donde "a" es el estado inicial, "0" es caracter de entrada "*" es el caracter que se escribe en la cinta, "b" es el estado al que pasa y R es la dirección a donde se mueve
    "estadoInicial": "a",
    "estadoAceptacion": "e"
    "estadoRechazo": "d"
}


"""

"""Función que define la máquina de Turing"""
def iniciarMaquina(maquinajson):
    maquina = maquinajson

    """ parámetros que definen el funcionamiento de la máquina """
    estados = list(maquina['estados'].split(",")) # crea una lista a partir de la cadena leída
    alfabetoEntrada = list(maquina['alfabetoEntrada'].split(","))
    alfabetoCinta = list(maquina['alfabetoCinta'].split(",")) 

    funcion0 = list(maquina['delta'].split(";")) # función de transición
    funcionFull = {} # diccionario con elementos de la función de transición delta, llave: (estado_inicial,caracter_entrada), argumento:(caracter_por_escribir, siguiente_estado, direccion)
    for i in funcion0:
        print(i)
        i1 = i.replace("(","").strip()
        i2 = i1.replace(")","")
        i3 = i2.split(",") 
        print(i3)

        
        
        llave = tuple(i3[:2])

        valor = tuple(i3[2:])
        funcionFull[llave] = valor



    estadoInicial = maquina['estadoInicial']
    estadoAceptacion = maquina['estadoAceptacion']
    estadoRechazo = maquina['estadoRechazo']

    print("\n------------Maquina Iniciada-------------\n")
    print("Q: %s\nSigma: %s\nGama: %s\nDelta: %s\nq0: %s\nqAccept: %s\nqReject: %s\n\n" %(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo))
    print("\n-----------------------------------------\n\n")
    return estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo


"""Función para evaluar la cadena en la máquina definida"""
#cadena como string e.g. "0000"
def evalCadena(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo, cadena, cinta = 1):

    cadenalista = list(cadena) # Convertir la cadena en una lista para facilitar iteración

    if len(cadenalista) == 0: # manejamos caso de cadena vacia
        cadenalista.append('*')
   
    for i in cadenalista: # verifica que cada elemento pertenezca al alfabeto de entrada de la máquina
        if i not in alfabetoEntrada:
            print("Caracter de entrada no pertenece a Sigma")
            return []
  
 
    estadoActual = estadoInicial # estadoActual es el estado donde está el puntero
    posicionEnCadena = 0 # Variable que guarda la posición del puntero 
    longitudCadena = len(cadenalista)  # variable para manejo de errores indexoutofrange

    # Primera iteración: indicar que el puntero (estadoActual) está en estadoInicial dentro de la cadena
    cadenatemp0 = cadenalista.copy()
    cadenatemp0.insert(posicionEnCadena,estadoActual) # Estado inicial se agrega a la cadena 
    print("Cadena actual: ", cadenatemp0) # Se presenta la primera iteración

    # Ciclo que realiza la función de transición 
    while ((estadoActual != estadoAceptacion) and (estadoActual != estadoRechazo)): # mientras el puntero no esté en los estados de aceptación/rechazo

        caracterEntrada = cadenalista[posicionEnCadena] # Lectura del caracter en la cadena 
      

        tuplaIn = (estadoActual,caracterEntrada) # Estado donde está el puntero, elemento actual leído en cadena 
        tuplaMov = funcionFull.get(tuplaIn) # Argumento de la llave en diccionario

        sobreescribir = tuplaMov[0] # Caracter que debe ser escrito en la cinta/cadena

        if sobreescribir == '-': # No se reescribe un nuevo caracter, continuar con el caracterEntrada 
            sobreescribir = caracterEntrada

        siguienteEstado = tuplaMov[1]  # Estado al que debe moverse el puntero
        direccion = tuplaMov[2] # Hacia donde desplaza el siguiente estado 

        cadenalista[posicionEnCadena] = sobreescribir # reemplaza el caracter en la posición dada en la cadena 
        estadoActual = siguienteEstado # se mueve al siguiente estado según la definición de la máquina
        


        if (estadoActual == estadoAceptacion) or (estadoActual == estadoRechazo): # valida si ha llegado a los estados de aceptación/rechazo para agregar a la cadena de resultado los estados 
            # Se verifica si llego a rechazo o aceptacion
            if (estadoActual == estadoAceptacion):
                
                print('Cadena Aceptada')
                return cadenalista
            elif (estadoActual == estadoRechazo):
                print('Cadena Rechazada')
            
        
            posicionEnCadena +=1 # Siempre que llegue a estado de aceptación o rechazo se mueve a la derecha por simplicidad.
            cadenatemp = cadenalista.copy()
            cadenatemp.insert(posicionEnCadena,estadoActual)
            print("Cadena final: ",cadenatemp)

            break
        
        # Si se mueve hacia la derecha la cadena
        if direccion == "R": 
            if posicionEnCadena == longitudCadena-1:  # valida que se encuentre en la última posición de la cadena resultante para agregar el espacio (*) al final de la cadena
                cadenalista.append("*")
                longitudCadena+=1

            posicionEnCadena +=1 # para mover el puntero una posición a la derecha dentro de la cadena 
            cadenatemp = cadenalista.copy() # copia de la cadena resultante para ser presentada
            cadenatemp.insert(posicionEnCadena,estadoActual) # en la nueva posición de la cadena, inserta el estado leído en la segunda tupla 
            if cinta == 1:
                print("Cadena actual: ",cadenatemp) # se muestra la iteración de la cadena resultante 
            continue
        
        #Si se mueve hacia la izquierda la cadena
        elif direccion == "L": 
            #Verifica que si el puntero esta en la primera posición no se mueva hacia la izquierda de nuevo
            if posicionEnCadena == 0: 
                print("Error en cadena")
                return []
            
            posicionEnCadena -=1 # para mover el puntero una posición a la izquierda dentro de la cadena 
            cadenatemp = cadenalista.copy() # copia de la cadena resultante para ser presentada
            cadenatemp.insert(posicionEnCadena,estadoActual) # en la nueva posición de la cadena, inserta el estado leído en la segunda tupla 
            if cinta == 1:
                print("Cadena actual: ",cadenatemp) # se muestra la iteración de la cadena resultante 
            continue
        else: 
            cadenatemp = cadenalista.copy() # copia de la cadena resultante para ser presentada
            cadenatemp.insert(posicionEnCadena,estadoActual) # en la nueva posición de la cadena, inserta el estado leído en la segunda tupla 
            if cinta == 1:
                print("Cadena actual: ",cadenatemp) # se muestra la iteración de la cadena resultante 
            continue
        

# * representa espacio
# - representa que no escribe nada

def readjson(path):
    with open(path) as json_data:  # lectura del archivo json dentro de la misma carpeta
        maquinajson = json.load(json_data)
        json_data.close()
    return maquinajson







def main(): # Loop principal

    print("Bienvenido al simulador de máquinas de Turing\n")

    on = True
    while (on):
        print("\n\nEscoja una opcion: \n1. Cargar una máquina\n2. Evaluar cadena en máquina actual (escribir cadena)\n3. Encontrar numero de fibonacci (escribir indice a encontrar) \n4. Salir.")
        try: 
            op = int(input("¿Que desea hacer? (escriba solo 1, 2, 3 o 4): "))
        except: 
            print("Escriba solo 1, 2, 3 o 4")
            continue
        
        if op == 1:
            path = input("Escriba el nombre de su archivo (e.g. maquina.json): ")
            try: # Trata de iniciar maquina con path específicado
                estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo = iniciarMaquina(readjson(path))
                continue
            except:
                print("Error en lectura de máquina, prueba de nuevo")
                continue

        elif op == 2:
            cadena = input("Escriba la cadena a evaluar: ")
            print('Desea ver la cinta? 1. Si 2. No')
            try: 
                cinta = int(input("Escriba solo 1 o 2: "))
            except: 
                print("Escriba solo 1 o 2")
                continue
            if cinta == 1:

                try: #Trata de eva
                    start = timeit.default_timer()
                    print(evalCadena(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo, cadena, 1))
                    stop = timeit.default_timer()
                    print('Time: ', stop - start)
                    continue
                except KeyboardInterrupt:
                    print("Ejecución detenida")
                    continue
                except Exception:
                    print("Debe iniciar una máquina primero")
            elif cinta == 2:
                try: #Trata de eva
                    start = timeit.default_timer()
                    print(evalCadena(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo, cadena, 0))
                    stop = timeit.default_timer()
                    print('Time: ', stop - start)
                    continue
                except KeyboardInterrupt:
                    print("Ejecución detenida")
                    continue
                except Exception:
                    print("Debe iniciar una máquina primero")

        elif op == 3:
            cadena = int(input("Escriba el indice del numero de fibonacci a calcular: "))
            cad = '1'*cadena
            print('Desea ver la cinta? 1. Si 2. No')
            try: 
                cinta = int(input("Escriba solo 1 o 2: "))
            except: 
                print("Escriba solo 1 o 2")
                continue
            if cinta == 1:

                try: #Trata de eva
                    start = timeit.default_timer()
                    res = evalCadena(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo, cad, 1)
                    print(res)
                    stop = timeit.default_timer()
                    #sum all 1s
                    print('Numero: ',res.count('1'))
                    print('Time: ', stop - start)
                    continue
                except KeyboardInterrupt:
                    print("Ejecución detenida")
                    continue
                except Exception:
                    print("Debe iniciar una máquina primero")
            elif cinta == 2:
                try: #Trata de eva
                    start = timeit.default_timer()
                    res = evalCadena(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo, cad, 0)
                    print(res)
                    stop = timeit.default_timer()
                    #sum all 1s
                    print('Numero: ',res.count('1'))
                    print('Time: ', stop - start)

                    continue
                except KeyboardInterrupt:
                    print("Ejecución detenida")
                    continue
                except Exception:
                    print("Debe iniciar una máquina primero")


        elif op == 4: 
            on = False
            break
        else: 
            print("Opción no es válida, intente de nuevo")
            continue

       


#main()

