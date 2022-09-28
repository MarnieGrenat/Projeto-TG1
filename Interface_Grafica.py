import tkinter as tk 
import sqlite3 as sq
#import Classes as cl
# tkinter será utilizado para formar a interface gráfica do projeto.



#connect = sq.connect('teste.db')

#cursor = connect.cursor()

#cursor.execute('''CREATE TABLE teste (
#    nome_completo text,
#    CPF text,
#    data_nascimento text,
#    estado_civil text,
#    CRM text,
#    COREN text
#    )
#''')
#
#connect.commit()
#connect.close()

def cadastrarPaciente():
    #cl.cadastrarDados()
    pass

def exportarDados():
    #cl.obterDados()
    pass

window = tk.Tk()
window.title('Ferramenta de Cadastro')

#Labels
label_nomeComp = tk.Label(window, text = 'Nome Completo:')
label_nomeComp.grid(row=0, column=0, padx=10, pady=10)

label_CPF = tk.Label(window, text = 'CPF:')
label_CPF.grid(row=1, column=0, padx=10, pady=10)

label_dataNasc = tk.Label(window, text = 'Data de Nascimento:')
label_dataNasc.grid(row=2, column=0, padx=10, pady=10)

label_estadoC = tk.Label(window, text = 'Estado Civil:')
label_estadoC.grid(row=3, column=0, padx=10, pady=10)

label_CRM = tk.Label(window, text = 'CRM:')
label_CRM.grid(row=4, column=0, padx=10, pady=10)

label_COREN = tk.Label(window, text = 'COREN:')
label_COREN.grid(row=5, column=0, padx=10, pady=10)

#Entrys
entry_nomeComp = tk.Entry(window, text = 'Nome Completo:')
entry_nomeComp.grid(row=0, column=1, padx=10, pady=10)

entry_CPF = tk.Entry(window, text = 'CPF:')
entry_CPF.grid(row=1, column=1, padx=10, pady=10)

entry_dataNasc = tk.Entry(window, text = 'Data de Nascimento:')
entry_dataNasc.grid(row=2, column=1, padx=10, pady=10)

entry_estadoC = tk.Entry(window, text = 'Estado Civil:')
entry_estadoC.grid(row=3, column=1, padx=10, pady=10)

entry_CRM = tk.Entry(window, text = 'CRM:')
entry_CRM.grid(row=4, column=1, padx=10, pady=10)

entry_COREN = tk.Entry(window, text = 'COREN:')
entry_COREN.grid(row=5, column=1, padx=10, pady=10)

#botão

button_cadastrar = tk.Button(window, text = 'Cadastrar Paciente', command = cadastrarPaciente)
button_cadastrar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=70)

button_exportar = tk.Button(window, text = 'Exportar Dados', command = exportarDados)
button_exportar.grid(row=7, column=0, padx=10, pady=10, columnspan=2, ipadx=70)


window.mainloop()
