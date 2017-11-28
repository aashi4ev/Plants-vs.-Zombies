from math import pi, sin, cos
import random
from tkinter import *

################################### Plants ####################################

# creates the class type "Plants"
class Plants(object):
    def __init__(self):
        pass

# uses 10 moneys
# creates one energy ball... equating to 15 money points
# moves up, in the y direction
class Sunflower(Plants):
    def __init__(self):
        self.shooting = False
        self.zombie = False
        self.score = 1
        self.money = 10
        self.shooter = "energy"
        self.velocity = 10
        self.flagzombie = False
        self.collisions = False
    def shoots(self, x, y):
        self.shooterx = x
        self.shootery = y

# uses 30 moneys
# creates one pin/thorn that kill the zombie
class Cactus(Plants):
    def __init__(self):
        self.shooting = False
        self.zombie = False
        self.score = 1
        self.velocity = 10
        self.flagzombie = False
        self.money = 30
        self.shooter = "pin"
        self.collisions = False
        self.shooterflag = False
    def shoots(self, x, y):
        self.shooterx = x
        self.shootery = y

# uses 5 moneys
# creates three peas each, one at each time, that attack the zombie
# zombies die in 5 shots of this
class Peashooter(Plants):
    def __init__(self):
        self.shooting = False
        self.zombie = False
        self.score = 3
        self.money = 5
        self.shooter = "pea"
        self.velocity = 10
        self.collisions = False
        self.flagzombie = False
        self.shooterflag = False
    def shoots(self, x, y):
        self.shooterx = x
        self.shootery = y

# uses 15 moneys
# prevents the zombies from moving
# if walnut has been present for over a certain amount of time, you lose
class Walnut(Plants):
    def __init__(self):
        self.money = 15
        self.shooting = False
        self.zombie = False
        self.shooter = "wall"
        self.score = 100
        self.velocity = 5
        self.flagzombie = False
        self.shoots = False
        self.collisions = False

################################### Zombies ####################################

# creates the zombies
# initializes their health and speed and whether or not they still exist
class Zombies(object):
    def __init__(self, row):
        self.row = row
        self.speed = 40
        self.score = 5
        self.collisions = False
        self.moving = True
        self.image = 1

#################################### Modes #####################################

def rgbString(red, blue, green):
    return "#%02x%02x%02x" % (red, blue, green)

def init(data):
    data.width = 500
    data.height = 500
    data.mode = "mainscreen"
    data.time = 0
    data.score = 0
    data.bestscore = 0
    data.Orange = rgbString(255, 165, 0)
    data.Scarlet = rgbString(255, 69, 0)
    data.darkRed = rgbString(178, 34, 34)
    data.level = 1
    data.rows = 5
    data.cols = 10
    mainscreeninit(data)
    gamemodeinit(data)
    losewinscreeninit(data)

def mainscreeninit(data):
    data.plantvszombiesColor = "Red"
    data.plantvszombieSize = 10
    data.flag = "up"
    data.flager = "yes"
    data.playinfox = 65
    data.helpinfox = data.width-65
    data.dark = rgbString(20, 50, 20)
    data.mainpic = PhotoImage(file = "mainbackground.GIF")
    
def losewinscreeninit(data):
    data.loser = data.width/3
    data.losesize = 30
    data.flag1 = False
    data.flag2 = False
    data.flag3 = False
    data.flag4 = False
    data.playagaincolor = "red"
    data.wincolor = "red"
    data.losepic = PhotoImage(file = "losebackground.GIF")
    data.winpic = PhotoImage(file = "winbackground.GIF")

def gamemodeinit(data):
    initinit(data)
    playinginit(data)
    imagesinit(data)

def imagesinit(data):
    data.grasspic = PhotoImage(file="grass.GIF")
    data.peashooterpic = PhotoImage(file="PeaShooter.GIF")
    data.cactuspic = PhotoImage(file="cactus.GIF")
    data.sunflowerpic = PhotoImage(file="sunflower.GIF")
    data.walnutpic = PhotoImage(file="walnut.GIF")
    data.zombiepic1 = PhotoImage(file="zombie1.GIF")
    data.zombiepic2 = PhotoImage(file="zombie2.GIF")
    data.zombiepic = data.zombiepic1
    data.peapic = PhotoImage(file="pea.GIF")
    data.energypic = PhotoImage(file="energy.GIF")
    data.pinpic = PhotoImage(file="pin.GIF")

def initinit(data):
    data.jewelpartdiff = 5
    data.cream = rgbString(255, 239, 213)
    data.sidewalk = rgbString(240, 240, 230)
    data.dotCount = 0
    data.optionsbarendy= 75
    data.pathend = 52
    data.dots = []
    while data.dotCount<300:
        data.dotCount += 1
        data.xdot = random.randint(0,data.pathend)
        data.ydot = random.randint(data.optionsbarendy, data.height)
        data.dots += [(data.xdot, data.ydot)]
    data.sidewalkdotCount = 0
    data.sidewalkdots = []
    while data.sidewalkdotCount<300:
        data.sidewalkdotCount += 1
        data.sidewalkxdot = random.randint(data.pathend+400,data.width)
        data.sidewalkydot = random.randint(data.optionsbarendy, data.height)
        data.sidewalkdots += [(data.sidewalkxdot, data.sidewalkydot)]
    data.startxi = data.pathend + 401
    data.startxend = data.width - 1
    data.startyi = data.optionsbarendy
    data.startyend = data.startyi + 30
    data.money = 40

# only gives values that are shared amongst all levels
# changed values per level are stored in initinit
# the imagesinit is always available to access
def playinginit(data):
    data.jewelx = data.width/7
    data.jewely = data.height/2
    data.start = False
    data.jewelflag = False
    data.board = []
    for l in range(data.rows):
        data.board += [[0]*data.cols]
    data.energy = 100
    data.playtime = 0
    data.walnuttime = 0
    data.walnutlose = False
    data.walnutcount = 0
    data.walnutexplode = False
    data.walnutexplodetime = 0
    data.money0 = False
    data.money0Time = 0
    data.selectPlant = False
    data.selectPlantTime = 0
    data.plants = ["Sunflower", "Cactus", "PeaShooter", "Wallnut"]
    data.plant = None
    data.zombie = None
    data.zombiecount = 0
    data.shooter = True
    data.zombiedeath = False
    data.zombiedying = False
    data.shooters = []
    for l in range(data.rows):
        data.shooters += [[0]*data.cols]
    data.energy = False
    data.pea = False
    data.pin = False
    data.walnut = False
    data.loseflagger = False
    data.pinspeed = random.randint(2, 9)
    data.peaspeed = random.randint(2, 5)
    data.energyspeed = random.randint(4, 7)
    data.explodingcount = 1
    data.leveler = 1

