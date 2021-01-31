import pyautogui
import pyperclip
import random
from datetime import datetime
pyautogui.FAILSAFE = False
def kp(a):
    pyautogui.hotkey("Tab", interval=0.1)
    pyperclip.copy(a)
    pyautogui.hotkey("ctrl", "v")
x,y=pyautogui.size()
pyautogui.click(x/2, y*2/5)
kp("阙铭君")
kp("河南办事处")
kp("无") if datetime.now().isoweekday()==1 or datetime.now().isoweekday()==7 else kp("到岗办公")
kp("无") if datetime.now().isoweekday()==6 or datetime.now().isoweekday()==7 else kp("到岗办公")
kp("已学习，来源：运营管理部")
kp("全部健康")
kp(round(random.uniform(36.2,36.8),1))
kp(round(random.uniform(36.2,36.8),1))
kp("无")
kp("无")
kp("无")
kp("无")
pyautogui.click((x/2,y*3/4-75))