import simpy
import procesos  
import cpu      
import analisis  

# Pedir parámetros al usuario
MEMORY_CAPACITY = int(input("Ingrese la capacidad de RAM: "))
INTERVALO_LLEGADA = int(input("Ingrese el intervalo de llegada de los procesos: "))
TOTAL_PROCESOS = int(input("Ingrese la cantidad total de procesos: "))
CPU_VELOCIDAD = int(input("Ingrese la velocidad del CPU (instrucciones por unidad de tiempo): "))

# Iniciar el entorno
env = simpy.Environment()
ram = simpy.Container(env, init=MEMORY_CAPACITY, capacity=MEMORY_CAPACITY)
cola_procesos = []  # Cola compartida con cpu.py
cPu = simpy.Resource(env, capacity=1)  # Un solo CPU, se puede modificar

# Iniciar simulación con procesos generados
env.process(procesos.iniciar_simulacion(env, ram, TOTAL_PROCESOS, INTERVALO_LLEGADA, cola_procesos))
env.run()

# Mostrar los procesos generados en la cola
print("\nProcesos listos para ser ejecutados en el CPU:")
for proceso in cola_procesos:
    print(proceso)

# Una vez que los procesos están generados, los enviamos a la CPU
for proceso in cola_procesos:
    nombre, instrucciones, memoria = proceso
    env.process(cpu.ejecutar_en_cpu(env, nombre, instrucciones, memoria, ram, cPu, CPU_VELOCIDAD))

# Ejecutar la simulación nuevamente para procesar los procesos en CPU
env.run()