def mousePressed(event, data):
    if (data.mode == "mainscreen"): mainscreenMousePressed(event, data)
    elif (data.mode == "helpscreen"): helpscreenMousePressed(event, data)
    elif (data.mode == "winscreen"): winscreenMousePressed(event, data)
    elif (data.mode == "losescreen"): losescreenMousePressed(event, data)
    elif (data.mode == "playmode"): playmodeMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "mainscreen"): mainscreenKeyPressed(event, data)
    elif (data.mode == "helpscreen"): helpscreenKeyPressed(event, data)
    elif (data.mode == "winscreen"): winscreenKeyPressed(event, data)
    elif (data.mode == "losescreen"): losescreenKeyPressed(event, data)
    elif (data.mode == "playmode"): playmodeKeyPressed(event, data)

def timerFired(data):
    data.time+=1
    if data.score>data.bestscore:
        data.bestscore = data.score
    if (data.mode == "mainscreen"): mainscreenTimerFired(data)
    elif (data.mode == "helpscreen"): helpscreenTimerFired(data)
    elif (data.mode == "winscreen"): winscreenTimerFired(data)
    elif (data.mode == "losescreen"): losescreenTimerFired(data)
    elif (data.mode == "playmode"): playmodeTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "mainscreen"): mainscreenRedrawAll(canvas, data)
    elif (data.mode == "helpscreen"): helpscreenRedrawAll(canvas, data)
    elif (data.mode == "winscreen"): winscreenRedrawAll(canvas, data)
    elif (data.mode == "losescreen"): losescreenRedrawAll(canvas, data)
    elif (data.mode == "playmode"): playmodeRedrawAll(canvas, data)

########## mainscreen ##########

def mainscreenMousePressed(event, data):
    # help button
    if (((data.width/2)-60)<event.x and event.x<((data.width/2)+60) and 
                (data.height-150)<event.y and event.y<(data.height-100)):
        data.mode = "helpscreen"
    # play button
    if (((data.width/2)-60)<event.x and event.x<((data.width/2)+60) and 
                (data.height-220)<event.y and event.y<(data.height-170)):
        data.mode = "playmode"

def mainscreenKeyPressed(event, data):
    if event.keysym=="h":
        data.mode = "helpscreen"
    if event.keysym=="p":
        data.mode = "playmode"

# for animations of text
def mainscreenTimerFired(data):
    if data.time%16==12:
        data.plantvszombiesColor = data.Orange
    if data.time%16==8:
        data.plantvszombiesColor = data.Scarlet
    if data.time%16==4:
        data.plantvszombiesColor = data.darkRed
    if data.time%16==0:
        data.plantvszombiesColor = "Red"
    if data.plantvszombieSize>=46:
        data.flag = "down"
    if data.plantvszombieSize<=14:
        data.flag = "up"
    if data.flag == "up":
        data.plantvszombieSize+=3
    else:
        data.plantvszombieSize-=3
    if data.playinfox<=65:
        data.flager = "no"
    if data.playinfox>=data.width-65:
        data.flager = "yes"
    if data.flager=="yes":
        data.playinfox -= 10
        data.helpinfox += 10
    if data.flager=="no":
        data.playinfox += 10
        data.helpinfox -= 10

def mainbackground(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.dark)
    canvas.create_image(data.width/2, 
        data.height/2, anchor=CENTER, 
        image=data.mainpic)

def drawPlayButton(canvas, data):
    canvas.create_rectangle(((data.width/2)-60), (data.height-170), 
                ((data.width/2)+60), (data.height-220), fill="hotPink", 
                                                    outline="pink", width = 3)
    canvas.create_rectangle(((data.width/2)-55), (data.height-175), 
                ((data.width/2)+55), (data.height-215), fill="pink", 
                                                        outline="pink")
    canvas.create_rectangle(((data.width/2)-50), (data.height-180), 
                ((data.width/2)+50), (data.height-210), fill="hotPink", 
                                                        outline="hotPink")
    canvas.create_text(data.width/2,data.height-195,
                text="Play", fill="green", font="comicsans 30")

def drawHelpButton(canvas, data):
    canvas.create_rectangle(((data.width/2)-60), (data.height-100), 
                ((data.width/2)+60), (data.height-150), fill="green", 
                                            outline = "limegreen", width = 3)
    canvas.create_rectangle(((data.width/2)-55), (data.height-105), 
                ((data.width/2)+55), (data.height-145), fill="limegreen", 
                                                    outline ="limegreen")
    canvas.create_rectangle(((data.width/2)-50), (data.height-110), 
                ((data.width/2)+50), (data.height-140), fill="green", 
                                                    outline = "green")
    canvas.create_text(data.width/2,data.height-125,
        text="Help", fill="hotPink", font="comicsans 30")

def drawText(canvas, data):
    canvas.create_text(data.width/2,(data.height/3)+5,text="Plants vs. Zombies",
                            fill=data.plantvszombiesColor,font="comicsans %d" 
                                                    % data.plantvszombieSize)
    canvas.create_text(data.width/2, (data.height/3)+50,text=("Level: %d") 
                % data.level, fill="green",font="comicsans 26" )
    canvas.create_text(data.playinfox, data.height-10, 
    text = "Press 'P' to play!", fill=data.plantvszombiesColor, font="Times 18")
    canvas.create_text(data.helpinfox,data.height-30,text="Press 'H' for help.", 
                                fill=data.plantvszombiesColor, font="Times 18")
    canvas.create_text(data.width/2, data.height/4, 
        text=("Guard the Jewel!"), fill = "yellow", font = "Times 30 bold")

def mainscreenRedrawAll(canvas, data):
    mainbackground(canvas, data)
    drawPlayButton(canvas, data)
    drawHelpButton(canvas, data)
    drawText(canvas, data)

########## helpscreen ##########

def helpscreenMousePressed(event, data):
    # home button
    if (event.x>20 and event.x<80 and 
        event.y>20 and event.y<50):
        data.mode = "mainscreen"
    # play button
    if (event.x>data.width-80 and event.x<data.width-20 and 
        event.y>20 and event.y<50):
        data.mode = "playmode"

def helpscreenKeyPressed(event, data):
    if event.keysym=="p":
        data.mode = "playmode"
    if event.keysym=="m":
        data.mode = "mainscreen"
    if event.keysym=="l":
        data.mode = "losescreen"
    if event.keysym=="w":
        data.mode = "winscreen"

