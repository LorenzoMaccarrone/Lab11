from model.model import Model
from database.DAO import DAO
myModel= Model()
myModel.createGraph(2018, "White")
lista=myModel.getPesoMaggiore()
for a in lista:
    print(a[0].Product_number,a[1].Product_number, a[2]["weight"])