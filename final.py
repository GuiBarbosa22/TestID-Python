import pyodbc
import tkinter as tk
from tkinter import messagebox
import datetime

# Conectar ao SQL Server
conn = pyodbc.connect('Driver={SQL Server};Server=Guilherme;Database=Programa_atendimentoZIP;UID=sa;PWD=alex3103')

import pyodbc
import tkinter as tk
from tkinter import messagebox

# Conectar ao SQL Server
conn = pyodbc.connect('Driver={SQL Server};Server=Guilherme;Database=Programa_atendimentoZIP;UID=sa;PWD=alex3103')

# Função para inserir dados no banco
def inserir_dados_no_banco(nome_cliente, empresa_cliente, problema, solucao):
    try:
        with conn.cursor() as cursor:
            sql_insert_atendimentos = "INSERT INTO Atendimentos (NomeCliente, EmpresaCliente, DataAtendimento, Problema) VALUES (?, ?, ?, ?)"
            data_atendimento = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dados_para_inserir_atendimentos = (nome_cliente, empresa_cliente, data_atendimento, problema)
            cursor.execute(sql_insert_atendimentos, dados_para_inserir_atendimentos)

            sql_insert_solucoes = "INSERT INTO Solucoes (Solucao) VALUES (?)"
            cursor.execute("SELECT SCOPE_IDENTITY()")
            id_ocorrencia = cursor.fetchone()[0]
            dados_para_inserir_solucoes = (solucao,)
            cursor.execute(sql_insert_solucoes, dados_para_inserir_solucoes)

        conn.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso no banco!")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Erro ao inserir dados no banco: {e}")

# Função para realizar login
def login(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username=? and password=?", (username, password))
    row = cursor.fetchone()

    if row:
        messagebox.showinfo("Sucesso", f"Login bem sucedido! Bem-vindo, {username}!")
        open_main_window()
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos. Por favor, tente novamente!")

# Função para cadastrar um novo usuário
def cadastrar(username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username=?", (username,))
    row = cursor.fetchone()

    if row:
        messagebox.showerror("Erro", "Nome de usuário já existente. Por favor, escolha outro!")
    else:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

# Função para limpar os campos de login
def clear_login_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Função chamada ao fechar a janela de login
def on_close_login():
    root_login.destroy()

# Função chamada ao fechar a janela principal
def on_close_main():
    root.destroy()

# Função para abrir a janela principal
def open_main_window():
    root_login.withdraw()
    root = tk.Tk()
    root.title("Barbosa Support Log")
    root.protocol("WM_DELETE_WINDOW", on_close_main)
    # Adicione aqui o código para a janela principal
    root.mainloop()

# Configurar a janela de login
root_login = tk.Tk()
root_login.title("Login")
root_login.protocol("WM_DELETE_WINDOW", on_close_login)

label_username = tk.Label(root_login, text="Nome de Usuário:")
label_username.pack()
entry_username = tk.Entry(root_login)
entry_username.pack()

label_password = tk.Label(root_login, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root_login, show="*")
entry_password.pack()

btn_login = tk.Button(root_login, text="Login", command=lambda: login(entry_username.get(), entry_password.get()))
btn_login.pack()

btn_cadastrar = tk.Button(root_login, text="Criar Conta", command=lambda: cadastrar(entry_username.get(), entry_password.get()))
btn_cadastrar.pack()

# Maximizar a janela de login na inicialização
root_login.state('zoomed')

# Iniciar o loop do tkinter para a janela de login
root_login.mainloop()

# Fechar a conexão
conn.close()

# Definir função para inserir dados no banco
def inserir_dados_no_banco(nome_cliente, empresa_cliente, problema, solucao):
    try:
        with conn.cursor() as cursor:
            sql_insert_atendimentos = "INSERT INTO Atendimentos (NomeCliente, EmpresaCliente, DataAtendimento, Problema) VALUES (?, ?, ?, ?)"
            data_atendimento = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dados_para_inserir_atendimentos = (nome_cliente, empresa_cliente, data_atendimento, problema)
            cursor.execute(sql_insert_atendimentos, dados_para_inserir_atendimentos)

            sql_insert_solucoes = "INSERT INTO Solucoes (Solucao) VALUES (?)"
            cursor.execute("SELECT SCOPE_IDENTITY()")
            id_ocorrencia = cursor.fetchone()[0]
            dados_para_inserir_solucoes = (solucao,)
            cursor.execute(sql_insert_solucoes, dados_para_inserir_solucoes)

        conn.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso no banco!")
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Erro ao inserir dados no banco: {e}")

# Função para cadastrar um novo usuário
def cadastrar():
    print("Por favor, preencha os campos abaixo para se cadastrar:")
    username = input("Nome de usuário: ")
    password = input("Insira sua senha: ")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username=?", (username,))
    row = cursor.fetchone()

    if row:
        print("Nome de usuário já existente. Por favor, escolha outro!")
    else:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Usuário cadastrado com sucesso!")

# Função para realizar login
def login():
    username = input("Digite o seu nome de usuário: ")
    password = input("Digite a senha: ")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username=? and password=?", (username, password))
    row = cursor.fetchone()

    if row:
        print("Login bem sucedido! Bem-vindo, " + username + "!")
    else:
        print("Nome de usuário ou senha incorretos. Por favor, tente novamente!")

# Função para limpar os campos
def clear_fields():
    entry_nome_cliente.delete(0, tk.END)
    entry_empresa_cliente.delete(0, tk.END)
    entry_problema.delete("1.0", tk.END)
    entry_solucao.delete("1.0", tk.END)

# Função chamada ao fechar a janela
def on_close():
    root.destroy()

# Configurar a janela principal
root = tk.Tk()
root.title("Barbosa Support Log")
root.configure(background="#f0f0f0")

# Configurar a grade para preencher a tela
for i in range(5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

# Definir os campos e botões na janela
label_nome_cliente = tk.Label(root, text="Nome do Cliente:", bg="#f0f0f0")
label_nome_cliente.grid(row=0, column=0, padx=(20, 5), pady=5, sticky="w")

entry_nome_cliente = tk.Entry(root)
entry_nome_cliente.grid(row=0, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

label_empresa_cliente = tk.Label(root, text="Empresa do Cliente:", bg="#f0f0f0")
label_empresa_cliente.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="w")

entry_empresa_cliente = tk.Entry(root)
entry_empresa_cliente.grid(row=1, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

label_problema = tk.Label(root, text="Problema Enfrentado:", bg="#f0f0f0")
label_problema.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="w")

entry_problema = tk.Text(root, height=4, width=30)
entry_problema.grid(row=2, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

label_solucao = tk.Label(root, text="Solução Encontrada:", bg="#f0f0f0")
label_solucao.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="w")

entry_solucao = tk.Text(root, height=4, width=30)
entry_solucao.grid(row=3, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

btn_inserir = tk.Button(root, text="Inserir Dados", command=lambda: inserir_dados_no_banco(entry_nome_cliente.get(), entry_empresa_cliente.get(), entry_problema.get("1.0",'end-1c'), entry_solucao.get("1.0",'end-1c')), bg="#0080ff", fg="white")
btn_inserir.grid(row=4, column=0, columnspan=5, pady=10, padx=(20, 20), sticky="ew")

# Configurar a ação ao fechar a janela
root.protocol("WM_DELETE_WINDOW", on_close)

# Maximizar a janela na inicialização
root.state('zoomed')

# Iniciar o loop do tkinter
root.mainloop()

# Fechar a conexão
conn.close()