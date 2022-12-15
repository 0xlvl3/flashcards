flashcards = {}


def addCard():
    # Create a loop to iterate over the flashcards
    while True:
        # Ask the user what they want to do
        action = input(
            "Do you want to (a)dd a flashcard, (s)ee current questions and answers or (q)uit? "
        )
        if action.lower() == "a":
            # Ask the user for the flashcard question and answer
            question = input("Enter the flashcard question: ")
            answer = input("Enter the flashcard answer: ")
            # Add the flashcard to the dictionary
            flashcards[question] = answer
        elif action.lower() == "s":
            for question, answer in flashcards.items():
                print("Question: " + question)
                print("Answer: " + answer)
        elif action.lower() == "q":
            break
