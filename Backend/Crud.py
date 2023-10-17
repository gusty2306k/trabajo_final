import sqlite3

def Atraer_Seleccion_Argentina(Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico):
    SQL = "SELECT * FROM Seleccion_Argentina"
    CONN = sqlite3.connect('Tabla')
    CURSOR = CONN.execute(SQL, (Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico))
    CONN.close()

def Eliminar_Seleccion_Argentina(id):
    SQL = "DELETE FROM Seleccion_Argentina WHERE id= ?"
    CONN = sqlite3.connect('Tabla')
    CURSOR = CONN.execute(SQL, (id,))
    CONN.commit()
    CONN.close()

def Insertar_Seleccion_Argentina(Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico):
    SQL = "INSERT INTO Seleccion_Argentina(Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico,id) VALUES(?,?,?,?,?)"
    CONN = sqlite3.connect('Tabla')
    CURSOR = CONN.execute(SQL, (Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico))
    CONN.commit()
    CONN.close()

def Actualizar_Seleccion_argentina(Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico,id):
    SQL = "UPDATE FROM Seleccion_Argentina SET Arqueros = ?, Defensores = ?,Mediocampistas = ?,Delanteros = ?,Tecnico = ? WHERE id = ?"
    CONN = sqlite3.connect('Tabla')
    CURSOR = CONN.execute(SQL, (Arqueros,Defensores,Mediocampistas,Delanteros,Tecnico))
    CONN.commit()
    CONN.close()
    
    print(Atraer_Seleccion_Argentina)
