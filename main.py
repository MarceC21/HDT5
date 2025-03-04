"""
===============================================================
Simulación de un Sistema Operativo con Manejo de Tareas y CPU
===============================================================
Descripción:
Este módulo principal coordina la simulación de un sistema operativo usando SimPy.
Administra la memoria RAM, el procesador y la llegada de tareas al sistema.
Las tareas se generan en `procesos.py`, se almacenan en una cola y luego se ejecutan en `cpu.py`.

Este código **coordina la simulación completa** llamando a los módulos de generación y ejecución de tareas.

===============================================================
"""
import simpy
import procesos  
import cpu      
import analisis  

# Pedir parámetros al usuario
MEMORIA_MAXIMA = int(input("Ingrese la capacidad de RAM: "))
INTERVALO_CREACION = int(input("Ingrese el intervalo de llegada de las tareas: "))
TOTAL_TAREAS = int(input("Ingrese la cantidad total de tareas: "))
VELOCIDAD_PROCESADOR = int(input("Ingrese la velocidad del procesador (instrucciones por unidad de tiempo): "))

# Iniciar el entorno de simulación
entorno = simpy.Environment()
memoria_virtual = simpy.Container(entorno, init=MEMORIA_MAXIMA, capacity=MEMORIA_MAXIMA)
cola_tareas = []  # Cola compartida con cpu.py
procesador = simpy.Resource(entorno, capacity=1)  # Un solo núcleo, configurable

# Iniciar simulación con las tareas generadas
entorno.process(procesos.iniciar_simulacion(entorno, memoria_virtual, TOTAL_TAREAS, INTERVALO_CREACION, cola_tareas))
entorno.run()

# Mostrar las tareas generadas en la cola
print("\nTareas en cola, listas para ejecución:")
for tarea in cola_tareas:
    print(tarea)

# Enviar las tareas generadas a la unidad de procesamiento
for tarea in cola_tareas:
    identificador, total_instrucciones, memoria_asignada = tarea
    entorno.process(cpu.ejecutar_en_unidad(entorno, identificador, total_instrucciones, memoria_asignada, memoria_virtual, procesador, VELOCIDAD_PROCESADOR))

# Ejecutar la simulación nuevamente para procesar las tareas
entorno.run()
