import pyautogui

print(pyautogui.size(), '\n')
width, height = pyautogui.size()
print(pyautogui.position(), '\n')

pyautogui.moveTo(10, 10, duration=1.5)
pyautogui.moveRel(200, 0, duration=2)
pyautogui.moveRel(0, -100, duration=1)

pyautogui.click(701, 23)
pyautogui.doubleClick()
pyautogui.rightClick()

pyautogui.displayMousePosition()