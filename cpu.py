import random

def ejecutar_en_cpu(env, nombre, instrucciones_totales, memoria_requerida, ram, cpu, velocidad):
    """ Simula la ejecución de un proceso en el CPU """
    while instrucciones_totales > 0:
        with cpu.request() as req:
            yield req  # Espera turno en CPU

            # Ejecuta las instrucciones (o menos si quedan menos)
            tareas_realizadas = min(velocidad, instrucciones_totales)
            print(f"{env.now}: {nombre} ejecuta {tareas_realizadas} instrucciones (restantes: {instrucciones_totales - tareas_realizadas})")

            instrucciones_totales -= tareas_realizadas
            yield env.timeout(1)  # Simula el tiempo de atención del CPU (1 ciclo completo)

            if instrucciones_totales == 0:
                # Caso a) Terminated
                print(f"{env.now}: {nombre} ha finalizado y libera {memoria_requerida} de RAM")
                ram.put(memoria_requerida)
                return

            # Generar número aleatorio para decidir el próximo estado
            siguiente_estado = random.randint(1, 2)

            if siguiente_estado == 1:
                # Caso b) Waiting (espera por I/O)
                print(f"{env.now}: {nombre} entra en estado Waiting")
                yield env.timeout(3)  # Simula tiempo en espera por I/O
                
            if siguiente_estado == 2:
                print(f"{env.now}: {nombre} regresa a Ready")
                yield env.timeout(3)  # Simula tiempo en espera por I/O
            







               