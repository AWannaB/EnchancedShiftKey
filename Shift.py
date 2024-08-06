import keyboard
while True:
    keyboard.wait('shift')
    key0 = keyboard.read_key()
    key1 = keyboard.read_key()
    key2 = key1.upper() if key1.isalpha() else key1
    keyboard.press_and_release('backspace')
    keyboard.write(key2)
