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

# Inicializar el entorno
random.seed(RANDOM_SEED)
env = simpy.Environment()
ram = simpy.Container(env, init=MEMORY_CAPACITY, capacity=MEMORY_CAPACITY)
cpu = simpy.Resource(env, capacity=1)  # Se puede modificar para 2 CPUs

# Iniciar la simulación
env.process(procesos.iniciar_simulacion(env, ram, cpu, TOTAL_PROCESOS, INTERVALO_LLEGADA))
env.run()

# Llamar al análisis de datos y generar gráficas
analisis.generar_graficas()
