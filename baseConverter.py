class BaseConverter:
    def __init__(self, converters):
        self.converters = converters

    def __convert(self, fromUnit, amount, toUnit, converterName):


        neededConverter = self.converters[converterName]

        value_in_base = amount / neededConverter[fromUnit]

        return {toUnit: value_in_base * neededConverter[toUnit]}

    def getValue(self):
        converterName = input(f"Choice converter {list(self.converters.keys())}: ")

        if converterName not in self.converters:
            print("No such converter")
            return False

        fromUnit = input("Enter from what unit you want to convert: ")

        if fromUnit not in self.converters[converterName]:
            print("No such unit")
            return False

        toUnit = input("Enter to what unit you want to convert: ")

        if toUnit not in self.converters[converterName]:
            print("No such unit")
            return False

        try:
            amount = float(input(f"Enter amount of {fromUnit} that you want to convert to {toUnit}: "))
        except ValueError:
            print("Invalid number")
            return False

        return self.__convert(fromUnit, amount, toUnit, converterName)