import tkinter as tk
from tkinter import messagebox

class SaborrapidoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x500")

        self.itens_menu = {"Hambúrguer": 10.00, "Batata Frita": 5.00, "Refrigerante": 3.00}
        self.pedido = []

        tk.Label(root, text="Selecione os itens do pedido", font=("Arial",12)).pack(pady=10)

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 10))
        self.atualizar_lista_menu()
        self.listbox.pack()

        tk.Button(root, text="Adicionar ao Pedido", command=self.adicionar_pedido).pack(pady=5)
        tk.Button(root, text="Visualizar pedido", command=self.visualizar_pedido).pack(pady=5)
        tk.Button(root, text="Finalizar Pedido", command=self.finalizar_pedido).pack(pady=10)

        tk.Label(root, text="Adicionar Novo item ao Menu", font=("Arial", 12)).pack(pady=10)
        self.entry_item = tk.Entry(root, font=("Arial", 10))
        self.entry_item.pack()
        self.entry_preco = tk.Entry(root, font=("Arial", 10))
        self.entry_preco.pack()
        tk.Button(root, text="Adicionar Item", command=self.adicionar_item_menu).pack(pady=5)

    def atualizar_lista_menu(self):
        self.listbox.delete(0, tk.END)
        for item in self.itens_menu.keys():
            self.listbox.insert(tk.END, item)

    def adicionar_pedido(self):
        selecionados = self.listbox.curselection()
        for index in selecionados:
            item = self.listbox.get(index)
            self.pedido.append(item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")

    def visualizar_pedido(self):
        if not self.pedido:
            messagebox.showinfo("Pedido", "Nenhum item no pedido")
            return
        pedido_texto = "\n".join(self.pedido)
        messagebox.showinfo("Pedido Atual", f"Itens no pedido:\n{pedido_texto}")

    def finalizar_pedido(self):
        if not self.pedido:
            messagebox.showinfo("Pedido", "Adicione itens antes de finalizar o pedido.")
            return
        total = sum(self.itens_menu[item] for item in self.pedido)
        messagebox.showinfo("Total", f"Total do pedido : R$ {total:.2f}\nPedido finalizado!")
        self.pedido.clear()

    def adicionar_item_menu(self):
        item = self.entry_item.get().strip()
        preco = self.entry_preco.get().strip()
        if item and preco:
            try:
                self.itens_menu[item] = float(preco)
                self.atualizar_lista_menu()
                self.entry_item.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
                messagebox.showinfo9("Sucesso", "Item adicionado ao menu com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Preencha ambos os campos corretamente.")
        else:
            messagebox.showerror("Erro", "Preencha ambos os campos corretamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaborrapidoApp(root)
    root.mainloop()

