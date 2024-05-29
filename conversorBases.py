import customtkinter


def converter_para_binario():
    try:
        num = int(num_entry.get())
        resultado = bin(num)[2:]
        resultado_label.configure(text=f"Número inserido: {
                                  num}\nResultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Por favor, insira um número válido.")


def converter_para_octal():
    try:
        num = int(num_entry.get())
        resultado = oct(num)[2:]
        resultado_label.configure(text=f"Número inserido: {
                                  num}\nResultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Por favor, insira um número válido.")


def converter_para_hexadecimal():
    try:
        num = int(num_entry.get())
        resultado = hex(num)[2:]
        resultado_label.configure(text=f"Número inserido: {
                                  num}\nResultado: {resultado}")
    except ValueError:
        resultado_label.configure(text="Por favor, insira um número válido.")


# criação da janela
janela = customtkinter.CTk()
janela.geometry("550x550")
janela.maxsize(width=850, height=850)
janela.maxsize(width=550, height=550)

# adiciona uma label
texto = customtkinter.CTkLabel(
    janela, text="Conversor de Bases", font=("Arial", 20))
texto.pack(padx=10, pady=10)

# adiciona uma entrada de texto
num_entry = customtkinter.CTkEntry(janela, placeholder_text="Número decimal")
num_entry.pack(padx=10, pady=10)

# Adiciona botões para as conversões
botao1 = customtkinter.CTkButton(
    janela, text="Converter para Binário", command=converter_para_binario)
botao1.pack(padx=10, pady=10)

botao2 = customtkinter.CTkButton(
    janela, text="Converter para Octal", command=converter_para_octal)
botao2.pack(padx=10, pady=10)

botao3 = customtkinter.CTkButton(
    janela, text="Converter para Hexadecimal", command=converter_para_hexadecimal)
botao3.pack(padx=10, pady=10)

# adiciona um botão para a conversão contrária [WIP]
botao_conversao_contraria = customtkinter.CTkButton(
    janela, text="Converter de Binário/Octal/Hexadecimal para Decimal")
botao_conversao_contraria.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-50)

# adiciona uma label para mostrar o resultado
resultado_label = customtkinter.CTkLabel(janela, text="Resultado: ")
resultado_label.pack(padx=10, pady=10)

# adiciona label de autor
autor_label = customtkinter.CTkLabel(janela, text="Autor: Gabriel Cézar")
autor_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

# loop principal da janela
janela.mainloop()
