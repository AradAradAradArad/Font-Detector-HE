# import pyautogui
# import time
# import random
#
# def pick_random_values(arr, num_values=5):
#     # Ensure the array has enough elements
#     if len(arr) < num_values:
#         raise ValueError("Array does not have enough elements")
#
#     # Use random.sample to pick num_values random elements from the array
#     random_values = random.sample(arr, num_values)
#     print(random_values)
#     return random_values
#
# # Wait for a few seconds to give time to switch to the desired window
# time.sleep(5)
#
# letters=['t','c','d','s','v','u','z','j','y','h','f','k','n','b','x','g','p','m','e','r','a',',',';','.','l','o','i']
#
# for i in range(1000):
#     pyautogui.hotkey(pick_random_values(letters))
#     pyautogui.hotkey('enter', 'enter')
#
#     pyautogui.keyDown('ctrl')
#     pyautogui.keyDown('a')
#
#     pyautogui.keyUp('a')
#     pyautogui.keyUp('ctrl')
#
#     pyautogui.hotkey('enter')
#
#     pyautogui.hotkey('backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace','backspace')
#
#
#
#