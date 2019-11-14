class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Gato(Player):
    def __init__(self, player1, player2):
        self.player1 = Player(player1.name, player1.symbol)
        self.player2 = Player(player2.name, player2.symbol)
    

    def checkIfPlayerWon(self, array, currentPlayer):
        if self.checkRows(array, currentPlayer) or self.checkColumns(array, currentPlayer) or self.checkCross( array, currentPlayer) or self.checkCross( array, currentPlayer, True):
            return True
        else:
            return False

    def checkRows(self, array, currentPlayer):
        winner = False
        for x in array:
            if winner:
                return True
            for y in x:
                if y == currentPlayer.symbol:
                    winner = True
                else:
                    winner = False
                    break
        if winner:
            return True
        return False

    def checkColumns(self, array, currentPlayer):
        winner = False
        for i in range(len(array[0])):
            if winner:
                return True
            for j in range(len(array[i])):
                if currentPlayer.symbol == array[j][i]:
                    winner = True
                else:
                    winner = False
                    break
        if winner:
            return True
        return False
        
    def checkCross(self, array, currentPlayer, inverted = False):
        winner = False
        for i in range(len(array[0])):
            if inverted:
                array[i] = array[i][::-1]
            if currentPlayer.symbol == array[i][i]:
                winner = True
                if inverted:
                    array[i] = array[i][::-1]
            else:
                winner = False
                if inverted:
                    array[i] = array[i][::-1]
                break
        if winner:
            return True
        return False

    