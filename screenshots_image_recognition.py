import pyautogui

pyautogui.screenshot('screenshot_example.png')

pyautogui.locateOnScreen('calc7key.png')
pyautogui.locateCenterOnScreen('calc7key.png')
pyautogui.moveTo((1132, 755), duration=1)
pyautogui.click((1132, 755))