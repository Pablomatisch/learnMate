def clear():
   print("\033[H\033[J", end="")

def inputwclose(text):
    answer = input(text)
    if answer == "/bye":
        exit()
    else:
        return answer