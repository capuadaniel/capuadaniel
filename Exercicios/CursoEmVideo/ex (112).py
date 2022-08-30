#dentro do pacote utilidadesCeV do ex 111, crie a função leiadinheiro() que aceite apenas numeros com uma validação e prova de digitação errada
# inclusive o modelo 'dados' deve aceitar digitação de preço com virgula em vez de ponto.
from UtilidadesCeV import moeda
from UtilidadesCeV import dados

p = dados.leiaDinheiro('Digite o preço R$ ')
moeda.resumo(p, 30, 50)