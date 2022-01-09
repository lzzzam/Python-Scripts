import os

DIR_NAME            = os.path.dirname(__file__)
INPUT_DIR           = os.path.join(DIR_NAME, 'Input')
OUTPUT_DIR          = os.path.join(DIR_NAME, 'Output')
INPUT_LETTER_PATH   = os.path.join(INPUT_DIR, 'starting_letter.txt')
INPUT_NAME_PATH     = os.path.join(INPUT_DIR, 'name.txt')

with open(INPUT_LETTER_PATH, "r") as fInputLetter:
    text = fInputLetter.read()

with open(INPUT_NAME_PATH, "r") as fInputName:
    nameList = fInputName.readlines()
    
for name in nameList:
    name = name.strip('\n')
    OUTPUT_LETTER_PATH = os.path.join(OUTPUT_DIR, f"invitation_{name}.txt")
    with open(OUTPUT_LETTER_PATH, "w") as fOutput:
        fOutput.write(text.replace("[name]", name))