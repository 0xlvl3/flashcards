import add_Card

from add_Card import addCard
import remove_Card


addCard()
flashcards = add_Card.flashcards
correct = 0
incorrect = 0
question_num = 0

for question, answer in flashcards.items():
    question_num += 1
    print(f"{question_num}: {question}")
    userInput = input("Type answer: ")
    if userInput.lower() == answer.lower():
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")
        incorrect += 1

print(f"\nYou got {correct} correct and {incorrect} incorrect")
