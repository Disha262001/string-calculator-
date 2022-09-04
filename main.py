class StringCalculator():
    def add(self, numbers=""):
        # If nullstring is passed
        if len(numbers) == 0:
            return 0
        #if a single digit number is passed
        try:
            x= int(numbers)
            return x
        #if two numbers are passes seperating with a delimiter ' comma(,)'
        except:
            position = 2

