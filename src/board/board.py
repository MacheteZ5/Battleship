from src.ship.ship import Ship
from src.enumeration.enumeration import PlayerType, Orientation
import random

class Board():
    def __init__(self):
        self.__destroyer = Ship("D", 2)
        self.__cruiser = Ship("C", 3)
        self.__submarine = Ship("S", 3)
        self.__battleship = Ship("B", 4)
        self.__carrier = Ship("C", 5)
        self.__ships_board = [['v' for column in range(10)] for row in range(10)]
        self.__attack_board = [[' ' for column in range(10)] for row in range(10)]

    @property
    def ships_board(self):
        for row in self.__ships_board:
            print(row)

    @property
    def attack_board(self):
        for row in self.__attack_board:
            print(row)

    def placeShips(self, player_type : int):
        print("---------------------------------------------------------", end="\n\n")
        player = "Player" if (player_type == PlayerType.player.value) else "CPU"
        print(f"{player}'s turn to select his ships position.", end="\n\n")
        self.__placeShips(self.__destroyer.ship_registry, self.__destroyer.size, player_type)
        self.__placeShips(self.__cruiser.ship_registry, self.__cruiser.size, player_type)
        self.__placeShips(self.__submarine.ship_registry, self.__submarine.size, player_type)
        self.__placeShips(self.__battleship.ship_registry, self.__battleship.size, player_type)
        self.__placeShips(self.__carrier.ship_registry, self.__carrier.size, player_type)

    def __placeShips(self, ship_registry : str, ship_size : int, player_type : int):
        print("---------------------------------------------------------", end="\n\n")
        while(True):
            print(f"The ship {ship_registry} is of size: {ship_size}")
            try:     
                row = int(input("Enter the ship's starting row: ")) if (player_type == PlayerType.player.value) else random.randint(0,9)
                column = int(input("Enter the ship's starting column: ")) if (player_type == PlayerType.player.value) else random.randint(0,9)
                orientation = int(input("Enter the ship's orientation (1. Horizontal | 2. Vertical): ")) if (player_type == PlayerType.player.value) else random.randint(1,2)
                if(self.__validatePositioningParameters(ship_registry, row, column, orientation, ship_size, False)):
                    self.__validatePositioningParameters(ship_registry, row, column, orientation, ship_size, True)
                    if (player_type == PlayerType.player.value): self.ships_board
                    break
                else:
                    print("The values ​​entered are invalid for one of the following reasons: ")
                    print("-> A ship is in a position that obstructs the selected values.")
                    print("-> The data entered exceeds the size of the dashboard.")
                    print("Double-check your dashboard and select other values.", end="\n\n")
            except ValueError as e:
                print("Error: The value entered is not a valid option.")
                print(f"An error has occurred: {e}")
            except IndexError as e:
                print("The values ​​entered are not valid for the matrix size.")
                print(f"An error has occurred: {e}")

    def __validatePositioningParameters(self, ship_registry : str, row : int, column : int, orientation : int, ship_size : int, validate_change : bool) -> bool:
        while(ship_size > 0):
            if(self.__ships_board[row][column] == "v"):
                self.__ships_board[row][column] = f"{ship_registry}" if(validate_change) else self.__ships_board[row][column]
                column = (column + 1) if (orientation == Orientation.horizontal.value) else (column)
                row = (row + 1) if (orientation == Orientation.vertical.value) else (row)
                ship_size -= 1
            else:
                print("The selected row, column, and orientation are not valid.", end="\n\n")
                break
        return True if(ship_size == 0) else False
    
    def positionAttack(self, player_type : int) -> list :
        attack = []
        while(True):
            try:
                row = int(input("Enter the row where you want to launch the attack: ")) if (player_type == PlayerType.player.value) else random.randint(0,9)
                column = int(input("Enter the column where you want to launch the attack: ")) if (player_type == PlayerType.player.value) else random.randint(0,9)
                if((row > -1 and row < 10) and (column > -1 and column < 10)):
                    if(self.__attack_board[row][column] == " "):
                        attack.append(row)
                        attack.append(column)
                        break
                    else:
                        print("The position you selected has already been attacked. Please select another position.")
                else:
                    print("The position you selected is not a valid position for a 10 x 10 board.")
            except ValueError as e:
                print("Error: The entered value is not a valid option")
                print(f"An error has occurred: {e}")
        return attack

    def markAttack(self, row : str, column : str, result_sign : str):
        self.__attack_board[row][column] = result_sign

    def hasLiveShips(self) -> bool:
        return True if (
            self.__destroyer.isAlive and 
            self.__cruiser.isAlive and 
            self.__submarine.isAlive and 
            self.__battleship.isAlive and 
            self.__carrier.isAlive
            ) else False
    
    def receiveEnemyAttack(self, attack : list) -> str :
        attack_result = self.__receiveEnemyAttack(attack)
        result_sign = attack_result[0]
        if(result_sign != "x"):
            ship_attacked = attack_result[1]
            if (ship_attacked == self.__destroyer.ship_registry):
                self.__destroyer.receiveAttack()
            elif (ship_attacked == self.__cruiser.ship_registry):
                self.__cruiser.receiveAttack()
            elif (ship_attacked == self.__submarine.ship_registry):
                self.__submarine.receiveAttack()
            elif (ship_attacked == self.__battleship.ship_registry):
                self.__battleship.receiveAttack()
            elif (ship_attacked == self.__carrier.ship_registry):
                self.__carrier.receiveAttack()  
        return result_sign  
    
    def __receiveEnemyAttack(self, attack: list) -> list :
        row = attack[0]
        column = attack[1]
        attack_result = []
        ship_attacked = "" if (self.__ships_board[row][column] == "v") else self.__ships_board[row][column] 
        self.__ships_board[row][column] = "x" if(self.__ships_board[row][column] == "v") else "o"
        attack_result_text = "Attack failed" if (self.__ships_board[row][column] == "v") else "Attack successful!!!"
        print(attack_result_text, end="\n\n")
        attack_result.append(self.__ships_board[row][column])
        attack_result.append(ship_attacked)
        return attack_result