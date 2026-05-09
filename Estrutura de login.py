import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import ttk
import pandas as pd

# Dicionário de usuários (credenciais)
usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"}
}


def abrir_tela_login():
    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def validar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            tipo_usuario = usuarios[usuario]["tipo"]
            login_win.destroy()
            iniciar_sistema(tipo_usuario, usuario)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    tk.Button(login_win, text="Entrar", command=validar_login).pack(pady=20)
    login_win.mainloop()

def iniciar_sistema(tipo_usuario, usuario):
    janela = tk.Tk()
    janela.title("Sistema de notas")
    janela.geometry("820x600")

    colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
    treeMedias = ttk.Treeview(janela, columns=colunas, show="headings")
    
    for coluna in colunas:
        treeMedias.heading(coluna, text=coluna)
        treeMedias.column(coluna, width=150)
    
    treeMedias.pack(pady=10)
    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeMedias.yview)
    treeMedias.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    carregar_dados(treeMedias, usuario, tipo_usuario)

    if tipo_usuario == "professor":
        tk.Button(janela, text="Cadastrar Aluno", command=lambda: cadastrar_aluno(treeMedias)).pack(pady=10)
        tk.Button(janela, text="Excluir Aluno", command=lambda: excluir_aluno(treeMedias, tipo_usuario)).pack(pady=10)

        janela.mainloop()

def carregar_dados(tree, usuario, tipo_usuario):
    try:
        df = pd.read_excel("planilha dos alunos.xlsx")
        tree.delete(*tree.get_children())

        if tipo_usuario == "professor":
            for _, row in df.iterrows():
                tree.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
        else:
            df_aluno = df[df["Aluno"] == usuario]
            for _, row in df_aluno.iterrows():
                tree.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        print("Nenhum dado encontrado")

def cadastrar_aluno(tree):
    nome = simpledialog.askstring("Cadastro", "Digite o nome do aluno:")
    nota1 = simpledialog.askfloat("Cadastro", "Digite a nota 1:")
    nota2 = simpledialog.askfloat("Cadastro", "Digite a nota 2:")
    media, situacao = verificar_situacao(nota1, nota2)

    tree.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))

def excluir_aluno(tree, tipo_usuario):
    if tipo_usuario != "professor":
        messagebox.showwarning("Acesso Negado", "Apenas professores podem excluir alunos.")
        return
    
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erro", "Nenhum aluno selecionado para exclusão.")
        return
    
    tree.delete(selected_item)
    salvar_dados(tree)


def salvar_dados(tree):
    dados = []
    for line in tree.get_children():
        valores = tree.item(line)["values"]
        dados.append(valores)

    df = pd.DataFrame(dados, columns=["Aluno", "Nota1", "Nota2", "Média", "Situação"])
    df.to_excel("planilha dos alunos.xlsx", index=False, engine='openpyxl')
    print("Dados salvos com sucesso!")

def verificar_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7.0:
        return media, "Aprovado"
    if media >= 5.0:
        return media, "em recuperação"
    else:
        return media, "Reprovado"
    
abrir_tela_login()

    

