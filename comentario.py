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
        # Array a uniao de palavras distintas registradas em ambos comentarios
        uniqWords = list(set(comentario.palavras) | set(self.palavras))

        # Variaveis para calculo de Jaccard
        f11 = 0.0
        f10ef01 = 0.0

        #Percorre as palavras e verifica a frequencia
        for word in uniqWords:
            if self.hasWord( word ) and comentario.hasWord( word ):
                f11+=1.0
            else:
                f10ef01+=1.0
        # Calcula a distancia de Jaccard
        return f11/(f11+f10ef01)

    # Metodo otimizado para calculo da distancia de Jaccard
    def jaccardDistance2( self, comentario ):
        str1 = set(comentario.palavras)
        str2 = set(self.palavras)
        return float(len(str1 & str2)) / len(str1 | str2)

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
                distancia = self.jaccardDistance2( comentario )
                neighbors_new.append( Vizinho( comentario.classificacao, distancia ))
            neighbors_new.sort(key=lambda vizinho: vizinho.distancia, reverse=True)
            self.neighbors = neighbors_new
            return neighbors_new

    # Verifica a classificacao da maioria dos vizinhos
    def getNeighborsClassification( self, trainList, size ):
        neighbors = self.getNeighbors( trainList )

        qtdeTipo1 = 0.0
        qtdeTipo0 = 0.0

        for i,neighbor in enumerate(neighbors[:size]):
            if neighbor.classificacao == '1':
                qtdeTipo1 += size-i
            else:
                qtdeTipo0 += size-i
        if qtdeTipo1 > qtdeTipo0: #se mais da metade dos vizinhos for 1 logo o comentario eh 1
            return '1'
        else:
            return '0'

class Vizinho(object):
    def __init__( self, classificacao, distancia ):
        self.classificacao = classificacao
        self.distancia = distancia
    def __str__( self ):
        return self.classificacao+' - '+repr(self.distancia)