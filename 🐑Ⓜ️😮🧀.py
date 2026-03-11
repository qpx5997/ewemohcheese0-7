import time
from pathlib import Path

# Set variables, lists, dictionaries
variables = {}
loopid = 0
to_iterate = {}
iterations = {}
loopstarts = {}

code_file_name = input("""👋➡️🐑Ⓜ️😮🧀0️⃣⏺️3️⃣❗❗❗❗
⌨️📁🏷️➡️➡️➡️ """)

try:
    with open (code_file_name, encoding="utf-8") as f:
        full_code = f.read()

except Exception as e:
    print(f"""☹️❌👎
📍⌨️📁
{e}
🙋🦥🛌""")
    exit()

if Path(code_file_name).suffix != ".🐑Ⓜ️😮🧀":
    print(f"""☹️❌👎
📍⌨️📁
⏺️🐑Ⓜ️😮🧀✅⏺️{Path(code_file_name).suffix}❌❌❌❌❌❌""")
    exit()

codelines = full_code.split("\n")

i = 1
while i <= len(codelines): # it has to be a while loop so loops work properly

    try:

        line = codelines[i - 1] # This is separate from the for line so loops can work properly
        linesegs = line.split("⏩")

        if linesegs[0] == "⬆️": # denotes end of a loop
            iterations[loopid] += 1
            if iterations[loopid] != to_iterate[loopid]:
                i = loopstarts[loopid]
            if iterations[loopid] == to_iterate[loopid]:
                to_iterate.pop(loopid)
                loopstarts.pop(loopid)
                iterations.pop(loopid)
                loopid -= 1

        elif linesegs[0] == "🖨️": # this is like pythons print() function
            if linesegs[1][0] == "📦":
                print(variables[linesegs[1][1:]])
            else:
                print(linesegs[1])

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

        elif linesegs[0] == "🚪": # bye bye user
            exit()

        i += 1

    except Exception as e:
        print(f"""☹️❌👎
📍{i}
{e}
🙋🦥🛌""")

        exit()
