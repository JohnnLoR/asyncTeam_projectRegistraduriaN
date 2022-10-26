import pymongo
import certifi
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_origin, get_args
import json

T = TypeVar('T')

class InterfaceRepositorio(Generic[T]):
    def __init__(self):
        ca = certifi.where()
        dataConfig = self.loadFileConfig()
        client = pymongo.MongoClient(dataConfig["data-db-connection"], tlsCAFile=ca)
        self.baseDatos = client[dataConfig["name-db"]]
        theClass = get_args(self.__orig_bases__[0])
        self.coleccion = theClass[0].__name__.lower()

    def loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data

    # DEV_WLombana
    def save(self, item: T):
        pass

    def delete(self, id):
        pass

    def update(self, id, item: T):
        pass

    # DEV_OrlandoMarmol
    def findById(self, id):
        pass

    def findAll(self):
        pass

    def query(self, theQuery):
        pass

    # DEV_WilliamForero200
    def queryAggregation(self, theQuery):
        pass

    def getValuesDBRef(self, x):
        pass

    def getValuesDBRefFromList(self, theList):
        pass

    # DEV_JohnnLoR
    def transformObjectIds(self, x):
        pass

    def formatList(self, x):
        pass

    def transformRefs(self, item):
        pass

    def ObjectToDBRef(self, item: T):
        pass