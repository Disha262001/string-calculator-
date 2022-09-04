class StringCalculator():
    def add(self, numbers=""):
        # If nullstring is passed
        if len(numbers) == 0:
            return 0
        #if a single digit number is passed
        else:
            sum = 0
            numbers = numbers.split(',')
            for i in numbers:
                sum += int(i)
            return sum
