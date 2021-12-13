''' This is where all the classes and functions needed for the game are implemented '''
import random

class Board:
    ''' Initiate the playing board. '''

    def __init__(self, size=[4, 4]):
        self.size = size
        self.width = self.size[0]
        self.length = self.size[1]
        self.empty_board = self.create_empty_board()
        self.answer = self.create_empty_board()
        self.number_of_tiles = 0

    def create_empty_board(self):
        board = []
        for row in range(self.length):
            board.append([0] * self.width)
        return board

    def fill_board(self):
        for row in self.answer:
            tiles_each_row = random.randint(0, self.width)
            tile_indexes = random.sample(range(0, self.width), tiles_each_row)

            for index in tile_indexes:
                row[index] = 1

            self.number_of_tiles += tiles_each_row

    def generate_statistics(self):
        row_stats = []
        column_stats = [0] * self.width

        for row in self.answer:
            row_stats.append(row.count(1))
            for i in range(self.width):
                if row[i] == 1:
                    column_stats[i] += 1

        return [row_stats, column_stats]

    def show_board(self):
        row_stats = self.generate_statistics()[0]
        column_stats = self.generate_statistics()[1]
        print(column_stats)
        for row_number in range(self.length):
            print(self.empty_board[row_number] + [row_stats[row_number]])

    def show_answer(self):
        for row in self.answer:
            print(row)


class Player:
    ''' Initiate a player. '''
    def __init__(self, name, playing_board):
        self.name = name
        self.playing_board = playing_board #put empty board here
        self.score = 0
        self.history = []

    def choose(self, choice):
        self.history.append(choice)
        x = choice[0] - 1
        y = choice[1] - 1
        if self.playing_board.answer[y][x] == 1:
            self.playing_board.empty_board[y][x] = "X"
            self.score += 1
            self.playing_board.number_of_tiles -= 1
        else:
            self.playing_board.empty_board[y][x] = "-"
            self.score -= 1

    def show_score(self):
        print("Your score is: " + str(self.score))


class ScoreBoard:
    ''' Initiate the scoreboard. '''
    def __init__(self):
        self.high_scores = {}

    def add_score(self, player):
        self.high_scores[player] = player.score

    def save_scores(self):
        f = open("scoreboard.txt", "a")
        for player in self.high_scores:
            f.write("{} - {}".format(player.name, self.high_scores[player]))

    def show_scores(self):
        f = open("scoreboard.txt", "r")
        print(f.read())

