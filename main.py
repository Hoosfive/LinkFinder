from tkinter import *
from tkinter import filedialog
import re

def findLinks(text):
    textField.delete(0.0, "end")
    regex = r"(^|\s|)((https?:\/\/)?[\w-]+(\.[a-z-]+)+\.?(:\d+)?(\/\S*)?)"

    matches = re.finditer(regex, text, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        link = match.group()
        if link[link.__len__() - 1] == ")":
            link = link.split(")")[0]
        if link[link.__len__() - 1] == ".":
            link = link.split(".")[0]
        textField.insert(1.0, link + "\n")


def chooseFileDialog(mode, files):
    labelChosenFile["text"] = "Выбран: "
    ftypes = [('Файлы', files)]
    dlg = filedialog.Open(filetypes=ftypes)
    fl = dlg.show()
    if fl != '':
        labelChosenFile["text"] += fl
        if mode == 0:
            readFile(fl)
        elif mode == 1:
            return fl


def readFile(filename):
    with open(filename, "r", encoding="utf-8", errors='ignore') as f:
        text = f.read()
    findLinks(text)


def txtExport():
    file = open(chooseFileDialog(1, ".txt"), 'a+')
    file.write(textField.get("1.0", END))
    file.close()


root = Tk()

labelChooseFile = Label(text="Выберите файл:", font="Arial 14")
labelChooseFile.pack()
labelChosenFile = Label(text="", font="Arial 10")
labelChosenFile.pack()
btnChooseFile = Button(text="Выбрать файл", command=lambda: chooseFileDialog(0, "*"))
btnChooseFile.pack()

labelWriteSomeText = Label(text="Результат:", font="Arial 14")
labelWriteSomeText.pack()
textField = Text(width=65, height=25)
scroll = Scrollbar(command=textField.yview)
scroll.pack(side=RIGHT, fill=Y, ipadx=3, padx=2)
textField.config(yscrollcommand=scroll.set, wrap=WORD, state="normal")
textField.pack()

btnTxtExport = Button(text="Экспорт в .txt", command=lambda: txtExport())
btnTxtExport.pack(side=LEFT, expand=True)

w = root.winfo_screenwidth() // 2 - 300
h = root.winfo_screenheight() // 2 - 300
root.geometry('600x600+{}+{}'.format(w, h))
root.title("Link Finder v1.0")
root.mainloop()
