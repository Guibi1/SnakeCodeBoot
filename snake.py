import ttgo as dev
import net
import mate
import apps
import ui
import playerSnake as player
import objects
import textures

bg = '#000'  # general background color
currentLevel = "grass"  # grass sand space
width = 11
height = 18

# game state

me = None  # is 0 when non-networked, and 0 or 1 when networked

# the following global variables are useful for the networked version

networked = False  # are we playing over the network?
msg_type = "SNAKENET"   # type of the messages sent between the nodes, set later
ping_timer = 0      # used to check that the mate is still with us
pong_timer = 0


def reset_mate_timeout():
    global pong_timer
    pong_timer = int(5 / ui.time_delta)  # reset peer timeout to 5 seconds


def quit():  # called to quit the game
    if networked:
        for id in mate.ids:
            net.send(id, [msg_type, 'quit'])
    leave()


def leave():
    global me
    me = None  # no longer playing
    if networked:
        net.pop_handler()  # remove message_handler
    apps.menu()  # go back to app menu


def init_game():
    global me, tick_counter, playerSnake, otherSnakes, pomme, blocks, tileIsSpecial
    me = None
    tick_counter = 1
    playerSnake = player.PlayerSnake()
    otherSnakes = {}
    pomme = None
    blocks = []
    setCurrentLevel(currentLevel)

    dev.clear_screen(bg)

    x = dev.screen_width//2

    def next():
        ui.center(x, dev.font_height*5, 'SSET', '#FFF', bg)
        dev.after(1, lambda: ui.center(x, dev.font_height*6, 'GO', '#FFF', bg))
    ui.center(x, dev.font_height*4, 'READY', '#FFF', bg)
    dev.after(1, next)


def gameOver():
    global me
    me = None
    dev.clear_screen(bg)


def setCurrentLevel(level):
    global currentLevel, tileIsSpecial

    currentLevel = level
    textures.currentLevel = level

    tileIsSpecial = []
    for _ in range(width):
        row = []
        tileIsSpecial.append(row)
        for _ in range(height):
            row.append(random() > (0.9 if currentLevel == "grass" else 0.98))


tick_counter = 1
playerSnake = player.PlayerSnake()
playerSnake.display()
otherSnakes = {}
pomme = None
blocks = []
tileIsSpecial = []



def button_handler(event, resume):
    global ping_timer, pong_timer, tick_counter, pomme, blocks
    if me is None:
        return  # not yet playing or no longer playing
    if event == 'cancel':
        quit()
    elif event == 'tick':
        tick_counter += 1

        ui.center(dev.screen_width//2, dev.screen_height -
                  16, "Score " + str(playerSnake.score), '#FFF', bg)

        if tick_counter % 5 != 0:
            dev.after(ui.time_delta, resume)  # need to wait...
            return

        rallonger = False
        if pomme is None:
            if not networked or master():
                pomme = getRandomPomme()
                pomme.display()
                if networked:
                    for id in mate.ids:
                        net.send(id, [msg_type, "newPomme",
                                      pomme.sorte, pomme.x, pomme.y])
        elif playerSnake.positions[-1] == pomme.getPosition():
            playerSnake.manger(pomme, blocks, tileIsSpecial, gameOver)
            pomme = None
            rallonger = True
            for id in mate.ids:
                net.send(id, [msg_type, "eatPomme"])

        if not rallonger:
            if tileIsSpecial[playerSnake.positions[0][0]][playerSnake.positions[0][1]]:
                dev.draw_image(
                    playerSnake.positions[0][0]*11 + 7, playerSnake.positions[0][1]*11 + 7, textures.getLevel()["special"])
            else:
                dev.draw_image(
                    playerSnake.positions[0][0]*11 + 7, playerSnake.positions[0][1]*11 + 7, textures.getLevel()["normal"])

        playerSnake.move(rallonger)
        playerSnake.display()
        if networked:
            for id in mate.ids:
                net.send(id, [msg_type, "snakePositions",
                              playerSnake.positions])

        if networked:
            pong_timer -= 1
            if pong_timer < 0:
                leave()
                return
            ping_timer -= 1
            if ping_timer < 0:
                ping_timer = int(2 / ui.time_delta)  # send ping every 2 secs
                for id in mate.ids:
                    net.send(id, [msg_type, 'ping'])

        dev.after(ui.time_delta, resume)  # need to wait...
    else:
        to = playerSnake.movingTo()
        if event == 'left_down':
            if to == "L":
                playerSnake.nextY = 1
                playerSnake.nextX = 0
            elif to == "R":
                playerSnake.nextY = -1
                playerSnake.nextX = 0
            elif to == "T":
                playerSnake.nextX = -1
                playerSnake.nextY = 0
            elif to == "B":
                playerSnake.nextX = 1
                playerSnake.nextY = 0
        elif event == 'right_down':
            if to == "L":
                playerSnake.nextY = -1
                playerSnake.nextX = 0
            elif to == "R":
                playerSnake.nextY = 1
                playerSnake.nextX = 0
            elif to == "T":
                playerSnake.nextX = 1
                playerSnake.nextY = 0
            elif to == "B":
                playerSnake.nextX = -1
                playerSnake.nextY = 0
        elif event == 'left_up':
            pass
        elif event == 'right_up':
            pass
        elif event == 'left_ok':
            pass
        elif event == 'right_ok':
            pass
        resume()

