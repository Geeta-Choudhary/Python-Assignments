'''
import os

if __name__ == '__main__':
    print("Welcome to My RboSpeaker")
    while True:
        x = input("Enter what you want me to speak:")
        if x =="u":
            os.system("say 'Thank you for using me!'")
            break
        command = f"say {x}"
        os.system(command)
'''

import os
import win32com.client

while True:
    x=input(f"Enter the word you want say: ")
    if x == 'q':
        speaker.Speak("bye bye friend")
        break
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(x )



