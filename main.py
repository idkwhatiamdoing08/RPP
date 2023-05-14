import cherrypy as cherrypy
from peewee import *

db = SqliteDatabase("products.db")


class Products(Model):
    class Meta:
        database = db


class Stock(Products):
    class Meta:
        db_table = "products"

    num = PrimaryKeyField(unique=True)
    vendor_code = TextField()
    name = TextField()
    quantity = IntegerField()
    price = IntegerField()

    def get_columns(self):
        cursor = db.cursor()
        cursor.execute('PRAGMA table_info("products")')

        return [i[1] for i in cursor.fetchall()]

    def get_rows(self):
        cursor = db.cursor()
        cursor.execute("SELECT * from products")
        res = cursor.fetchall()

        return res

    def _update(self, nnum, nvendor_code, nname, nquantity, nprice):
        stock = Stock.get(num=nnum)
        stock.vendor_code = nvendor_code
        stock.name = nname
        stock.quantity = nquantity
        stock.price = nprice
        stock.save()

    def _add(self, nvendor_code, nname, nquantity, nprice):
        Stock(vendor_code=nvendor_code,name = nname, quantity = nquantity, price = nprice).save()


class Page(object):
    columns = ""
    rows = ""

    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows

    @cherrypy.expose
    def index(self):
        return f'''
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Lab6</title>
                        <link href="styles.css" rel="stylesheet"/>
                    </head>
                        <body>
                            <h1>Товары на складе</h1>
                            <table>
                                <tr>
                                    {self.columns}
                                </tr>   
                                    {self.rows}
                            </table>
                        </body>
                </html>
                '''


if __name__ == '__main__':
    db.create_tables([Stock])
    item = Stock()
    #app._add("1С", "Сидор", "45", " 30")
    item._update("4", "1Я", "Яблоки", "30", "400")

    columns = item.get_columns()
    rows = item.get_rows()

    columns_html = "".join([f"<th>{i}</th>" for i in columns])
    rows_html = ""

    for row in rows:
        rows_html += "<tr>"
        for item in row:
            rows_html += "<td>"
            rows_html += str(item)
            rows_html += "</td>"
        rows_html += "</tr>"

    cherrypy.quickstart(Page(columns_html, rows_html), "/")

    db.close()