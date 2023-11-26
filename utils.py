from models import Pessoas


#insere dados na tablea pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Assis', idade=23)
    print(pessoa)
    pessoa.save()

# realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Assis').first()
    print(pessoa.idade)


# altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Assis').first()
    pessoa.nome = 'Felipe'
    pessoa.save()


# exclui dados na tablea pessoas
def excllui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jader').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    excllui_pessoa()
    consulta_pessoas()