def helpscreenTimerFired(data):
    pass

def helpscreenRedrawAll(canvas, data):
    text1 = "Prevent the zombies from attaining access"
    text2 = "to the jewel!"
    textstart = "Click on the start button to start the level."
    text3 = "Click on a plant to select it from the Options Bar."
    text4 = "Then, click on the board where you want to place the plant."
    text5 = "The Sunflower plant generates money."
    text6 = "The Peashooter shoots peas at the zombies to attack them."
    text7 = "The Cactus shoots pins at the zombies to kill them."
    text8 = "The Wall-nut prevents the zombies from moving forward"
    text9 = "towards the jewel."
    canvas.create_rectangle(0,0,data.width,data.height,
                                    fill=data.darkRed,outline="red")
    canvas.create_text(data.width/2, 95, text=text1, 
        fill = "Black", font = "arial 24")
    canvas.create_text(data.width/2, 125, text=text2, 
        fill = "Black", font = "arial 24")
    canvas.create_text(data.width/2,170,text=textstart, 
                                            fill = "Black", font = "arial 22")
    canvas.create_text(data.width/2, 215, 
        text=text3, 
        fill="Black", font="arial 18")
    canvas.create_text(data.width/2, 245, 
        text=text4, 
        fill="Black", font="arial 18")
    canvas.create_text(data.width/2,275,text=text5, 
                    fill = "Black", font = "arial 18")
    canvas.create_text(data.width/2,305,
            text=text6, 
                    fill = "Black", font = "arial 18")
    canvas.create_text(data.width/2,335,
            text=text7, fill = "Black", font = "arial 18")
    canvas.create_text(data.width/2,365,
            text=text8, fill = "Black", font = "arial 18")
    canvas.create_text(data.width/2,385,
            text=text9, fill = "Black", font = "arial 18")
    drawhPlayButton(canvas, data)
    drawhMainButton(canvas, data)

def drawhPlayButton(canvas, data):
    canvas.create_rectangle(data.width-80,20,data.width-20,50,
        fill=data.darkRed,outline="darkgreen",width=10)
    canvas.create_text(data.width-50,35,
        text="Play",fill="green", font="comicsans 14 bold")

def drawhMainButton(canvas, data):
    canvas.create_rectangle(20,20,80,50,
                                 fill=data.darkRed,outline="darkgreen",width=10)
    canvas.create_text(50, 35,text="Home",fill="green", 
        font="comicsans 14 bold")

########## playmode ##########

# get which plant was selected
def getPlant(x, data):
    width = data.width/(len(data.plants))
    if x<width and x>0:
        data.plant = Sunflower()
    if x<(width*2) and x>width:
        data.plant = Peashooter()
    if x<(width*3) and x>(width*2):
        data.plant = Cactus()
    if x<data.width and x>(width*3):
        data.plant = Walnut()

# find the cell to place the plant in 
def getCell(x, y, data):
    widthi = data.pathend
    width = 400/data.cols
    heighti = data.optionsbarendy
    height = (data.height-data.optionsbarendy)/data.rows
    if x>widthi and x<widthi+width:
        col = 0
    if x>widthi+width and x<(widthi+(width*2)):
        col = 1
    if x>(widthi+(width*2)) and x<(widthi+(width*3)):
        col = 2
    if x>(widthi+(width*3)) and x<(widthi+(width*4)):
        col = 3
    if x>(widthi+(width*4)) and x<(widthi+(width*5)):
        col = 4
    if x>(widthi+(width*5)) and x<(widthi+(width*6)):
        col = 5
    if x>(widthi+(width*6)) and x<(widthi+(width*7)):
        col = 6
    if x>(widthi+(width*7)) and x<(widthi+(width*8)):
        col = 7
    if x>(widthi+(width*8)) and x<(widthi+(width*9)):
        col = 8
    if x>(widthi+(width*9)) and x<(widthi+(width*10)):
        col = 9
    if y>heighti and y<heighti+height:
        row = 0
    if y>heighti+height and y<(heighti+(height*2)):
        row = 1
    if y>(height+(height*2)) and y<(heighti+(height*3)):
        row = 2
    if y>(heighti+(height*3)) and y<(heighti+(height*4)):
        row = 3
    if y>(heighti+(height*4)) and y<(heighti+(height*5)):
        row = 4
    data.money -= (data.plant).money
    if data.money >= 0:
        if data.board[row][col]==0:
            data.board[row][col] = data.plant
            if isinstance(data.plant, Walnut):
                data.walnutcount += 1
    else:
        data.money0 = True
        data.money+=(data.plant).money
    if isinstance(data.plant, Walnut):
        data.walnut=True

# checks that if there is a plant in a row
# and if there is a zombie in a row
# the plant will shoot if both are in the same row
def play(data):
    for rowinboard in (data.board):
        flagplant = False
        flagzombie = False
        row = (data.board).index(rowinboard)
        plantsinrow = []
        for spot in rowinboard:
            if isinstance(spot, Plants):
                flagplant = True
                plantsinrow+=[rowinboard.index(spot)]
            if isinstance(spot, Zombies):
                flagzombie = True
        if flagzombie==True and flagplant==True:
            for plantcol in (plantsinrow):
                (data.board[row][plantcol]).zombie = True
        if flagplant == True and flagzombie == False:
            for plantcol in (plantsinrow):
                (data.board[row][plantcol]).zombie = False

# place the desired plants in the desired locations
def planting(event, data):
    if event.y>0 and event.y<data.optionsbarendy:
        getPlant(event.x, data)
    else:
        if event.x>data.pathend and event.x<data.pathend+400:
            if data.plant!=None:
                getCell(event.x, event.y, data)
            else:
                data.selectPlant = True

# start or help button pressed on the right of the screen
def buttonsClicked(event, data):
    if (event.y<data.startyend and event.y>data.startyi 
        and event.x<data.startxend and event.x>data.startxi):
        if data.start == True:
            data.start = False
        elif data.start==False:
            data.start = True
    if (event.y<data.height and event.y>(data.height-30) 
        and event.x<data.startxend and event.x>data.startxi):
        data.mode = "helpscreen"

def playmodeMousePressed(event, data):
    planting(event, data)
    buttonsClicked(event, data)

# change the modes of the game
def playmodeKeyPressed(event, data):
    if event.keysym=="m":
        data.mode = "mainscreen"
    if event.keysym=="h":
        data.mode = "helpscreen"
    if event.keysym=="s":
        if data.start == True:
            data.start = False
        elif data.start==False:
            data.start = True
    if event.keysym=="r":
        init(data)

