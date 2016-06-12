# KNN-IMDB
K-Nearest Neighbors Algorithm for IMDB Comments

Para execução do algoritmo podem ser usados os seguintes parâmetros.

-i ou --train - Endereço do arquivo de treino

-t ou --test - Endereço do arquivo de teste

-s ou --stopwords - Endereço do arquivo com lista de stopwords a serem removidas

-k ou --neighbors - Tamanho da vizinhança a ser considerada

-f ou --folds - TRUE se for executar o teste para dimensionamento de vizinhanças, omitir caso não esteja fazendo a validação cruzada

Exemplo:
python main.py -i files/imdb_train -t files/imdb_test -k 7 -s files/stopword_list

O exemplo acima, aplica o processo de classificação através da base de treino imdb_train, testa com a imdb_test, considrera a vizinhança de dimensão 7 e utiliza a lista de stopWords stopword_list.
