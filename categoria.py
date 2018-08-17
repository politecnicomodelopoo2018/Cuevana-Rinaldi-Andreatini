from BD import DB

class Categoria(object):
    idCategoria = None
    nombreCategoria = None

    def altaCategoria(self):
        DB().run("INSERT INTO Categoria(idCategoria,nombreCategoria)" +
                 "VALUES (" + str(self.idCategoria) + ",'" + self.nombreCategoria + "');")

    def bajaCategoria(self):
        DB().run("DELETE FROM Categoria WHERE idCategoria = " + str(self.idCategoria) + ";")

    def modificacionCategoria(self):
        DB().run("UPDATE Categoria SET nombreCategoria = '" + self.nombreCategoria + "' WHERE idCategoria = "
                 + str(self.idCategoria) + ";")