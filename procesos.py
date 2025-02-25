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
import random

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


