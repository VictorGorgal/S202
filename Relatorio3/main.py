from database import Database
from pokedex import Pokedex


if __name__ == '__main__':
    db = Database(database="pokedex", collection="pokemons")
    db.resetDatabase()

    pokedex = Pokedex(db)

    pokedex.query_1()
    pokedex.query_2()
    pokedex.query_3()
    pokedex.query_4()
    pokedex.query_5()
