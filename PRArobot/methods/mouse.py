import time

import pyautogui as auto


#鼠标点击的自动方法
#参数 x,y,button,nums
#x坐标
#y坐标
#button:左键，右键，滚轮
#nums:点击次数
def mouse_click(x, y, button, nums):
    time.sleep(0.5)
    thisbutton = 'left'
    if button == '右键':
        thisbutton = 'right'
    elif button == '滚轮':
        thisbutton = 'middle'
    print(x, y, thisbutton, nums)
    auto.click(int(x), int(y),clicks=int(nums),interval=0.2,button=thisbutton)

#鼠标移动的自动方法
#参数 x,y,duration
def mouse_move(x,y,duration):
    time.sleep(0.5)
    print(x,y,duration)
    auto.moveTo(int(x),int(y),duration=float(duration))

#拖动方法
def mouse_drag(x,y,duration,button):
    time.sleep(0.5)
    thisbutton = 'left'
    if button == '右键':
        thisbutton = 'right'
    elif button == '滚轮':
        thisbutton = 'middle'
    print(x,y,duration,button)
    auto.dragTo(int(x),int(y),duration=float(duration),button=thisbutton)

#鼠标滚动
def mouse_scroll(nums):
    time.sleep(0.5)
    try:
        print(nums)
        auto.scroll(int(nums))
    except Exception as e:
        print(e)

