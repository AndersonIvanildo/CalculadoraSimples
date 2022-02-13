from tkinter import *

class JanelaPrincipal:
    def __init__(self, instanciaTk) -> None:
        self.framePrincipal = Frame(instanciaTk)
        self.framePrincipal.pack()

        self.frameTela = Frame(self.framePrincipal, bg="grey", height=60, width=280) # Tela onde os resultados são mostrados.
        self.telaRESULTADO = Label(self.frameTela, padx=20, pady=20, text="", font=("Arial Black", 25)) # Tela onde mostrará o resultado.
        self.frameBotoes = Frame(self.framePrincipal, bg="black", height=400, width=280)  # Lugar onde estão os botões.
        
        self.telaRESULTADO.pack()
        self.frameTela.pack()
        self.frameBotoes.pack()

        #Distribuição dos botões

        # LINHA 1
        self.botaoCLEAR = Button(self.frameBotoes, text="CE", width=8, height=4, command=lambda: pegaString("clear")).grid(row=0, column=0)
        self.botaoEXP = Button(self.frameBotoes, text="EXP", width=8, height=4, command=lambda: pegaString("^")).grid(row=0, column=1)
        self.botaoROOT = Button(self.frameBotoes, text="ROOT", width=8, height=4, command=lambda: pegaString("RQ")).grid(row=0, column=2)
        self.botaoDEL = Button(self.frameBotoes, text="DEL", width=8, height=4, command=lambda: pegaString("del")).grid(row=0, column=3)

        # LINHA 2
        self.botaoNum7 = Button(self.frameBotoes, text="7", width=8, height=4, command=lambda: pegaString("7")).grid(row=1, column=0)
        self.botaoNum8 = Button(self.frameBotoes, text="8", width=8, height=4, command=lambda: pegaString("8")).grid(row=1, column=1)
        self.botaoNum9 = Button(self.frameBotoes, text="9", width=8, height=4, command=lambda: pegaString("9")).grid(row=1, column=2)
        self.botaoTIMES = Button(self.frameBotoes, text="x", width=8, height=4, command=lambda: pegaString("x")).grid(row=1, column=3)

        # LINHA 3
        self.botaoNum4 = Button(self.frameBotoes, text="4", width=8, height=4, command=lambda: pegaString("4")).grid(row=2, column=0)
        self.botaoNum5 = Button(self.frameBotoes, text="5", width=8, height=4, command=lambda: pegaString("5")).grid(row=2, column=1)
        self.botaoNum6 = Button(self.frameBotoes, text="6", width=8, height=4, command=lambda: pegaString("6")).grid(row=2, column=2)
        self.botaoMINUS = Button(self.frameBotoes, text="-", width=8, height=4, command=lambda: pegaString("-")).grid(row=2, column=3)

        # LINHA 4
        self.botaoNum1 = Button(self.frameBotoes, text="1", width=8, height=4, command=lambda: pegaString("1")).grid(row=3, column=0)
        self.botaoNum2 = Button(self.frameBotoes, text="2", width=8, height=4, command=lambda: pegaString("2")).grid(row=3, column=1)
        self.botaoNum3 = Button(self.frameBotoes, text="3", width=8, height=4, command=lambda: pegaString("3")).grid(row=3, column=2)
        self.botaoSUM = Button(self.frameBotoes, text="+", width=8, height=4, command=lambda: pegaString("+")).grid(row=3, column=3)
       
        # LINHA 5
        self.botaoDIV = Button(self.frameBotoes, text="/", width=8, height=4, command=lambda: pegaString("/")).grid(row=4, column=0)
        self.botaoNum0 = Button(self.frameBotoes, text="0",width=8, height=4, command=lambda: pegaString("0")).grid(row=4, column=1)
        self.botaoCOMMON = Button(self.frameBotoes, text=".", width=8, height=4, command=lambda: pegaString(".")).grid(row=4, column=2)
        self.botaoEQUAL = Button(self.frameBotoes, text="=", width=8, height=4, command=lambda: pegaString("=")).grid(row=4, column=3)

        self.valor01 = ""
        self.valor02 = ""

        def pegaString(valor):   
            if valor.isdecimal():
                if self.valor01 == "" or self.valor01[-1] != "_":
                    self.valor01 += valor
                    self.telaRESULTADO['text'] += valor
                else:
                    self.valor02 += valor
                    self.telaRESULTADO['text'] += valor
            elif valor == "clear":
                self.telaRESULTADO['text'] = ""
                self.valor01 = ""
                self.valor02 = ""

            elif valor in ['+', '-', 'x', '/', '^']:
                if self.valor01 != "":
                    self.telaRESULTADO['text'] += valor
                    self.valor01 += "_"
                    self.calculo = valor

            elif valor == ".":
                if self.valor01 != "" and self.valor01[-1] != "_" and "." not in self.valor01:
                    self.valor01 += valor
                    self.telaRESULTADO['text'] += valor
                elif self.valor02 != "" and "." not in self.valor02:
                    self.valor02 += valor
                    self.telaRESULTADO['text'] += valor


            elif valor == "RQ":
                if self.valor01 != "":
                    self.valor01 = self.valor01.replace('_', "")
                    self.valor01 = float(self.valor01)
                    operacao(self.valor01, 1, "RQ")

            elif valor == "del":
                if self.telaRESULTADO['text'] != "":
                    self.telaRESULTADO['text'] = self.telaRESULTADO['text'].replace(self.telaRESULTADO['text'][-1], "")

            elif valor == "=":
                self.valor01 = self.valor01.replace('_', "")
                self.valor01 = float(self.valor01)
                self.valor02 = float(self.valor02)
                operacao(self.valor01, self.valor02, self.calculo)
                self.valor01 = ""
                self.valor02 = ""

        def operacao(exp1, exp2, expressao):
            if expressao == "+":
                self.telaRESULTADO['text'] = f"{exp1 + exp2:.4f}"

            elif expressao == "-":
                self.telaRESULTADO['text'] = f"{exp1 - exp2:.4f}"

            elif expressao == "x":
                self.telaRESULTADO['text'] = f"{exp1 * exp2:.4f}"

            elif expressao == "/":
                self.telaRESULTADO['text'] = f"{exp1 / exp2:.4f}"

            elif expressao == "^":
                self.telaRESULTADO['text'] = f"{exp1 ** exp2:.4f}"

            elif expressao == "RQ":
                self.telaRESULTADO['text'] = f"{(exp1 * 1) ** (1/2):.4f}"

root = Tk()
root.title("CALCULADORA")
root.resizable(False, False)
JanelaPrincipal(root)
root.mainloop()