# jewel movement time
def time(data):
    if data.start==True:
        data.playtime += 1
    if data.time%30==0:
        data.jewelpartdiff = 5

# boxes of info if something selected will not work
def displayInfo(data):
    if data.selectPlant==True:
        data.selectPlantTime += 1
        if data.selectPlantTime==15:
            data.selectPlant = False
            data.selectPlantTime = 0
    if data.money0 == True:
        data.money0Time += 1
        if data.money0Time==15:
            data.money0 = False
            data.money0Time = 0

def winOrlose(data):
    # if walnuts have been on the board for too long without the player winning
    if data.walnut==True:
        data.walnuttime += 1
        walnutwinlosetime = 150 - (data.level**data.walnutcount)
        if data.walnuttime%walnutwinlosetime==0:
            data.walnutexplode = True
            if data.explodingcount>=3:
                data.mode = "losescreen"
                data.walnutlose = True
    flag = False
    # if there are no zombies on the board after the playing started
    zombiewinlosetime = (30*(2**(data.level*0.5)))
    if data.playtime>=zombiewinlosetime and data.loseflagger==False:
        for row in range(len(data.board)):
            for col in range(len(data.board[0])):
                if isinstance(data.board[row][col], Zombies):
                    flag = True
        if flag == False and data.start==True:
            data.mode = "winscreen"
            data.money += 5
            data.level += 1
            data.start = False
            data.playtime = 0
            playinginit(data)
    # if zombies reach the jewel territory
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if isinstance(data.board[row][col], Zombies):
                if col==0:
                    data.mode = "losescreen"

# keeps the zombie from moving forward
def walnutCollisions(data):
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if isinstance(data.board[row][col], Zombies):
                if (isinstance((data.board[row][col-1]), Zombies) and 
                    (data.board[row][col-1]).moving==False):
                    (data.board[row][col]).moving = False
                else:
                    (data.board[row][col]).moving = True
                if isinstance((data.board[row][col-1]), Walnut):
                    (data.board[row][col]).moving = False

def makeZombies(data):
    # makes zombies
    if data.start == True:
        # interval of new zombie creation
        if data.playtime % 15 == 0:
            if data.zombiecount<(2**(data.level)):
                data.zombiecount += 1
                # randomly choose which row the zombie will attack
                zombierow = random.randint(0, data.rows-1)
                data.zombie=Zombies(zombierow)
                data.board[zombierow][data.cols-1] = data.zombie
    
def moveZombies(data):
    # moves each zombie
    # walks each zombie (pics)
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            # each zombie moves over a col in this time interval
            if isinstance((data.board[row][col]), Zombies):
                if ((data.board[row][col]).moving)==True:
                    if data.playtime % 7 == 0:
                        if (data.board[row][col]).image == 1:
                            data.zombiepic = data.zombiepic2
                            (data.board[row][col]).image = 2
                        else:
                            data.zombiepic = data.zombiepic1
                            (data.board[row][col]).image = 1
                        if isinstance(data.board[row][col], Zombies):
                            zombie = data.board[row][col]
                            data.board[row][col] = 0
                            data.board[row][col-1] = zombie

# finds which col the shooter has moved to
# only for peas and pins
def getCol(x, data):
    widthi = data.pathend
    width = 400/data.cols
    heighti = data.optionsbarendy
    height = (data.height-data.optionsbarendy)/data.rows
    if x>=widthi and x<=widthi+width:
        col = 0
    if x>=widthi+width and x<=(widthi+(width*2)):
        col = 1
    if x>=(widthi+(width*2)) and x<=(widthi+(width*3)):
        col = 2
    if x>=(widthi+(width*3)) and x<=(widthi+(width*4)):
        col = 3
    if x>=(widthi+(width*4)) and x<=(widthi+(width*5)):
        col = 4
    if x>=(widthi+(width*5)) and x<=(widthi+(width*6)):
        col = 5
    if x>=(widthi+(width*6)) and x<=(widthi+(width*7)):
        col = 6
    if x>=(widthi+(width*7)) and x<=(widthi+(width*8)):
        col = 7
    if x>=(widthi+(width*8)) and x<=(widthi+(width*9)):
        col = 8
    if x>=(widthi+(width*9)) and x<=(widthi+(width*10)):
        col = 9
    return col

# for each plant
def makeShooters(data):
    height = (data.height-data.optionsbarendy)/data.rows
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            makeEnergy(data, row, col, height)
            makePeas(data, row, col, height)
            makePins(data, row, col, height)

# only for sunflower
def makeEnergy(data, row, col, height):
    if isinstance(data.board[row][col], Sunflower):
        if (data.playtime % data.energyspeed == 0 and 
        (data.board[row][col]).score>0):
            (data.board[row][col]).score -= 1
            (data.board[row][col]).collisions = False
            (data.board[row][col]).shooting = True
            data.shooters[row][col] = "energy"
            data.energy = True
            (data.board[row][col]).shoots(row, col)
            (data.board[row][col]).shooterx = data.pathend+20+(col*40)
            (data.board[row][col]).shootery = (data.optionsbarendy+ 
                                            (height/2) + (height*row))

# only for cacti
def makePins(data, row, col, height):
    if (isinstance(data.board[row][col], Cactus) and 
    (data.board[row][col]).score>0):
        if (data.playtime % data.peaspeed == 0 and 
        (data.board[row][col]).zombie == True):
            (data.board[row][col]).collisions = False
            (data.board[row][col]).shooting = True
            (data.board[row][col]).score -= 1
            data.shooters[row][col] = "pin"
            data.pin = True
            (data.board[row][col]).shoots(row, col)
            (data.board[row][col]).shooterx = data.pathend+20+(col*40)
            (data.board[row][col]).shootery = (data.optionsbarendy+ 
                                            (height/2) + (height*row))
            shooterrow = row
            shootercol = getCol((data.board[row][col]).shooterx, data)
            if isinstance(data.board[shooterrow][shootercol], Zombies):
                data.board[shooterrow][shootercol] = 0
            
