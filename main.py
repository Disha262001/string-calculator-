class StringCalculator():
    def add(self, numbers=""):
        sum = 0
        # If nullstring is passed
        if len(numbers) == 0:
            return 0
       #if a single digit number is passed
        elif (',' or ';' or '\n' or '//' not in numbers) :
            sum = int(numbers)
            return sum

        numbers = numbers.replace("\n", ",")
        numbers = numbers.replace("//", "")
        numbers = numbers.replace(";", ",")
        numbers=numbers.split(",")

        for i in range(len(numbers)):
            sum+=int(numbers[i])

        return sum
