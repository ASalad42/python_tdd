class SimpleCalc:

    def add(self, value1,value2):
        return value1 + value2

    def sub(self,value1,value2):
        return value1 - value2
    #

    def mul (self,value1,value2):
        return value1 * value2

    def div (self,value1,value2):
        return value1 / value2

    # dob and %
    def per(self, value1,value2):
        return (value1 / value2) * 100

    # def dob(self, value1, value2):
    #     return (f"your b day is in month {value1} year {value2}")

    # other function for cm to m

    def convert(self, value1):
        return value1/100