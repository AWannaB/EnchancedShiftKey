import keyboard
import time
# Starts a Loop
while True:
    # Pauses the porgram until the shift key is pressed
    keyboard.wait('shift')
    # Easiest way to get rid of the problem where the code will read the shift key and capitalize it
    key0 = keyboard.read_key()
    # Reads the key that needs the be capitalized 
    key1 = keyboard.read_key()
    # If the key is not in the alphabet and if it is only 1 character it will not run
    if key1.isalpha() and len(key1) == 1:
        # Capitalize they key
        key2 = key1.upper()
        # Deletes the lowercase letter
        keyboard.press_and_release('backspace')
        time.sleep(0.05)
        # Writes the capitalized key 
        keyboard.write(key2)
    else:
        continue
