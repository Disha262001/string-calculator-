class StringCalculator():
    def add(self, numbers=""):
        negativesList = []
        # If nullstring is passed
        if len(numbers) == 0:
            return 0
        #if a single digit number is passed
        elif ',' not in numbers:
            return int(numbers)

        numbers = numbers.replace("\n", ",")
        total = 0

        for number in numbers.split(','):

            if int(number) <= 1000:
                total += int(number)

        return total