def getRandomPomme():
    nbRandom = int(random()*120+1)
    x = int(random()*11)
    y = int(random()*11)

    if nbRandom > 110:
        return objects.Apple("multi", x, y)
    elif nbRandom > 100:
        return objects.Apple("portal", x, y)
    elif nbRandom > 90:
        return objects.Apple("poison", x, y)
    elif nbRandom > 80:
        p = objects.Apple("chrono", x, y)
        dev.after(5, manger(p))
        return p
    elif nbRandom > 70:
        return objects.Apple("block", x, y)
    elif nbRandom > 60:
        return objects.Apple("speed", x, y)
    elif nbRandom > 50:
        return objects.Apple("god", x, y)
    elif nbRandom > 40:
        return objects.Apple("smallDick", x, y)
    return objects.Apple("mid", x, y)



def manger(pomme):
    if pomme.sorte == "mid":
        playerSnake.score += 1

    elif pomme.sorte == "god":
        playerSnake.score += 10

    elif pomme.sorte == "block":
        bloc = objects.Blocs(
            playerSnake.positions[0][0], playerSnake.positions[0][-1])
        blocks.append(bloc)

    elif pomme.sorte == "smallDick":
        ranTemp = int((random() * (len(playerSnake.positions)/5))+1)
        for i in range(ranTemp):
            pos = playerSnake.positions.pop(0)
            if tileIsSpecial[pos[0]][pos[1]]:
                dev.draw_image(
                    pos[0]*11 + 7, pos[1]*11 + 7, textures.getLevel()["special"])
            else:
                dev.draw_image(
                    pos[0]*11 + 7, pos[1]*11 + 7, textures.getLevel()["normal"])

    elif pomme.sorte == "poison":
        gameOver()

    elif pomme.sorte == "chrono":
        if playerSnake.positions[-1] == pomme.getPosition():
            pass
        else:
            playerSnake.score -= 5

    elif pomme.sorte == "portal":
        playerSnake.nextX = 5-pomme.x
        playerSnake.nextY = 5-pomme.y


def start_game_soon(player):
    dev.after(3, lambda: start_game(player))


def start_game(player):
    global me
    me = player
    reset_mate_timeout()
    ui.track_button_presses(button_handler)  # start tracking button presses
    dev.clear_screen(bg)
    for y in range(height):
        for x in range(width):
            if (tileIsSpecial[x][y]):
                dev.draw_image(7 + x * 11, 7 + y * 11,
                               textures.getLevel()["special"])
            else:
                dev.draw_image(7 + x * 11, 7 + y * 11,
                               textures.getLevel()["normal"])


def snake_non_networked():
    init_game()
    start_game_soon(0)

# The following functions are used when playing the game over the network


def master():  # the master is the node with the smallest id
    for id in mate.ids:
        if net.id > id:
            return False
    return True


def message_handler(peer, msg):
    global pong_timer, otherSnakes, pomme, currentLevel
    if peer is None:
        if msg == 'start':
            networkStart()
        else:
            print('system message', msg)  # ignore other messages from system
    elif type(msg) is list and msg[0] == msg_type:
        if msg[1] == 'quit':
            leave()
        elif msg[1] == 'ping':
            reset_mate_timeout()
        elif msg[1] == 'snakePositions':
            if otherSnakes.get(peer, None) != None:
                if tileIsSpecial[otherSnakes[peer][0][0]][otherSnakes[peer][0][1]]:
                    dev.draw_image(
                        otherSnakes[peer][0][0]*11 + 7, otherSnakes[peer][0][1]*11 + 7, textures.getLevel()["special"])
                else:
                    dev.draw_image(
                        otherSnakes[peer][0][0]*11 + 7, otherSnakes[peer][0][1]*11 + 7, textures.getLevel()["normal"])
            otherSnakes[peer] = msg[2]
            player.displaySnake(otherSnakes[peer])
        elif msg[1] == 'newPomme':
            pomme = objects.Apple(msg[2], msg[3], msg[4])
            pomme.display()
        elif msg[1] == 'eatPomme':
            pomme = None
        elif msg[1] == 'setLevel':
            setCurrentLevel(msg[2])
        elif me == None:
            start_game_soon(master() ^ int(random() * 2))
        else:
            print('received', peer, msg)


def networkStart():
    init_game()
    for id in mate.ids:
        net.send(id, [msg_type, ""])


def snake(n):
    global networked
    networked = n

    if networked:
        mate.find(msg_type, message_handler,
                  lambda m, s: askMap(lambda: start(m, s)))

        def start(start_msg, mateStart):
            for id in mate.ids:
                net.send(id, start_msg)
                net.send(id, [msg_type, "setLevel", currentLevel])
            mateStart()
    else:
        askMap(snake_non_networked)


def askMap(then):
    color = '#4CF'

    def menu_handler(level, cont):
        if level is None:
            cont()
        elif level is False:
            apps.menu()
        else:
            setCurrentLevel(level.lower())
            then()

    dev.clear_screen(bg)
    ui.menu(4, 111, 8, 7, 2, [color, '#000'], lambda: [
            "Sand", "Grass", "Space"], "Grass", menu_handler)


apps.register('SNAKE', lambda: snake(False), False)
apps.register('SNAKENET', lambda: snake(True), True)
