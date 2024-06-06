import pyautogui as auto
import pyperclip

#英文输入
def input_english(english):
    auto.typewrite(english,interval=0.05)

#中文输入 使用复制粘贴实现
def input_chinese(chinese):
    pyperclip.copy(chinese)
    auto.hotkey('ctrl', 'v')

#快捷键
def input_hotkey(hotkeya,hotkeyb,hotkeyc):
    hotkeys = []
    if hotkeya != "":
        hotkeys.append(hotkeya)
    if hotkeyb != "":
        hotkeys.append(hotkeyb)
    if hotkeyc != "":
        hotkeys.append(hotkeyc)
    auto.hotkey(*hotkeys)

