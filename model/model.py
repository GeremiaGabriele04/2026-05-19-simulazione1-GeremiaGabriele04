from itertools import combinations

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
        self._graph.add_nodes_from(nodi)
        idMapArtists = {}
        for a in nodi:
            idMapArtists[a.ArtistId] = a

        allEdges = DAO.getAllEdges()
        allPop = DAO.getPopolarita() #dict
        artistiGenere = set(idMapArtists.keys())

        #creo il dizionario {clienteId : [artistId1,...]}
        acquisti = {}
        for riga in allEdges:
            if riga[1] not in artistiGenere:
                continue

            if riga[0] not in acquisti.keys():
                acquisti[riga[0]] = [riga[1]]
            else:
                acquisti[riga[0]].append(riga[1])

        #ciclo sui values e creo tutte le coppie per il cliente x
        for listaA in acquisti.values():
            lista_coppie = list(combinations(listaA, 2))
            #sulla coppia, verifico le popolarità e creo larco fissando il verso
            for coppia in lista_coppie:
                a = int(allPop[coppia[0]])
                b = int(allPop[coppia[1]])
                art1 = idMapArtists.get(coppia[0])
                art2 = idMapArtists.get(coppia[1])
                if a != b:
                    if a > b:
                        self._graph.add_edge(art1, art2, weight = a+b)
                    else:
                        self._graph.add_edge(art2, art1, weight=a + b)
                else:
                    self._graph.add_edge(art1, art2, weight=a + b)
                    self._graph.add_edge(art2, art1, weight=a + b)

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)