# only for peashooters
def makePeas(data, row, col, height):
    if isinstance(data.board[row][col], Peashooter):
        if (data.playtime % data.pinspeed == 0 and 
        (data.board[row][col]).score>0 and
        (data.board[row][col]).zombie == True):
            (data.board[row][col]).collisions = False
            (data.board[row][col]).shooting = True
            data.shooters[row][col] = "pea"
            data.pea = True
            (data.board[row][col]).shoots(row, col)
            (data.board[row][col]).shooterx = data.pathend+20+(col*40)
            (data.board[row][col]).shootery = (data.optionsbarendy+ 
                                            (height/2) + (height*row))
            shooterrow = row
            shootercol = getCol((data.board[row][col]).shooterx, data)
            if isinstance(data.board[shooterrow][shootercol], Zombies):
                (data.board[shooterrow][shootercol]).score -= 1
                if (data.board[shooterrow][shootercol]).score <= 0:
                    data.board[shooterrow][shootercol] = 0

# collision with zombie to decrease health / kill it
def PeaCollision(data, row, col, shooterrow, shootercol):
    if isinstance(data.board[shooterrow][shootercol], Zombies):
        (data.board[row][col]).collisions = True
        (data.board[row][col]).shooting = False
        (data.board[shooterrow][shootercol]).score -= 1
        (data.board[row][col]).velocity = 0
        if (data.board[shooterrow][shootercol]).score <= 0:
            # kills Zombie!
            (data.board[shooterrow][shootercol]) = 0

# kills zombie upon collision
def PinCollision(data, row, col, shooterrow, shootercol):
    if isinstance(data.board[shooterrow][shootercol], Zombies):
        # kills Zombie! 
        data.board[shooterrow][shootercol] = 0
        (data.board[row][col]).shooting = False
        (data.board[row][col]).velocity = 0

# peas and pins move in the same way to shoot
# this function moves them, only x coordinate moves
def movePeaPin(data, row, col):
    if (data.board[row][col]).shooting == True:
        height = (data.height-data.optionsbarendy)/data.rows
        if isinstance((data.board[row][col]), Peashooter):
            shooter = "pea"
        if isinstance((data.board[row][col]), Cactus):
            shooter = "pin"
        if ((data.pathend+20+(col*40) + (data.board[row][col]).velocity) >= 
        (data.pathend + 400)):
            (data.board[row][col]).shooting = False
            (data.board[row][col]).velocity = 0
        else:
            (data.board[row][col]).shooterx = (
                                data.pathend+20+(col*40) + 
                                (data.board[row][col]).velocity)
            (data.board[row][col]).shootery = (data.optionsbarendy+ 
                                (height/2) + (height*row))
            shooterrow = row
            shootercol = getCol((data.board[row][col]).shooterx, data)
            (data.board[row][col]).velocity += 10
            if shooter == "pea":
                PeaCollision(data, row, col, shooterrow, shootercol)
            if shooter == "pin":
                PinCollision(data, row, col, shooterrow, shootercol)

# moves the money ball up, floats up to optionsbar
# makes the moneyball draw continuously if game has not yet started
# if started, moneyball will blink upwards
def moveEnergy(data, row, col):
    if data.board[row][col].shooting == True:
        height = (data.height-data.optionsbarendy)/data.rows
        shooter = "energy"
        (data.board[row][col]).velocity += 5
        (data.board[row][col]).shooterx = (
                                    data.pathend+20+(col*40))
        (data.board[row][col]).shootery = (data.optionsbarendy+ 
            (height/2) + (height*row) - 
            (data.board[row][col]).velocity)
        if (data.board[row][col]).shootery<=data.optionsbarendy:
            (data.board[row][col]).shooting = False
            data.money += 20

# moves each shooter
def moveShooters(data):
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if (isinstance(data.board[row][col], Cactus) or
            isinstance((data.board[row][col]), Peashooter)):
                movePeaPin(data, row, col)
            if isinstance(data.board[row][col], Sunflower):
                moveEnergy(data, row, col)

# if the zombies collide with the plants itself
def SPCCollisions(data):
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if (isinstance(data.board[row][col], Plants) and  
                not isinstance(data.board[row][col], Walnut) and 
                isinstance(data.board[row][col], Zombies)):
                    data.board[row][col] = data.board[row][col]

def playmodeTimerFired(data):
    time(data)
    displayInfo(data)
    winOrlose(data)
    play(data)
    walnutCollisions(data)
    makeZombies(data)
    moveZombies(data)
    makeShooters(data)
    moveShooters(data)
    SPCCollisions(data)

# grid background image
def drawGrass(canvas, data):
    canvas.create_image(data.pathend + 200, 
        (data.height-data.optionsbarendy)/2 +100, anchor=CENTER, 
        image=data.grasspic)

# draws gridlines over the grass to see rows and cols
def drawBoard(canvas, data):
    count = 0
    widthi = data.pathend+1
    width = 40
    heighti = data.optionsbarendy+2
    height = (data.height-data.optionsbarendy)/data.rows
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            canvas.create_rectangle(widthi, heighti, 
                widthi+(width*(col+1)), heighti+(height*(row+1)), 
                outline = "darkgreen")

# sidewalk info bar on the right of the screen
def drawSidewalk(canvas, data):
    count = 0
    length = (data.height-data.optionsbarendy/data.rows)
    for row in range(data.rows):
        canvas.create_rectangle((data.pathend+400),
            data.optionsbarendy+(length*row), data.width+1,
            data.optionsbarendy+(length*(row+1)), fill=data.sidewalk, 
            outline="black", width = 2)
    canvas.create_line(data.pathend+400, data.height+2, 
        data.width, data.height+2, fill="black", width = 2)
    for (xdot, ydot) in data.sidewalkdots:
        canvas.create_oval(xdot, ydot, xdot+1, ydot+1, fill="black")

# jewel box on the left of the screen
def drawPath(canvas, data):
    count = 0
    length = (data.height-data.optionsbarendy/data.rows)
    for row in range(data.rows):
        canvas.create_rectangle(0,data.optionsbarendy+(length*row),data.pathend,
        data.optionsbarendy+(length*(row+1)), fill=data.sidewalk, 
        outline=data.sidewalk, width=3)
    for (xdot, ydot) in data.dots:
        canvas.create_oval(xdot, ydot, xdot+1, ydot+1, fill="black")

# how the jewel spins and shrinks
def drawpart(canvas, data):
    data.jewelx = 25
    data.jewely = 287.5
    canvas.create_polygon(25, 262.5+data.jewelpartdiff, 
        45-data.jewelpartdiff, 287.5, 
        25, 312.5-data.jewelpartdiff, 
        5+data.jewelpartdiff, 287.5, fill=data.darkRed, outline="black")

