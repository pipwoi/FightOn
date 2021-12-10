#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Main import *

import tkinter as tk
from tkinter import*
from tkinter import scrolledtext

def get_data():
    from Buffer import Buffer
    from LexicalAnalyzer import LexicalAnalyzer

    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    # Lists for every list returned list from the function tokenize
    token = []
    lexeme = []
    row = []
    column = []
    lexerror = []
    tab_row = []

    # Tokenize and reload of the buffer
    for i in Buffer.load_buffer():
        t, lex, lin, col, le, tr = Analyzer.tokenize(i)
        token += t
        lexeme += lex
        row += lin
        column += col
        lexerror += le
        tab_row += tr

    print('\nRecognize Tokens: ', token)
    print(*lexerror, sep='')

    return tab_row, lexerror


root = tk.Tk()
root.title("Fight0n Lexical Analyzer")

lbl_Code = Label(root, text="Code to Analyze", fg='blue', font=("Helvetica", 16))
lbl_Code.place(x=50, y=10)

lbl_lex = Label(root, text="LEXEME", font=("Helvetica", 12))
lbl_lex.place(x=480, y=10)

lbl_token = Label(root, text="TOKEN", font=("Helvetica", 12))
lbl_token.place(x=620, y=10)

lbl_line = Label(root, text="LINE", font=("Helvetica", 12))
lbl_line.place(x=740, y=10)

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(root, text="Lexical", variable=v0, value=1)
r2 = Radiobutton(root, text="Syntax", variable=v0, value=2)
r1.place(x=920, y=10)  # Lexical
r2.place(x=1050, y=10)  # Syntax

text_area = scrolledtext.ScrolledText(root,
                                      width=40, height=12,
                                      font=("Times New Roman", 15))

text_area.grid(column=0, row=2, pady=50, padx=10)
# placing cursor in text area
text_area.focus()

output1 = scrolledtext.ScrolledText(root, height = 17, state=NORMAL,  #state=DISABLED,
              width = 48,
              bg = "light cyan")

output2 = scrolledtext.ScrolledText(root, height = 17, state=NORMAL,
              width = 40,
              bg = "pink")

output1.grid(column=10, row=2, pady=1, padx=10)
output2.grid(column=360, row=2, pady=50, padx=10)


print('\n')


def printBox():
    codefile = open("program.txt", "r")
    text_area.insert(INSERT, codefile.read())
    codefile.close()

    op1,op2 = get_data()

    for tok in op1:
        output1.insert(INSERT, tok)

    for le in op2:
        output2.insert(INSERT, le)

def LexButton():
    toRead = text_area.get(1.0,END)
    codefile2 = open("program.txt", "w")
    codefile2.write(toRead)
    codefile2.close()

    text_area.delete('1.0', END)
    output1.delete('1.0', END)
    output2.delete('1.0', END)

    printBox()


btn=Button(root, text="Analyze Code", fg='blue', command = LexButton)
btn.place(x=250, y=10) # Analyze Btn

printBox()

root.geometry("1220x400+300+200")
root.mainloop()
