'''alunos: Guilherme Ramos, Ryan Alves e Victoria Moraes

Descrição do Trabalho Prático
Jéssica Renata Nogueira (Passos)

9 de abr. (editado: 1 de jul.)
valor: 2,50 pt
Data de entrega: 11 de ago., 23:59
Primeiro Trabalho Prático de Teor1a da Computação: 
Funções Recursivas Primitivas 


**dois ou tres jogadores
**numero total de partidas deve ser igual a 5
escolher forma de pontuar perguntas 
**sortear perguntas 
**ter as perguntas com valores aleatorios
**mostrar pontuaçao dos jogadores ordenada a cada rodada
**ranking final


1) Neste trabalho deverá ser implementado um quiz de perguntas matemáticas, que pode ser jogado por dois ou três jogadores.
 O número de jogadores deve ser solicitado ao usuário e, em seguida, deve ser informado que o número total de partidas por 
 jogador é 5. A forma de pontuar cada pergunta respondida de forma correta fica a critério de cada grupo. O jogo deve 
 realizar o sorteio de cada pergunta, que deve conter as seguintes opções de operações matemáticas: 
soma (o valor de x e y deve ser definido de forma aleatória) 
⁠subtração (o valor de x e y deve ser definido de forma aleatória) 
⁠multiplicação (o valor de x e y deve ser definido de forma aleatória)
⁠elevado (o valor de x e y deve ser definido de forma aleatória) 
⁠fatorial (o valor de x deve ser definido de forma aleatória) 
divisão chão (o valor de x e y deve ser definido de forma aleatória)⁠ 
divisão teto(o valor de x e y deve ser definido de forma aleatória)⁠ 
percentual (o valor de x e y deve ser definido de forma aleatória, sendo que y deve estar entre 0 e 100) 
resto da divisão (o valor de x e y deve ser definido de forma aleatória)⁠ 
A cada rodada deve ser informada a pontuação máxima e mínima dos jogadores participantes e, ao final, deve ser 
apresentado o ranking.

É obrigatório definir as seguintes funções de forma recursiva primitiva: soma, subtração, multiplicação, elevado, 
fatorial, divisão chão, divisão teto, percentual, resto da divisão, máximo, mínimo, igual e diferente (caso sejam usadas
 para comparação). Sempre que possível, utilizem outras funções que estejam definidas através de recursão. 

2) Por meio de funções recursivas primitivas, defina as funções máximo, mínimo e percentual, utilizando composição de 
funções e recursão primitiva. Apresente um exemplo de sua aplicação. Essa resposta pode ser feita na folha e digitalizada
 ou já digitada. 

Observação: 
1) o trabalho deve ser realizado em duplas e em linguagem C ou Python 
2) haverá uma apresentação breve do trabalho, que ocorrerá no dia 29/04, que também é a data de entrega 
3) entregas fora do prazo não serão aceitas'''

import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Funções Recursivas
def soma(x, y):
    if y == 0:
        return x
    return soma(x + 1, y - 1)

def subtracao(x, y):
    if y == 0:
        return x
    return subtracao(x - 1, y - 1)

def multiplicacao(x, y):
    if y == 0:
        return 0
    else:
        return soma(x, multiplicacao(x, y - 1))

def elevado(x, y):
    if y == 0:
        return 1
    return multiplicacao(x, elevado(x, y - 1))

def fatorial(x):
    if x == 0 or x == 1:
        return 1
    return multiplicacao(x, fatorial(x - 1))

def divisao_chao(x, y):
    if y == 0:
        raise ValueError("Divisão por zero")
    if x < y:
        return 0
    return soma(1, divisao_chao(subtracao(x, y), y))

def divisao_teto(x, y):
    if y == 0:
        raise ValueError("Divisão por zero")
    resultado = divisao_chao(x, y)
    if multiplicacao(resultado, y) == x:
        return resultado
    return soma(resultado, 1)

def percentual(x, y):
    if y == 0:
        raise ValueError("Divisor não pode ser zero")
    return divisao_chao(multiplicacao(x, y), 100)

def resto_divisao(x, y):
    if y == 0:
        raise ValueError("Divisor não pode ser zero")
    return subtracao(x, multiplicacao(divisao_chao(x, y), y))
# Função para encontrar o máximo de dois números
def maximo(x, y):
    if x == y:
        return x
    elif x > y:
        return x
    else:
        return y

