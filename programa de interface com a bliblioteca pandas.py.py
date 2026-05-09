import tkinter as tk
from tkinter import ttk
import pandas as pd


class PrincipalRad:
    def __init__(self, win):
        # componentes
        self.lblNome = tk.Label(win, text="Nome do Aluno:")
        self.lblNota1 = tk.Label(win, text="Nota1")
        self.lblNota2 = tk.Label(win, text="Nota2")
        self.lblMedia = tk.Label(win, text="Média")

        self.txtNome = tk.Entry(win, bd=3)
        self.txtNota1 = tk.Entry(win)
        self.txtNota2 = tk.Entry(win)

        self.btnCalcular = tk.Button(win, text='Calcular Média', command=self.fCalcularMedia)

        # componentes treeView
        self.dadosColunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")

        self.treeMedias = ttk.Treeview(win,
                                       columns=self.dadosColunas,
                                       selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeMedias.yview)

        self.verscrlbar.pack(side='right', fill='y')

        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)

        self.treeMedias.heading("Aluno", text="Aluno")
        self.treeMedias.heading("Nota1", text="Nota1")
        self.treeMedias.heading("Nota2", text="Nota2")
        self.treeMedias.heading("Média", text="Média")
        self.treeMedias.heading("Situação", text="Situação")

        self.treeMedias.column("Aluno", minwidth=0, width=100)
        self.treeMedias.column("Nota1", minwidth=0, width=100)
        self.treeMedias.column("Nota2", minwidth=0, width=100)
        self.treeMedias.column("Média", minwidth=0, width=100)
        self.treeMedias.column("Situação", minwidth=0, width=100)

        self.treeMedias.pack(padx=10, pady=10)

        # POSICIONAMENTO DOS COMPONENTES NA JANELA
        self.lblNome.place(x=100, y=50)
        self.txtNome.place(x=200, y=50)

        self.lblNota1.place(x=100, y=100)
        self.txtNota1.place(x=200, y=100)

        self.lblNota2.place(x=100, y=150)
        self.txtNota2.place(x=200, y=150)

        self.btnCalcular.place(x=100, y=200)

        self.treeMedias.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)

        self.id = 0
        self.iid = 0

        self.carregarDadosIniciais()

    def carregarDadosIniciais(self):
        try:
            fsave = 'planilhaAlunos.xlsx'
            dados = pd.read_excel(fsave)
            print("*********** dados disponíveis*******")
            print(dados)

            nn = len(dados["Aluno"])
            for i in range(nn):
                nome = dados['Aluno'][i]
                nota1 = str(dados['Nota1'][i])
                nota2 = str(dados["Nota2"][i])
                media = str(dados["Média"][i])
                situacao = dados["Situação"][i]

                self.treeMedias.insert('', 'end',
                                       iid=self.iid,
                                       values=(nome,
                                               nota1,
                                               nota2,
                                               media,
                                               situacao))

                self.iid = self.iid + 1
                self.id = self.id + 1
        except:
            print("Ainda não existem dados para carregar")

    def fsalvarDados(self):
     try:
        fsave = 'planilhaAlunos.xlsx'
        dados = []

        for line in self.treeMedias.get_children():
            lstDados = self.treeMedias.item(line)['values']
            dados.append(lstDados)

        df = pd.DataFrame(data=dados, columns=self.dadosColunas)

        # Usando contexto para evitar problemas de fechamento
        with pd.ExcelWriter(fsave, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, sheet_name='Inconsistencias', index=False)

        print('dados salvos')
     except Exception as e:
        print("Não foi possível salvar os dados:", e)


    def fverificarSituacao(self, media):
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    def fCalcularMedia(self):
        try:
            nome = self.txtNome.get()
            nota1 = float(self.txtNota1.get())
            nota2 = float(self.txtNota2.get())

            media = (nota1 + nota2) / 2
            situacao = self.fverificarSituacao(media)

            self.treeMedias.insert('', 'end',
                                   iid=self.iid,
                                   values=(nome,
                                           nota1,
                                           nota2,
                                           media,
                                           situacao))

            self.iid = self.iid + 1
            self.id = self.id + 1

            self.fsalvarDados()
        except ValueError:
            print('Entre com valores válidos')
        finally:
            self.txtNome.delete(0, tk.END)
            self.txtNota1.delete(0, tk.END)
            self.txtNota2.delete(0, tk.END)


# Programa Principal
janela = tk.Tk()
Principal = PrincipalRad(janela)
janela.title("Sistema de Gestão Escolar")
janela.geometry("820x600+10+10")
janela.mainloop()
