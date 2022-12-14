# Create a flashcard app within the terminal
# Have mutliple options
# Add a new flashcard
# Play through flashcards
# Make it T/F first then move into type

flashcards = {
    "TCP stands for? ": "Transmission Control Protocol",
    "UDP stands for? ": "User Datagram Protocol",
}


def playFlashcards():
    for question, answer in flashcards.items():
        user_answer = input(question + " ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print("Incorrect. The answer is:" + answer)


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

        # Remove the flashcard from the dictionary
        del flashcards[question]
    elif action.lower() == "q":
        # Quit the program
        break


playFlashcards()
