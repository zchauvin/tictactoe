from Board import Board
from Human import Human

N = 3

def get_is_human_x() -> bool:
    while True:
        selection = input('Would you like to play as x? y/n: ')
        if selection in ['y', 'n']:
            break
        print('Invalid entry!')
    return selection == 'y'
            

def play(is_human_x: bool) -> None:
    # TODO: select one player to be AI based on is_human_x
    players = [Human('x'), Human('o')]
    board = Board(N)
    lines = board.get_lines()
    turn = 0
    while turn < N * N:
        player = players[turn % 2]
        board.set(player.get_move(board), player.character)
        if board.has_player_won(lines, player.character):
            print(f'Player {player.character} has won!')
            return
        turn += 1
    
    print('Cat\'s game!')

if __name__ == '__main__':
    print('Welcome to TicTacToe!')
    is_human_x = get_is_human_x()
    play(is_human_x)
