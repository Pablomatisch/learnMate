from functions import clear, inputwclose
import subprograms

clear()
print("Hello, I am learnMate. I can help you to learn things with the power of AI. Choose one of the following options:")
print("To close the program type '/bye'")
print("1 - Chat with me")
print("2 - learn vocabulary")
program = inputwclose("Your choose: ")
clear()
if program == "1":
    subprograms.chat()
if program == "2":
    subprograms.vocabulary()
