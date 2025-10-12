
#PART A
def perfect_number_sum_calculator():
    def get_integer_input(prompt):
        while True:
            try:
                value = int(input(prompt))#input as integer.
                return value
            
            except ValueError:
                print("Invalid input. Please enter a whole number (integer) only.")

    a = get_integer_input("Enter first number: ")#inputs for range
    b = get_integer_input("Enter second number: ")

    x = min(a, b)#Min vak=lue and max vaule
    y = max(a, b)
    Total = 0

    for i in range(x, y + 1):
        if i <= 1: #take value greater then 1 only
            continue
            
        factor_total = 1
        
        for denominator in range(2, int(i**0.5) + 1): #Loop for factors
            if i % denominator == 0:
                factor_total += denominator
                onlyonce = i // denominator
                if onlyonce != denominator:#to refrain from adding perfect number again
                    factor_total += onlyonce

        if factor_total == i:
            Total += i
    print("Sum of perfect numbers is:", Total)


def Weight_Unit_Converter():
    try:
        weightvalue = float(input("Enter the weight: "))
    except ValueError:
        print("Please Enter a number")
        return

    Convert = input("Enter 'K' for kg to lb, or 'P' for lb to kg: ").upper()
    result = None
    #Conversion
    if Convert == 'K':#kg to lb -  / 2.20462
        result = weightvalue * 2.20462
        ufrom = "kg"
        uto = "lb"
        
    elif Convert== 'P':#lb to kg -  * 2.20462
        result = weightvalue / 2.20462
        ufrom = "lb"
        uto = "kg"

    else:
        print("Error.Enter 'p' or 'Q' only")
        return
    finalresult = round(result, 2)#2decimals places
    print(f"Result: {weightvalue} {ufrom} is equal to {finalresult} {uto}")


def vowel_counter():
    c = input("Enter the Text: ")

    vowels = {'a', 'e', 'i', 'o', 'u'}#Vovels set
    text_lower = c.lower()
    count = 0
 
    for char in text_lower:
        if char in vowels:
            count += 1
    print(f"{c} contains {count} vowels.")

def Average_and_Range_Finder():
    number = [] #list stores number

    while True:
        try:#input check
            count = int(input("Total number of observations:"))
            if count > 0:
                break
            else:
                print("Please Enter Number Greater Than Zero!")
        except ValueError:
            print("Invalid.. Please enter a whole number.")
    print(f"Please enter {count} numbers:")

    for i in range(count):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                number.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    if not number:
        print("No numbers are entered.")
        return
    
    total_sum = sum(number)#Average
    average = total_sum / count

    maximum = max(number)
    minimum = min(number)
    data_range = maximum - minimum#Range

    print(f"Input Numbers: {number}")
    print(f"Average: {round(average, 2)}")
    print(f"Range: {round(data_range, 2)}")

def String_Reverser_and_Word_Count():
    text = input("Enter the text string: ")
    reversed_string = text[::-1]
    words = text.split()
    word_count = len(words)
    print(f"Original String: '{text}'")
    print(f"Reversed String: '{reversed_string}'")
    print(f"Word Count: {word_count}")


def Specific_Word_Counter():
    import string
    TEXT_CONTENT = """
    Not my story: I worked for a while for a (now defunct) search engine company whose middleware had been written
    by an insane person (about 5000 Java source files) who had moved on. Some of the characteristics:
    Most methods began with for(;;) so that continue statements could be used as gotos
    Almost all methods returned an object which wrapped an int, a string, a boolean and an object array,
    so the return type could be changed later (and woe be unto any code using the return value).
    Classes and packages all had random names - I mean, literally,
    the author kept a huge printout of random unique strings in his desk and crossed one off every time he had to create
    a package or class
    Shutdown was accomplished by killing threads in a loop repeatedly until they were all dead -
    like if the way you shut off your car was to open the hood and hit things with a hammer until the engine stopped
    All thrown runtime errors were logged as more unique random strings - to diagnose, you grepped the source code
    Every assignment was immediately followed by a test that the value had actually been assigned
    This company had a new CEO who wanted to sell this stuff to other industries than their one customer, a three-letter agency
    of the US government, and I was hired to replace this stuff with something reliable. However, they made all their money on
    "consultants" who sat in basements in Virginia babysitting the thing and fixing things with hex editors when it corrupted
    its own data, which was a few times daily. The software being embarrassingly broken *was* their cash cow. And I learned that
    this was not unusual.
    So I do not wonder why Snowden had access to what he had access to, or why the first version of the Obamacare web site was a
    disaster, or why Hillary might not have wanted to use a mail system run by contractors such as this. This is the state of
    government IT.
    src: https://www.quora.com/What-is-the-most-absurd-code-youve-ever-seen
    """


    wordcount = ["is", "are", "has", "have"]
    text_lower = TEXT_CONTENT.lower()

    translator = str.maketrans('', '', string.punctuation)
    text_cleaned = text_lower.translate(translator)
    
    words_list = text_cleaned.split()

    word_counts = {word: 0 for word in wordcount}
    
    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1
            
    print("Occurrences of specific words:")
    for word, count in word_counts.items():
        print(f'"{word}": {count}')
        
    return word_counts



def display_menu():
    while True:
        print("\nSelect a Function(1-6) or 0 to Exit:")
        print("1. Perfect Number Sum Calculator ")
        print("2. Weight Unit Converter")
        print("3. Vowel Counter")
        print("4. Average and Range Finder")
        print("5. String Reverser with Word Count")
        print("6. Specific Word Counter")
        print("0. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Invalid input. Please enter a number (0-6).")
            continue

        if choice == 1:
            perfect_number_sum_calculator()

        elif choice == 2:
            Weight_Unit_Converter()
            
        elif choice == 3:
            vowel_counter()
            
        elif choice == 4:
            Average_and_Range_Finder()

        elif choice == 5:
            String_Reverser_and_Word_Count()

        elif choice == 6:
            Specific_Word_Counter()
        
        elif choice == 0:
            print("Exiting program")
            break 
            
        else:
            print("Error: Invalid choice. Please select a number between 0 and 6.")

display_menu()