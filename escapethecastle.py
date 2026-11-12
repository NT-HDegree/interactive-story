#Welcome the player
print("===ESCAPE THE CASTLE===")
print("Welcome sad one. You are in a bit of a tough situation, so best of luck with escaping the old king's grasp. You will need it.")

#Get player name, age and character class
charName = input("Tell me, sad one, what is your name? ")
age = int(input("Good. And how many years have you lived before now? "))
charClass = input("How sad. And what is your class? I need to know if there is anything special about you. ")
print("I think I can work with that. You might not die here.")

#Set starting values
health = 100
gold = 20
hasCellKey = False
hasChainKey = False

#Display the character profile
print("\n===CHARACTER PROFILE===")
print(f"Name: {charName}")
print(f"Age: {age}")
print(f"Class: {charClass}")
print(f"Health: {health}")
print(f"Gold: {gold}")
print(f"Has Cell Key: {hasCellKey}")

# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================

 #Introduce the scene to the player
print("You wake up in a dark castle cell.")
print("You can see a doctor, a window and an old bed.")

#Ask the player what they want to investigate
#.lower() converts their answer to lowercase
choice = input("Do you want to investigate the door, window or bed?: ").lower()

#Check whether the player chose the door
if choice == "door":
    print("You walk towards the door.")
    print("You try the handle, but it is locked.")

#Check whether the player chose the window
elif choice == "window":
    print("You look through the window")
    print("It is too small to escape through.")

#Check whether the player chose the bed
elif choice == "bed":
    print("You look under the bed.")
    print("You find a small iron key.")

else:
    print("You decide not to investigate.")