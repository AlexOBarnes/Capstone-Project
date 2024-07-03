def drawing(num, wrong_letters):
    images = [r"""
    +---+
        |
        |
        |
        |
        |
  =========""", r"""
    +---+
    |   |
        |
        |
        |
        |
  =========""", r""" 
    +---+
    |   |
    O   |
        |
        |
        |
  =========""", r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========""", r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========="""]
    print(f"The hallows are as follows:\n{images[num-1]}")
    if num == 1:
        print(f"\nSo far you have made {num} wrong guess")
    elif 1 < num < 8:
        print(f"\nSo far you have made {num} wrong guesses")
    print(f"The letters you have guessed wrong so far are as follows: {(','.join(wrong_letters)).upper()}\n")
