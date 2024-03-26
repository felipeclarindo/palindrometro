from customtkinter import *

class GUI:
    def __init__(self) -> None:
        self.screen = CTk()

    def configure(self):
        self.screen.title("Palindrometro")
        self.screen.geometry("350x300")
        self.screen.resizable(False, False)
        self.screen._set_appearance_mode("dark")

    def main(self):
        self.bg = self.screen["bg"]
        self.title = CTkLabel(self.screen, width=350, height=40, text = "Palindrometro")
        self.title.pack()

        self.input = CTkEntry(self.screen, width=150 , height=40, bg_color=self.bg)
        self.input.pack(pady = 30)

        self.button = CTkButton(self.screen,width=100, height=40, text="Verificar", bg_color=self.bg , text_color="white")
        self.button.pack()


    def executar(self):
        self.configure()
        self.main()
        self.screen.mainloop()
        
if __name__ == "__main__":
    screen = GUI()
    screen.executar()