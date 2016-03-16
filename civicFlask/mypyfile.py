
class cypherQry(object):
    ''' Directory for the cypher queries.
    '''

    def getAllNodes(lbl):
        qry =  "match (s:"+lbl+") return s"
        return qry

    def getNodeBy(self, lbl, key, vlu):
        pass

    def getAllNodesRelatedTo(self, key, vlu, rel):
        pass



    def addNode(self, lbl, data='{"name":"Jack", "age":45}'):
        qry =  "merge (s:"+lbl+" ) return s"
        return qry


