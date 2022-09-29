# The board is represented by two arrays
# The arrays are index 0 - 6
# index 0 is always the


class GameBoard:

    def __init__ ( self ):
        self.__top = [0]*6
        self.__topStore = 0
        self.__bottom = [0]*6
        self.__bottomStore = 0
        for i in range( 0,6 ) :
            self.__top[i] = 4
        for i in range(0, 6):
            self.__bottom[i] = 4


    def printBoard(self):
        self.__top.reverse()
        print("----------------------------------")
        print("   ",self.__top[0:6])
        print(self.__topStore , "                      ",self.__bottomStore )
        print("   ",self.__bottom[0:6] )
        print("----------------------------------")
        self.__top.reverse()

    def makeMove(self , player , choice ):
        # based on the player, change the Top or Bottom
        # Player 1 is the Top
        # Player 2 is the Bottom
        if player == 1:
            chips = self.__top[choice-1]
            self.__top[choice - 1] = 0
            playAgain = self.sowing( chips , player, choice )
        else:
            chips = self.__bottom[choice - 1]
            self.__bottom[choice - 1] = 0
            playAgain = self.sowing(chips, player, choice)
        return playAgain

    def sowing(self , chips , player , choice ):
        while chips > 0 :
            if player == 1 :
                self.__top[choice] += 1
                chips -= 1
                choice += 1
            else:
                self.__bottom[choice] += 1
                chips -= 1
                choice += 1
            if chips == 0:
                break
            if choice == 6:
                choice = 0
                if player == 1:
                    self.__topStore+=1
                    chips-=1
                    player = 2
                else:
                    self.__bottomStore += 1
                    chips -= 1
                    player = 1
        return True