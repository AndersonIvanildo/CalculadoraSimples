from calculadora import Calculadora
from tkinter import Tk

def main():
    root = Tk()
    root.title("CALCULADORA")
    root.geometry("367x600")
    root.resizable(False, False)
    Calculadora(root)
    root.mainloop()

if __name__ == '__main__':
    main()
