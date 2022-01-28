PLAYERDICT = {}             #Dictionary of players (key = user ID)
ACTIVE_BOSSFIGHT = None     #Currently active boss fight
modifier = 5                #How much to divide level multiplier by when calculating damage
SCOREBOARD = []             #Keeps track of player score

#Stores a scoreboard entry
class Score:
    def __init__(self, player, wins, losses):
        self.player = player
        self.wins = wins
        self.losses = losses

#Stores information on a move in training
class Training:
    def __init__(self, player, move, level, time, done = False):
        self.player = player
        self.move = move
        self.level = level
        self.time = time 
        self.done = done

#Stores information on each move
class Move:
    def __init__(self, name, elem, hp, level):
        self.name = name
        self.elem = elem
        self.hp = hp
        self.level = int(level)

    def getAccuracy(self):
        
        miss = float(self.level) 
        
        if int(self.hp) >= int(8):
            
            miss -= float((30-(float(self.level))) + (float(self.hp)))
            
            #Process caps
            if miss > -10:
                miss = -10
            if miss < -25:
                miss = -25

        return int(miss)

    def getDamage(self):
        
        toHit = int(self.hp)*((self.level/modifier))
        
        #Cap at minimum of 5
        if toHit < 5:
            toHit = 5
        
        #Calculate special moves
        if self.name == 'Pinch':
            toHit = 1

        return toHit

#Stores information on player's movesets
class Player:
    def __init__(self, name, moveNames, wins, losses, effect=None, last=None):
        self.name = name
        self.moveNames = moveNames
        self.wins = int(wins)
        self.losses = int(losses)
        self.training = False
        self.effect = None
        self.last = None

    def setEffect(self, effect):
        self.effect = effect

    def getEffect(self):
        return self.effect
 
    def setMoves(self, moves):
        self.moves = []
        self.moves = moves

    def setTraining(self, isTraining):
        self.training = isTraining

    def getTraining(self):
        return self.training

#Stores information on an active fight
class Fight:
    def __init__(self, player1, player2, p1health, p2health, turn, lastMove = None, stage = None):
        self.player1 = player1
        self.player2 = player2
        self.p1health = int(p1health)
        self.p2health = int(p2health)
        self.turn = turn
        self.lastMove = lastMove
        self.stage = 'lobby'

#Stores all information on boss fight instances
class Bossfight:
    def __init__(self, boss, turn, p1, p2=None, p3=None, lastMove = None, stage = None, lobby = None):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.turn = turn
        self.lastMove = lastMove
        self.stage = 'lobby'
        self.p1hp = 100
        self.p2hp = 100
        self.p3hp = 100
        self.lobby = [p1]
        self.boss = boss

#Stores all information on boss characters
class Boss:
    def __init__(self, name, hp, maxhp, reward, moves = None):
        self.name = name
        self.hp = hp
        self.moves = moves
        self.maxhp = maxhp
        self.reward = reward