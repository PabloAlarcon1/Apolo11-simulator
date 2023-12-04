import sched
import time


def realizar_tarea():
    print("Realizando transmision de archivos")


scheduler = sched.scheduler(time.time, time.sleep)


def ejecutar_tarea(intervalo, action):
    scheduler.enter(intervalo, 1, ejecutar_tarea, (intervalo, action))
    action()


intervalo_segundos = 20
scheduler.enter(0, 1, ejecutar_tarea, (intervalo_segundos, realizar_tarea))

print("Scheduler iniciado. Presiona Ctrl + C para detener.")
try:
    scheduler.run()
except KeyboardInterrupt:
    print("Scheduler interrumpido manualmente.")