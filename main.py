# International Morse code
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': ' / '
}

TITLE = """#     #                                 #####                      
##   ##  ####  #####   ####  ######    #     #  ####  #####  ######
# # # # #    # #    # #      #         #       #    # #    # #     
#  #  # #    # #    #  ####  #####     #       #    # #    # ##### 
#     # #    # #####       # #         #       #    # #    # #     
#     # #    # #   #  #    # #         #     # #    # #    # #     
#     #  ####  #    #  ####  ######     #####   ####  #####  ######
 #####                                                             
#     #  ####  #    # #    # ###### #####  ##### ###### #####      
#       #    # ##   # #    # #      #    #   #   #      #    #     
#       #    # # #  # #    # #####  #    #   #   #####  #    #     
#       #    # #  # # #    # #      #####    #   #      #####      
#     # #    # #   ##  #  #  #      #   #    #   #      #   #      
 #####   ####  #    #   ##   ###### #    #   #   ###### #    #     """

def convert_to_morse():
    morse_code = []

    text = input("\nEnter text to be converted: ").upper().strip()

    if not text or text == " ":
         print("You didn't enter valid text.")
         return
    
    for x in text:
        if x not in MORSE_CODE_DICT.keys():
            print(f"{x} is not a valid character.")
            return
        else:
            morse_code.append(MORSE_CODE_DICT[x])
    
    print(f"Morse Code: {''.join(morse_code)}")

def main():
    print(TITLE)

    try_again = True
    
    while try_again:
        convert_to_morse()
        
        choice = input("\nTry again? y/n: ").lower()

        if choice == "n" or choice == "no":
            try_again = False

if __name__ == "__main__":
    main()