# if jewel is growing, shrinking, or spinning
def drawJewel(canvas, data):
    if data.jewelpartdiff<=20:
        data.jewelflag=False
    elif data.jewelpartdiff>=20:
        data.jewelflag=True
    if data.jewelflag==True:
        data.jewelpartdiff-=1
    if data.jewelflag==False:
        data.jewelpartdiff+=1
    drawpart(canvas, data)

# draws the box and the jewel
def drawHome(canvas, data):
    drawPath(canvas, data)
    drawJewel(canvas, data)

def drawpStartButton(canvas, data):
    canvas.create_rectangle(data.startxi, data.startyi, data.startxend, 
        data.startyend, fill = "yellow", outline = "gold")
    canvas.create_rectangle(data.startxi+5, data.startyi+5, data.startxend-5, 
        data.startyend-5, fill = "gold", outline = "gold")
    canvas.create_text((data.startxi+data.startxend)/2, 
        (data.startyi+data.startyend)/2, text="Start", font = "Times 16 bold")

def drawpHelpButton(canvas, data):
    canvas.create_rectangle(data.startxi, data.height-30, data.startxend, 
        data.height, fill = "green", outline = "limegreen")
    canvas.create_rectangle(data.startxi+5, data.height-30+5, 
        data.startxend-5, data.height-5, fill = "limegreen",outline="limegreen")
    canvas.create_text((data.startxi+data.startxend)/2, 
        data.height - 15, 
        text="Help", font = "Times 16 bold")

# if the player attempts to do a command that is not allowed
# a info / error box will appear
def drawinfotext(canvas, data):
    y1 = ((data.height - data.startyend)/2) - 30
    y2 = (y1 + (data.height - data.startyend)/2) + 40
    canvas.create_rectangle(data.pathend+401, y1, data.width-1, y2, 
        fill = "brown", outline = "brown")
    canvas.create_text((data.pathend+402+data.width)/2, y1 + 117, 
        text = "Kill the", font = "Times 12")
    canvas.create_text((data.pathend+402+data.width)/2, y1 + 132, 
        text = "Zombies!", font = "Times 12")
    canvas.create_text((data.pathend+402+data.width)/2, y1 + 70, 
        text = "Money:", font = "Times 12")
    canvas.create_text((data.pathend+400+data.width)/2, y1 + 85, 
        text = "%d" % data.money, font = "Times 12")
    canvas.create_text((data.pathend+400+data.width)/2, y1 + 35, 
        text = "Level: %d" % data.level, font = "Times 12 bold") 
    canvas.create_text((data.pathend+400+data.width)/2, y1 + 170, 
        text = "Selected", font = "Times 12")
    canvas.create_text((data.pathend+400+data.width)/2, y1 + 185, 
        text = "Plant:", font = "Times 12")
    if isinstance(data.plant, Cactus):
        plant = "Cactus"
    if isinstance(data.plant, Sunflower):
        plant = "Sunflower"
    if isinstance(data.plant, Walnut):
        plant = "Walnut"
    if isinstance(data.plant, Peashooter):
        plant = "Peashooter"
    if data.plant==None:
        plant = "None!"
    canvas.create_text((data.pathend+400+data.width)/2, y1 + 200, 
        text = "%s" % plant, font = "Times 12")

def drawpText(canvas, data):
    drawpStartButton(canvas, data)
    drawpHelpButton(canvas, data)
    drawinfotext(canvas, data)

# draws all plants and zombies on the baord
def drawPlantsZombies(canvas, data):
    rx = 400/data.cols
    ry = (data.height - data.optionsbarendy)/data.rows
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if data.board[row][col]==0:
                continue
            else:
                if isinstance(data.board[row][col], Zombies):
                    
                    canvas.create_image(data.pathend+(col*rx)+(rx/2), 
                    data.optionsbarendy+((row*ry))+(ry/2), anchor=CENTER,
                    image = data.zombiepic)
                
                if isinstance(data.board[row][col], Plants):
                    
                    if isinstance(data.board[row][col], Cactus):
                        canvas.create_image(data.pathend+(col*rx)+(rx/2), 
                        data.optionsbarendy+((row*ry))+(ry/2), anchor=CENTER,
                        image = data.cactuspic)
                    
                    if isinstance(data.board[row][col], Sunflower):
                        canvas.create_image(data.pathend+(col*rx)+(rx/2), 
                        data.optionsbarendy+((row*ry))+(ry/2), anchor=CENTER,
                        image = data.sunflowerpic)
                    
                    if isinstance(data.board[row][col], Peashooter):
                        canvas.create_image(data.pathend+(col*rx)+(rx/2), 
                        data.optionsbarendy+((row*ry))+(ry/2), anchor=CENTER,
                        image = data.peashooterpic)
                    
                    if isinstance(data.board[row][col], Walnut):
                        canvas.create_image(data.pathend+(col*rx)+(rx/2), 
                        data.optionsbarendy+((row*ry))+(ry/2), anchor=CENTER,
                        image = data.walnutpic)

# draws cactus shooter
def drawPin(canvas, data):
    if data.pin==True:
        for row in range(len(data.board)):
            for col in range(len(data.board[0])):
                if (isinstance((data.board[row][col]), Cactus) and 
                    (data.board[row][col]).shooterflag == False
                    and (data.board[row][col]).shooting==True):
                        canvas.create_image((data.board[row][col]).shooterx, 
                        (data.board[row][col]).shootery, anchor=CENTER, 
                        image = data.pinpic)

# sunflower shooter
def drawEnergy(canvas, data):
    if data.energy == True:
        for row in range(len(data.board)):
            for col in range(len(data.board[0])):
                if (isinstance((data.board[row][col]), Sunflower) and 
                    data.playtime % data.energyspeed == 0):
                    if (data.board[row][col]).shootery>data.optionsbarendy:   
                        canvas.create_image((data.board[row][col]).shooterx, 
                            (data.board[row][col]).shootery, anchor=CENTER, 
                            image = data.energypic)

# peashoooter shooter
def drawPea(canvas, data):
    if data.pea == True:
        for row in range(len(data.board)):
            for col in range(len(data.board[0])):
                if (isinstance((data.board[row][col]), Peashooter) and 
                    (data.board[row][col]).shooterflag == False
                    and (data.board[row][col]).shooting==True):
                    canvas.create_image((data.board[row][col]).shooterx, 
                        (data.board[row][col]).shootery, anchor=CENTER, 
                        image = data.peapic)

def drawShooters(canvas, data):
    drawPin(canvas, data)
    drawEnergy(canvas, data)
    drawPea(canvas, data)

