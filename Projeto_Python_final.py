# -*- coding: utf-8 -*-

"""
Programa gráfico que auxilia no calculo de integrais definidas e indefinidas:

autores:
    Amanda Gutierrez Sato - Interface gráfica; implementação do algoritimo 
    Arthur Duran  - Documentação
    Eduardo Ribeiro - Documentação
    Letícia Anteghini - Desenvolvimento e implementação do algoritimo
    Eduarda Wiltiner - Desenvolvimento e implementação do algoritimo
    Heimilly Lavele - Interface gráfica e Layout
    Lucas Pereira - Controle de versões e distribuições; Interface gráfica
    Alexandre Leal - Interface gráfica e Layout
"""

#BIBLIOTECAS IMPORTADAS
import tkinter.messagebox as msg  
from tkinter import filedialog                                      # Usos para a interface GUI
import webbrowser                                                   #
import tkinter as tk                                                # Biblioteca de interface GUI 
import matplotlib.pyplot as plt                                     # Usos para a montagem do gráfico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg     # Importando função da matplot, para o gráfico
import numpy as np                                                  # Biblioteca matemática
import re                                                           #
from sympy.parsing.sympy_parser import parse_expr                   #
from sympy.abc import x                                             #
from sympy import integrate                                         # Importando a função intergrar da biblioteca simpy
import scipy.integrate as spi                                       # Importa a função integrate da biblioteca scipy

######## TODAS AS PARTES SEPARADINHAS RESPECTIVAMENTE ###########

        ### JANELA 
        ### FRAME1 ONDE A FUNÇÃO, OS LIMITES E O ERRO SERÃO DEFINIDOS
        ### FRAME2 ONDE SERÁ MOSTRADO O RESULTADO DA INTEGRAL
        ### FRAME3 ONDE SERÁ PLOTADO O GRÁFICO
        ### FUNÇÂO CÀLCULO DAS INTEGRAIS DEFINIDAS E INDEFINIDAS
        ### ENTRADAS
        ### DEFINIÇÃO DO GRÁFICO DA FUNÇÃO 
        ### BOTOẼS
        ### IMAGEM DO SÍMBOLO DA INTEGRAL
        ### POSIÇÃO DO FRAME1 E DE TUDO DENTRO DO FRAME1
        ### POSIÇÃO DO FRAME2 E DE TUDO DENTRO DO FRAME2
        ### FINAL

        

###JANELA 

janela = tk.Tk()                                                        # Criação da Janela principal do programa
janela.title('Calculadora Gráfica de Integral')                         # Nome do programa
janela.configure(bg = 'alice blue')                                     # Cor do background da janela
janela.geometry("1000x500")                                             # Tamanho da Janela
janela.focus_set()                                                      #
janela.bind("<Escape>", lambda e: e.widget.quit())                      #
janela.resizable(0, 0)                                                  # Não permite alterar o tamanho da janela

#--------------------------------------------------------------------------------------------------------
###FRAME1 ONDE A FUNÇÃO, OS LIMITES E O ERRO SERÃO DEFINIDOS

Frame1 = tk.Frame(janela , bd = 60, bg = '#B0C4DE', width = 500, height= 500)       # Criação do Frame1, região onde os inputs da função serão dados
Frame1.pack()

	## text1f1 é o título do frame 1, os textnf1 de 2 a 5 são os títulos das 4 caixas de texto a serem inseridos
text1f1 = tk.Label(Frame1, text = 'Integração utilizando função', width=40, bg = '#B0C4DE',fg = 'black', font = ("Verdana","10","bold"))   # Título do Frame1
text1f1.pack()

text2f1 = tk.Label(Frame1, text = 'xi', bg = '#B0C4DE',fg = 'black')      # Legendas das Caixas de texto 
text2f1.pack()

text3f1 = tk.Label(Frame1, text = 'xf', bg = '#B0C4DE',fg = 'black')      # Legendas das Caixas de texto
text3f1.pack()

text4f1 = tk.Label(Frame1, text = 'f(x)',bg = '#B0C4DE',fg = 'black')     # Legendas das Caixas de texto
text4f1.pack()

text5f1 = tk.Label(Frame1, text = 'erro', bg = '#B0C4DE',fg = 'black')    # Legendas das Caixas de texto
text5f1.pack()

	## Os text 6 e 7 representam os subtópicos para o cálculo da integral
  
