from database.DB_connect import DBConnect
from model.artista import Artista
from model.genere import Genere


class DAO:
    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.GenreId as id, g.Name as nome
                    from genre g """

        cursor.execute(query)

        for row in cursor:
            result.append(Genere(row["id"], row["nome"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllArtists(id):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
                    from artist a 
                    where a.ArtistId in (select distinct ArtistId 
                                            from album a 
                                            where AlbumId in (select distinct AlbumId 
                                                                from track t 
                                                                where GenreId = %s)) """

        cursor.execute(query, (id,))

        for row in cursor:
            result.append(Artista(row["ArtistId"], row["Name"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select i2.CustomerId , a.ArtistId, sum(i2.Total) as totale
                    from invoiceline i , invoice i2 , track t , album a 
                    where i.InvoiceId = i2.InvoiceId and i.TrackId = t.TrackId and t.AlbumId = a.AlbumId 
                    group by i2.CustomerId , a.ArtistId"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["i2.CustomerId"], row["a.ArtistId"], row["totale"]))

        cursor.close()
        conn.close()
        return result


