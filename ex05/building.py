import sys


def text_analyzer(text):
    """Count and display the different types of characters in a string."""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    num_uppercase = sum(1 for c in text if c.isupper())
    num_lowercase = sum(1 for c in text if c.islower())
    num_punctuation = sum(1 for c in text if c in punctuation)
    num_spaces = sum(1 for c in text if c.isspace())
    num_digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{num_uppercase} upper letters")
    print(f"{num_lowercase} lower letters")
    print(f"{num_punctuation} punctuation marks")
    print(f"{num_spaces} spaces")
    print(f"{num_digits} digits")


def main():
    """Run the text analyzer program."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        text = sys.argv[1] if len(sys.argv) == 2 else None
        if not text:
            print("What is the text to count?")
            text = sys.stdin.readline()
        text_analyzer(text)
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