text6f1 = tk.Label(Frame1, text = 'Limites de integração', bg = '#B0C4DE',fg = 'black', font = ("Verdana","8","bold"))  # Título das Legendas
text6f1.pack()

text7f1 = tk.Label(Frame1, text = 'Função e Erro', bg = '#B0C4DE',fg = 'black', font = ("Verdana","8","bold"))          # Título das Legendas
text7f1.pack()
    
	## Os quatro valores inseridos serão captados nesses inputs
    
input1 = tk.StringVar()     # xi (limite esquerdo do domínio de integração)
input3 = tk.DoubleVar()     # xf (limite direito do domínio de integração)
input4 = tk.DoubleVar()     # Função de x --> f(x)
input5 = tk.DoubleVar()     # Erro 

	## Opção de realizar a integral indefinida, usando um botão de on,off.
v = tk.IntVar()
C = tk.Checkbutton(Frame1, text='Intergral indefinida',variable=v,fg = 'black',bg = 'white') # Botão de 'Switch' entre a integral indefinida e a definida 
C.var = v
C.pack()
#----------------------------------------------------------------------------------------------

###FRAME2 ONDE SERÁ MOSTRADO O RESULTADO DA INTEGRAL

Frame2 = tk.Frame(janela, bd = 50, width= 500, height = 150, bg = '#050951') # Criação do Frame2, região onde os outputs da função ou da tabela serão dados
Frame2.pack(side= 'bottom')

text1f2 = tk.Label(Frame2, text= 'Resultado da integral definida ou (Função primitiva) G(x)',bg = '#050951',fg = 'white', font= ("Verdana","8","bold"))  # Título da caixa de texto que mostra o resultado
text1f2.pack()

xLabel = tk.Label(Frame2, width=30, bg = 'alice blue', bd=3, relief= 'raised')   # Caixa que indica o resultado
xLabel.pack()
#----------------------------------------------------------------------------------------------

###FRAME3 ONDE SERÁ PLOTADO O GRÁFICO

Frame3 = tk.Frame(janela,bd = 50, bg = 'white', width= 100, height = 100)  # Criação do Frame3, região onde o gráfico de f(x) é plotado
Frame3.pack(side='left')                    # Posição do Frame3 dentro da janela
Frame3.place(relx=.4, rely = .9)            # Posição do Frame3 dentro da janela

text1f3 = tk.Label(Frame3, text = 'Região onde o gráfico de f(x) será plotado', width=40, bg = 'white' , fg= 'black', font = ("Verdana","10","bold"))  # Título do Frame3
text1f3.pack()
#----------------------------------------------------------------------------------------------

###FRAME4 ONDE SERÃO IMPORTADOS DADOS 

Frame4 = tk.Frame(janela,bd = 50, width= 500, height = 135, bg = '#050951') # Criação do Frame4, região onde os inputs de tabela são feitos
Frame4.pack()

text2f4 = tk.Label(Frame4, text = 'Integração utilizando uma tabela', width=40, bg = '#050951',fg = 'white', font = ("Verdana","10","bold"))  # Título do Frame4 
text2f4.pack()

text1f4 = tk.Label(Frame4, text= 'Diretório do arquivo',fg= 'white', bg = '#050951')  # Legenda da caixa de texto
text1f4.pack()

dados = tk.StringVar()        # 

#----------------------------------------------------------------------------------------------

###FUNÇÂO CÀLCULO DAS INTEGRAIS DEFINIDAS E INDEFINIDAS

fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master= Frame3)
canvas.get_tk_widget().pack()

def result():
    try:
        novafunção = input1.get()
        limS = input4.get()
        limI = input3.get()
        if str(limS)=='inf' or str(limS)=='inf' or str(limI)=='inf' or str(limI)=='-inf' :
            msg.showinfo("Erro", "Caracterer invalido!!, limites infinitos não aceitos")
        err = input5.get()
        x2 = np.linspace(-10,10,100) 
        x1 = np.linspace(limI,limS,100)
    except:
         msg.showinfo("Erro", "Caracterer invalido!!")
         
         
    if v.get()== 1:
