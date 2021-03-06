from Board import Board
from Computer import Computer
from Human import Human

N = 3

# use human input to return a bool indicating x/o selection
def get_is_human_x() -> bool:
    while True:
        selection = input('Would you like to play as x? y/n: ')
        if selection in ['y', 'n']:
            break
        print('Invalid entry!')
    return selection == 'y'
            

def play(is_human_x: bool) -> None:
    players = [Human('x'), Computer('o', 'x')] if is_human_x else [Computer('x', 'o'), Human('o')] 
    board = Board(N)
    turn = 0
    print(board)
    while turn < N * N:
        # alternate the turns between the two players
        player = players[turn % 2]
        # take a move according to the player's selection
        board.set(player.get_move(board), player.character)
        print(board)
        if board.has_player_won(player.character):
            print(f'Player {player.character} has won!')
            return
        turn += 1
    
    print('Cat\'s game!')

if __name__ == '__main__':
    print('Welcome to TicTacToe!')
    is_human_x = get_is_human_x()
    play(is_human_x)
