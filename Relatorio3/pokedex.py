from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, database):
        self.db = database

    def query_1(self):
        result = self.db.collection.find({"type": "Fire"})
        writeAJson(result, "Query 1 finalizada")
        return result

    def query_2(self):
        result = self.db.collection.find({"weaknesses": {"$size": 7}})
        writeAJson(result, "Query 2 finalizada")
        return result

    def query_3(self):
        result = self.db.collection.find({"$or": [{"type": "Fire"}, {"weaknesses": "Fire"}]})
        writeAJson(result, "Query 3 finalizada")
        return result

    def query_4(self):
        result = self.db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
        writeAJson(result, "Query 4 finalizada")
        return result

    def query_5(self):
        result = self.db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
        writeAJson(result, "Query 5 finalizada")
        return result
