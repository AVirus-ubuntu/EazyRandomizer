from random import choice as ch
from tkinter import filedialog as fd, messagebox as msgb
if (file:=fd.askopenfilename())=='':exit()
else:
    if not file.endswith('.txt'): msgb.showwarning('!!!','Формат файла не .txt, могут быть ошибки!')
    with open(file,'r',-1,'utf-8') as fi:msgb.showinfo('Ur Result',f'U Got:\n\n{ch(fi.read().split("\n"))}')