# Função para encontrar o mínimo de dois números
def minimo(x, y):
    if x == y:
        return x
    elif x < y:
        return x
    else:
        return y

# Função para encontrar o máximo em uma lista de números usando recursão primitiva
def maximo_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return maximo(lista[0], maximo_lista(lista[1:]))

# Função para encontrar o mínimo em uma lista de números usando recursão primitiva
def minimo_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return minimo(lista[0], minimo_lista(lista[1:]))
    
# Função para gerar perguntas
def gerar_pergunta():
    operacoes = [
        ("soma", soma, "fácil"),
        ("subtração", subtracao, "fácil"),
        ("multiplicação", multiplicacao, "médio"),
        ("elevação", elevado, "difícil"),
        ("fatorial", fatorial, "difícil"),
        ("divisão chão", divisao_chao, "médio"),
        ("divisão teto", divisao_teto, "médio"),
        ("percentual", percentual, "médio"),
        ("resto da divisão", resto_divisao, "fácil")
    ]

    operacao, funcao, dificuldade = random.choice(operacoes)
    
    if dificuldade == "fácil":
        pontos = 5
    elif dificuldade == "médio":
        pontos = 10
    else:  # "difícil"
        pontos = 15

    if operacao == "fatorial":
        x = random.randint(1, 6)
        resposta_correta = funcao(x)
        return f"{operacao} de {x}", resposta_correta, pontos
    
    elif operacao == "percentual":
        x = random.randint(1, 10)
        y = random.randint(1, 100)
        resposta_correta = float(funcao(x, y))
        return f"{operacao} de {x} e {y}", resposta_correta, pontos
    
    elif operacao == "elevação":
        x = random.randint(1, 5)
        y = random.randint(1, 4)
        resposta_correta = funcao(x, y)
        return f"{operacao} de {x} e {y}", resposta_correta, pontos
    
    elif operacao == "multiplicação":
        x = random.randint(1, 30)
        y = random.randint(1, 30)
        resposta_correta = funcao(x, y)
        return f"{operacao} de {x} e {y}", resposta_correta, pontos
    
    else:
        x = random.randint(1, 100)
        y = random.randint(1, x)
        resposta_correta = funcao(x, y)
        return f"{operacao} de {x} e {y}", resposta_correta, pontos

