import numpy

class Comentario(object):
    # Metodo construtor
    def __init__( self, classificacao, texto ):
        self.classificacao = classificacao
        self.texto = texto
        self.palavras = texto.split(" ")
        self.neighbors = None

    # Metodo de impressao de objeto
    def __str__( self ):
        return self.classificacao+' - '+self.texto

    # Verifica se o comentario possui uma dada plavra
    def hasWord( self, word ):
        return word in self.palavras

    # Calcula a distancia de Jaccard para um dado comentario
    def jaccardDistance( self, comentario):
        # Array de palavras unicas
        uniqWords  = []
        # Array a uniao de palavras registradas em ambos comentarios
        allWords 	= numpy.concatenate([comentario.palavras, self.palavras])

        # Montando lista de palavras unicas
        for word in allWords:
            if word not in uniqWords:
                uniqWords.append(word)

        # Variaveis para calculo de Jaccard
        f11 = 0.0
        f10 = 0.0
        f01 = 0.0

        for word in uniqWords:
            if self.hasWord( word ) and comentario.hasWord( word ):
                f11+=1.0
            elif self.hasWord( word ):
                f10+=1.0
            elif comentario.hasWord( word ):
                f01+=1.0
        # Calcula a distancia de Jaccard
        return f11/(f10+f01+f11)

    # Retorna lista de vizinhos mais semelhantes
    def getNeighbors( self, trainList ):
        # Nao recalcula vizinhanca caso o comentario ja possua a estrutura
        # Utilizado apenas para no metodo de captura de multiplos tamanhos de vizinhancas (Fitting)
        if self.neighbors is not None:
            return self.neighbors
        else:
            neighbors_new = [] #Copia vetor para alteracao
            # Calcula similaridade
            for comentario in trainList:
                distancia = self.jaccardDistance( comentario )
                neighbors_new.append( Vizinho( comentario.classificacao, distancia ))
            neighbors_new.sort(key=lambda vizinho: vizinho.distancia, reverse=True)
            self.neighbors = neighbors_new
            return neighbors_new

    # Verifica a classificacao da maioria dos vizinhos
    def getNeighborsClassification( self, trainList, size ):
        neighbors = self.getNeighbors( trainList )
        count = 0
        for neighbor in neighbors[:size]:
            if neighbor.classificacao == '1':
                count+=1
        if count > size/2.0: #se mais da metade dos vizinhos for 1
            return '1'
        else:
            return '0'

class Vizinho(object):
    classificacao = None
    distancia = None
    def __init__( self, classificacao, distancia ):
        self.classificacao = classificacao
        self.distancia = distancia
    def __str__( self ):
        return self.classificacao+' - '+repr(self.distancia)