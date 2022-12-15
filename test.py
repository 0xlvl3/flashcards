import os


def createDeck():
    while True:
        print(
            """
            -----------------------
            (c) create a new deck
            (d) delete a deck
            (l) list current decks
            (e) exit this menu
            -----------------------
              """
        )
        userInput = input("Navigate to: ")
        print("\n")
        # Create a deck
        if userInput == "c":
            directoryName = input(
                "Your deck name will be converted to lowercase\nEnter the name of the deck: "
            )
            os.mkdir(directoryName.lower())
            print(f"\nNew deck {directoryName.lower()} created!")

        # List current decks
        elif userInput == "l":
            # Removes files from the list
            files_and_directories = os.listdir()
            directories = [f for f in files_and_directories if os.path.isdir(f)]

            # Ignore directories starting with
            ignore = [".", "_"]

            # List comprehension to filter out ignore
            directories = [
                d for d in directories if not any(d.startswith(c) for c in ignore)
            ]

            # Iterate over remaining items in list, which should be directories
            print("Current decks: ")
            for directory in directories:
                print(directory)

        # Delete deck
        elif userInput == "d":

            # Warn user
            print(
                "Before you proceed this will delete all flashcards in the deck as well"
            )
            userAck = input("Do you want to proceed Y/N ").lower()

            # Delete deck
            if userAck == "y":
                deleteDeck = input(
                    "Type the name of the deck you wish to delete: "
                ).lower()
                print(deleteDeck)
                if os.path.exists(deleteDeck.lower()):
                    os.rmdir(deleteDeck.lower())
                    print(f"\n{deleteDeck.lower()} has been removed!")
                else:
                    print(f"\n{deleteDeck.lower()} is not a deck")

            else:
                # Return to menu
                continue
        # Exit
        elif userInput == "e":
            break


createDeck()
