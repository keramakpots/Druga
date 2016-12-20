
def reading_file(game_stat):
    with open('game_stat.txt', "r") as reader:
        return reader.readlines()
def count_games(game_stat):
    distance = 0
    for line in reading_file(game_stat):
        distance +=1
    return distance
def print_count_games(game_stat):
    print("There are",count_games(game_stat), "games in the file.")
def decide(game_stat, year):
    year = str(year)
    for line in reading_file(game_stat):
        rows = line.split('\t')
        if year in rows:
            return True
        else:
            continue
    else:
        return False
def decide_print(game_stat, year):
    if decide(game_stat, year) == False:
        print("There are no games in", year,"year")
    elif decide(game_stat, year) == True:
        print("Yes, there is a game in", year ,"year.")
def get_latest(game_stat):
    empty = []
    distance = 0
    for line in reading_file(game_stat):
        distance +=1
    for line in reading_file(game_stat):
        rows = line.split('\t')
        empty.append(rows[2])
        #it creates list of all years in file
        while len(empty) == distance:
            latest = max(empty)
            break
    for line in reading_file(game_stat):
        rows = line.split('\t')
        if latest in rows:
            return rows[0]
def get_latest_print(game_stat):
    print(get_latest(game_stat), "is the latest game.")
def count_by_genre(game_stat, genre):
    counter = 0
    for line in reading_file(game_stat):
        rows = line.split('\t')
        if genre in rows:
            counter += 1
    return counter
def count_by_genre_print(game_stat, genre):
    print("There is", count_by_genre(game_stat, genre), genre, "games")
def get_line_number_by_title(game_stat, title):
    lines = 1
    for line in reading_file(game_stat):
        rows = line.split('\t')
        if title != rows[0]:
            lines +=1
        elif title == rows[0]:
            break
    return lines
def get_line_number_by_title_print(game_stat, title):
    if get_line_number_by_title(game_stat, title) <=count_games(game_stat):
        print("Game", title, "is in", get_line_number_by_title(game_stat, title),"line.")
    elif get_line_number_by_title(game_stat, title) > count_games(game_stat):
        raise ValueError("There is no", title,"in our library.")
        exit()
game_stat = 'game_stat.txt'
year = input("Year: ")
genre=input("What genre? ")
title = input("What title are you looking for? ")
reading_file(game_stat)
count_games(game_stat)
print_count_games(game_stat)
decide(game_stat, year)
decide_print(game_stat, year)
get_latest(game_stat)
get_latest_print(game_stat)

count_by_genre(game_stat, genre)
count_by_genre_print(game_stat, genre)

get_line_number_by_title(game_stat, title)
get_line_number_by_title_print(game_stat, title)
