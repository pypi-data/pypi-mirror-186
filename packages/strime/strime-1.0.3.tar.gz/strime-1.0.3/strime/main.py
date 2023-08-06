# main.py
# A simple string (time+unit) to seconds converter.
# https://github.com/woidzero/strime



class Strime:
    def __init__(self, prompt: str):
        self.unit = ''.join(i for i in prompt if not i.isdigit())

        if len(prompt) <= 1:
            raise ValueError("Prompt must contain at least 2 characters.")
        elif not self.unit:
            raise ValueError("Prompt must contain a unit of time.")  
                
        self.value = prompt.replace(self.unit, '')
        self.seconds = self.converter(self.value, self.unit)


    def converter(self, value, unit) -> int:
        try:
            value = int(value)

            if unit == "ms":
                return value * 1000
            elif unit == "s":
                return value
            elif unit == "m":
                return value * 60
            elif unit == "h":
                return value * 3600
            elif unit == "d":
                return value * 86400
            elif unit == "w":
                return value * 604800
            elif unit == "mn":
                return value * 2628000
            elif unit == "y":
                return value * 60 * 60 * 24 * 365
            elif unit == "c":
                return value * 60 * 60 * 24 * 365 * 100
            else:
                raise ValueError(f"Undefined time unit: {unit}")
        except ValueError:
            raise ValueError(f"Prompt must contain a time.")
