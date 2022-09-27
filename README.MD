# Projeto TG1, Programação Orientada a Dados
**Versão:** 2022.09.27

**Professor:**
- Dr. Dalvan Griebler

**Autores:**
- Gabriela Dellamora Paim
- João Enrique Rego Cairuga


## Apresentação do Projeto:
#### Linguagem utilizada:
- Python
#### Ferramentas:
- Jupyter Notebook, JupyterLab
- VSCODE
### Contextualização:
  O Hospital São Lucas da PUCRS (HSL) decidiu implementar um novo sistema de teste para controlar pacientes em
pós operatório. Eles precisam de uma solução que forneça um **mapeamento dos funcionários disponíveis para
atendimento (médicos (as) e enfermeiros (as)), fazer o controle da entrada e saída de pacientes e gerenciar
receituários médicos.** Aproveitando que este semestre está ocorrendo a disciplina de Programação Orientada a
Dados, convidaram o professor para criar uma lista de requisitos para um protótipo do novo sistema de
gerenciamento da divisão de pós operatório do HSL, com o objetivo de avaliar o seu conhecimento e o quão apto
você está para atuar no desenvolvimento deste projeto.
### Restrições:
- permitido utilizar **todos** métodos da classe str e estrutura de dados compostas;
- Apenas os módulos **abc** e **sys** podem ser importados;
- Outros métodos como len() que são nativos e não dependem de importação de módulos estão autorizados ([lista de métodos](https://docs.python.org/3/library/functions.html#open));
- **Métodos não apresentados em aula devem ser justificados e explicados através de comentários no código**.
### Requisitos do Código:
O sistema de divisão de pós operatório deve ser devolvido para que possa ser usado como um pacote do Python. Além disso, deve ser
desenvolvido uma aplicação (main) em Python que utilize esse pacote.
1. ## Especificações e requisitos do sistema de clínica pós-operatório:
    Pacote deve se chamar **Clinica**, composto de um módulo chamado **clinicaSys**.

 2. ## O módulo **clinicaSys** precisa implementar pelo menos **cinco classes principais**:
    * Secretária
    * Medico
    * Enfermeiro
    * Paciente
    * Pessoa
    
 3. ##  **Classe Pessoa:**
    * Classe *abstrata*
    * Métodos:
        * cadastrarDados
        * obterDados
        * **Métodos esses que  manipulam arquivo** [funcionarios.dat](ADDLINK)
    * **Atributos**:
        * Nome Completo
        * CPF
        * Data de Nascimento
        * Estado Civil
        
 4. ## **Classe Médico:**
    * Subclasse de [Pessoa](ADDLINK)
        * implementa cadastrarDados
        * implementa obterDados
    * Atributos:
        * CRM
        * Deve-se garantir que não haja CRM duplicado.
    * Métodos:
        * Internar
        * Liberar
        * diagnosticar
        * **Métodos esses que manipulam arquivo** [pacientes.dat](ADDLINK)
    
 5. ##  **Classe Enfermeira**
    * Subclasse de [Pessoa](ADDLINK)
       * implementa cadastrarDados
       * implementa obterDados
    * Atributos:
       * COREN
       * Deve-se garantir que não haja COREN duplicado.
    * Métodos:
       * cadastrarPacientes
       * [gerarRelatório](ADDLINK)
          * recebe como argumento uma instância da classe médico e outra instância da classe paciente.
          Deve criar um novo arquivo com nome **rel_<cpf_paciente>.txt** e escrever dentro um simples relatório.
          
           (ADD TEMPLATE)
6. ## **Classe Secretaria**
    * Subclasse de [Pessoa](ADDLINK)
       * implementa cadastrarDados
       * implementa obterDados
    * Métodos:
      * cadastrarFuncionario
          * recebe como argumento uma instância da classe Secretária, Médico ou Enfermeira.
7. ## **Classe Paciente**          
    * Subclasse de [Pessoa](ADDLINK)
    * Atributos:
      * Convenio (instância da classe Convenio)
8. ## **Classe Convenio**
    * Atributos:
      * tipo (Qual o convênio do paciente)
      * Crédito
      * **Para convênio SUS, deve-ser creditado zero crédito e consultas devem ser gratuitas.**
    * ### Informações sobre funcionalidade de Créditos:
      * **PACIENTE INTERNADO** -= 500 créditos
      * **PACIENTE DIAGNOSTICADO** -= 150 créditos
      * **PACIENTE COM CRÉDITO NEGATIVO** = **Não será atendido**
9. ## Protocolo de Gerenciamento de contexto
    * Pelo menos uma das classes criadas deve suportar o protocolo de gerenciamento de contexto para ser utilizada na aplicação. 
    * DICA: Implementar na classe Secretária
10. ## Tratamento de Erros
    * É necessário também tratar erros com tipos de dados inválidos e incoerentes
    * **CPF, COREM, CRM, ESTADO CIVIL E DATA DE NASCIMENTO**
11. ## Especificações e requisitos:
    * A aplicação deve receber como argumento uma lista de arquivos texto (.txt), onde cada arquivo representa um dia de funcionamento da clínica, contendo uma sequência de ações e operações que devem ser feitas pela aplicação.
    * A aplicação não pode parar caso receber operações inválidas ou não permitidas. Os erros devem ser armazenaods em um arquivo de log.
 ## Entrega:
 * Entregar por meio de um *pull request* no GitHub:
    * **Clinica**: Diretório do pacote desenvolvido (clinicaSys).
    * **database**: Diretório contendo os arquivos de registro do sistema.
    * **operações**: Diretório contendo os arquivos de operações.
    * **logs**: Diretório contendo os arquivos de log
    * **saida-esperada (Fornecido pelo professor)**:
        * **database**:
            * Exemplo dos bancos de dados funcionarios e pacientes.
        * **relatórios**:
            * Exemplo de relatórios gerados para cada paciente.
   * **app.py**: aplicação onde serão realizadas as operações (MAIN)
   * **README.md**: arquivo descrevendo como utilizar a aplicação e o pacote.
   * **RESUMO.md**: arquivo contendo o resumo de no máximo 400 palavras descrevendo dificuldades, observações, desafios e comentários sobre o desenvolvimento deste trabalho.


# Desenvolvimento do Projeto:

    
    
    