# top options bar from where you choose your plant
def drawOptionsBar(canvas, data):
    widthi = 0
    width = data.width/(len(data.plants))
    for data.plantbox in range(len(data.plants)):    
        canvas.create_rectangle(widthi+(width*data.plantbox), 0, 
            width*(data.plantbox+1),data.optionsbarendy,fill = data.cream, 
                                        outline = "Black", width=3)
    # sunflower option info
    sunflowerOption = Sunflower()
    canvas.create_image(width/2, data.optionsbarendy/2, anchor=CENTER, 
        image=data.sunflowerpic)
    canvas.create_text(width/2, data.optionsbarendy-9, 
        text="Money: %d" % sunflowerOption.money)
    canvas.create_text(width/2, data.optionsbarendy-20, text= "Sunflower")
    
    # peashooter option info
    peashooterOption = Peashooter()
    canvas.create_image(width + (width/2) + 6, 
        (data.optionsbarendy/2) - 10, anchor=CENTER, 
        image=data.peashooterpic)
    canvas.create_text(width + (width/2), 
         data.optionsbarendy-9, text= "Money: %d" % peashooterOption.money)
    canvas.create_text(width + (width/2), 
         data.optionsbarendy-20, text= "Peashooter")
    
    # cactus option info
    canvas.create_image((width*2) + (width/2), 
        data.optionsbarendy/2, anchor=CENTER, 
        image=data.cactuspic)
    cactusOption = Cactus()
    canvas.create_text((width*2) + (width/2), 
         data.optionsbarendy-9, text= "Money: %d" % cactusOption.money)
    canvas.create_text((width*2) + (width/2), 
         data.optionsbarendy-20, text= "Cactus")
   
    # walnut option info
    canvas.create_image((width*3) + (width/2), 
        (data.optionsbarendy/2) - 12, anchor=CENTER, 
        image=data.walnutpic)
    walnutOption = Walnut()
    canvas.create_text((width*3) + (width/2), 
         data.optionsbarendy-20, text= "Wall-nut")    
    canvas.create_text((width*3) + (width/2), 
         data.optionsbarendy-9, text= "Money: %d" % walnutOption.money)

# help with directions because of errors
def drawInfo(canvas, data):
    if data.selectPlant==True:
        canvas.create_rectangle((data.width/2)-180, (data.height/2)-20,
            (data.width/2)+180, (data.height/2)+20, fill="maroon", 
            outline="brown", width = 10)
        canvas.create_text(data.width/2, data.height/2, 
            text="Select a plant to be placed at this location!", 
            font = "Times 16")
    if data.money0 == True:
        canvas.create_rectangle((data.width/2)-180, (data.height/2)-20,
            (data.width/2)+180, (data.height/2)+20, fill="maroon", 
            outline="brown", width = 10)
        canvas.create_text(data.width/2, data.height/2, 
            text="You do not have enough money to create this plant!", 
            font = "Times 16")

# creates the explosion algorithm for walnut exploding
def nextExplode(canvas, last, level, row, col, data):
    new = ""
    for part in last:
        if part == "t":  
            nextpart = "t+t-t" 
        else:
            nextpart = ""
        new = new + nextpart
    return new

# part of creating the algorithm to explode
# algorithm is not in relation to location, but in relation to explosion radius
def explode(canvas, data, levels, start, row, col):
    if data.explodingcount<=3:
        data.explodingcount += 1
        starting = start
        ending = ""
        for level in range(levels):
            ending = nextExplode(canvas, starting, level, row, col, data)
            starting = ending
            drawit(canvas, data, ending, start, row, col)
    else:
        data.mode = "losescreen"
        data.walnutlose = True
 
 # actually draws the "bombs"
def drawit(canvas, data, ending, start, row, col):
    for part in ending:
        if part=="t":
            data.leveler += 1
            leveler = round(data.leveler*0.5)
            r = random.randint(5, 25)
            redness = random.randint(5, 250)
            color = rgbString(redness, 0, 0)
            xi = data.pathend + (col*(40))
            xend = xi + 40
            x = random.randint(xi, xend)
            yi = (data.optionsbarendy + 
                         (row*((data.height-data.optionsbarendy)/data.rows)))
            yend = yi + 40
            y = random.randint(yi, yend)
            canvas.create_oval(x - r, y - r, x + r, y + r, fill = color, 
                                                                outline = color)
        if part == "+":
            data.leveler += 5
        if part == "-":
            data.leveler -= 15

def drawWalnutExplosions(canvas, data):
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            if isinstance(data.board[row][col], Walnut):
                start = "t"
                levels = data.zombiecount**data.zombiecount
                drawing = explode(canvas, data, levels, start, row, col)

def playmodeRedrawAll(canvas, data):
    drawGrass(canvas, data)
    drawBoard(canvas, data)
    drawSidewalk(canvas, data)
    drawHome(canvas, data)
    drawpText(canvas, data)
    drawPlantsZombies(canvas, data)
    drawShooters(canvas, data)
    drawOptionsBar(canvas, data)
    drawInfo(canvas, data)
    # walnut explosions uses the L-system fractal algorithm
    # https://en.wikipedia.org/wiki/L-system#Example_2:_Pythagoras_tree
    # this is the algorithm found and used
    if data.walnutexplode == True:
        drawWalnutExplosions(canvas, data)

########## winscreen ##########

def winscreenMousePressed(event, data):
    # home button
    if (event.x>(data.width/2)-50 and event.x<(data.width/2)+50 and 
        event.y>data.height-215 and event.y<data.height-175):
        data.mode = "mainscreen"
    # play button
    if (event.x>(data.width/2)-50 and event.x<(data.width/2)+50 and 
        event.y>data.height-165 and event.y<data.height-125):
        data.mode = "helpscreen"

def winscreenKeyPressed(event, data):
    if event.keysym=="p":
        data.mode = "mainscreen"
    if event.keysym=="h":
        data.mode = "helpscreen"

# helps define color for text on this screen
def winscreenTimerFired(data):
    if data.time%16==4:
        data.wincolor = data.Orange
    if data.time%16==8:
        data.wincolor = data.Scarlet
    if data.time%16==12:
        data.wincolor = "red"
    if data.time%16==0:
        data.wincolor = data.darkRed

def winbackground(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill="darkgreen")
    canvas.create_image(data.width, 
        data.height, anchor=SE, 
        image=data.winpic)

def wintext(canvas, data):
    canvas.create_text(data.width/2, data.height/3, text="You Win!", 
        fill=data.wincolor, font="comicsans 40")
    canvas.create_text(data.width/2, data.height-15, 
        text="Press 'P' to play next level!",fill=data.wincolor,
        font="comicsans 20")
    canvas.create_text(data.width/2, (data.height/3)+50, 
        text = ("Level: %d" % data.level), fill = "green", font="Times 30")

