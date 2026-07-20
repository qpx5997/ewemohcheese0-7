import time
from pathlib import Path
import traceback

# Set variables, lists, dictionaries
variables = {}
loopid = 0      # if in a loop, loopid = 1, if in a loop in a loop, loopid = 2, and so on
to_iterate = {} # how many times a loop has to iterate
iterations = {} # how many times a loop has iterated
loopstarts = {} # which line a loop starts at

ifid = 0 # level of nesting for if statements
ifends = [] # stores the ending lines of if statements

code_file_name = input("""👋➡️🐑Ⓜ️😮🧀0️⃣⏺️8️⃣❗❗❗❗
⌨️📁🏷️➡️➡️➡️ """)

try:
    with open (code_file_name, encoding="utf-8") as f:
        full_code = f.read()

except Exception as e:
    print(f"""☹️❌👎
📍⌨️📁
{e}
🙋🦥🛌
👉⌨️""")
    input()
    exit()

if Path(code_file_name).suffix != ".🐑Ⓜ️😮🧀":
    print(f"""☹️❌👎
📍⌨️📁
⏺️🐑Ⓜ️😮🧀✅⏺️{Path(code_file_name).suffix}❌❌❌❌❌❌
👉⌨️""")
    input()
    exit()

codelines = full_code.split("\n")

i = 1
while i <= len(codelines): # it has to be a while loop so loops work properly

    try:

        line = codelines[i - 1] # This is separate from the for line so loops can work properly
        line = line.lstrip() # Remove whitespace so indentation works
        linesegs = line.split("⏩")

        if linesegs[0] == "⬆️": # denotes end of a loop
            iterations[loopid] += 1 # adds 1 to the iterations to kep track of how much has iterated
            if iterations[loopid] != to_iterate[loopid]:
                i = loopstarts[loopid] # return to start of loop
            if iterations[loopid] == to_iterate[loopid]: # end the loop, delete all loop data
                to_iterate.pop(loopid)
                loopstarts.pop(loopid)
                iterations.pop(loopid)
                loopid -= 1

        if linesegs[0] == "❓⬆️": # denotes end of an if statement
            ifid -= 1 # clear necessary if-statement data
            ifends.remove(ifends[ifid])

        elif linesegs[0] == "🔄️": # continue statement, perfect for ETERNALITY
            i = loopstarts[loopid]

        elif linesegs[0] == "🖨️": # this is like pythons print() function
            if linesegs[1][0] == "📦":
                print(variables[linesegs[1][1:]])
            else:
                print(linesegs[1])

        elif linesegs[0] == "🖨️🔚": # this is like pythons print("", end="") function
            if linesegs[1][0] == "📦":
                print(variables[linesegs[1][1:]], end="")
            else:
                print(linesegs[1], end="")

        elif linesegs[0] == "⏳": # this just makes it wait for a specified amount of time
            if linesegs[1][0] == "📦":
                time.sleep(float(variables[linesegs[1][1:]]))
            else:
                time.sleep(float(linesegs[1]))

        elif linesegs[0] == "🗒️": # comments
            pass

        elif linesegs[0] == "📦": # variable assignment!!!!!
            if linesegs[2][0] == "📦": # put this to set a variable to an existing variable
                variables[linesegs[1]] = variables[linesegs[2][1:]]
            elif linesegs[2] == "⌨️": # put this to set it to the most recent user input
                variables[linesegs[1]] = most_recent_answer
            else:
                if linesegs[2][0] == "🔢": # put 🔢 at the front to show its an integer
                    variables[linesegs[1]] = int(linesegs[2][1:])
                else: # or it will be a string
                   variables[linesegs[1]] = linesegs[2]

        elif linesegs[0] == "➕": #incrementation!
            if linesegs[2][0] == "📦":
                variables[linesegs[1]] += variables[linesegs[2][1:]]
            else:
                variables[linesegs[1]] += int(linesegs[2])

        elif linesegs[0] == "➖": #decrementation!
            if linesegs[2][0] == "📦":
                variables[linesegs[1]] -= variables[linesegs[2][1:]]
            else:
                variables[linesegs[1]] -= int(linesegs[2])

        elif linesegs[0] == "✖️": #multiplication!
            if linesegs[2][0] == "📦":
                variables[linesegs[1]] = variables[linesegs[1]] * variables[linesegs[2][1:]]
            else:
                variables[linesegs[1]] = variables[linesegs[1]] * int(linesegs[2])

        elif linesegs[0] == "➗": #division!
            if linesegs[2][0] == "📦":
                variables[linesegs[1]] = variables[linesegs[1]] / variables[linesegs[2][1:]]
            else:
                variables[linesegs[1]] = variables[linesegs[1]] / int(linesegs[2])

        elif linesegs[0] == "🥕": #exponentiation!
            if linesegs[2][0] == "📦":
                variables[linesegs[1]] = variables[linesegs[1]] ** variables[linesegs[2][1:]]
            else:
                variables[linesegs[1]] = variables[linesegs[1]] ** int(linesegs[2])

        elif linesegs[0] == "➰": #loops
            # loop data setup
            if linesegs[1][0] == "📦":
                loopid += 1
                to_iterate[loopid] = variables[linesegs[1][1:]]
            else:
                loopid += 1
                to_iterate[loopid] = int(linesegs[1])
            iterations[loopid] = 0
            loopstarts[loopid] = i

        elif linesegs[0] == "⌨️":
            most_recent_answer = input()

        elif linesegs[0] == "⌨️🔢": # user input but number
            most_recent_answer = int(input())

        elif linesegs[0] == "❓": # IF
            ifid += 1

            j = i
            while True: # check where the end of the if statement is

                if "❓⬆️" in codelines[j]: # just to be a bit lenient
                    ifends.append(j)
                    break
                else:
                    j += 1

            if linesegs[1] == "🟰": # if something equals something.
                if variables[linesegs[2]] == variables[linesegs[3]]:
                    pass
                else:
                    i = ifends[ifid - 1] # jump to nearest ❓⬆️, aka end of the if-statement

        elif linesegs[0] == "🚪": # bye bye user
            exit()

        i += 1

    except Exception as e:
        print(f"""☹️❌👎
📍{i}
{e}
🙋🦥🛌
👉⌨️""")
        input()
        exit()
