import math
from random import randint


class MovieTheater:

    def __init__(self, rows=10, cols=20):
        self.assignments = {}
        self.seats = [['.'] * cols for _ in range(rows)]

    def inBounds(self, i, j):
        return 0 <= i < len(self.seats) and 0 <= j < len(self.seats[0])

    # Return the amount of buffer that would be created with adding seat reservations
    # Return math.inf if the seat reservation can't fit there

    def count_buffer(self, i, j, r_size):
        count = 0
        # left
        for k in range(1, 4):
            if self.inBounds(i, j - k):
                if self.seats[i][j-k] == '.':
                    count += 1
                elif self.seats[i][j-k] != '*':
                    return math.inf

        # top
        for k in range(r_size):
            if self.inBounds(i - 1, j + k):
                if self.seats[i - 1][j + k] == '.':
                    count += 1
                elif self.seats[i - 1][j + k] != '*':
                    return math.inf
        # bot
        for k in range(r_size):
            if self.inBounds(i + 1, j + k):
                if self.seats[i + 1][j + k] == '.':
                    count += 1
                elif self.seats[i + 1][j + k] != '*':
                    return math.inf
        # right
        for k in range(3):
            if self.inBounds(i, j + r_size + k):
                if self.seats[i][j+r_size + k] == '.':
                    count += 1
                elif self.seats[i][j+r_size + k] != '*':
                    return math.inf
        return count

    # marks the 2d array where the seats are taken with the token and marks buffers

    def reserve_seats(self, seats, token):
        i, j = seats[0]
        r_size = len(seats)
        # left
        for k in range(1, 4):
            if self.inBounds(i, j - k):
                self.seats[i][j-k] = '*'
        # top
        for k in range(r_size):
            if self.inBounds(i - 1, j + k):
                self.seats[i - 1][j + k] = '*'
        # bot
        for k in range(r_size):
            if self.inBounds(i + 1, j + k):
                self.seats[i + 1][j + k] = '*'
        # right
        for k in range(3):
            if self.inBounds(i, j + r_size + k):
                self.seats[i][j+r_size + k] = '*'

        # fill in the taken seats with the token
        for seat in seats:
            x, y = seat
            self.seats[x][y] = token

    # Assigns reservations so that they create the least amount of buffer space

    def greedy_assignment(self, token, num_people):
        r_size = num_people
        min_num_buffer = math.inf
        br, bc = -1, -1
        for i in range(len(self.seats)):
            for j in range(len(self.seats[0]) - r_size + 1):
                if self.seats[i][j] != '.':
                    continue
                num_buffer = self.count_buffer(i, j, r_size)
                if num_buffer < min_num_buffer:
                    br, bc = i, j
                    min_num_buffer = num_buffer

        if br == -1 and bc == -1:
            self.assignments[token] = [(-1, -1)]
            return
        assignment = [(br, bc + x) for x in range(r_size)]
        # print(assignment)
        self.reserve_seats(assignment, token)
        self.assignments[token] = assignment
        return


    # Returns the string of the seat assignments in the requested format
    def output(self):
        s = []
        for key, assignment in self.assignments.items():
            if assignment[0][0] == -1:
                s.append(key + " cannot fulfill reservation")
            else:
                s.append(key +" "+ ",".join([chr(65 + x) + str(y + 1) for x, y in assignment]))
        return s

    # Returs a string representation of the movie theater
    def __str__(self):
        s = "\t[[     SCREEN     ]]\n\t--------------------\n"

        for i, row in enumerate(self.seats):
            s += chr(65+i) + "\t" + "".join(row) + "\n"
        s += "\t1       ...      20"
        return s