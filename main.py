class StringCalculator():
    def add(self, numbers=""):
        # If nullstring is passed
        if len(numbers) == 0:
            return 0
        else:
            return int(numbers)