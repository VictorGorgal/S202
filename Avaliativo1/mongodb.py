from pymongo import MongoClient


class MongoDB:
    def __init__(self, db_name="bancoiot", collection_name="sensores"):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def criar_sensor(self, nome_sensor):
        self.collection.update_one(
            {"nomeSensor": nome_sensor},
            {"$setOnInsert": {"nomeSensor": nome_sensor, "valorSensor": None, "unidadeMedida": "C°",
                              "sensorAlarmado": False}},
            upsert=True
        )

    def update_sensor(self, nome_sensor, valor_sensor):
        self.collection.update_one(
            {"nomeSensor": nome_sensor},
            {"$set": {"valorSensor": valor_sensor, "unidadeMedida": "C°"}}
        )

    def alarmar_sensor(self, nome_sensor):
        self.collection.update_one(
            {"nomeSensor": nome_sensor},
            {"$set": {"sensorAlarmado": True}}
        )

    def get_sensor(self, nome_sensor):
        return self.collection.find_one({"nomeSensor": nome_sensor})
