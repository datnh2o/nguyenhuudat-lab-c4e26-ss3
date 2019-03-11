from pymongo import MongoClient
#ex4
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
clent = MongoClient(uri)
db = clent.c4e
river_collection = db["river"]
#ex5
river_in_Africa = river_collection.find(
    {
        "continent": "Africa",
    }
)
#ex6
river_in_America = river_collection.find(
    {
        "continent": "S.America",
        "lenght": {"$lt": 1000},
    }
)