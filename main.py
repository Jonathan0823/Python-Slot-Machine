import random
def spin_row():
    symbols = ["🍒", "🍉", "🔔", "⭐", "🤣"]
    result = [random.choice(symbols) for i in range(3)]
    return result


def show_row(row):
    print("===============")
    print(row[0] + " | " + row[1] + " | " + row[2])
    print("===============")

def get_payment(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🔔":
            return bet * 2
        elif row[0] == "⭐":
            return bet * 1
        elif row[0] == "🤣":
            return bet * 10

    return 0

def main():
    balance = 100

    print("=======Welcome to Python Slot Machine=======")
    print("Symbols: 🍒 🍉 🔔 ⭐ 🤣")
    print("===========================================")

    while balance > 0:
        print(f"Your balance is ${balance:,.2f}")
        print("===========================================")
        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Invalid input")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Invalid bet")
            continue

        balance -= bet

        print("Spinning...")
        row = spin_row()
        show_row(row)

        payout = get_payment(row, bet)
        if payout > 0:
            print(f"You won ${payout:,.2f} 🤑🤑🤑🤑💵💵💵🤑🤑💵🤑🤑")
        else:
            print("You lost")

        balance += payout

        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() != "y":
            break
        else:
            continue
    
    if balance == 0:
        print("You ran out of money 😭")

    print("Thank you for playing")

     

if __name__ == "__main__":
    main()