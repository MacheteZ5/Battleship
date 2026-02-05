from src.menu.menu import selectGameMode, continueGame
from src.player.player import Player
from src.enumeration.enumeration import PlayerType, GameMode

def main():
    while(True):
        try:
            game_mode = selectGameMode()
            players_turn = True
            round = 1
            player = Player()
            challenger = Player()
            player.placeShips(PlayerType.player.value)
            player_type = PlayerType.cpu.value if(game_mode == GameMode.singlePlayer.value) else PlayerType.player.value
            challenger.placeShips(player_type)
            while(True):
                print("---------------------------------------------------------", end="\n\n")
                print(f"Round No.{round}")
                print("It is player's turn " if (players_turn) else "It is challenger's turn: ")
                print("---------------------------------------------------------", end="\n\n")
                if(players_turn):
                    player.showShipsBoard()
                    attack = player.attackEnemy(PlayerType.player.value)
                    result_sign = challenger.receiveAttack(attack)
                    player.markAttack(attack, result_sign)
                    player.showAttackBoard()
                    players_turn = False
                else:
                    if (player_type == PlayerType.player.value): player.showShipsBoard()
                    attack = challenger.attackEnemy(player_type)
                    result_sign = player.receiveAttack(attack)
                    challenger.markAttack(attack, result_sign)
                    if (player_type == PlayerType.player.value): player.showAttackBoard()
                    players_turn = True
                if(challenger.endOfGame() or player.endOfGame()):
                    break
                round += 1
            if(not continueGame()):
                print("Game Over", end="\n\n")
                break
        except ValueError as e:
            print("Error: The entered value is not a valid option.")
            print(f"An error has occurred: {e}")
    print("\n\n Thanks for playing!!!")

if __name__ == '__main__':
    main()