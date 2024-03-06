def number_guesser(low, high):
    print("Welcome to the number guesser! Pick a number in your mind and I'll try to guess it!")
    ready = input("Are you ready? (yes or no?)").lower()
    if ready == "yes":
        print("Great!")

        while low <= high:
            mid = (low + high)//2
            guess = input(f"Is it {mid}? (yes or no?)")
            if guess == "yes":
                print("Yay! I guessed correctly! Thanks for playing!")
                return
            elif guess == "no":
                response = input("Was that too high or too low? (high or low?)")
                if response == "high":
                    high = mid - 1
                elif response == "low":
                    low = mid + 1
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.")

    elif ready == "no":
        print()
        print("Are you ready now?")
        print()
        number_guesser(low, high)     

    else:
        print("Invalid input.")

number_guesser(0, 100)