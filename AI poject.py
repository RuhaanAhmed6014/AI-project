import random
import time

# ===============================
# MEMORY MATCHING GAME
# ===============================

def generate_pairs():
    symbols = list(range(8)) * 2  # 8 pairs
    random.shuffle(symbols)
    return symbols

def display_memory_board(cards, revealed):
    print("\n🧠 Memory Matching Game")
    print("------------------------")
    for i in range(0, 16, 4):
        row = [str(cards[j]) if revealed[j] else "*" for j in range(i, i+4)]
        print(" ".join(row))
    print("------------------------")

def play_memory_game():
    cards = generate_pairs()
    revealed = [False] * 16
    attempts = 0
    matches = 0

    print("🔍 Memorize the positions! You have 5 seconds...")
    display_memory_board(cards, [True] * 16)
    time.sleep(5)

    while matches < 8:
        display_memory_board(cards, revealed)

        try:
            choice1 = int(input("Pick your first card (0–15): "))
            if revealed[choice1]:
                print("⚠️ Already revealed. Try another.")
                continue

            revealed[choice1] = True
            display_memory_board(cards, revealed)

            choice2 = int(input("Pick your second card (0–15): "))
            if choice1 == choice2 or revealed[choice2]:
                print("⚠️ Invalid second choice. Try again.")
                revealed[choice1] = False
                continue

            revealed[choice2] = True
            display_memory_board(cards, revealed)

            attempts += 1
            if cards[choice1] == cards[choice2]:
                print("✅ Match found!")
                matches += 1
            else:
                print("❌ Not a match.")
                time.sleep(1)
                revealed[choice1] = False
                revealed[choice2] = False

        except (ValueError, IndexError):
            print("⚠️ Invalid input. Enter numbers between 0 and 15.")

    print(f"\n🎉 You completed the game in {attempts} attempts!")

# ===============================
# TIC TAC TOE
# ===============================

def create_ttt_grid():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_ttt_board(board):
    print("\n🎯 Tic Tac Toe")
    print("    A   B   C")
    for i, row in enumerate(board):
        print(f" {i+1}  " + " | ".join(row))
        if i < 2:
            print("   ---+---+---")
    print()

def get_ttt_symbols():
    symbol_1 = input("Player 1, choose X or O: ").upper()
    while symbol_1 not in ["X", "O"]:
        symbol_1 = input("Invalid input. Please enter X or O: ").upper()
    symbol_2 = "O" if symbol_1 == "X" else "X"
    print(f"✅ Player 1: {symbol_1}, Player 2: {symbol_2}")
    return symbol_1, symbol_2

def get_ttt_input(board):
    col_map = {'A': 0, 'B': 1, 'C': 2}
    row_map = {'1': 0, '2': 1, '3': 2}

    while True:
        row = input("Row (1-3): ").strip()
        col = input("Column (A-C): ").strip().upper()

        if row in row_map and col in col_map:
            r = row_map[row]
            c = col_map[col]
            if board[r][c] == " ":
                return r, c
            else:
                print("⚠️ That spot is already taken.")
        else:
            print("⚠️ Invalid row or column.")

def is_ttt_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)): return True
        if all(board[j][i] == symbol for j in range(3)): return True
    if all(board[i][i] == symbol for i in range(3)): return True
    if all(board[i][2-i] == symbol for i in range(3)): return True
    return False

def play_ttt_game():
    board = create_ttt_grid()
    symbol_1, symbol_2 = get_ttt_symbols()
    current_symbol = symbol_1
    moves = 0

    print_ttt_board(board)

    while moves < 9:
        print(f"🎮 Move {moves + 1}: Player {current_symbol}")
        r, c = get_ttt_input(board)
        board[r][c] = current_symbol
        print_ttt_board(board)

        if is_ttt_winner(board, current_symbol):
            print(f"🎉 Player {current_symbol} wins!")
            return

        current_symbol = symbol_2 if current_symbol == symbol_1 else symbol_1
        moves += 1

    print("🤝 It's a tie!")

# ===============================
# ROCK PAPER SCISSORS
# ===============================

def play_rps_game():
    options = ["rock", "paper", "scissors"]
    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in options:
            print("⚠️ Invalid input.")
            continue

        computer = random.choice(options)
        print(f"🖥️ Computer chose: {computer}")

        if user == computer:
            print("🤝 It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break

# ===============================
# NUMBER GUESSING GAME
# ===============================

def play_guess_game():
    print("🎯 Guess the Number (1 to 100)!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("📉 Too low.")
            elif guess > number:
                print("📈 Too high.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

# ===============================
# MAIN MENU
# ===============================

def main():
    while True:
        print("\n🎮 WELCOME TO THE GAME HUB 🎮")
        print("1. Tic Tac Toe")
        print("2. Memory Matching")
        print("3. Rock Paper Scissors")
        print("4. Number Guessing")
        print("5. Exit")

        choice = input("Select a game (1–5): ")

        if choice == "1":
            play_ttt_game()
        elif choice == "2":
            play_memory_game()
        elif choice == "3":
            play_rps_game()
        elif choice == "4":
            play_guess_game()
        elif choice == "5":
            print("👋 Thanks for playing. Goodbye!")
            break
        else:
            print("⚠️ Invalid selection. Try again.")

# Run the main menu
if __name__ == "__main__":
    main()
