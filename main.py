class StringCalculator():
    def add(self, numbers=""):
        # If nullstring is passed
        if len(numbers) == 0:
            return 0
        #if a single digit number is passed
        elif ',' not in numbers:
            return int(numbers)

        # if more than one number is present in the string and seperated by delimeter 'comma(,)'
        else:
            alphaList = []
        for i in range(97, 123, 1):
            alphaList.append(chr(i))

        # separating all the numbers or alphabets present in the string and creating a list from it
        numList = numbers.split(',')
        for key, val in enumerate(numList):

            # runs if current element is number and converts the character of string into integer
            try:
                val = int(val)

            # runs if the current element is alphabet and takes the index of that alphabet from alphaList and gets the value corresponding to that alphabet
            except:
                val = alphaList.index(val) + 1

            # allocates the int value corresponding to the character present at that index
            numList[key] = val

        return sum(numList)