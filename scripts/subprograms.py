from functions import clear, inputwclose
import generate_answer
import pickle
import os
import glob
import time

path = os.path.dirname(os.path.realpath(__file__))

def chat():
    print("AI: Hi, i'm your assistant. How can i help you? Please keep your question short and to the point.")
    while True:
        question = input("You: ")
        if question == "/bye":
            break
        generate_answer.generatestream(question)
        #answer = generate_answer.generate(question)
        #print("AI: " + answer)
    clear()
def vocabulary():
    while True:
        print("Choose beetween these options:")
        print("1 - Create new list")
        print("2 - Edit list")
        print("3 - Show list")
        print("4 - Learn simple")
        print("5 - Learn with chat")
        print("6 - Exit")

        choose = input("Your choose: ")
        clear()
        if choose == "1":
            name = input("Name of list: ")
            list = []
            print("Now add words like this to the list: 'Hallo Welt(vocabulary) - hello world(translation)', when you are done just type '/done'")
            while True:
                word = input("Word: ")
                if word == "/done":
                    break
                else:
                    list.append(word)
            
            with open(f'{path}/cache/lists/{name}.pkl', 'wb') as f:
                pickle.dump(list, f)
            print("List created: " + name)
            for i in range(len(list)):
                print(str(i) + " - " + list[i])

        if choose == "2":
            print("Which list do you want to edit?:")
            print(glob.glob(f"{path}/cache/lists/*.pkl"))
            listname = input("Name of list: ")

            with open(f'{path}/cache/lists/{listname}.pkl', 'rb') as f:
                list = pickle.load(f)
            clear()
            while True:
                clear()

                for i in range(len(list)):
                    print(str(i) + " - " + list[i])
                print("------")
                print("Choose an option:")
                print("1 - Add words")
                print("2 - Remove words")
                print("3 - sort list")
                print("4 - delete list")
                print("5 - Exit")

                choose = input("Your choose: ")

                if choose == "1":
                    print("Now add words like this to the list: 'Hallo Welt(vocabulary) - hello world(translation)', when you are done just type '/done'")
                    while True:
                        word = input("Word: ")
                        if word == "/done":
                            break
                        else:
                            list.append(word)
                
                if choose == "2":
                    print("Which word do you want to remove?:")
                    print(list)
                    word = input("Word: ")
                    list.remove(word)
                
                if choose == "3":
                    list.sort()
                
                if choose == "4":
                    os.remove(f'{path}/cache/lists/{listname}.pkl')
                    print("List deleted: " + listname)
                    time.sleep(3)
                    clear()
                    break

                if choose == "5":
                    with open(f'{path}/cache/lists/{listname}.pkl', 'wb') as f:
                        pickle.dump(list, f)
                    clear()
                    break


        if choose == "3":
            print("Which list do you want to show?:")
            print(glob.glob(f"{path}/cache/lists/*.pkl"))
            listname = input("Name of list: ")
            with open(f'{path}/cache/lists/{listname}.pkl', 'rb') as f:
                list = pickle.load(f)
            clear()
            print("List: " + listname)
            for i in range(len(list)):
                print(str(i) + " - " + list[i])
            input("Press any key to continue...")

        if choose == "4":
            print("Which list do you want to learn?:")
            print(glob.glob(f"{path}/cache/lists/*.pkl"))
            listname = input("Name of list: ")
            with open(f'{path}/cache/lists/{listname}.pkl', 'rb') as f:
                list = pickle.load(f)
            clear()
            for i in range(len(list)):
                print("translation: " + list[i].split(" - ")[1])
                useranswer = input("Your answer: ")
                if useranswer == list[i].split(" - ")[0]:
                    print("Correct")
                else:
                    print("Wrong - correct answer: " + list[i].split(" - ")[0])
                input("Press any key to continue...")
                clear()
        
        if choose == "5":
            print("Which list do you want to learn?:")
            print(glob.glob(f"{path}/cache/lists/*.pkl"))
            listname = input("Name of list: ")
            with open(f'{path}/cache/lists/{listname}.pkl', 'rb') as f:
                list = pickle.load(f)
            clear()
            print("Start a conversation by typing...   ---   '/bye' to exit")
            while True:
                question = input("You: ")
                if question == "/bye":
                    break
                else:
                    generate_answer.generatestream(f"{question} /// This was the users question, make a conversation with him and try to use only standard vocabulary and words from this list:{list}, speak in the language he was typing in! Keep your answered shortly!!! ")

        if choose == "6":
            clear()
            break
            


# Laden aus der Datei
# with open(f'{name}.pkl', 'rb') as f:
#     loaded_list = pickle.load(f)

# print(loaded_list)