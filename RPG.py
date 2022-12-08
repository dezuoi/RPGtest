#Global variabel for våpen. Den vil enten være true eller false, avhengig av om spilleren har funnet den ennå eller ikke. Våpenet kan endre utfallet i noen av rommene.
weapon = False


#Om spilleren har funnet våpenet, så kan de bruke det til å drepe monsteret de møter på her og rømme.
#Om de ikke har våpenet så kan de bare rømme, eller så blir de drept om de velger å slåss.
def strangeCreature():
    actions = ["fight","flee"]
    global weapon
    print("A strange ghoul like creature has appeared. You are scared, but you can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You kill the ghoul with the knife you found earlier. After moving forward, you find an exit and escape.")
                print("Would you like to quit, or retry?")
                print("Options: quit/retry")
                userInput = input()
                if userInput == "quit":
                    quit()
                if userInput == "retry":
                    break
            else:
                print("The ghoul has killed you.")
                print("Would you like to quit, or retry?")
                print("Options: quit/retry")
                userInput = input()
                if userInput == "quit":
                    quit()
                if userInput == "retry":
                    break
        elif userInput == "flee":
            showSkeletons()
        else:
            print("Please enter a valid option.")

#Dette er et av rommene der spilleren kan finne våpenet. Om spilleren finner det, så blir weapon variabelen satt til true.
#De kan bruke våpenet i det neste rommet om de finner det.
def showSkeletons():
    directions = ["backward","forward"]
    global weapon
    print("You see a wall of skeletons as you walk into the room. You have this eerie feeling, like someone is watching you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
            weapon = True
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            strangeCreature()
        else:
            print("Please enter a valid option.")

#Dette er enda et sted der spilleren kan rømme, eller bli drept. Uansett hva skjer så får de igjen et valg om de vil retry eller quit.
def hauntedRoom():
    directions = ["right","left","backward"]
    print("You hear strange voices. You think you have awoken some of the dead. Wwhere would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("Multiple ghoul-like creatures start emerging as you enter the room. You are murdered.")
            print("Would you like to quit, or retry?")
            print("Options: quit/retry")
            userInput = input()
            if userInput == "quit":
                quit()
            if userInput == "retry":
                break
        elif userInput == "left":
            print ("You made it! You found an exit.")
            print("Would you like to quit, or retry?")
            print("Options: quit/retry")
            userInput = input()
            if userInput == "quit":
                quit()
            if userInput == "retry":
                break
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")


#Om spilleren valgte å gå right fra forrige scenen, ender de opp her. Dette er ett av stedene de kan finne en utgang.
#Om de når utgangen så får de et valg om å retry, eller quit. De kan også gå backward fra her.
def cameraScene():
    directions = ["forward","backward"]
    print("You see a camera that has been dropped on the ground. Someone has been here recently. What would you like to do?")
    userInput =""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            print("You made it! You've found an exit.")
            print("Would you like to quit, or retry?")
            print("Options: quit/retry")
            userInput = input()
            if userInput == "quit":
                quit()
            if userInput == "retry":
                break
        elif userInput == "backward":
            showShadowFigure()
        else: print("Please enter a valid option.")

#Om spilleren går backward fra dette rommet, går de tilbake til intro scenen.
#Om de går left eller right så spilles en ny scene av.
def showShadowFigure():
    directions = ["right","backward"]
    print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            cameraScene()
        elif userInput == "left":
            print("You find that this door opens into a wall.")
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")


#introScene() funksjonen. Starter eventyret og gir spilleren et valg om hvor de vil gå videre. Avhengig av hva spilleren velger, så starter en annen scene.
#For eksempel. hvis brukeren skriver "left", så begynner showShadowFigure() scenen. 
def introScene():
    directions = ["left","right","forward"]
    print("You are at a crossroads and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput =""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input() 
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "forward":
            hauntedRoom()
        elif userInput == "backward":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")

#Startfunksjonen. Gir en velkomst til spilleren så starter den en annen funksjon introScene(). Spilleren kan skrive navnet sitt her.
if __name__ == "__main__":
    while True:
        print("Welcome!")
        print("As a passionate traveler, you have decided to visit (place).")
        print("However, during your adventures, you managed to get lost.")
        print("Let's start with your name.")
        name = input()
        print("Have fun, " +name+ ".")
        introScene()
