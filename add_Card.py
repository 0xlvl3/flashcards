import os
import json

flashcards = {}


def addCard():
    # Create a loop to iterate over the flashcards
    while True:
        # Ask the user what they want to do
        action = input(
            """ 
                ----------------------------
                (a) add flashcard
                (s) see current flashcards
                (e) exit add mode 
                ----------------------------
                Input: """
        )
        if action.lower() == "a":
            # Ask the user for the flashcard question and answer
            question = input("Enter the flashcard question: ")
            answer = input("Enter the flashcard answer: ")
            # Add the flashcard to the dictionary
            flashcards[question] = answer

            specifyDeck = input("Name of the deck you wish to add this card: ")
            if os.path.isdir(specifyDeck):
                print(f"{specifyDeck} exists")
                print(f"Card has been added to {specifyDeck}")

                with open(f"{specifyDeck}/flashcard.txt", "a") as file:
                    json_data = json.dumps(flashcards)
                    file.write(json_data)
            else:
                userInput = input(
                    f"{specifyDeck} doesn't exist do you want to create it? Y/N"
                ).lower()
                if userInput.lower() == "y":
                    os.mkdir(specifyDeck)
                    with open(f"{specifyDeck}/flashcard.txt", "a") as file:
                        json_data = json.dumps(flashcards)
                        file.write(json_data)

                else:
                    print("Returning to menu")
                    continue

        elif action.lower() == "s":
            for question, answer in flashcards.items():
                print("Question: " + question)
                print("Answer: " + answer)
        elif action.lower() == "e":
            break


addCard()
