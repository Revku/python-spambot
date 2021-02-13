import pyautogui, time
delay = open('config/delay.txt', 'r').read()
print('Spam will be started for', delay, 'seconds...')
time.sleep(int(delay))
messages = open('config/messages.txt', 'r');

for message in messages:
    pyautogui.typewrite(message)
    pyautogui.press('enter')