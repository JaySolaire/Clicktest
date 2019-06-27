import win32api, win32con
from win32api import GetSystemMetrics
import time
import random
import winsound


resWidth = GetSystemMetrics(0)
resHeight= GetSystemMetrics(1)
def click(x,y):
			win32api.SetCursorPos((x,y))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while(1):
		#print "hi"
		pitch = random.randint(800, 8000)
		winsound.Beep(pitch,5)
		mouseX = random.randint (5, resWidth-5)
		mouseY = random.randint (5, resHeight-5)
		click(mouseX, mouseY)
		click(mouseX, mouseY)
		#time.sleep(.100)
