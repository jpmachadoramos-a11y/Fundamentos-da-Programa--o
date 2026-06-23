from pessoa import Pessoa
# nome, cpf, data de nascimento, ANO DE INGRESSO, NOTAS, MATRÍCULO, E SE ESTÁ ATIVO OU NÃO
class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matriculo: str):
        super().__init__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = self.matricula
        self.ativo = True
        self.notas = []
