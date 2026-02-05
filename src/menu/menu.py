from src.enumeration.enumeration import ContinueGame

def selectGameMode() -> int:
    while(True):
        try:
            print("Select game mode")
            print("1. Player vs CPU \n", end = "2. Player vs Player \n")
            valid_mode = (1,2)
            game_mode = int(input("Enter game mode:"))
            if(game_mode in valid_mode):
                return game_mode
            else:
                print("The value entered is invalid. You must choose one of the options displayed on the screen.")
        except ValueError:
            print("You must enter a numeric value.")

def continueGame() -> bool:
    while(True):
        try:
            print("Do you want to play again?")
            print("1. Yes \n", end = "2. No \n")
            valid_continue_game = (1,2)
            continue_game = int(input("Enter the respective value: "))
            if(continue_game in valid_continue_game):
                return True if (continue_game == ContinueGame.yes.value) else False
            else:
                print("The value entered is invalid. You must choose one of the options displayed on the screen.")
        except ValueError:
            print("You must enter a numeric value.")