#integral indefinida
        try:
            

            fun = parse_expr(novafunção)
            a = str(integrate(fun,x)) + ' + C'
            resultado2= str(a)
            xLabel.config(text = resultado2)
            w = x2
            resultado2= str(a)
            novafunção = re.sub("cos", "np.cos", novafunção)
            novafunção = re.sub("sin", "np.sin", novafunção)
            novafunção = re.sub("tan", "np.tan", novafunção)
            novafunção = re.sub("anp.cos", "np.arccos", novafunção)
            novafunção = re.sub("anp.sin", "np.arcsin", novafunção)
            novafunção = re.sub("anp.tan", "np.arctan", novafunção)
            novafunção = re.sub("anp.sinh", "np.arcsinh", novafunção)
            novafunção = re.sub("anp.cosh", "np.arccosh", novafunção)
            novafunção = re.sub("anp.tanh", "np.arctanh", novafunção)
            novafunção = re.sub("ln", "np.log", novafunção)
            novafunção = re.sub("exp", "np.exp",novafunção)
            input4.set(10)
            input3.set(-10)
            def f(x):
                return eval(novafunção)  
          
        except:
            msg.showinfo("Erro", "Operação não disponível!")
    else:
#integral definida
        try:
            novafunção = re.sub("cos", "np.cos", novafunção)
            novafunção = re.sub("sin", "np.sin", novafunção)
            novafunção = re.sub("tan", "np.tan", novafunção)
            novafunção = re.sub("anp.cos", "np.arccos", novafunção)
            novafunção = re.sub("anp.sin", "np.arcsin", novafunção)
            novafunção = re.sub("anp.tan", "np.arctan", novafunção)
            novafunção = re.sub("anp.sinh", "np.arcsinh", novafunção)
            novafunção = re.sub("anp.cosh", "np.arccosh", novafunção)
            novafunção = re.sub("anp.tanh", "np.arctanh", novafunção)
            novafunção = re.sub("ln", "np.log", novafunção)
            novafunção = re.sub("exp", "np.exp",novafunção)
            def f(x):
                return eval(novafunção)  
        
            resultado, erro = spi.quad(f,limI, limS, epsabs = err)

            resultado1 = str(resultado) 
            xLabel.config(text = resultado1)
            w=x1
            y = f(w)
    
            fig.clear()
        
            plt.axhline(0, color='k')
            plt.axvline(0, color='k')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfico de f(x)')
            plt.fill_between(w,y, alpha=.4)
            
        
            fig.canvas.draw_idle()
        except:
            msg.showinfo("Erro", "Operação não disponível!")
    y = f(w)
    
    fig.clear()
        
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de f(x)')
    plt.fill_between(w,y, alpha=.4)
            
        
    fig.canvas.draw_idle()
#----------------------------------------------------------------------------------------------------  

###FUNÇÃO QUE ABRE E LÊ O ARQUIVO

def AbreArquivo():


    try:
        name = filedialog.askopenfilename(initialdir="C:/Desktop/",filetypes =(("Text File", "*.txt"),("All Files","*.*")),
        title = "Choose a file.")

        Arquivo.insert(tk.INSERT, name)

        dadosx, dadosy = np.genfromtxt( name , unpack = True)
        n = (len(dadosx) - 1) #saber quantos intervalos meu gráfico vai ser dividido
        
    
    except:
        msg.showinfo("Erro", "Arquivo não existente, ou tipo não suportado!")
        dados.set('')
    
    def método_trapézio(x1, x2, n, dados_novos):
        y = dados_novos
        h = float(x2 - x1)/n
        soma = y[0] + 2. * np.sum(y[1 : -1]) + y[-1]
        return .5 * h * soma

    integ = método_trapézio(dadosx[1],dadosx[-1],n,dadosy)
    xLabel.config(text = str(integ))

    fig.clear()

    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    plt.title('Gráfico')
    plt.plot(dadosx, dadosy, 'r')
    plt.fill_between(dadosx,dadosy, alpha=.4)
    plt.grid()

    fig.canvas.draw_idle()
    input1.set('')
    input3.set(dadosx[1])
    input4.set(dadosx[-1])    
#função que abre a pagina de ajuda
def ajuda():
    webbrowser.open('https://github.com/lucp770/Projeto_Python_Programa_de_Integracao/blob/master/Tutorial%20da%20Calculadora%20Gr%C3%A1fica%20de%20Integral.pdf') 
       
#----------------------------------------------------------------------------------------------------    

###ENTRADAS DAS VARIÁVEIS/DEFININDO OS VALORES DAS VARIÁVEIS
Arquivo = tk.Entry(Frame4, textvariable = dados, bd =10, borderwidth=0)         # Entrada de dados pela tabela
Arquivo.pack()

