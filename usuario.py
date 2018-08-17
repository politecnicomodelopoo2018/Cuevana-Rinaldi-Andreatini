from BD import DB

class Usuario(object):
    idUsuario = None
    nombreUsuario = None
    apellidoUsuario = None
    contrasenia = None
    nickName = None
    mail = None

    def altaUsuario(self):
        DB().run("INSERT INTO Usuario(idUsuario,nombreUsuario,apellidoUsuario,nickName,contraseña,mail)" +
                 "VALUES ("+str(self.idUsuario)+",'"+self.nombreUsuario+"','"+self.apellidoUsuario+"','" +
                 self.contrasenia+"','"+self.nickName+"','"+self.mail+"');")

    def bajaUsuario(self):
        DB().run("DELETE FROM Usuario WHERE idUsuario = " + str(self.idUsuario) +";")

    def modificacionUsuario(self):
        DB().run("UPDATE Usuario SET nombreUsuario = '"+self.nombreUsuario +
                 "', apellidoUsuario = '"+self.apellidoUsuario +
                 "', contraseña = '"+self.contrasenia + "',nickName = '"+self.nickName +
                 "', mail = '"+self.mail + "';")
