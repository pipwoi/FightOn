#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer

import tkinter as tk
from tkinter import*
from tkinter import scrolledtext




if __name__ == '__main__':
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


root = tk.Tk()

root.title("Fight0n Lexical Analyzer")


lbl_Code=Label(root, text="Code to Analyze", fg='blue', font=("Helvetica", 16))
lbl_Code.place(x=50, y=10)  # Code to Analyze


btn=Button(root, text="Analyze Code", fg='blue')
btn.place(x=300, y=10) # Analyze Btn

v0=IntVar()
v0.set(1)
r1=Radiobutton(root, text="Lexical", variable=v0,value=1)
r2=Radiobutton(root, text="Syntax", variable=v0,value=2)
r1.place(x=520, y=10)  # Lexical
r2.place(x=700, y=10)  # Syntax


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

for tok in tab_row:
    output1.insert(INSERT, tok)

for le in lexerror:
    output2.insert(INSERT, le)


root.geometry("1220x400+300+200")
root.mainloop()







