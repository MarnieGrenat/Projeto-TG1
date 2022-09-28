#Desenvolvimento do projeto TG1 em aula 2022-09-26

"""O Hospital São Lucas da PUCRS (HSL) decidiu implementar um novo sistema de teste para controlar pacientes em
pós operatório. Eles precisam de uma solução que forneça um mapeamento dos funcionários disponíveis para
atendimento (médicos (as) e enfermeiros (as)), fazer o controle da entrada e saída de pacientes e gerenciar
receituários médicos. Aproveitando que este semestre está ocorrendo a disciplina de Programação Orientada a
Dados, convidaram o professor para criar uma lista de requisitos para um protótipo do novo sistema de
gerenciamento da divisão de pós operatório do HSL, com o objetivo de avaliar o seu conhecimento e o quão apto
você está para atuar no desenvolvimento deste projeto."""

##Deve-se criar arquivos para armazenamento de dados




#CLASSES
from abc import ABC, abstractmethod

class Pessoa(ABC):
    """Classe abstrata | atributos: Nome Completo, CPF, Data de Nascimento e Estado Civil |  métodos: cadastrarDados e obterDados"""
    def __init__(self, nomeComp, cpf, dataNasc, estadoC):
        self._nomeComp = nomeComp
        self._cpf = cpf
        self._dataNasc = dataNasc
        self._estadoC = estadoC
    
    @abstractmethod
    def obterDados():
        pass

    
    @abstractmethod
    def cadastrarDados():
        #Utilizando arquivo teste para checar funcionalidade do algoritmo
        arquivo = open("arquivo_teste.dat", "a")
        arquivo.writelines("TESTE \n")
        arquivo.close()
    


class Medico(Pessoa):
    """Subclasse de Pessoa | possui atributo CRM. |  métodos: a internar, liberar e diagnosticar"""
    __listaCRM = listaM[]
    def __init__(self, nomeComp, cpf, dataNasc, estadoC, crm):
        Pessoa.__init__(self,nomeComp,cpf,dataNasc,estadoC)
        
        self._crm = "" #garantir que um mesmo médico (mesmo CRM) não possa ser cadastrado duas vezes. #criar lista para testar se já existe crm !  e criar exceção
    #desenvolver os métodos (acredito que obter dados e cadastrar dados sao os getters e setters)


class Enfermeiro(Pessoa):
    """Subclasse de Pessoa | possui atibuto COREN | métodos: cadastrarPaciente e gerarRelatorio"""
    __listaCOREN = listaE[]
    def __init__(self, nomeComp, cpf, dataNasc, estadoC, coren):
        Pessoa.__init__(self, nomeComp, cpf, dataNasc, estadoC)

        self._coren = "" 
    
    def cadastrarPaciente():
        pass

    def gerarRelatorio():
        pass


class Secretaria(Pessoa):
    """Subclasse de Pessoa() | métodos: cadastrarFuncionario"""
    def __init__(self, nomeComp, cpf, dataNasc, estadoC):
        super().__init__(self, nomeComp, cpf, dataNasc, estadoC)

    def cadastrarFuncionario():
        pass


class Convenio(ABC):
    """atributos: tipo, crédito"""
    def __init__(self, tipo, credito):
        self.tipo = ""
        self.credito = ""


class Paciente(Pessoa, Convenio):
    """Subclasse de Pessoa() | atributos: convenio"""
    def __init__(self, nomeComp, cpf, dataNasc, estadoC):
        super().__init__(nomeComp, cpf, dataNasc, estadoC)