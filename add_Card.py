import os
import json
import shutil

flashcards = {}


def check_key_value_pair(question, answer, json_data):
    if question in json_data and json_data[question] == answer:
        return True
    return False


def addCard():
    # Create a loop to iterate over the flashcards
    while True:
        # Ask the user what they want to do
        action = input(
            """       
                        #--------------------------------------#
                        |          TERMINAL FLASHCARDS         |
                        |        ----------------------        |
             _.---------|.--..      Select an option           |
          .-'  `      .'/   ``;                                |
       .-'           .' |    /;                                |
    .-'         |   /   `.__//                                 |
 .-'           _.--/        /    (c) create deck               |
|        _  .-'   /        /     (a) add flashcard             |
|     ._  \      /     `  /      (p) play deck                 |
|        ` .    /     `  /       (i) inspect deck              |
|         \ \ '/        /        (d) delete deck               |
|        - \  /        /|        (e) exit program              |
|        '  .'        / |                                      |
|          '         |.'|                                      |
|                    |  | Made by: 0xlvl3                      |
|                    |  #--------------------------------------#
|                    |.'                                       
|                    /                                         
|                   /                                          
|                  /                                           
'------------------#
                Input: """
        )

        if action.lower() == "a":
            # Ask the user for the flashcard question and answer
            question = input("\nEnter the flashcard question: ").lower()
            answer = input("Enter the flashcard answer: ").lower()

            specifyDeck = input("Name of the deck you wish to add this card: ").lower()
            if os.path.isdir(specifyDeck):
                with open(f"{specifyDeck}/flashcard.json", "r") as file:
                    flashcards = json.load(file)
                if check_key_value_pair(question, answer, flashcards):
                    print("The flashcard already exists")
                    continue
                # Add the flashcard to the dictionary
                flashcards[question] = answer
                print(f'\n### "{question}" card has been added to {specifyDeck}')
                with open(f"{specifyDeck}/flashcard.json", "w") as file:
                    json.dump(flashcards, file, indent=4)
            else:
                userInput = input(
                    f"{specifyDeck} doesn't exist do you want to create it? Y/N:  "
                ).lower()
                if userInput.lower() == "y":
                    os.mkdir(specifyDeck)
                    with open(f"{specifyDeck}/flashcard.json", "w") as file:
                        flashcards = {question: answer}
                        json.dump(flashcards, file, indent=4)
                else:
                    print("Returning to menu")
                    continue

        # Inspect deck
        elif action.lower() == "i":
            specifyDeck = input("Name of the deck you wish to inspect: ").lower()

            # If deck exists
            if os.path.exists(specifyDeck):
                json_file = None
                for file in os.listdir(specifyDeck):
                    if file.endswith(".json"):
                        json_file = file
                        break
                print(f"These are the current flashcards in {specifyDeck}")
                with open(os.path.join(specifyDeck, json_file)) as f:
                    data = json.load(f)
                    for question, answer in data.items():
                        print(
                            f"""
            +---------------------------------------
            | Question: {question}
            | Answer: {answer}
                        """
                        )

            # If deck doesn't exist
            else:
                userInput = input(
                    f"\n{specifyDeck} doesn't exist do you want to create it? Y/N:  "
                ).lower()
                if userInput.lower() == "y":
                    os.mkdir(specifyDeck)
                    with open(f"{specifyDeck}/flashcard.json", "w") as file:
                        flashcards = {}
                        json.dump(flashcards, file)
                        print(f"\n{specifyDeck} has been created, go add flashcards!")
                else:
                    print("Returning to menu")
                    continue

        # Create deck
        elif action.lower() == "c":
            print("\n### Deck will be saved all lowercase")
            userInput = input(f"\nName your neck deck: ").lower()
            os.mkdir(userInput)
            with open(f"{userInput}/flashcard.json", "w") as file:
                flashcards = {}
                json.dump(flashcards, file)
                print(f"\n{userInput} has been created, go add flashcards!")

        # Delete deck
        elif action == "d":

            # Warn user
            print(
                "\nBefore you proceed this will delete all flashcards in the deck as well"
            )
            userAck = input("Do you wish to proceed Y/N : ").lower()

            # Delete deck
            if userAck == "y":
                deleteDeck = input(
                    "\nType the name of the deck you wish to delete: "
                ).lower()
                if os.path.exists(deleteDeck):
                    shutil.rmtree(deleteDeck)
                    print(f"\n{deleteDeck} has been removed!")
                else:
                    print(f"\n{deleteDeck} is not a deck")
            else:
                # Return to menu
                continue

        # Play Deck
        elif action == "p":
            userInput = input("Which deck do you want to run through? ").lower()
            if os.path.exists(userInput):
                with open(f"{userInput}/flashcard.json", "r") as f:
                    data = json.load(f)
                    cardCount = 0
                    correct = 0
                    incorrect = 0
                    for question, answer in data.items():
                        cardCount += 1
                        print("\n")
                        print(f"{cardCount}. {question}")
                        userAnswer = input("Type answer here: ").lower()
                        if userAnswer == answer:
                            correct += 1
                        else:
                            incorrect += 1

                    print(
                        f"""
(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧・ﾟ✧
Out of {cardCount} you got {correct} correct and {incorrect} incorrect
                        """
                    )

            else:
                print(f"{userInput} deck does not exist returning to menu")

        # Exit program
        elif action.lower() == "e":
            exit()


addCard()
