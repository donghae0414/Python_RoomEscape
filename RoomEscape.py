#
# 20141095  Yang,Dong-wuk
#

from bangtal import *

image_path = 'Images/RoomEscape/'

###
### Scene1
###
scene1 = Scene('Room1', image_path + '배경-2.png')
scene1.setLight(0.8)

### Scene1 Objects
scene1_switch = Object(image_path + '스위치.png')
scene1_switch.locate(scene1, 1040, 400)
scene1_switch.setScale(2)
scene1_switch.show()

scene1_door1 = Object(image_path + '문-오른쪽-닫힘.png')
scene1_door1.locate(scene1, 910, 270)
scene1_door1.show()

scene1_right_flowerpot = Object(image_path + '화분.png')
scene1_right_flowerpot.x = 1000
scene1_right_flowerpot.y = 260
scene1_right_flowerpot.locate(scene1, scene1_right_flowerpot.x, scene1_right_flowerpot.y)
scene1_right_flowerpot.show()

scene1_left_flowerpot1 = Object(image_path + '화분.png')
scene1_left_flowerpot1.locate(scene1, 100, 230)
scene1_left_flowerpot1.show()
scene1_left_flowerpot2 = Object(image_path + '화분.png')
scene1_left_flowerpot2.locate(scene1, 330, 270)
scene1_left_flowerpot2.show()
scene1_left_flowerpot3 = Object(image_path + '화분.png')
scene1_left_flowerpot3.locate(scene1, 560, 310)
scene1_left_flowerpot3.show()


### Scene1 Evenet
def scene1_left_flowerpot1_onMouseAction(x, y, action):
    showMessage('힝 속았지?')
scene1_left_flowerpot1.onMouseAction = scene1_left_flowerpot1_onMouseAction
scene1_left_flowerpot2.onMouseAction = scene1_left_flowerpot1_onMouseAction
scene1_left_flowerpot3.onMouseAction = scene1_left_flowerpot1_onMouseAction

scene1_right_flowerpot.is_moved = False
def scene1_right_flowerpot_onMouseAction(x, y, action):
    if not scene1_right_flowerpot.is_moved and action == MouseAction.DRAG_RIGHT:
        showMessage('어떻게 알았지..')
        scene1_right_flowerpot.locate(scene1, 1100, 230)
        scene1_right_flowerpot.is_moved = True
scene1_right_flowerpot.onMouseAction = scene1_right_flowerpot_onMouseAction

scene1_door1.is_closed = True
def scene1_switch_onMouseAction(x, y, action):
    if scene1_door1.is_closed:
        scene1_door1.setImage(image_path + '문-오른쪽-열림.png')
        scene1_door1.is_closed = False
    else:
        scene1_door1.setImage(image_path + '문-오른쪽-닫힘.png')
        scene1_door1.is_closed = True
scene1_switch.onMouseAction = scene1_switch_onMouseAction

def scene1_door1_onMouseAction(x, y, action):
    if action == MouseAction.CLICK:
        if not scene1_door1.is_closed:
            scene2.enter()
scene1_door1.onMouseAction = scene1_door1_onMouseAction


###
### Scene2
###
scene2 = Scene('Room2', image_path + '/배경-1.png')
scene2.is_bright = True

### Scene2 Object
scene2_right_door = Object(image_path + '문-오른쪽-닫힘.png')
scene2_right_door.is_closed = True
scene2_right_door.locate(scene2, 800, 270)
scene2_right_door.hide()

scene2_left_door = Object(image_path + '문-왼쪽-열림.png')
scene2_left_door.locate(scene2, 230, 285)
scene2_left_door.show()

scene2_keypad = Object(image_path + '키패드.png')
scene2_keypad.locate(scene2, 925, 420)
scene2_keypad.setScale(1.5)
scene2_keypad.show()

scene2_switch = Object(image_path + '스위치.png')
scene2_switch.locate(scene2, 920, 440)
scene2_switch.setScale(1.5)
scene2_switch.show()

scene2_password = Object(image_path + '암호.png')
scene2_password.locate(scene2, 400, 100)
scene2_password.hide()

scene2_key = Object(image_path + '열쇠.png')
scene2_key.hide()

### Scene2 Event
def scene2_left_door_onMouseAction(x, y, action):
    showMessage('거긴 아닌데...')
    scene1.enter()
scene2_left_door.onMouseAction = scene2_left_door_onMouseAction

def scene2_keypad_onMouseAction(x, y, action):
    showKeypad('bangtal', scene2_right_door)
scene2_keypad.onMouseAction = scene2_keypad_onMouseAction

def scene2_right_door_onKeypad():
    scene2_right_door.show()
    showMessage('열쇠와 문이 나타났다!')
    scene2_key.pick()
scene2_right_door.onKeypad = scene2_right_door_onKeypad

scene2_right_door.is_closed = True
def scene2_right_door_onMouseAction(x, y, action):
    if scene2_key.inHand:
        if scene2_right_door.is_closed:
            scene2_right_door.setImage(image_path + '문-오른쪽-열림.png')
            scene2_right_door.is_closed = False
        else:
            endGame()
scene2_right_door.onMouseAction = scene2_right_door_onMouseAction

def scene2_switch_onMouseAction(x, y, action):
    if scene2.is_bright:
        scene2.setLight(0.3)
        scene2_password.show()
    else:
        scene2.setLight(1)
        scene2_password.hide()
    scene2.is_bright = not scene2.is_bright
scene2_switch.onMouseAction = scene2_switch_onMouseAction


# Start Game
showMessage('어떤 화분을 옮겨야할까?')
startGame(scene1)
