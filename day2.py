input = """""" # Enter your input here! (https://adventofcode.com/2023/day/2/input)

def task1(given_input):
    max_red = 12
    max_green = 13
    max_blue = 14
    games = given_input.split("\n")
    sum = 0
    for game in games: # ex. for game: Game 98: 4 red, 5 green, 6 blue; 2 red, 9 green, 6 blue; 2 blue, 11 red, 14 green; 6 green, 4 blue; 11 blue, 11 red, 8 green
        game = game.split(": ")
        game_id = int(game[0].split(" ")[1])
        game = game[1]
        game_reveals = game.split("; ")
        impossible = False
        for reveal in game_reveals: # ex. for reveal: 4 red, 5 green, 6 blue
            reveal_items = reveal.split(", ")
            for reveal_item in reveal_items: # ex. for reveal_item: 5 green
                item_count = int(reveal_item.split(" ")[0])
                if "red" in reveal_item:
                    if item_count > max_red:
                        impossible = True
                if "green" in reveal_item:
                    if item_count > max_green:
                        impossible = True
                if "blue" in reveal_item:
                    if item_count > max_blue:
                        impossible = True
        if impossible is False:
            sum += game_id
    return sum

def task2(given_input):
    games = given_input.split("\n")
    sum = 0
    for game in games: # ex. for game: Game 98: 4 red, 5 green, 6 blue; 2 red, 9 green, 6 blue; 2 blue, 11 red, 14 green; 6 green, 4 blue; 11 blue, 11 red, 8 green
        greens = []
        reds = []
        blues = []
        game = game.split(": ")
        game = game[1]
        game_reveals = game.split("; ")
        for reveal in game_reveals: # ex. for reveal: 4 red, 5 green, 6 blue
            reveal_items = reveal.split(", ")
            for reveal_item in reveal_items: # ex. for reveal_item: 5 green
                item_count = int(reveal_item.split(" ")[0])
                if "red" in reveal_item:
                    reds.append(item_count)
                elif "green" in reveal_item:
                    greens.append(item_count)
                elif "blue" in reveal_item:
                    blues.append(item_count)
        reds.sort(reverse=True)
        greens.sort(reverse=True)
        blues.sort(reverse=True)
        power = reds[0] * greens[0] * blues[0]
        sum += power
    return sum
        


print(task1(input))
print(task2(input))
