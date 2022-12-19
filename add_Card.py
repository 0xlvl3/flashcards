import os
import json

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
                ----------------------------
                (a) add flashcard
                (i) inspect deck (will show current flashcards)
                (e) exit add mode 
                ----------------------------
                Input: """
        )

        if action.lower() == "a":
            # Ask the user for the flashcard question and answer
            question = input("Enter the flashcard question: ").lower()
            answer = input("Enter the flashcard answer: ").lower()

            specifyDeck = input("Name of the deck you wish to add this card: ").lower()
            if os.path.isdir(specifyDeck):
                print(f"{specifyDeck} exists")
                with open(f"{specifyDeck}/flashcard.json", "r") as file:
                    flashcards = json.load(file)
                if check_key_value_pair(question, answer, flashcards):
                    print("The flashcard already exists")
                    continue
                # Add the flashcard to the dictionary
                flashcards[question] = answer
                print(f"Card has been added to {specifyDeck}")
                with open(f"{specifyDeck}/flashcard.json", "w") as file:
                    json.dump(flashcards, file)
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

        elif action.lower() == "i":
            specifyDeck = input("Name of the deck you wish to inspect: ").lower()
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
                        ---------------------------------------
                        Question: {question}: answer: {answer}
                        """
                        )
            else:
                print(f"{specifyDeck} doesn't exist returning to menu")
            continue

        elif action.lower() == "e":
            break


addCard()
