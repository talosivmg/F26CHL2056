import sys
temperatureMode = sys.argv [1]

with open ("challenge.data", "r") as rawFile:
    contents = rawFile.read().strip()
    contentsValue = float(contents)

def convertTemperature(inputMode):
    if inputMode == "FtoC":
        tempCalculation = ( contentsValue -32 ) * 5 / 9
    elif inputMode == "CtoF":
        tempCalculation = ( contentsValue * 9 / 5 ) + 32
    return tempCalculation

result = convertTemperature(temperatureMode)

with open ( "challenge.out", "w") as outputFile:
    outputFile.write(str(result))