Func = tk.Entry(Frame1, textvariable = input1 , bd = 10, borderwidth= 0)        # Entrada do valor função
Func.bind("<Return>", result )
Func.pack()
Lim1 = tk.Entry(Frame1, textvariable = input3 , bd = 10, borderwidth= 0)        # Entrada da variável Lim1
Lim1.pack()
Lim2 = tk.Entry(Frame1, textvariable = input4 , bd = 10,borderwidth= 0)         # Entrada da variável Lim2
Lim2.pack()
Error = tk.Entry(Frame1, textvariable = input5 , bd = 10,borderwidth= 0)        # Entrada da variável Error
Error.pack()
a=0.001
input5.set('')
Error.insert(tk.INSERT, a)

###BOTOẼS

Bu1f1 = tk.Button(Frame1, text = 'Calcular', command = result, fg = 'black' ,bg = 'white') # Botão para calcular, fica na região de inserir a função (Frame1)
Bu1f1.pack()

Bu2f1 = tk.Button(Frame1, text = 'Ajuda',fg = 'black',bg = 'white', command = ajuda)      # Botão de Ajuda, abre o browser com um manual de como usar o programa   
Bu2f1.pack() 

Bu1f4 = tk.Button(Frame4, text = 'Pesquisar', command = AbreArquivo, bg = 'white' , fg = 'black' )   # Botão que abre uma aba para o usuário abrir o arquivo que deseja pedir para a calculadora ler.
Bu1f4.pack()


###POSIÇÃO DO FRAME1 E DE TUDO DENTRO DO FRAME1
	## Usando 'place' nos temos as coordenadas de cada 'widget' da nossa interface.  
  
Frame1.place(anchor = 'nw')                      # Posição do Frame 1 
text1f1.place(relx = .0, rely = .15)             # Posição de Título da região/frame
text4f1.place(relx = .030, rely = .36)           # Legenda do início do domínio
text5f1.place(relx = .020, rely = .46)           # Legenda do final do domínio
text2f1.place(relx = .55, rely =.36)             # Legenda da função
text3f1.place(relx = .55, rely =.46)             # Legenda do erro 
text6f1.place(relx = .575, rely =.27)            # Título de Limites de integração
text7f1.place(relx = .115, rely =.27)            # Título de Função e erro
Lim1.place(relx = .60, rely = .37)               # Caixa de texto para se inserir o limite inicial do domínío              
Lim2.place(relx = .60, rely = .47)               # Caixa de texto para se inserir o limite final do domínío   
Func.place(relx = .1, rely = .37)                # Caixa de texto para se inserir a função   
Error.place(relx = .1, rely = .47)               # Caixa de texto para se inserir o erro
Bu1f1.place(relx = .125, rely = .7)              # Botão de calcular
Bu2f1.place(relx = -.1, rely = -.1)              # Botão de ajuda
C.place(relx = -.10, rely = .0)                  # Marcador de integral indefinida

###POSIÇÃO DO FRAME2 E DE TUDO DENTRO DO FRAME2

Frame2.place(rely=.87)                           # Posição do Frame 2 na Janela; O Frame 2 é a parte dos resultados da integral, onde mostra a primitiva de f(x) => G(x)
text1f2.place(relx=.0,rely=-0.8)                 # Posição do título da caixa de texto
xLabel.place(relx=.19, rely=-0.35)               # Posição da Regição onde G(x) será mostrada

### POSIÇÃO DO FRAME3 E DE TUDO DENTRO DO FRAME 3 

Frame3.place(relx = .5,rely=0.22)                # Posição do Frame 3 (Região onde um gráfico de f(x) será plotado)
text1f3.place(relx = .08, rely = -.07)           # Posição do título da região

###POSIÇÃO DO FRAME4 E DE TUDO DENTRO DO FRAME4

Frame4.place(relx =.5)                           # Posição do Frame 4 (Região onde a tabela será inserida)
text1f4.place(relx=.05 , rely=.3)                # Posição da legenda da caixa de texto de input do arquivo da tabela
Bu1f4.place(relx=.675 , rely =.3)                # Posição do botão buscar arquivo
Arquivo.place(relx=.35 , rely=.4 )               # Caixa de texto para se inserir o diretório do arquivo
text2f4.place(relx = .0, rely =-.5)              # Posição do Título do Frame 4


###FINAL

janela.bind('<Return>')

janela.mainloop()
