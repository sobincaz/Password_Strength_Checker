
import math
import string
import getpass

# Common passwords (basic dictionary check)
COMMON_PASSWORDS = {
    "password", "password123", "123456",
    "123456789", "qwerty", "admin",
    "welcome", "letmein", "iloveyou",
    "abc123", "admin123"
}

def calculate_entropy(password):
    """Calculate estimated password entropy in bits."""

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def check_password(password):
    feedback = []
    score = 0

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Uppercase check
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase check
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Digit check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special character check
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a commonly used password.")
        score = 0

    # Entropy calculation
    entropy = calculate_entropy(password)

    # Strength classification
    if score == 0 or entropy < 28:
        strength = "Weak"
    elif entropy < 50 or score <= 3:
        strength = "Moderate"
    elif entropy < 70 or score <= 5:
        strength = "Strong"
    else:
        strength = "Exceptional"

    return entropy, strength, feedback


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("Enter your password: ");

    entropy, strength, feedback = check_password(password)

    print("\n------ PASSWORD SECURITY REPORT ------")
    print(f"Password Length : {len(password)}")
    print(f"Estimated Entropy: {entropy:.2f} bits")
    print(f"Strength Level  : {strength}")

    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print("- " + suggestion)
    else:
        print("\nGreat! Your password meets all basic policy checks.")

    print("\n---------------------------------------")


if __name__ == "__main__":
    main()
