import customtkinter

# Função para converter para binário


def converter_para_binario():
    try:
        num = int(num_entry.get())
        resultado = bin(num)[2:]
        resultado_label.configure(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Por favor, insira um número válido.")

# Função para converter para octal


def converter_para_octal():
    try:
        num = int(num_entry.get())
        resultado = oct(num)[2:]
        resultado_label.configure(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Por favor, insira um número válido.")

# Função para converter para hexadecimal


def converter_para_hexadecimal():
    try:
        num = int(num_entry.get())
        resultado = hex(num)[2:]
        resultado_label.configure(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Por favor, insira um número válido.")


# Criação da janela principal
janela = customtkinter.CTk()
janela.geometry("550x550")

# Adiciona um rótulo (label)
texto = customtkinter.CTkLabel(janela, text="Conversor de Bases")
texto.pack(padx=10, pady=10)

# Adiciona uma entrada de texto
num_entry = customtkinter.CTkEntry(janela, placeholder_text="Número decimal")
num_entry.pack(padx=10, pady=10)

# Adiciona botões para cada conversão
botao1 = customtkinter.CTkButton(
    janela, text="Converter para Binário", command=converter_para_binario)
botao1.pack(padx=10, pady=10)

botao2 = customtkinter.CTkButton(
    janela, text="Converter para Octal", command=converter_para_octal)
botao2.pack(padx=10, pady=10)

botao3 = customtkinter.CTkButton(
    janela, text="Converter para Hexadecimal", command=converter_para_hexadecimal)
botao3.pack(padx=10, pady=10)

# Adiciona um rótulo para mostrar o resultado
resultado_label = customtkinter.CTkLabel(janela, text="Resultado: ")
resultado_label.pack(padx=10, pady=10)

# Adiciona um rótulo para o autor
autor_label = customtkinter.CTkLabel(janela, text="Autor: Gabriel Cézar")
autor_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# Executa o loop principal da janela
janela.mainloop()
