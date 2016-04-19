from comentario import Comentario

def lerarquivo( nome_arquivo ):
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

def lerStopWords( nome_arquivo ):
    stopWords = []
    arquivo = open( nome_arquivo, 'r' )  # abre o arquivo para leitura
    print( "Lendo arquivo '%s'..." %nome_arquivo )
    for linha in arquivo: # percorre cada linha do arquivo
        stopWords.append( linha.lower().replace('\n','') ) # limpa texto e adiciona ao final da estrutura
    arquivo.close()  # depois do uso, fecha o arquivo
    return stopWords

def main():
    teste_inicial = lerarquivo( "files/teste_inicial.txt" )
    imdb_test = lerarquivo( "files/imdb_test" )
    imdb_train = lerarquivo( "files/imdb_train" )
    stopword_list = lerStopWords( "files/stopword_list" )
    for palavra in teste_inicial:
        print palavra, ' = ', palavra.hasWord( 'brito' )
main()