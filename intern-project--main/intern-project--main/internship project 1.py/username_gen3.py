import random
import string

def main():
    print("\n=== Random Username Generator ===")
    print("Welcome! Let's create some unique usernames for you.\n")
    
    # Define lists of adjectives and nouns
    adjectives = [
        "Cool", "Happy", "Swift", "Brave", "Gentle", "Wild", "Silent", "Lucky", 
        "Bright", "Calm", "Daring", "Eager", "Fierce", "Golden", "Honest", "Jolly",
        "Kind", "Mighty", "Noble", "Proud", "Quick", "Royal", "Smart", "Tough",
        "Vivid", "Wise", "Young", "Zesty", "Adventurous", "Bold", "Creative"
    ]
    
    nouns = [
        "Tiger", "Dragon", "Eagle", "Wolf", "Lion", "Bear", "Falcon", "Shark",
        "Phoenix", "Panther", "Hawk", "Fox", "Rhino", "Owl", "Raven", "Jaguar",
        "Cheetah", "Gorilla", "Elephant", "Panda", "Koala", "Kangaroo", "Peacock",
        "Sparrow", "Whale", "Dolphin", "Octopus", "Penguin", "Unicorn", "Griffin"
    ]
    
    while True:
        print("\n=== Menu ===")
        print("1. Generate a simple username (adjective + noun)")
        print("2. Generate a username with numbers")
        print("3. Generate a username with special characters")
        print("4. Generate a username with both numbers and special characters")
        print("5. View all generated usernames")
        print("6. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
        except ValueError:
            print("Please enter a valid number between 1 and 6.")
            continue
            
        if choice == 1:
            username = generate_simple_username(adjectives, nouns)
            print(f"\nYour new username: {username}")
            save_username(username)
        elif choice == 2:
            username = generate_username_with_numbers(adjectives, nouns)
            print(f"\nYour new username: {username}")
            save_username(username)
        elif choice == 3:
            username = generate_username_with_special_chars(adjectives, nouns)
            print(f"\nYour new username: {username}")
            save_username(username)
        elif choice == 4:
            username = generate_username_with_both(adjectives, nouns)
            print(f"\nYour new username: {username}")
            save_username(username)
        elif choice == 5:
            view_saved_usernames()
        elif choice == 6:
            print("\nThank you for using the Random Username Generator!")
            print("All your usernames have been saved to 'usernames.txt'.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def generate_simple_username(adjectives, nouns):
    """Generate a simple username (adjective + noun)"""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective}{noun}"

def generate_username_with_numbers(adjectives, nouns):
    """Generate a username with numbers added"""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    numbers = ''.join(random.choices(string.digits, k=random.randint(2, 4)))
    return f"{adjective}{noun}{numbers}"

def generate_username_with_special_chars(adjectives, nouns):
    """Generate a username with special characters"""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    special_chars = ''.join(random.choices("!@#$%^&*", k=random.randint(1, 2)))
    # Randomly decide where to put special chars (beginning, middle, or end)
    position = random.randint(0, 2)
    if position == 0:
        return f"{special_chars}{adjective}{noun}"
    elif position == 1:
        return f"{adjective}{special_chars}{noun}"
    else:
        return f"{adjective}{noun}{special_chars}"

def generate_username_with_both(adjectives, nouns):
    """Generate a username with both numbers and special characters"""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    numbers = ''.join(random.choices(string.digits, k=random.randint(2, 3)))
    special_chars = ''.join(random.choices("!@#$%^&*", k=random.randint(1, 2)))
    
    # Create different patterns
    patterns = [
        f"{adjective}{noun}{numbers}{special_chars}",
        f"{special_chars}{adjective}{noun}{numbers}",
        f"{adjective}{special_chars}{noun}{numbers}",
        f"{adjective}{numbers}{noun}{special_chars}"
    ]
    
    return random.choice(patterns)

def save_username(username):
    """Save the generated username to a file"""
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")

def view_saved_usernames():
    """Display all previously generated usernames"""
    try:
        with open("usernames.txt", "r") as file:
            usernames = file.readlines()
            
        if not usernames:
            print("\nNo usernames have been generated yet.")
        else:
            print("\n=== Previously Generated Usernames ===")
            for i, username in enumerate(usernames, 1):
                print(f"{i}. {username.strip()}")
    except FileNotFoundError:
        print("\nNo usernames have been generated yet.")

if __name__ == "__main__":
    main()