import random
from itertools import product, cycle

# variavel global que vai nos ajudar
# board é um tipo de lista que vamos mexer através dos índices, sendo 9 posições
board = [None] * 9 # criando uma lista com 9 posições
free_positions = list(range(0,9)) # cria uma lista de posições livres
random.shuffle(free_positions) # Embaralha posições livres
player = cycle(["X", "O"])
current_player = next(player)

# função que exibe o tabuleiro
print_board = lambda: print(f"\n{'--' * 5}\n".join(" | ".join(x or " " for x in board[i:i + 3]) for i in range(0, len(board), 3)))

# função que busca e retorna o ganhador
def get_winner():
    combinations = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4], board[2:-1:2]]
    # Cria um gerador que testa todos as condições de vitoria para os dois jogadores
    winner = [value for value, sub_list in product(["X", "O"], combinations) if set(sub_list) == set(value)]
    return "".join(set(winner)) # Retorna 'X', 'O', ou ''
    
def make_move(current_player):
    if current_player == "X":
        print_board()
        inputPosition = int(input("Escolha uma posição de 1 a 9: "))
        #verificar se a posição é válida (de 1 a 9 os quadradinhos) e vazia
        if inputPosition-1 in free_positions: # verifica se a posição selecionada esta na lista de posições livres
            board[inputPosition - 1] = current_player # adiciona um X em uma posição selecionada
            free_positions.remove(inputPosition-1) # remove uma a posição selecionada da lista de posições livres
        else:
            raise IndexError()
    else:
        if free_positions:
            board[free_positions.pop()] = current_player # adiciona um O em uma posição livre no tabuleiro

while not get_winner() and free_positions: # roda o jogo até que aja um ganhador ou não tenha mais posições no taboleiro
    try:
        make_move(current_player)
        current_player = next(player)
    except IndexError:
        print("Posição inválida, tente novamente")
    except ValueError:
        print("Caractere inválido, tente novamente")

print_board()
print(f"O jogador {get_winner()} venceu!" if get_winner() else "O Jogo terminou em empate!")
