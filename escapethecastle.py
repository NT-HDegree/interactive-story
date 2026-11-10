#Welcome the player
print("===ESCAPE THE CASTLE===")
print("Welcome sad one. You are in a bit of a tough situation, so best of luck with escaping the old king's grasp. You will need it.")

#Get player name, age and character class
charName = input("Tell me, sad one, what is your name? ")
age = int(input("Good. And how many years have lead up to this moment?"))
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
print(f"Has Chain Key: {hasChainKey}")

#Begin the story
print("\nYou wake up in the dingy cell of a castle, your ankle chained to the floor with a medium-length chain")
print("Good luck with escaping.")