def drawwPlayButton(canvas, data):
    canvas.create_rectangle(((data.width/2)-60), (data.height-170), 
                ((data.width/2)+60), (data.height-220), fill="hotPink", 
                                                    outline="pink", width = 3)
    canvas.create_rectangle(((data.width/2)-55), (data.height-175), 
                ((data.width/2)+55), (data.height-215), fill="pink", 
                                                        outline="pink")
    canvas.create_rectangle(((data.width/2)-50), (data.height-180), 
                ((data.width/2)+50), (data.height-210), fill="hotPink", 
                                                        outline="hotPink")
    canvas.create_text(data.width/2,data.height-195,
                text="Play", fill="green", font="comicsans 30")

def drawwHelpButton(canvas, data):
    canvas.create_rectangle(((data.width/2)-60), (data.height-100), 
                ((data.width/2)+60), (data.height-150), fill="green", 
                                            outline = "limegreen", width = 3)
    canvas.create_rectangle(((data.width/2)-55), (data.height-105), 
                ((data.width/2)+55), (data.height-145), fill="limegreen", 
                                                    outline ="limegreen")
    canvas.create_rectangle(((data.width/2)-50), (data.height-110), 
                ((data.width/2)+50), (data.height-140), fill="green", 
                                                    outline = "green")
    canvas.create_text(data.width/2,data.height-125,
        text="Help", fill="hotPink", font="comicsans 30")

def winscreenRedrawAll(canvas, data):
    winbackground(canvas, data)
    wintext(canvas, data)
    drawwPlayButton(canvas, data)
    drawwHelpButton(canvas, data)

########## losecreen ##########

def losescreenMousePressed(event, data):
    # home button
    if (event.x>(data.width/2)-50 and event.x<(data.width/2)+50 and 
        event.y>data.height-215 and event.y<data.height-175):
        data.mode = "mainscreen"
        init(data)
    # play button
    if (event.x>(data.width/2)-50 and event.x<(data.width/2)+50 and 
        event.y>data.height-165 and event.y<data.height-125):
        data.mode = "helpscreen"

def losescreenKeyPressed(event, data):
    if event.keysym=="p":
        data.mode = "mainscreen"
        init(data)
    if event.keysym=="h":
        init(data)
        data.mode = "helpscreen"

# helps with colors display and which youlose displays
def losescreenTimerFired(data):
    if data.time%4==0:
        data.flag4 = True
        data.flag3 = False
        data.flag2 = False
        data.flag1 = False
    if data.time%4==1:
        data.flag1 = True
        data.flag3 = False
        data.flag2 = False
        data.flag4 = False
    if data.time%4==2:
        data.flag2 = True
        data.flag3 = False
        data.flag4 = False
        data.flag1 = False
    if data.time%4==3:
        data.flag3 = True
        data.flag4 = False
        data.flag2 = False
        data.flag1 = False
    if data.time%16==4:
        data.playagaincolor = data.Orange
    if data.time%16==8:
        data.playagaincolor = data.Scarlet
    if data.time%16==12:
        data.playagaincolor = "red"
    if data.time%16==0:
        data.playagaincolor = data.darkRed

def losebackground(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill="black")
    canvas.create_image(data.width, data.height+15, anchor=SE, 
                                                            image=data.losepic)

def youLose(canvas, data):
    if data.flag1:
        canvas.create_text(data.width/2 - data.loser, data.height/2,
            text="You Lose",fill=data.darkRed, font="Arial %d" % data.losesize)
    if data.flag2:
        Silver = rgbString(190, 190, 190)
        canvas.create_text(data.width/2 + data.loser, data.height/2,
        text="You Lose",fill=data.Scarlet, font="comicsans %d" % data.losesize)
    if data.flag3: 
        canvas.create_text(data.width/2, data.height/2 + data.loser,
        text="You Lose",fill=data.Orange, font="comicsans %d" % data.losesize)
    if data.flag4:
        canvas.create_text(data.width/2, data.height/2 - data.loser,
            text="You Lose",fill="red", font="comicsans %d" %data.losesize)
    canvas.create_text(data.width/2, data.height/3,
    text="Press 'P' to play again!",fill=data.playagaincolor,font="arial 30")

def drawlPlayButton(canvas, data):
    canvas.create_rectangle(((data.width/2)-50), (data.height-215), 
                ((data.width/2)+50), (data.height-175), fill="hotPink", 
                                                        outline="Pink",width=3)
    canvas.create_rectangle(((data.width/2)-45), (data.height-210), 
                ((data.width/2)+45), (data.height-180), fill="Pink",
                                                        outline = "pink")
    canvas.create_rectangle(((data.width/2)-40), (data.height-205), 
                ((data.width/2)+40), (data.height-185), fill="hotPink", 
                                                        outline="hotPink")
    canvas.create_text(data.width/2,data.height-195,
                text="Play", fill="green", font="comicsans 26")

def drawlHelpButton(canvas, data):
    canvas.create_rectangle(((data.width/2)-50), (data.height-165), 
                ((data.width/2)+50), (data.height-125), fill="green", 
                                                 outline = "limegreen",width=3)
    canvas.create_rectangle(((data.width/2)-45), (data.height-160), 
                ((data.width/2)+45), (data.height-130), fill="limegreen", 
                                                    outline = "limegreen")
    canvas.create_rectangle(((data.width/2)-40), (data.height-155), 
                ((data.width/2)+40), (data.height-135), fill="green", 
                                                    outline = "green")
    canvas.create_text(data.width/2,data.height-145,
        text="Help", fill="hotPink", font="comicsans 26")

def drawWalnutLoseScreen(canvas, data):
    canvas.create_text(data.width/2, 20, anchor=CENTER, text 
    = "Don't leave the walnuts for too long,",
    fill = "white", font = "comicsans 24")
    if data.flag3 or data.flag4:
        canvas.create_text(data.width/2, 45, anchor=CENTER, text 
        = "they will explode!", fill = "white", font = "comicsans 24")

def losescreenRedrawAll(canvas, data):
    losebackground(canvas, data)
    youLose(canvas, data)
    drawlPlayButton(canvas, data)
    drawlHelpButton(canvas, data)
    if data.walnutlose == True:
        drawWalnutLoseScreen(canvas, data)

############################################################################
### run ### #from the class notes
############################################################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    data.timerDelay = 100 # milliseconds
    init(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
run (500, 500)
