class Comentario(object):
    def __init__( self, classificacao, texto ):
        self.classificacao = classificacao
        self.texto = texto
        self.palavras = texto.split(" ")
    def __str__( self ):
        return self.classificacao+' - '+self.texto
    def hasWord( self, palavra ):
        return palavra in self.palavras