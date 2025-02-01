from customtkinter import *
from .modules.verificar_palindromo import verificar_palindromo


class App:
    def __init__(self) -> None:
        """
        Inicializa a classe GUI e configura a tela principal.

        Cria uma instância do CTk (CustomTkinter) e define a variável
        de resultado como uma string vazia.
        """
        self.screen = CTk()
        self.resultado = ""

    def configure(self):
        """
        Configura a janela principal da aplicação.

        Define o título da janela, o tamanho, a capacidade de redimensionamento e o modo de aparência.
        """
        self.screen.title("Palindrometro")
        self.screen.geometry("350x300")
        self.screen.resizable(False, False)
        self.screen._set_appearance_mode("dark")

    def verificar_palindromo(self):
        """
        Obtém o texto da entrada do usuário e verifica se é um palíndromo.

        Atualiza o rótulo de resposta com o resultado da verificação.
        """
        palavra = self.input.get()
        self.resultado = verificar_palindromo(palavra)
        self.response.configure(text=self.resultado)

    def main(self):
        """
        Configura e exibe os elementos principais da interface gráfica.

        Adiciona os widgets (rótulo, entrada, botão e rótulo de resposta) à tela principal.
        """
        self.bg = self.screen["bg"]

        # Cria e adiciona o rótulo de título
        self.title = CTkLabel(
            self.screen,
            width=350,
            height=40,
            text="Palindrometro",
            font=("sans-serif", 16),
            bg_color=self.bg,
        )
        self.title.pack(pady=15)

        # Cria e adiciona o campo de entrada de texto
        self.input = CTkEntry(self.screen, width=150, height=40, bg_color=self.bg)
        self.input.pack()

        # Cria e adiciona o botão para verificar se a palavra é um palíndromo
        self.button = CTkButton(
            self.screen,
            command=self.verificar_palindromo,
            width=100,
            height=40,
            text="Verificar",
            bg_color=self.bg,
            text_color="white",
        )
        self.button.pack(pady=20)

        # Cria e adiciona o rótulo que exibirá o resultado
        self.response = CTkLabel(self.screen, width=350, height=40, text=self.resultado)
        self.response.pack(pady=10)

    def run(self):
        """
        Executa a configuração e o loop principal da aplicação.

        Configura a interface gráfica e inicia o loop principal do Tkinter.
        """
        self.configure()
        self.main()
        self.screen.mainloop()
