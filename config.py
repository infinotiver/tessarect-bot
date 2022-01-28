import data

#Admin variables
adminPass = 'xyz'   # Password for admin commands
adminID =  0     # Admin account ID for debug 
saveUser = 0     # Account to send logs to
activity = ''
lastSave = 0

#Bot token (Which bot to run the program on)
botToken = ''

#Boss data
BOSS_CRIT_CHANCE = 15

BOSSES = []

BOSS_MOVES = []

#Boss move assignment
BOSSES[0].moves = []
BOSSES[1].moves = []
BOSSES[2].moves = []
BOSSES[3].moves = []

#Global variables / modifiers
missChance = 20                   # Base percentage to miss an attack
trainTime = 900                   # Number of seconds it takes to train a move
bossMoveModifier = float(2.0)     # Multiplier for first move against a boss each turn
LEVEL_DIFF = 1                    # How many levels different should give buff to opponent
LEVELCAP = 30                     # Maximum move level

#Status effect system - Chance variables
HIGH_CHANCE = 45
MED_CHANCE = 25
LOW_CHANCE = 10
RUSH_CHANCE = 10
SELF_CHANCE = 10

#Status effect system - Chance Lists
concussListHIGH = []
concussListMED = []
concussListLOW = []
windHIGH = [] 
windMED = []
barmHIGH = []
blegVERYLOW = []