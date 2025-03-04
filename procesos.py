"""
===============================================================
Simulación de Tareas en un Sistema Operativo (Manejo de Colas)
===============================================================
Descripción:
Este módulo genera tareas en un sistema operativo simulado usando SimPy.
Las tareas requieren memoria RAM y esperan en una cola hasta que puedan ser atendidas por la unidad de procesamiento.
Cada tarea solicita una cantidad aleatoria de memoria y un número aleatorio de instrucciones a ejecutar.

Este código solo maneja la **creación y gestión de tareas**.
La ejecución en la unidad de procesamiento se realiza en otro módulo (`cpu.py`).

===============================================================
"""
import random

def generar_tarea(env, identificador, memoria_virtual, cola_tareas):
    """ Simula el ciclo de vida de una tarea en un sistema operativo """
    memoria_solicitada = random.randint(1, 10)
    total_instrucciones = random.randint(1, 10)

    print(f"{env.now}: {identificador} llega al sistema (requiere {memoria_solicitada} de RAM)")

    # Solicitar RAM (espera hasta obtenerla)
    yield memoria_virtual.get(memoria_solicitada)
    print(f"{env.now}: {identificador} obtiene {memoria_solicitada} de RAM y está listo para ejecutarse")

    # Agregar tarea a la cola de ejecución
    cola_tareas.append((identificador, total_instrucciones, memoria_solicitada))

def iniciar_simulacion(env, memoria_virtual, num_tareas, intervalo_llegada, cola_tareas):
    """ Genera tareas siguiendo una distribución exponencial """
    for i in range(num_tareas):
        env.process(generar_tarea(env, f"Tarea-{i+1}", memoria_virtual, cola_tareas))
        yield env.timeout(random.expovariate(1.0 / intervalo_llegada))
