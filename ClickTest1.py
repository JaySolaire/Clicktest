import win32api, win32con
import time
def click(x,y):
			win32api.SetCursorPos((x,y))
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

while 1:
	click(1000,100)
	time.sleep(10)