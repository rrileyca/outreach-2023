import string
import time
import hashlib
import curses
import itertools

# A list of common passwords to try first
common_passwords = ["123456", "password", "qwerty", "111111", "abc123", "iloveyou", "letmein", "monkey", "dragon",
                    "master"]


# A function to generate a sequential password of a given length
def generate_password(characters, length):
    # Use itertools.product to create an iterator that returns all possible combinations of the chosen characters
    # Use itertools.islice to skip the first n passwords that have been tried before
    # Use next to get the next password from the iterator
    global n  # Use a global variable to keep track of how many passwords have been tried
    password_iterator = itertools.product(characters, repeat=length)
    password = "".join(next(itertools.islice(password_iterator, n, None)))
    n += 1  # Increment n by 1
    return password


# A function to check if a password is correct by comparing it to a given hash
def check_password(password, hash):
    # Use the hashlib module to hash the password using SHA-256 algorithm
    # The hexdigest() method returns the hash as a hexadecimal string
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    # Return True if the hashes match, False otherwise
    return password_hash == hash


# A function to calculate the progress in searching the total search space so far
def calculate_progress(characters, length):
    # Calculate the size of the search space as the number of possible combinations of the chosen characters
    search_space = len(characters) ** length
    # Calculate the progress as the ratio of passwords tried to the search space
    progress = n / search_space
    # Return the progress as a percentage
    return progress * 100


# A function to crack a password by brute force using curses for UI
def crack_password(stdscr, hash, length):
    # Start a timer to measure how long it takes to crack the password
    start_time = time.time() - 1
    # Initialize a counter for the number of attempts
    attempts = 0
    # Initialize a global variable for how many passwords have been tried
    global n
    n = 0
    # Choose from lowercase letters, uppercase letters, digits and symbols
    characters = string.ascii_lowercase + string.digits  # + string.ascii_uppercase  + string.punctuation
    # Try the common passwords first
    for password in common_passwords:
        # Increment the counter
        attempts += 1
        # Clear the screen using stdscr.clear()
        stdscr.clear()
        # Print the current password and its hash being tried and the number of attempts per second at row 0 and column 0 using stdscr.addstr()
        stdscr.addstr(0, 0, f"Trying: {password}")
        stdscr.addstr(1, 0, f"Hash: {hashlib.sha256(password.encode()).hexdigest()}")
        stdscr.addstr(2, 0, f"Attempts per second: {attempts / (time.time() - start_time):.2f}")
        # Refresh the screen using stdscr.refresh()
        stdscr.refresh()
        # If the password is correct, print it and return
        if check_password(password, hash):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Password cracked: {password}")
            stdscr.addstr(1, 0, f"Hash: {hashlib.sha256(password.encode()).hexdigest()}")
            stdscr.addstr(2, 0, f"Time taken: {round(time.time() - start_time, 2)} seconds")
            stdscr.addstr(3, 0, f"Passwords guessed: {n}")
            stdscr.refresh()
            # stdscr.addstr(3, 0, f"Password cracked: {password}")
            # stdscr.addstr(4, 0, f"Time taken: {time.time() - start_time} seconds")
            # stdscr.refresh()
            # Sleep forever because the screen clears when the function exits
            time.sleep(9999)
            return
    # If none of the common passwords work, generate sequential passwords of the given length and try them
    while True:
        # Generate a sequential password
        password = generate_password(characters, length)
        # Increment the counter
        attempts += 1
        # Clear the screen using stdscr.clear()
        stdscr.clear()
        # Print the current password and its hash being tried and the number of attempts per second at row 0 and column 0 using stdscr.addstr()
        stdscr.addstr(0, 0, f"Trying: {password}")
        stdscr.addstr(1, 0, f"Hash: {hashlib.sha256(password.encode()).hexdigest()}")
        stdscr.addstr(2, 0, f"Attempts per second: {attempts / (time.time() - start_time):.2f}")
        stdscr.addstr(3, 0, f"Percentage complete: {round(calculate_progress(characters, length), 2)}%")
        # Refresh the screen using stdscr.refresh()
        stdscr.refresh()
        # If the password is correct, print it and return
        if check_password(password, hash):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Password cracked: {password}")
            stdscr.addstr(1, 0, f"Hash: {hashlib.sha256(password.encode()).hexdigest()}")
            stdscr.addstr(2, 0, f"Time taken: {round(time.time() - start_time, 2)} seconds")
            stdscr.addstr(3, 0, f"Passwords guessed: {n}")
            stdscr.refresh()
            # Sleep forever because the screen clears when the function exits
            time.sleep(9999)
            return


# A sample password and its hash to crack
password = "iloveyou"
hash = hashlib.sha256(password.encode()).hexdigest()

# Initialize curses and call crack_password with a standard screen object as an argument using curses.wrapper()
curses.wrapper(crack_password, hash, len(password))
