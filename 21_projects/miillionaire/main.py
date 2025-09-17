qustions = [
    ["Who is srk?", "WWE Fighter", "Panwala", "Hakla meme", "A famous Indian actor and film producer", 4],
    ["What is SRK's full name?", "Shah Rukh Khan", "Shah Raj Kumar", "Sanjay Kapoor", "Salman Khan", 1],
    ["Which movie is known for SRK's iconic 'K-K-K-Kiran' dialogue?", "Kuch Kuch Hota Hai", "Dilwale Dulhania Le Jayenge", "Darr", "Dil To Pagal Hai", 3],
    ["SRK is often referred to as the 'King of...'", "Comedy", "Bollywood", "Romance", "Action", 2],
    ["Which of these is a movie starring Shah Rukh Khan?", "Gadar: Ek Prem Katha", "Pathaan", "Baahubali: The Beginning", "Dhoom", 2]
]
prize = [100,200, 500, 1000, 100000]
i = 0
def greandPrize():
    for prize in range(10):
        print(f"You won {prize[i]}$ ______\n")

for qustion in qustions:
    print(qustion[0])
    print(f"a. {qustion[1]}")
    print(f"b. {qustion[2]}")
    print(f"c. {qustion[3]}")
    print(f"d. {qustion[4]}")

    # chake if ans corect or not
    try:
        a =  int(input("Enter your answer. \n1 = a, 2 = b, \n3 = c, 4 = d\nChose any: "))

        if(qustion[5] == a):
            print(f"\n______Correct Answer You won {prize[i]}$ ______\n")
            i = i + 1
        else:
            print(f"Incorrect, the answer is {qustion[5]}")
            print("=============== Better luck next time! ===============")
            break
    except Exception as e:
        print("=============== Better luck next time! ===============")
        break