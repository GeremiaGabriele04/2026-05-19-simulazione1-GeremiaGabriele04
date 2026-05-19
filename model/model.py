import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._generi = DAO.getAllGeneri()
        self._graph = nx.DiGraph()


    def getListaGeneri(self):
        return sorted(self._generi, key=lambda x: x.Name)

    def buildGraph(self, idGenere):
        nodi = DAO.getAllArtists(idGenere)
        idMapArtists = {}
        for a in nodi:
            idMapArtists[a.ArtistId] = a

        allEdges = DAO.getAllEdges()

        #da tutti gli archi prendo solo quelli con dentro idArtist che sono nella mia idMap
        archi_validi = []
        clienti = []
        for a in allEdges:
            if a[1] in idMapArtists.keys():
                archi_validi.append(a)











