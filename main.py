import simpy
import random
import procesos  # Código del Estudiante 1
import cpu       # Código del Estudiante 2
import analisis  # Código del Estudiante 3

# Configuración inicial
RANDOM_SEED = 42
MEMORY_CAPACITY = 100  # Puede cambiarse en las pruebas
INTERVALO_LLEGADA = 10  # Se cambiará en diferentes escenarios
TOTAL_PROCESOS = 25  # Se probará con 25, 50, 100, 150, 200 procesos
RANDOM_SEED = 42
CPU_VELOCIDAD = 3  # Instrucciones por unidad de tiempo (puede ser 3 o 6)
PROB_WAITING = 1 / 2  # Probabilidad de entrar en estado de Waiting

#Iniciar el entorno
env = simpy.Environment()
ram = simpy.Container(env, init=MEMORY_CAPACITY, capacity=MEMORY_CAPACITY)
cola_procesos = []  # Cola compartida con cpu.py
cPu = simpy.Resource(env, capacity=1)  # Un solo CPU, se puede modificar



# Iniciar simulación con procesos generados
env.process(procesos.iniciar_simulacion(env, ram, TOTAL_PROCESOS, INTERVALO_LLEGADA, cola_procesos))
env.run()

# Mostrar los procesos generados en la cola
print("\n📌 Procesos listos para ser ejecutados en el CPU:")
for proceso in cola_procesos:
    print(proceso)

# Una vez que los procesos están generados, los enviamos a la CPU
for proceso in cola_procesos:
    nombre, instrucciones, memoria = proceso
    env.process(cpu.ejecutar_en_cpu(env, nombre, instrucciones, memoria, ram, cPu, CPU_VELOCIDAD, PROB_WAITING))

# Ejecutar la simulación nuevamente para procesar los procesos en CPU
env.run()




# Llamar al análisis de datos y generar gráficas
#analisis.generar_graficas()
