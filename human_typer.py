import pyautogui
import time
import random

# --- IMPORTANT ---
# FAILSAFE: To stop the script immediately, slam your mouse into the
#           top-left corner of your screen!
pyautogui.FAILSAFE = True

# --- The text you want to type ---
text_to_type = """
Hello, I am a very realistic human typing simulation.
I'm simulating continuous activity directly in your VSCode editor,
with natural, random pauses between each character.
You'll notice I pause slightly at punctuation like commas, periods, and new lines.
This script is currently running on your Chromebook's Linux environment!
"""

# --- GET READY ---
# Gives you 5 seconds to click on the editor window where you want the typing to start.
print("--- Starting Human Typer Script ---")
print("Click on your VSCode editor window NOW. You have 5 seconds...")
time.sleep(5)
print("Typing started...")


# --- The "Human" Typing Loop ---
for char in text_to_type:
    # 1. Type the character
    pyautogui.write(char)
    
    # 2. Calculate a base random delay (30ms to 120ms)
    delay = random.uniform(0.03, 0.12)
    
    # 3. Add extra human-like pauses for certain characters
    if char in [',', '.', '?', '!']:
        delay += random.uniform(0.15, 0.35) # Longer pause for punctuation
    elif char == ' ':
        delay += random.uniform(0.02, 0.08)  # Small hesitation at spaces
    elif char == '\n':
        delay += random.uniform(0.4, 0.9)  # "Thinking" pause for a new line
        
    # 4. Apply the calculated delay
    time.sleep(delay)

print("Typing simulation finished.")
