from src.board.board import Board
from src.enumeration.enumeration import ShowDashboard


class Player:
    def __init__(self):
        self.__board = Board()

    def showShipsBoard(self):
        if self.__showDashboard("Ships") == ShowDashboard.yes.value:
            self.__showShipsBoard()

    def showAttackBoard(self):
        if self.__showDashboard("Attack") == ShowDashboard.yes.value:
            self.__showAttackBoard()

    def __showDashboard(self, board_type: str) -> int:
        print(f"Do you want to view your {board_type} board?")
        print("1. Yes")
        print("2. No")
        return int(input("Enter the option you want: "))

    def __showShipsBoard(self):
        self.__board.ships_board

    def __showAttackBoard(self):
        self.__board.attack_board

    def placeShips(self, player_type: int):
        self.__board.placeShips(player_type)

    def attackEnemy(self, player_type: int) -> list:
        return self.__board.positionAttack(player_type)

    def receiveAttack(self, attack: list) -> str:
        return self.__board.receiveEnemyAttack(attack)

    def markAttack(self, attack: list, result_sign: str):
        self.__board.markAttack(attack[0], attack[1], result_sign)

    def endOfGame(self):
        return True if (not self.__board.hasLiveShips()) else False
