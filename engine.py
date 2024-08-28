import copy
from gui_window import *
from copy import deepcopy
import time
import random
EASY_1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
EASY_2 = [
    [9, 0, 0, 0, 8, 3, 2, 5, 0],
    [4, 0, 0, 9, 0, 5, 0, 0, 0],
    [0, 8, 5, 0, 2, 0, 9, 0, 3],
    [3, 0, 0, 5, 0, 8, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [1, 0, 2, 7, 6, 4, 5, 3, 8],
    [0, 6, 0, 0, 7, 0, 0, 0, 0],
    [5, 1, 8, 0, 0, 9, 7, 0, 6],
    [0, 3, 0, 0, 0, 0, 8, 9, 1]
]
EASY_3 = [
    [5, 6, 8, 0, 4, 0, 0, 0, 3],
    [0, 0, 2, 0, 9, 0, 0, 0, 7],
    [0, 9, 7, 8, 6, 0, 0, 0, 0],
    [6, 0, 0, 3, 1, 0, 4, 0, 9],
    [0, 3, 0, 0, 5, 0, 0, 6, 2],
    [0, 1, 9, 6, 0, 0, 5, 0, 8],
    [0, 0, 3, 0, 0, 6, 8, 0, 1],
    [0, 5, 1, 0, 0, 0, 0, 2, 0],
    [9, 0, 0, 7, 0, 0, 3, 4, 5]
]
MEDIUM_1 = [
    [0, 0, 4, 3, 0, 0, 0, 0, 2],
    [3, 0, 0, 0, 2, 9, 0, 1, 5],
    [0, 0, 9, 5, 6, 1, 0, 3, 4],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [7, 5, 1, 0, 3, 0, 9, 0, 0],
    [0, 0, 3, 0, 0, 5, 0, 2, 0],
    [9, 4, 0, 6, 0, 3, 2, 0, 0],
    [0, 0, 6, 9, 8, 4, 0, 0, 0],
    [1, 0, 8, 2, 5, 0, 0, 6, 9]]
MEDIUM_2 = [
    [8, 2, 0, 0, 1, 0, 0, 0, 0],
    [0, 5, 1, 0, 0, 0, 0, 8, 6],
    [0, 0, 0, 0, 0, 9, 2, 0, 0],
    [0, 0, 6, 7, 9, 0, 0, 0, 0],
    [7, 8, 0, 1, 4, 0, 6, 9, 3],
    [5, 4, 9, 2, 3, 0, 1, 0, 8],
    [0, 0, 5, 0, 8, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 1, 0, 2, 9],
    [0, 0, 0, 0, 6, 4, 8, 0, 7]]
MEDIUM_3 = [
    [0, 1, 2, 0, 0, 0, 6, 5, 0],
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 1, 7, 0, 9],
    [4, 0, 1, 0, 5, 6, 8, 2, 7],
    [6, 0, 7, 2, 0, 0, 0, 0, 0],
    [9, 0, 8, 7, 1, 3, 5, 4, 0],
    [0, 0, 0, 4, 3, 0, 2, 0, 5],
    [0, 0, 4, 0, 9, 5, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 9, 0]]
HARD_1 = [
    [0, 0, 0, 0, 6, 2, 0, 0, 8],
    [0, 0, 3, 0, 8, 5, 0, 0, 0],
    [9, 2, 0, 0, 7, 0, 0, 0, 1],
    [1, 0, 0, 4, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 0, 4, 7, 0],
    [2, 0, 0, 0, 5, 0, 0, 0, 0],
    [6, 0, 2, 5, 0, 0, 0, 9, 0],
    [0, 3, 0, 0, 0, 0, 0, 2, 7],
    [0, 0, 0, 8, 2, 7, 1, 6, 0]]
HARD_2 = [
    [9, 0, 0, 0, 0, 0, 5, 0, 3],
    [8, 0, 0, 0, 4, 9, 0, 0, 7],
    [0, 7, 0, 2, 5, 6, 1, 0, 0],
    [0, 0, 0, 4, 2, 7, 0, 1, 9],
    [0, 0, 2, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 3, 4, 0, 2],
    [0, 8, 0, 0, 3, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 5],
    [0, 0, 4, 0, 0, 0, 2, 0, 0]]
HARD_3 = [
    [0, 0, 0, 1, 4, 5, 0, 0, 0],
    [0, 1, 5, 0, 7, 0, 0, 0, 0],
    [0, 3, 0, 2, 9, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 4],
    [4, 0, 9, 0, 8, 0, 0, 0, 7],
    [0, 0, 7, 4, 5, 0, 6, 0, 3],
    [5, 7, 0, 0, 0, 0, 1, 0, 6],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 7, 0, 3, 2]]
EASY = [EASY_1,EASY_2,EASY_3]
MEDIUM = [MEDIUM_1,MEDIUM_2,MEDIUM_3]
HARD = [HARD_1,HARD_2,HARD_3]
class State:
    def __init__(self):
        self.board = copy.deepcopy(EASY_1)
        self.starting_position = copy.deepcopy(EASY_1)
        self.solve_iteration = 0
        self.current_game = 1
        self.message = ""

    def delete_number(self, row, col):
        if self.starting_position[row][col] == 0:
            self.board[row][col] = 0
        else:
            self.message = "You can't delete part of the question"
            return False
        return True

    def update(self, number, place):  # update(1-9,(row,col))
        if valid(self.board, number, place):
            row = place[0]
            col = place[1]
            if self.starting_position[row][col] == 0:
                self.board[row][col] = number
            else:
                self.message = "You can't change part of the question"
        else:
            self.message = "Invalid placement of number"
            return False
        self.message = ""
        return True

    def solve(self, screen):
        self.solve_iteration += 1

        draw_numbers(screen, self)
        p.display.flip()
        if self.solve_iteration <= 100:
            time.sleep(0.05)
        elif self.solve_iteration <= 500:
            time.sleep(0.01)
        else:
            time.sleep(0.001)
        find = find_empty(self.board)
        if not find:
            self.message = ""
            return True
        else:
            row, col = find
        for i in range(1, 10):
            if valid(self.board, i, (row, col)):
                self.board[row][col] = i
                if State.solve(self, screen):
                    return True
                self.board[row][col] = 0
                wipe_number(screen, row, col)
        return False


    def new_game(self,difficulty):
        number = random.randint(0, 2)
        while number == self.current_game:
            number = random.randint(0, 2)
        if difficulty == "easy":
            self.board = copy.deepcopy(EASY[number])
            self.starting_position = copy.deepcopy(EASY[number])
            self.current_game = number
        elif difficulty == "medium":
            number = random.randint(0, 2)
            self.board = copy.deepcopy(MEDIUM[number])
            self.starting_position = copy.deepcopy(MEDIUM[number])
            self.current_game = number
        elif difficulty == "hard":
            number = random.randint(0, 2)
            self.board = copy.deepcopy(HARD[number])
            self.starting_position = copy.deepcopy(HARD[number])
            self.current_game = number





def solve(board):
    print_board(board)
    print("******************************")
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


def valid(board, number, position):  # position: (i,j) = (y, x)
    if number == 0:
        return True
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    for j in range(len(board)):
        if board[j][position[1]] == number and position[0] != j:
            return False
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # y, x
    return False


def main():
    pass


if __name__ == "__main__":
    main()
