def line_counter(file_name):
    with open(file_name, 'r') as file:
        count = 0
        large_comment = False
        for line in file:
            line = line.strip()
            line.replace(" ", "")
            if line == "":
                continue
            elif line[0] == '#':
                continue

            elif "'''" in line:
                back_quote = line.find(r'\"') + 1
                trip_quote = line.find("'''")
                quote = line.find('"')

                pass1 = back_quote != -1 and quote == back_quote
                pass2 = quote != -1 and quote < trip_quote

                if not pass1 and not pass2:
                    if large_comment == True:
                        large_comment = False
                    elif large_comment == False:
                        large_comment = True
                    continue

            if large_comment == False:
                count += 1
    return(count)



try:
    print("Simple line counter function that ignores:\n")
    print("'''\ntriple\nquote\nblocks\n'''")
    print("#single line comments\n")
    print("\nand whitespace.\n")
    get = input("Type python file name: ")
    print("{} has {} lines!".format(get, line_counter(get)))
except FileNotFoundError:
    print("Couldn't find file: \"{}\"".format(get))
