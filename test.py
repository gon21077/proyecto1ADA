from proyecto5 import *
import timeit
import matplotlib.pyplot as plt


tests = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo = iniciarMaquina(readjson('maquinafibo.json'))
respuestas = []
tiempos = []

for i in tests:
    cad = '1'*i
    start = timeit.default_timer()
    temp = evalCadena(estados, alfabetoEntrada, alfabetoCinta, funcionFull, estadoInicial, estadoAceptacion, estadoRechazo, cad, 0)
    stop = timeit.default_timer()
    res = temp.count('1')
    print("Resultado: ", res)
    respuestas.append(res)
    tiempos.append(stop-start)
    print("Tiempo de ejecución: ", stop-start)

#export n, tiempo
f = open("tiempos.txt", "w")
for i in range(len(tests)):
    f.write(str(tests[i]) + ", " + str(tiempos[i]) + "\n")
f.close()


#plot x = n, y = tiempo
plt.plot(tests, tiempos)
plt.xlabel('Longitud de la cadena')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de la máquina de fibonacci')
plt.show()
