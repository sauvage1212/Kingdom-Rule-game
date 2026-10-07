from colorama import Fore
import json
import random
# print(Fore.RED + "")

kingdom_stats = {
    "recources": 50,
    "people": 50,
    "happiness": 50,
    "gold": 50
}

with open("problems.json") as file:
    problems = json.load(file)

# print(answers["1"])

def printStats(stats):
    line_1 = ""
    line_2 = ""
    for stat in stats:
        line_1 += f"{stat} "
        line_2 += f"{stats[stat]}        "
    print(Fore.BLUE + line_1)
    print(line_2)

def ariseProblem():
    global gameloop
    current_id, current_problem = random.choice(list(problems.items()))
    decision = input(Fore.RED + current_problem[0])
    if decision == "":
        gameloop = False
    elif decision == "yes":
        list_stats = ["recources", "people", "happiness", "gold"]
        for i in range(4):
            kingdom_stats[list_stats[i]] += current_problem[1][i]
    elif decision == "no":
        list_stats = ["recources", "people", "happiness", "gold"]
        for i in range(4):
            kingdom_stats[list_stats[i]] += current_problem[2][i]
    else:
        gameloop = False

gameloop = True

print(Fore.WHITE + "Your Kingdom:")
while gameloop:
    printStats(kingdom_stats)
    ariseProblem()

print(Fore.RESET + "Thanks for playing!")