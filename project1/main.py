import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

rows=3
cols=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, value):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        won = True
        for column in columns:
            if column[line] != symbol:
                won = False 
                break
        if won:
            winnings += value[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range (cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end ="")
        print()


def deposit():
    while True:
        amount=input("What amount would you like to deposit?\n->₹")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0 :
                break
            else:
                print("Please enter a valid digit")
        else:
            print("Please enter a valid digit")
    return amount



def get_no_of_lines():
    while True:
        lines=input(f"Enter no of lines to bet on (1-{MAX_LINES}):")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("beyound range enter valid number")
        else:
            print("Please enter a valid digit")
    return lines

def get_bet():
    while True:
        bet=input("What is the amount you want to bet on each line?\n->₹")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET}-₹{MAX_BET}")
        else:
            print("Please enter a valid digit")
    return bet


def spin(balance):
    lines=get_no_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet * lines
        if total_bet>balance:
            print(f"You can't bet your current balance is not sufficient for betting ₹{total_bet}.Your current balance is ₹{balance}")
        else:
            break
        
    print (f"You are betting ₹{bet} on each line and total lines which you had choosen is {lines} lines so your total bet is ₹{total_bet}")
    
    slots=get_slot_machine_spin(rows,cols,symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines=check_winnings(slots, lines, bet, symbol_values)
    print(f"You Won ₹{winnings}")
    print(f"You Won on lines:", *winnings_lines)
    return winnings-total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        spins = input("Press enter to play (q to quit)")
        if spins == "q":
            break
        balance += spin(balance)
    print(f"You left with ₹{balance}")
main()