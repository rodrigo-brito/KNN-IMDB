from comentario import Comentario

# Le arquivo de comentarios e retorna vetor com objetos separados
def readComments( nome_arquivo ):
    comentarios = []
    arquivo = open( nome_arquivo, 'r' )  # abre o arquivo para leitura
    print( "Lendo arquivo '%s'..." %nome_arquivo )
    for linha in arquivo: # percorre cada linha do arquivo
        classificaco = linha[0] # primeira posicao define classificacao
        texto = linha[2:].lower().replace( '\n','' ) # restante da linha define o comentario
        comentario = Comentario( classificaco, texto ) # cria objeto
        comentarios.append( comentario ) # adiciona ao vetor final de comentarios
    arquivo.close()  # depois do uso, fecha o arquivo
    return comentarios

# Le arquivo com lista de stopwords
def readStopWords( nome_arquivo ):
    stopWords = []
    arquivo = open( nome_arquivo, 'r' )  # abre o arquivo para leitura
    print( "Lendo arquivo '%s'..." %nome_arquivo )
    for linha in arquivo: # percorre cada linha do arquivo
        stopWords.append( linha.lower().replace('\n','') ) # limpa texto e adiciona ao final da estrutura
    arquivo.close()  # depois do uso, fecha o arquivo
    return stopWords

# Percorre cada comentario e remove as palavras presentes no stopworlist
def removeStopWords( dataset, stopword_list ):
    print "Removendo StopWords..."
    for data in dataset:
        for word in data.palavras:
            if word in stopword_list:
                data.palavras.remove( word )


# Metodo principal
def main():
    teste_inicial = readComments( "files/teste_inicial.txt" )
    imdb_test = readComments( "files/imdb_test" )
    imdb_train = readComments( "files/imdb_train" )
    stopword_list = readStopWords( "files/stopword_list" )

    removeStopWords( teste_inicial, stopword_list )
    for c in teste_inicial:
        print c.palavras

    print "KNN = ",imdb_test[0].getNeighborsClass(imdb_train[:100], 100),
    print " REAL = ",imdb_test[0].classificacao
main()