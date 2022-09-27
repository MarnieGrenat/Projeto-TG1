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
    """Classe abstrata com atributos: Nome Completo, CPF, Data de Nascimento e Estado Civil, e métodos: cadastrarDados e obterDados"""
    def __init__(self,nomeComp,cpf,dataNasc,estadoC):
        self._nomeComp = ""
        self._cpf = ""
        self._dataNasc = ""
        self._estadoC = ""
    
    @abstractmethod
    def cadastrarDados():
        pass
    

    @abstractmethod
    def obterDados():
        pass


class Medico(Pessoa):
    """Subclasse de Pessoa, possui atributo CRM, e métodos: a internar, liberar e diagnosticar"""
    __listaCRM = lista[]
    def __init__(self,nomeComp,cpf,dataNasc,estadoC,crm):
        Pessoa.__init__(self,nomeComp,cpf,dataNasc,estadoC)
        
        self._crm = "" #garantir que um mesmo médico (mesmo CRM) não possa ser cadastrado duas vezes. #criar lista para testar se já existe crm !  e criar exceção

    #desenvolver os métodos (acredito que obterdadops e cadastrar dados sao os getters e setters)


class Enfermeiro(Pessoa):
    """Subclasse de Pessoa,