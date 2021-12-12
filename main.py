''' Main interface to initiate the game. '''
from picross_classes import Board, Player, ScoreBoard

# Create, fill and generate statistics for the board
board = Board([4,4])
board.fill_board()
board.generate_statistics()
board.show_board()

# Create the player
player = Player("Quan", board)

# Create the scoreboard to store scores afterwards
scoreboard = ScoreBoard()

# Continue the game until the number of filled tiles reach 0
while board.number_of_tiles > 0:
    choice = list(map(int,input().strip().split()))
    if (choice not in player.history) and (0 <= choice[0] < board.width) and (0 <= choice[1] < board.length):
        player.choose(choice)
        board.show_board()
    else:
        print("Please choose another tile.")
        continue

print("\n")
player.show_score()

print("\n")
board.show_answer()

print("\n")
scoreboard.add_score(player)
scoreboard.save_scores()
scoreboard.show_scores()

