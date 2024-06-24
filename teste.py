import pyodbc
import tkinter as tk
from tkinter import messagebox
import datetime

# Conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};Server=Guilherme;Database=Programa_atendimentoZIP;UID=sa;PWD=alex3103')

# Função para inserir dados no banco de dados
def inserir_dados_no_banco(nome_cliente, empresa_cliente, problema, solucao):
    try:
        with conn.cursor() as cursor:
            # Inserindo dados na tabela de Atendimentos
            sql_insert_atendimentos = "INSERT INTO Atendimentos (NomeCliente, EmpresaCliente, DataAtendimento, Problema) VALUES (?, ?, ?, ?)"
            data_atendimento = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dados_para_inserir_atendimentos = (nome_cliente, empresa_cliente, data_atendimento, problema)
            cursor.execute(sql_insert_atendimentos, dados_para_inserir_atendimentos)

            # Obtendo o ID da última inserção na tabela de Atendimentos
            cursor.execute("SELECT SCOPE_IDENTITY()")
            id_ocorrencia = cursor.fetchone()[0]

            # Inserindo dados na tabela de Soluções
            sql_insert_solucoes = "INSERT INTO Solucoes (ID_Ocorrencia, Solucao) VALUES (?, ?)"
            dados_para_inserir_solucoes = (id_ocorrencia, solucao)
            cursor.execute(sql_insert_solucoes, dados_para_inserir_solucoes)

        # Confirmar a transação
        conn.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso no banco!")
    except Exception as e:
        # Em caso de erro, fazer rollback
        conn.rollback()
        messagebox.showerror("Erro", f"Erro ao inserir dados no banco: {e}")

# Função para abrir a tela de registro de atendimentos
def abrir_tela_atendimentos():
    root_atendimentos = tk.Tk()
    root_atendimentos.title("Registro de Atendimentos")
    root_atendimentos.configure(background="#f0f0f0")

    # Configurar a grade para preencher a tela
    for i in range(5):
        root_atendimentos.rowconfigure(i, weight=1)
        root_atendimentos.columnconfigure(i, weight=1)

    # Definir os campos e botões na janela de atendimentos
    label_nome_cliente = tk.Label(root_atendimentos, text="Nome do Cliente:", bg="#f0f0f0")
    label_nome_cliente.grid(row=0, column=0, padx=(20, 5), pady=5, sticky="w")

    entry_nome_cliente = tk.Entry(root_atendimentos)
    entry_nome_cliente.grid(row=0, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")
    entry_nome_cliente.focus_set()

    label_empresa_cliente = tk.Label(root_atendimentos, text="Empresa do Cliente:", bg="#f0f0f0")
    label_empresa_cliente.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="w")

    entry_empresa_cliente = tk.Entry(root_atendimentos)
    entry_empresa_cliente.grid(row=1, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

    label_problema = tk.Label(root_atendimentos, text="Problema Enfrentado:", bg="#f0f0f0")
    label_problema.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="w")

    entry_problema = tk.Text(root_atendimentos, height=4, width=30)
    entry_problema.grid(row=2, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

    label_solucao = tk.Label(root_atendimentos, text="Solução Encontrada:", bg="#f0f0f0")
    label_solucao.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="w")

    entry_solucao = tk.Text(root_atendimentos, height=4, width=30)
    entry_solucao.grid(row=3, column=1, columnspan=4, padx=(5, 20), pady=5, sticky="ew")

    btn_inserir = tk.Button(root_atendimentos, text="Inserir Dados", command=lambda: inserir_dados_no_banco(entry_nome_cliente.get(), entry_empresa_cliente.get(), entry_problema.get("1.0",'end-1c'), entry_solucao.get("1.0",'end-1c')), bg="#0080ff", fg="white")
    btn_inserir.grid(row=4, column=0, columnspan=5, pady=10, padx=(20, 20), sticky="ew")

    # Configurar a ação ao fechar a janela de atendimentos
    root_atendimentos.protocol("WM_DELETE_WINDOW", lambda: on_close_atendimentos(root_atendimentos))

    # Iniciar o loop do tkinter para a janela de atendimentos
    root_atendimentos.mainloop()

# Função chamada ao fechar a janela de atendimentos
def on_close_atendimentos(janela):
    janela.destroy()

# Função para realizar login
def login(event=None):
    usuario = entry_username.get()
    senha = entry_password.get()

    # Verificar as credenciais
    usuarios = {'guilherme': 'guigui22', 'laura': '1011'}
    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Sucesso", "Login bem sucedido!")
        abrir_tela_atendimentos()  # Se o login for bem-sucedido, abre a tela de atendimentos
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos. Por favor, tente novamente!")

# Configuração da janela de login
root_login = tk.Tk()
root_login.title("Login")

label_username = tk.Label(root_login, text="Nome de Usuário:")
label_username.pack()
entry_username = tk.Entry(root_login)
entry_username.pack()
entry_username.bind("<Return>", login)

label_password = tk.Label(root_login, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root_login, show="*")
entry_password.pack()
entry_password.bind("<Return>", login)

btn_login = tk.Button(root_login, text="Login", command=login)
btn_login.pack()

# Iniciar o loop do tkinter para a janela de login
root_login.mainloop()

# Fechar a conexão com o banco de dados ao final do programa
conn.close()




