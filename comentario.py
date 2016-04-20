import numpy

class Comentario(object):
    # Metodo construtor
    def __init__( self, classificacao, texto ):
        self.classificacao = classificacao
        self.texto = texto
        self.palavras = texto.split(" ")

    # Metodo de impressao de objeto
    def __str__( self ):
        return self.classificacao+' - '+self.texto

    # Verifica se o comentario possui uma dada plavra
    def hasWord( self, word ):
        return word in self.palavras

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
    def getNeighbors(self, trainList, size ):
        neighbors = trainList[:] #Copia vetor para alteracao
        # Calcula similaridade
        for comentario in neighbors:
            comentario.jaccard = self.jaccardDistance( comentario )
        neighbors.sort(key=lambda comentario: comentario.jaccard, reverse=True)
        return neighbors[:size]

    # Verifica a classificacao da maioria dos vizinhos
    def getNeighborsClass( self, trainList, size ):
        neighbors = self.getNeighbors( trainList, size )
        count = 0
        for neighbor in neighbors:
            if neighbor.classificacao == '1':
                count+=1
        if count >= size/2: #se mais da metade dos vizinhos for 1
            return 1
        else:
            return 0