# Classe principal do jogo
class QuizGame:
    def __init__(self, root):
        # Inicializar pygame para tocar música
        pygame.mixer.init()
        pygame.mixer.music.load("quiz-game-music-loop-bpm-90-61070.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)  # -1 faz com que a música toque em loop
        # Carregar som de acerto
        self.som_acerto = pygame.mixer.Sound("correct-6033.mp3")
        self.som_erro = pygame.mixer.Sound("error-126627.mp3")
        
        self.root = root
        self.root.title("Quiz Matemático")
        self.root.configure(bg='#2E2E2E')  # Fundo da janela principal
        self.root.attributes('-fullscreen', True)  # Modo tela cheia
        
        self.jogadores = []
        self.ranking = {}
        self.rodada = 0
        self.total_rodadas = 5
        self.jogador_atual_index = 0
        
        # Configuração do Frame de Menu
        self.menu_frame = tk.Frame(self.root, bg='#2E2E2E')
        self.menu_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label_title = tk.Label(self.menu_frame, text="Bem-vindo ao Quiz Matemático!", font=("Arial", 30), fg='white', bg='#2E2E2E')
        self.label_title.pack(pady=20)
        
        self.label_instructions = tk.Label(self.menu_frame, text="Escolha o número de jogadores:", font=("Arial", 20), fg='white', bg='#2E2E2E')
        self.label_instructions.pack(pady=10)
        
        self.button_two_players = tk.Button(self.menu_frame, text="Dois jogadores", command=lambda: self.iniciar_jogo(2), bg='#3A3A3A', fg='white', font=("Arial", 18))
        self.button_two_players.pack(pady=5)
        
        self.button_three_players = tk.Button(self.menu_frame, text="Três jogadores", command=lambda: self.iniciar_jogo(3), bg='#3A3A3A', fg='white', font=("Arial", 18))
        self.button_three_players.pack(pady=5)
        
        self.button_exit = tk.Button(self.menu_frame, text="Sair", command=root.quit, bg='#3A3A3A', fg='white', font=("Arial", 18))
        self.button_exit.pack(pady=20)

    def iniciar_jogo(self, num_jogadores):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load("news-flash-ticking-power-221763.mp3")
         # Definir o volume da música (ex: 0.2 para 20% do volume)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)  # -1 faz com que a música toque em loop
        
        self.jogadores = [f"Jogador {i+1}" for i in range(num_jogadores)]
        self.ranking = {jogador: {"pontuacao": 0, "erros": 0, "acertos": 0} for jogador in self.jogadores}
        self.rodada = 0
        self.jogador_atual_index = 0
        self.menu_frame.place_forget()
        
        # Criação da nova janela para o quiz
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Quiz em Andamento")
        self.quiz_window.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.quiz_window.configure(bg='#2E2E2E')
        self.quiz_window.attributes('-fullscreen', True)  # Modo tela cheia

        # Configuração do Frame do Quiz
        self.quiz_frame = tk.Frame(self.quiz_window, bg='#2E2E2E', width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Adicionar botão Sair
        self.button_exit = tk.Button(self.quiz_frame, text="Sair", command=self.sair_do_jogo, bg='#3A3A3A', fg='white', font=("Arial", 18))
        self.button_exit.pack(pady=10, side=tk.BOTTOM)
        
        self.contagem_regressiva()

    def contagem_regressiva(self):
        self.label_contagem = tk.Label(self.quiz_frame, text="A partida iniciará em:", font=("Arial", 30), fg='white', bg='#2E2E2E')
        self.label_contagem.pack(pady=20)

        self.contador = 5
        self.label_tempo = tk.Label(self.quiz_frame, text=str(self.contador), font=("Arial", 80), fg='white', bg='#2E2E2E')
        self.label_tempo.pack(pady=20)

        self.update_contagem()

    def update_contagem(self):
        if self.contador > 0:
            self.contador -= 1
            self.label_tempo.config(text=str(self.contador))
            self.root.after(1000, self.update_contagem)
        else:
            self.label_tempo.destroy()
            self.label_contagem.config(text="Prepare-se!")
            self.nova_rodada()

    def sair_do_jogo(self):
        if messagebox.askyesno("Sair", "Você tem certeza que deseja sair do quiz?"):
            # Fechar a janela do quiz
            self.quiz_window.destroy()
            
            # Redefinir o estado do jogo
            self.rodada = 0
            self.jogador_atual_index = 0
            self.ranking.clear()
            
            # Mostrar o frame do menu
            self.menu_frame.place(relx=0.5, rely=0.5, anchor='center')

    def limpar_tela(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()


    def nova_rodada(self):
        # Apenas incrementa a rodada se todos os jogadores tiverem jogado
        if self.jogador_atual_index == 0:
            self.rodada += 1
            
        if self.rodada > self.total_rodadas:
            self.exibir_ranking_final()
            return

        self.limpar_tela()
        
        self.label_rodada = tk.Label(self.quiz_frame, text=f"Rodada {self.rodada} de {self.total_rodadas}", font=("Arial", 24), fg='white', bg='#2E2E2E')
        self.label_rodada.pack(pady=10)
        self.jogador_atual = self.jogadores[self.jogador_atual_index]

        self.label_jogador = tk.Label(self.quiz_frame, text=f"Vez de {self.jogador_atual}", font=("Arial", 28), fg='white', bg='#2E2E2E')
        self.label_jogador.pack(pady=10)

        self.pergunta, self.resposta_correta, self.pontos = gerar_pergunta()
        self.label_pergunta = tk.Label(self.quiz_frame, text=self.pergunta, font=("Arial", 30), fg='#F7DC6F', bg='#2E2E2E')
        self.label_pergunta.pack(pady=20)
        
        self.entry_resposta = tk.Entry(self.quiz_frame, font=("Arial", 24), fg='black', bg='white')
        self.entry_resposta.pack(pady=10)
        self.entry_resposta.bind('<Return>', self.verificar_resposta)  # Bind da tecla Enter para submissão da resposta
        self.entry_resposta.focus_set()

    def proxima_vez(self):
        # Avança para o próximo jogador
        self.jogador_atual_index += 1
        
        if self.jogador_atual_index >= len(self.jogadores):
            self.jogador_atual_index = 0
            self.exibir_ranking_parcial()
        else:
            self.nova_rodada()

    def verificar_resposta(self, event):
        resposta = self.entry_resposta.get()
        try:
            resposta = float(resposta)  # Convertendo a resposta para float
        except ValueError:
            self.label_feedback = tk.Label(self.quiz_frame, text="Por favor, insira um número válido.", font=("Arial", 20), fg='red', bg='#2E2E2E')
            self.label_feedback.pack(pady=10)
            return

        # Arredondando a resposta correta para duas casas decimais
        resposta_correta_arredondada = round(self.resposta_correta, 2)
        resposta_arredondada = round(resposta, 2)

        if resposta_arredondada == resposta_correta_arredondada:
            self.som_acerto.play()  # Toca o som de acerto
            self.ranking[self.jogador_atual]["pontuacao"] += self.pontos
            self.ranking[self.jogador_atual]["acertos"] += 1
            self.label_feedback = tk.Label(self.quiz_frame, text=f"Correto! Você ganhou {self.pontos} pontos.", font=("Arial", 20), fg='green', bg='#2E2E2E')
        else:
            self.som_erro.play()
            self.ranking[self.jogador_atual]["erros"] += 1
            self.label_feedback = tk.Label(self.quiz_frame, text=f"Incorreto! A resposta certa era {self.resposta_correta:}", font=("Arial", 20), fg='red', bg='#2E2E2E')
        self.label_feedback.pack(pady=10)

        self.root.after(2000, self.proxima_vez)

    
    def exibir_ranking_parcial(self):
        self.limpar_tela()

        self.label_ranking = tk.Label(self.quiz_frame, text=f"Ranking após a rodada {self.rodada}", font=("Arial", 26), fg='white', bg='#2E2E2E')
        self.label_ranking.pack(pady=10)
        
        # Ordenar o ranking com base na pontuação em ordem decrescente
        ranking_ordenado = sorted(self.ranking.items(), key=lambda item: item[1]["pontuacao"], reverse=True)
        
        for jogador, dados in ranking_ordenado:
            stats = f"{jogador}: {dados['pontuacao']} pontos, {dados['acertos']} acertos, {dados['erros']} erros"
            label_stats = tk.Label(self.quiz_frame, text=stats, font=("Arial", 20), fg='#F7DC6F', bg='#2E2E2E')
            label_stats.pack(pady=5)

        self.root.after(3000, self.nova_rodada)

    def exibir_ranking_final(self):
        self.limpar_tela()

        self.label_ranking = tk.Label(self.quiz_frame, text="Ranking Final", font=("Arial", 26), fg='white', bg='#2E2E2E')
        self.label_ranking.pack(pady=10)

        # Ordenar o ranking com base na pontuação em ordem decrescente
        ranking_ordenado = sorted(self.ranking.items(), key=lambda item: item[1]["pontuacao"], reverse=True)
        
        for jogador, dados in ranking_ordenado:
            total_perguntas = dados['acertos'] + dados['erros']
            porcentagem_erros = (dados['erros'] / total_perguntas) * 100 if total_perguntas > 0 else 0
            stats = f"{jogador}: {dados['pontuacao']} pontos, {dados['acertos']} acertos, {dados['erros']} erros, {porcentagem_erros:.2f}% de erros"
            label_stats = tk.Label(self.quiz_frame, text=stats, font=("Arial", 20), fg='#F7DC6F', bg='#2E2E2E')
            label_stats.pack(pady=5)

        self.button_sair = tk.Button(self.quiz_frame, text="Sair", command=self.voltar_ao_menu, bg='#3A3A3A', fg='white', font=("Arial", 18))
        self.button_sair.pack(pady=20)

    def voltar_ao_menu(self):
        self.quiz_frame.place_forget()
        # Fechar a janela do quiz
        self.quiz_window.destroy()
        # Redefinir o estado do jogo
        self.rodada = 0
        self.jogador_atual_index = 0
        self.ranking.clear()
        pygame.mixer.music.load("quiz-game-music-loop-bpm-90-61070.mp3")
        pygame.mixer.music.play(-1)  # -1 faz com que a música toque em loop
            
        self.menu_frame.place(relx=0.5, rely=0.5, anchor='center')

root = tk.Tk()
game = QuizGame(root)
root.mainloop()