from database.DB_connect import DBConnect
from model.product import Product

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getColors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.Product_color 
                    from go_products gp"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProducts():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct * 
                    from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(colore, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct * 
                    from go_products gp
                    where gp.Product_color = %s """

        cursor.execute(query, (colore,))

        for row in cursor:
            #in questo modo posso avere una lista di oggetti come result
            result.append(idMap[row["Product_number"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(v0, v1, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    select table1.Product_number, table2.Product_number,table1.`Date`, table2.`Date`,count(table1.`Date`) as peso
                    from(
                    select distinct gp.Product_number, gds.`Date`,gds.Retailer_code 
                    from go_products gp, go_daily_sales gds 
                    where gp.Product_number=%s
                    and gp.Product_number =gds.Product_number 
                    )as table1,
                    (select distinct gp.Product_number, gds.`Date`,gds.Retailer_code 
                    from go_products gp, go_daily_sales gds 
                    where gp.Product_number=%s
                    and gp.Product_number =gds.Product_number 
                    )as table2
                    where YEAR(table1.`Date`)=%s 
                    and YEAR(table1.`Date`)=YEAR(table2.`Date`)
                    and table1.`Date`=table2.`Date`
                    and table1.Retailer_code= table2.Retailer_code
                    and table1.Product_number<table2.Product_number
                    group by table1.Product_number, table2.Product_number """

        cursor.execute(query, (v0,v1,year))

        for row in cursor:
            # in questo modo posso avere una lista di oggetti come result
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result
