class InvalidTelevisionError(Exception):
    """Custom exception for invalid Television data."""
    pass

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0.0

    def input_data(self):
        try:
            self.model_number = int(input("Enter model number: "))
        except ValueError:
            raise InvalidTelevisionError("Model number must be an integer")

        try:
            self.screen_size = float(input("Enter screen size (in inches): "))
        except ValueError:
            raise InvalidTelevisionError("Screen size must be a number")

        try:
            self.price = float(input("Enter price (in Rs): "))
        except ValueError:
            raise InvalidTelevisionError("Price must be a number")

        
        if self.model_number < 0 or self.model_number > 9999:
            raise InvalidTelevisionError("Invalid model number: must be at most 4 digits and non-negative")

        if self.screen_size < 12 or self.screen_size > 70:
            raise InvalidTelevisionError("Invalid screen size: must be between 12 and 70 inches")

       
        if self.price < 0 or self.price > 5000:
            raise InvalidTelevisionError("Invalid price: must be between 0 and 5000 Rs")

    def display(self):
        print(f"Model Number: {self.model_number}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Price: Rs {self.price}")

    def reset(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0.0


def main():
    tv = Television()
    try:
        tv.input_data()
    except InvalidTelevisionError as e:
        print(f"Exception caught: {e}")
        print("Resetting all values to zero.")
        tv.reset()

    print("Displaying TV details:")
    tv.display()


if __name__ == "__main__":
    main()
