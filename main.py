import sys, argparse
from comentario import Comentario

# Le arquivo de comentarios e retorna vetor com objetos separados
def readComments( nome_arquivo ):
    comentarios = []
    arquivo = open( nome_arquivo, 'r' )  # abre o arquivo para leitura
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
    for linha in arquivo: # percorre cada linha do arquivo
        stopWords.append( linha.lower().replace('\n','') ) # limpa texto e adiciona ao final da estrutura
    arquivo.close()  # depois do uso, fecha o arquivo
    return stopWords

# Percorre cada comentario e remove as palavras presentes no stopworlist
def removeStopWords( dataset, stopword_list ):
    for data in dataset:
        for word in data.palavras:
            if word in stopword_list:
                data.palavras.remove( word )

# Metodo utilizado para definiar o tamanho adequando para as vizinhancas
def qualityNeighborsSize( imdb_test, imdb_train ):
    for v in range(1, 25):
        calculaQualidade( imdb_test, imdb_train, v )

# Metodo para verificacao de multiplas vizinhancas (1 a 200) (Calculo de Fitting)
def getAllNeighbors( imdb_test, imdb_train ):
    for v in range(1,200):
        print "V = ",v,"\n-----------"
        for comentario in imdb_test:
            print comentario.classificacao,"\t",comentario.getNeighborsClassification(imdb_train, v)

# Analisa a quantidade de elementos de cada tipo em um dataset passado
def analiseDataset( dataset ):
    total = len(dataset)
    f0 = 0.0
    f1 = 0.0
    for comentario in dataset:
        if comentario.classificacao == '1':
            f1 += 1
        else:
            f0 += 1
    print "F0 = ",f0
    print "F1 = ",f1

# Calulcula a qualidade da solucao retornada
def calculaQualidade( imdb_test, imdb_train, vinzinhanca ):
    f11 = 0.0
    f10 = 0.0
    f01 = 0.0
    f00 = 0.0
    for comentario in imdb_test:
        classificado = comentario.getNeighborsClassification( imdb_train, vinzinhanca )
        real = comentario.classificacao
        if real == '1' and classificado == '1' :
            f11 += 1.0
        elif real == '1' and classificado == '0' :
            f10 += 1.0
        elif real == '0' and classificado == '1' :
            f01 += 1.0
        elif real == '0' and classificado == '0' :
            f00 += 1.0
    acuracia = (f11+f00)/(f11+f10+f01+f00)
    recall = (f11)/(f11+f10)
    especificidade = (f00)/(f00+f01)
    if f11+f01 > 0:
        precisao = (f11)/(f11+f01)
    else:
        precisao = 0
    if recall+precisao > 0:
        f1 = 2*recall*precisao/(recall+precisao)
    else:
        f1 = 0
    # Vizinhanca    F11     F10     F01     F00     Acuracia    Recall  Especificidade  Precisao    F1
    print vinzinhanca,"\t",f11,"\t",f10,"\t",f01,"\t",f00,"\t",acuracia,"\t",recall,"\t",especificidade,"\t",precisao,"\t",f1

# Metodo principal
def main():
    # Definicao de parametros de entrada via terminal
    parser = argparse.ArgumentParser(description='KNN for IMDB Dataset')
    parser.add_argument('-i','--train', help='Arquivo de treino, informe a url do arquivo para leitura dos dados',required=True)
    parser.add_argument('-t','--test', help='Arquivo de teste, informe a url do arquivo para leitura dos dados', required=True)
    parser.add_argument('-k','--neighbors', help='Numero de vizinhos a ser considerado no processo de treinamento', required=True)
    parser.add_argument('-s','--stopwords', help='Arquivo de stopwords, informe a url do arquivo de stopwords a serem desconsideradas', required=False)
    parser.add_argument('-p','--path', help='Identifica teste de fracionamento para multiplas vizinhancas', required=False)
    args = parser.parse_args()

    # Efetura leitura de arquivos
    imdb_test = readComments( args.test )
    imdb_train = readComments( args.train )
    num_vizinhos = int( args.neighbors )
    print "Test"
    analiseDataset(imdb_test)
    print "Train"
    analiseDataset(imdb_train)

    # Remove StopWords caso passado por parametro
    if args.stopwords is not None:
        stopword_list = readStopWords( args.stopwords )
        removeStopWords( imdb_train, stopword_list )
        removeStopWords( imdb_test, stopword_list )

    # Caso seja uma execucao de treino, testa para todas as vizinhancas
    if args.path is not None:
        qualityNeighborsSize( imdb_test, imdb_train )
    else:
        # Imprime resultado final para cada comentario da base de teste
        #for comentario in imdb_test:
            #print comentario.getNeighborsClassification(imdb_train, num_vizinhos)
        calculaQualidade( imdb_test, imdb_train, num_vizinhos )
main()