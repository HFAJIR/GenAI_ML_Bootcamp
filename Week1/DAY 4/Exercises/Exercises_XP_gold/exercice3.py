
import random

def throw_dice():
    """Return a random integer between 1 and 6."""
    return random.randint(1, 6)

def throw_until_doubles():
    """Keep throwing two dice until both show the same number. Return the number of throws."""
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:  # doubles
            break
    return count

def main():
    results = []  # collection to store the number of throws for each doubles
    total_doubles = 100
    
    for _ in range(total_doubles):
        throws = throw_until_doubles()
        results.append(throws)
    
    total_throws = sum(results)
    average_throws = total_throws / total_doubles
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

# Call main
main()