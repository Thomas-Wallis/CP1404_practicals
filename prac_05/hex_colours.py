HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "faebd7", "antiquewhite1": "ffefdb", "antiquewhite2": "#eedfcc",
               "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "aquamarine1": "#8b8378",
               "aquamarine2": "#7fffd4", "aquamarine4": "#76eec6", "azure1": "#f0ffff", "azure2": "#e0eeee"}
colour = input("Please enter the colour you would like to check the hexadecimal code of: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("Code - {}".format(HEX_COLOURS[colour]))
    else:
        print("Invalid input")
    colour = input("Please enter the colour you would like to check the hexadecimal code of: ").lower()