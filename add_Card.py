def addCard():
    # Create a loop to iterate over the flashcards
    while True:
        # Ask the user what they want to do
        action = input(
            "Do you want to (a)dd a flashcard, (r)emove a flashcard, or (q)uit? "
        )

        if action.lower() == "a":
            # Ask the user for the flashcard question and answer
            question = input("Enter the flashcard question: ")
            answer = input("Enter the flashcard answer: ")

            # Add the flashcard to the dictionary
            flashcards[question] = answer
        elif action.lower() == "r":
            # Ask the user for the flashcard question
            question = input("Enter the flashcard question: ")

        else:
            break
