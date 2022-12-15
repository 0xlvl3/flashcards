import add_Card

from add_Card import addCard
import remove_Card


addCard()
flashcards = add_Card.flashcards
correct = 0
incorrect = 0

for question, answer in flashcards.items():
    print(question + " ")
    userInput = input("Type answer: ")
    if userInput.lower() == answer.lower():
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")
        incorrect += 2

print(f"You got {correct} correct and {incorrect} incorrect")
