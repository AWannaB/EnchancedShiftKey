import keyboard
import time
# Starts an infinite loop
while True:
    # The program does nothing until the Shift key is pressed
    keyboard.wait('shift')
    # Reads the shift key (this is the fastest way to solve the issue of the code capitalizing the shift key and having no effect)
    key0 = keyboard.read_key()
    # Reads the key that needs to be capitalized
    key1 = keyboard.read_key()
    # Capitalizes the key if it is an alphabetic key and does nothing if it is not
    key2 = key1.upper() if key1.isalpha() else key1
    # Stops from printing the following keys
    if key2 == key1 or key2 == 'SHIFT' or key2 == 'RIGHT SHIFT' or key2 == 'ENTER':
        continue
    elif key2 == 'BACKSPACE' or key2 == 'TAB' or key2 == 'CTRL' or key2 == 'SPACE' or key2 == 'ALT':
        continue
    else:
        # Deletes the lower case letter
        keyboard.press_and_release('backspace')
        '''Fixes bug on lower-end systems form interpreting the 
        backspace and writeing the capitalized letter in the wrong order'''
        time.sleep(0.05)
        # Writes the capitalized letter
        keyboard.write(key2)
