import simpy
import random

def ejecutar_en_cpu(env, nombre, instrucciones_totales, memoria_requerida, ram, cpu, velocidad, prob_waiting):
    """ Simula la ejecución de un proceso en el CPU """
    while instrucciones_totales > 0:
        with cpu.request() as req:
            yield req  # Espera turno en CPU
            #Determina cuántas instrucciones se ejecutarán en esta unidad de tiempo
            ejecutadas = min(velocidad, instrucciones_totales) #La velocidad es el máximo de instrucciones que el CPU puede ejecutar por unidad de tiempo
            print(f"{env.now}: {nombre} ejecuta {ejecutadas} instrucciones (restantes: {instrucciones_totales - ejecutadas})")
            #Para ver las intrucciones que faltan de ser ejecutadas
            instrucciones_totales -= ejecutadas
            yield env.timeout(1)  # Simula tiempo de ejecución

            # Posible entrada a estado Waiting (operaciones I/O)
            #Solo aplica si quedan instrucciones pendientes 
            if instrucciones_totales > 0 and random.random() < prob_waiting:
                print(f"{env.now}: {nombre} entra en estado Waiting")
                yield env.timeout(3)  # Simula tiempo en espera por I/O

    # Proceso finaliza y libera memoria
    print(f"{env.now}: {nombre} ha finalizado y libera {memoria_requerida} de RAM")
    ram.put(memoria_requerida)