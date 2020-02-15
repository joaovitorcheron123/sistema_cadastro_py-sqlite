from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import db

#janela
janela = Tk()
janela.title("Meu Sistema - Login e Cadastro")
janela.geometry("600x300")
janela.attributes("-alpha", 0.978) #transparencia
janela.iconbitmap(default="image/icon.ico")
janela.resizable(width=False, height=False) #janela nao redimensionavel
janela.configure(background="white")

logo = PhotoImage(file="image/logo.png")
LeftFrame = Frame(janela, width=200, height=300, bg="DarkSlateGray4", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=395, height=300, bg="DarkSlateGray3", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="DarkSlateGray4")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg="DarkSlateGray3", fg="White")
UserLabel.place(x=50, y=100)

UserEntrada = ttk.Entry(RightFrame, width=30)
UserEntrada.place(x=160, y=111)

SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="DarkSlateGray3", fg="White")
SenhaLabel.place(x=65, y=150)

EntradaSenha = ttk.Entry(RightFrame, show="•", width=30)
EntradaSenha.place(x=160, y=161)

def Login():
    db.cursor.execute("""
    SELECT * FROM Users
    WHERE (Usuario = ? AND Senha = ?)
    """),(Usuario,Senha)
    print("")
    VerificaLogin = db.cursor.fetchone()
    try:
        if(Usuario in VerificaLogin and Senha in VerificaLogin):
            messagebox.showinfo(title="Login", message="Bem Vindo!")
    except:
        messagebox.showinfo(title="Erro", message="Senha ou usuário inválido!")

#Button
LoginButton = Button(RightFrame, text="Fazer Login", width=30, command=Login)
LoginButton.place(x=100,y=205)

def Cadastro(): #tela de cadastro
    #remove button
    LoginButton.place(x=10000)
    CadastroButton.place(x=10000)
    #insere widget
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="DarkSlateGray3", fg="White")
    NomeLabel.place(x=65,y=5)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=160, y=17)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="DarkSlateGray3", fg="White")
    EmailLabel.place(x=69, y=53)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=160, y=63)

    def CadastroParaDB(): #conectar ao banco
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntrada.get()
        Senha = EntradaSenha.get()

        if(Nome == "" or Email == ("") or Usuario == ("") or Senha == ("")):
            messagebox.showinfo(title="Erro no cadastro!", message="Preencha todos os campos!")
        else:
            db.cursor.execute("""
            INSERT INTO Users(Nome, Email, Usuario, Senha) VALUES(?,?,?,?)
            """,(Nome,Email,Usuario,Senha))
            db.conn.commit()
            messagebox.showinfo(title="Cadastrar Dados", message="Cadastrado com sucesso!")

    Cadastro = ttk.Button(RightFrame, text="Cadastrar-se", width=30, command=CadastroParaDB)
    Cadastro.place(x=105,y=200)

    def BackLogin(): #voltar ao login
        #remove widget cadastro
        NomeLabel.place(x=10000)
        NomeEntry.place(x=10000)
        EmailLabel.place(x=10000)
        EmailEntry.place(x=10000)
        Cadastro.place(x=10000)
        Voltar.place(x=10000)
        #widget back
        LoginButton.place(x=100)
        CadastroButton.place(x=135)

    Voltar = ttk.Button(RightFrame, text="Voltar", width=30, command=BackLogin)
    Voltar.place(x=105,y=230)

CadastroButton = Button(RightFrame, text="Cadastrar-se", width=20, command=Cadastro)
CadastroButton.place(x=130,y=235)

janela.mainloop()
