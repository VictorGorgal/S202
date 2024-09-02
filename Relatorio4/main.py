from database import Database
from helper.writeAJson import writeAJson


if __name__ == '__main__':
    db = Database(database="mercado", collection="compras")
    db.resetDatabase()

    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {
            "_id": "$data_compra",
            "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
        }},
        {"$sort": {"_id": 1}}  # Opcional: ordena por data
    ])

    writeAJson(result, "Total de vendas por dia")

    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {
            "_id": "$produtos.descricao",
            "total_quantidade": {"$sum": "$produtos.quantidade"}
        }},
        {"$sort": {"total_quantidade": -1}},
        {"$limit": 1}
    ])

    writeAJson(result, "Produto mais vendido em todas as compras")

    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {
            "_id": {"cliente": "$cliente_id", "data_compra": "$data_compra"},
            "total_compra": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
        }},
        {"$sort": {"total_compra": -1}},
        {"$group": {
            "_id": "$_id.cliente",
            "maior_gasto": {"$first": "$total_compra"},
            "data_compra": {"$first": "$_id.data_compra"}
        }},
        {"$sort": {"maior_gasto": -1}},
        {"$limit": 1}
    ])

    writeAJson(result, "Cliente que mais gastou em uma única compra")

    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {
            "_id": "$produtos.descricao",
            "total_quantidade": {"$sum": "$produtos.quantidade"}
        }},
        {"$match": {"total_quantidade": {"$gt": 1}}},
        {"$sort": {"total_quantidade": -1}}  # Opcional: ordena por quantidade
    ])

    writeAJson(result, "Produtos que tiveram uma quantidade vendida acima de 1 unidade")
