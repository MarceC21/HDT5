"""
===============================================================
Simulación de Procesos en un Sistema Operativo (Manejo de Colas)
===============================================================
Autor: [Tu Nombre o Equipo]
Fecha: [Fecha]
Descripción:
Este módulo genera procesos en un sistema operativo simulado usando SimPy.
Los procesos requieren memoria RAM y esperan en una cola hasta que puedan ser atendidos por el CPU.
Cada proceso solicita una cantidad aleatoria de memoria y un número aleatorio de instrucciones a ejecutar.

Este código solo maneja la **creación y gestión de procesos**.
La ejecución en CPU se realiza en otro módulo (`cpu.py`).

===============================================================
"""
import simpy
import random

# Configuración global
RANDOM_SEED = 42
MEMORY_CAPACITY = 100  # Capacidad inicial de RAM
INTERVALO_LLEGADA = 10  # Se modificará en pruebas
TOTAL_PROCESOS = 25  # Se probará con 25, 50, 100, 150, 200 procesos

random.seed(RANDOM_SEED)

def generar_proceso(env, nombre, ram, cola_procesos):
    """ Simula el ciclo de vida de un proceso en un sistema operativo """
    memoria_requerida = random.randint(1, 10)
    instrucciones_totales = random.randint(1, 10)

    print(f"{env.now}: {nombre} llega al sistema (requiere {memoria_requerida} de RAM)")

    # Solicitar RAM (espera hasta obtenerla)
    yield ram.get(memoria_requerida)
    print(f"{env.now}: {nombre} obtiene {memoria_requerida} de RAM y está listo para ejecutarse")

    # Agregar proceso a la cola para el CPU (espera en la cola hasta que CPU lo atienda)
    cola_procesos.append((nombre, instrucciones_totales, memoria_requerida))

def iniciar_simulacion(env, ram, num_procesos, intervalo_llegada, cola_procesos):
    """ Genera procesos siguiendo una distribución exponencial """
    for i in range(num_procesos):
        env.process(generar_proceso(env, f"Proceso-{i+1}", ram, cola_procesos))
        yield env.timeout(random.expovariate(1.0 / intervalo_llegada))

# Si se ejecuta este archivo directamente, se puede probar la generación de procesos
if __name__ == "__main__":
    # Inicializar entorno de SimPy
    env = simpy.Environment()
    ram = simpy.Container(env, init=MEMORY_CAPACITY, capacity=MEMORY_CAPACITY)
    cola_procesos = []  # Cola compartida con cpu.py

    # Iniciar simulación con procesos generados
    env.process(iniciar_simulacion(env, ram, TOTAL_PROCESOS, INTERVALO_LLEGADA, cola_procesos))
    env.run()

    # Mostrar los procesos generados en la cola
    print("\n📌 Procesos listos para ser ejecutados en el CPU:")
    for proceso in cola_procesos:
        print(proceso)
