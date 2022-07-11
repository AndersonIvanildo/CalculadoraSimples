from tkinter import *

class Calculadora:

    def __init__(self, instanciaDoTk) -> None:
        
        """ =========================== Definindo os elementos a serem utilizados na aplicação ========================== """
        

        self.frame_principal = Frame(instanciaDoTk, bg="#686868") # Frame responsável por armazenar todos os elementos da aplicação.
        self.frame_principal.propagate(False) # Características do formato do frame imutável

        self.frame_tela = Frame(self.frame_principal) # Frame onde será exibido os resultados.
        self.textoTela = StringVar() # String a ser exibida no "display" da calculadora.
        self.textoTela.set("") # Valor inicial.
        self.informacaoTela = Label(self.frame_tela, textvariable=self.textoTela, font=("Roboto", 20), anchor="e")

        self.frame_botoes = Frame(self.frame_principal, bg="#686868") # Frame onde será alocado todos os botões necessários para aplicação.

        self.botao_limpar_tudo =         Button(self.frame_botoes, text="AC", font=("Roboto", 35), command= lambda: limpaTela())
        self.botao_parenteses_esquerdo = Button(self.frame_botoes, text="(", font=("Roboto", 35))
        self.botao_parenteses_direita =  Button(self.frame_botoes, text=")", font=("Roboto", 35))
        self.botao_apagar =              Button(self.frame_botoes, text="<-", font=("Roboto", 35), command=lambda: apagarUltimoDigito())
        self.botao_somar =               Button(self.frame_botoes, text="+", font=("Roboto", 40), command= lambda: capturaOperador("+"))
        self.botao_subtrair =            Button(self.frame_botoes, text="-", font=("Roboto", 40), command= lambda: capturaOperador("-"))
        self.botao_multiplicar =         Button(self.frame_botoes, text="x", font=("Roboto", 40), command= lambda: capturaOperador("x"))
        self.botao_dividir =             Button(self.frame_botoes, text="/", font=("Roboto", 40), command= lambda: capturaOperador("/"))
        self.botao_ponto_flutuante =     Button(self.frame_botoes, text=".", font=("Roboto", 40))
        self.botao_resultado =           Button(self.frame_botoes, text="=", font=("Roboto", 40))

        self.botao_0 =                   Button(self.frame_botoes, text="0", font=("Roboto", 40), command=lambda: capturaDigito("0"))
        self.botao_1 =                   Button(self.frame_botoes, text="1", font=("Roboto", 40), command=lambda: capturaDigito("1"))
        self.botao_2 =                   Button(self.frame_botoes, text="2", font=("Roboto", 40), command=lambda: capturaDigito("2"))
        self.botao_3 =                   Button(self.frame_botoes, text="3", font=("Roboto", 40), command=lambda: capturaDigito("3"))
        self.botao_4 =                   Button(self.frame_botoes, text="4", font=("Roboto", 40), command=lambda: capturaDigito("4"))
        self.botao_5 =                   Button(self.frame_botoes, text="5", font=("Roboto", 40), command=lambda: capturaDigito("5"))
        self.botao_6 =                   Button(self.frame_botoes, text="6", font=("Roboto", 40), command=lambda: capturaDigito("6"))
        self.botao_7 =                   Button(self.frame_botoes, text="7", font=("Roboto", 40), command=lambda: capturaDigito("7"))
        self.botao_8 =                   Button(self.frame_botoes, text="8", font=("Roboto", 40), command=lambda: capturaDigito("8"))
        self.botao_9 =                   Button(self.frame_botoes, text="9", font=("Roboto", 40), command=lambda: capturaDigito("9"))

        """=============================== Posicionando os elementos nos devidos lugares ==============================="""

        # Psocionamento dos widgets
        self.frame_principal.place(x=0, y=0, width=367, height=600)
        self.frame_tela.place(x=17, y=20, width=333, height=97)
        self.informacaoTela.place(width=333, height=97)
        self.frame_botoes.place(x=0, y=126, width=367, height=474)

        # Linha 1 de botões
        self.botao_limpar_tudo.place(x=17, y=12, width=75, height=75)
        self.botao_parenteses_esquerdo.place(x=103, y=12, width=75, height=75)
        self.botao_parenteses_direita.place(x=189, y=12, width=75, height=75)
        self.botao_apagar.place(x=275, y=12, width=75, height=75)

        # Linha 2 de botões
        self.botao_9.place(x=17, y=102, width=75, height=75)
        self.botao_8.place(x=103, y=102, width=75, height=75)
        self.botao_7.place(x=189, y=102, width=75, height=75)
        self.botao_multiplicar.place(x=275, y=102, width=75, height=75)

        # Linha 3 de botões
        self.botao_6.place(x=17, y=192, width=75, height=75)
        self.botao_5.place(x=103, y=192, width=75, height=75)
        self.botao_4.place(x=189, y=192, width=75, height=75)
        self.botao_subtrair.place(x=275, y=192, width=75, height=75)

        # Linha 4 de botões
        self.botao_3.place(x=17, y=282, width=75, height=75)
        self.botao_2.place(x=103, y=282, width=75, height=75)
        self.botao_1.place(x=189, y=282, width=75, height=75)
        self.botao_somar.place(x=275, y=282, width=75, height=75)

        # Linha 5 de botões
        self.botao_dividir.place(x=17, y=372, width=75, height=75)
        self.botao_0.place(x=103, y=372, width=75, height=75)
        self.botao_ponto_flutuante.place(x=189, y=372, width=75, height=75)
        self.botao_resultado.place(x=275, y=372, width=75, height=75)


        """ ================= Funções para tratar a entrada de valores a serem processados posteriormente ================= """
        def limpaTela():
            self.textoTela.set("")
        
        def apagarUltimoDigito():
            self.textoTela.set(self.textoTela.get()[:-1])

        def capturaDigito(digito):
            self.textoTela.set(self.textoTela.get() + digito)

        def capturaOperador(operacao):
            if self.textoTela.get() == "": # Caso ainda não tenha nenhum dígito inserido.
                if operacao == "-": # Caso o número digitado seja negativo.
                    self.textoTela.set(self.textoTela.get() + operacao)
            else:
                if operacao in ["+", "-", "x", "/"]: 
                    if self.textoTela.get()[-1] not in ["+", "-", "x", "/"]: # Se não há um sinal de operando antes da inserção...
                        self.textoTela.set(self.textoTela.get() + operacao)
                    else:
                        self.textoTela.set(self.textoTela.get()[:-1] + operacao) # ...Caso, haja um sinal, este é substituído pelo novo operando.
            
