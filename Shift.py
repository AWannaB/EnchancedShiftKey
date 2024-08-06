import keyboard
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
    # Deletes the lower case letter
    keyboard.press_and_release('backspace')
    # Writes the capitalized letter
    keyboard.write(key2)
