import sqlite3

conn = sqlite3.connect ('Faculdade.db')

cursor = conn.cursor ()

def criar_tabela ():
    sql = """
    CREATE TABLE albums (titulo text, artista text ,data_lancamento text,gravadora text, midia text)
    """

    
    cursor.execute (sql)

    conn.commit ()



def grava_album():
    sql ="INSERT INTO albums Values ('Os Palestrinos','Palmeiras', '2002', 'DeckDisc' ,'CD')"


    cursor.execute (sql)

    conn.commit ()



def gravar_muitos():
    albums = [('legacy', 'Gusttavo Lima', '25/11/2020', 'Sony Music','Streaming'), ('Better Now', 'Post Malone', '01/02/2016', 'Entertaiment', 'DVD')] 


    cursor.executemany ("INSERT INTO albums VALUES (?,?,?,?,?)",albums)

    conn.commit ()

def atualiza():
    sql="""
    UPDATE albums SET midia = 'Spotify'
    WHERE midia = 'MP3'
    """

    cursor.execute(sql)

    conn.commit ()


def excluir():
    sql= """
    DELETE FROM albums where artista = 'Andy Hunter'
    """

    cursor.execute (sql)

    conn.commit ()