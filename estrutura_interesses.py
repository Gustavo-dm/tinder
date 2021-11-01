database = {}  # um dicionário, que tem a chave interesses para o controle
# dos interesses (que pessoa se interessa por que outra), e pessoas para o controle de pessoas (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)
# voce pode controlar as pessoas de outra forma se quiser, nao precisa mudar nada
# do seu código para usar essa váriavel

# esse voce só faz se quiser guardar nessa lista os dicionários das pessoas
database['PESSOA'] = [{"nome": "lucas", "id": 12},
                      {"nome": "beatriz", "id": 13}]

# em todo esse codigo que estou compartilhando, as variaveis interessado, alvo de interesse, pessoa, pessoa1 e pessoa2 sao sempre IDs de pessoas


class NotFoundError(Exception):
    pass


class IncompatibleError(Exception):
    pass
# Assim, poderemos adicionar pessoas: i.adiciona_pessoa({'nome':'fernando','id':1})
# Pegar a lista de todas as pessoas : i.todas_as_pessoas()
# Consultar uma pessoa por id       : i.localiza_pessoa(1) (retorna o dicionario do fernando)

# Tb queremos uma função reseta.    : i.reseta() faz a lista de pessoas ficar vazia


def todas_as_pessoas():
    return database['PESSOA']


def localiza_pessoa(id_pessoa):
    for dic_pessoa in database['PESSOA']:
        if id_pessoa == dic_pessoa['id']:
            return dic_pessoa
    raise NotFoundError


def reseta():
    database['PESSOA'] = []
    database['interesses'] = {}


# Quais as funções que tem que ser feitas pra essa parte?
# adiciona_interesse(id1,id2) : marca que 1 quer falar com 2
# consulta_interesses(id1)    : devolve a lista de todos os interesses de 1
# remove_interesse(id1,id2)   : marca que 1 não quer mais falar com 2
# Detalhes:
# * Essas funções devem verificar se o usuário não é válido. Se for o caso,
# devem lançar a excessão NotFoundError
# * O reseta também deve funcionar para apagar os interesses


database['interesses'] = {
    100: [101, 102, 103, 40],
    200: [100],
    30: []
}


def adiciona_pessoa(dic_pessoa):
    database['PESSOA'].append(dic_pessoa)
    id_pessoa = dic_pessoa['id']
    database['interesses'][id_pessoa] = []


def isCompatible(id_interesse, id_interessado):
    interesse = localiza_pessoa(id_interesse)
    interessado = localiza_pessoa(id_interessado)
    if 'sexo' in interesse and 'buscando' in interessado:
        if interesse['sexo'] in interessado['buscando']:
            return IncompatibleError()
        else:
            return True


def adiciona_interesse(id_interessado, id_alvo_de_interesse):  # (100,40)
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    lista_interessado = database.get('interesses', [])[id_interessado]
    lista_interessado.append(id_alvo_de_interesse)


def consulta_interesses(id_interessado):
    localiza_pessoa(id_interessado)
    return database['interesses'][id_interessado]

# essa funcao só vai ser testada
# quando estivermos fazendo matches


def remove_interesse(id_interessado, id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    interesses = database['interesses'][id_interessado]
    if id_alvo_de_interesse in interesses:
        interesses.remove(id_alvo_de_interesse)


def lista_matches(id_pessoa):
    matches = []
    interessado = localiza_pessoa(id_pessoa)
    interesses = consulta_interesses(id_pessoa)
    # Verifica se os interesses são correspondidos

    for interesse in interesses:
        match = consulta_interesses(interesse)
        foo = localiza_pessoa(interesse)
        # Verifica se é match
       #
        if id_pessoa in match:

            matches.append(interesse)
    return matches
