import random 

# variavel global que vai nos ajudar
# board é um tipo de lista que vamos mexer através dos índices, sendo 9 posições
board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

currentPlayer = "X"
winner = None #sem valor pra começar
gameIsGoing = True

#função do quadro, os índices serão adicionados de acordo com o player
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--" * 5)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--" * 5)
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)
    
def playerTurn(board):
    inputPosition = int(input("Escolha uma posição de 1 a 9: "))
    #verificar se a posição é válida (de 1 a 9 os quadradinhos) e vazia
    if inputPosition >= 1 and inputPosition <= 9 and board[inputPosition - 1] == "-":
        board[inputPosition - 1] = currentPlayer
    else:
        print("Posição inválida, tente novamente") 

    
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1]!= "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkEmpate(board):
    global gameIsGoing
    if "-" not in board:
        gameIsGoing = False
        print("Empate!")
        
def trocarJogador():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWinner():
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"O jogador {winner} venceu!")
        return True
    
def bot(board):
    while currentPlayer == "O":
        botPosition = random.randint(0, 8)
        if board[botPosition] == "-":
            board[botPosition] = "O"
            trocarJogador()

while gameIsGoing:
    printBoard(board)
    playerTurn(board)
    checkWinner()
    checkEmpate(board)
    trocarJogador()
    bot(board)
    checkWinner()
    if checkEmpate(board) or checkWinner():
        gameIsGoing = False