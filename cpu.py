"""
===============================================================
Simulación de Ejecución de Tareas en la Unidad de Procesamiento
===============================================================
Descripción:
Este módulo gestiona la ejecución de tareas en la unidad de procesamiento del sistema operativo simulado usando SimPy.
Las tareas consumen instrucciones y pueden alternar entre estados de ejecución y espera.
Una vez finalizadas, liberan la memoria que habían solicitado.

Este código solo maneja la **ejecución de tareas** en la unidad de procesamiento.
La generación de tareas se realiza en otro módulo (`procesos.py`).

===============================================================
"""
import random

def ejecutar_en_unidad(env, identificador, total_instrucciones, memoria_utilizada, memoria_virtual, procesador, rendimiento):
    """ Simula la ejecución de una tarea en la unidad de procesamiento """
    while total_instrucciones > 0:
        with procesador.request() as acceso:
            yield acceso  # Espera su turno en la unidad de procesamiento

            # Ejecuta las instrucciones o la cantidad restante si es menor
            instrucciones_realizadas = min(rendimiento, total_instrucciones)
            print(f"{env.now}: {identificador} ejecuta {instrucciones_realizadas} instrucciones (restantes: {total_instrucciones - instrucciones_realizadas})")

            total_instrucciones -= instrucciones_realizadas
            yield env.timeout(1)  # Simula el tiempo de procesamiento (1 ciclo)

            if total_instrucciones == 0:
                # Caso a) Finalizado
                print(f"{env.now}: {identificador} ha finalizado y libera {memoria_utilizada} de RAM")
                memoria_virtual.put(memoria_utilizada)
                return

            # Genera un número aleatorio para determinar el siguiente estado
            proximo_estado = random.randint(1, 2)

            if proximo_estado == 1:
                # Caso b) Esperando (I/O)
                print(f"{env.now}: {identificador} entra en estado de Espera")
                yield env.timeout(3)  # Simula tiempo en espera de I/O
                
            if proximo_estado == 2:
                print(f"{env.now}: {identificador} regresa a Listo")
                yield env.timeout(3)  # Simula tiempo en espera de I/O
