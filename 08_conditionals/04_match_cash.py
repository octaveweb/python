a = int(input("Gusse the number between (0 - 9): "))
match a:
    case 4:
        print("The number is 4 you ( Win )")
    case 6:
        print("The number is 6 you ( Win )")
    case 9:
        print("The number is 9 you ( Win )")
    case _:
        print("Better Luck next time!")