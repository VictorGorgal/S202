import threading
import random
import time
from mongodb import MongoDB


def sensor_thread(nome_sensor, bd):
    bd.criar_sensor(nome_sensor)

    while True:
        sensor_data = bd.get_sensor(nome_sensor)

        if sensor_data and sensor_data["sensorAlarmado"]:
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!")
            break

        valor_sensor = random.uniform(30, 40)
        print(f"{nome_sensor} gerou a temperatura: {valor_sensor:.2f}°C")

        bd.update_sensor(nome_sensor, valor_sensor)

        if valor_sensor > 38:
            bd.alarmar_sensor(nome_sensor)

        time.sleep(2)


if __name__ == '__main__':
    mongoDB = MongoDB()
    sensors = ["Temp1", "Temp2", "Temp3"]
    threads = []

    for sensor in sensors:
        t = threading.Thread(target=sensor_thread, args=(sensor, mongoDB))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
