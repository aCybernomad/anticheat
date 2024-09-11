import hashlib
import random
import string
import colorama 

colorama.init()

def pre_game_hash(nickname):
    # Generate a random salt
    salt = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

    # Stores what I need for crosscheck (Maybe quests completion/other triggers etc) 
    var1 = 10
    var2 = 20
    var3 = 30

    # Concatenate everything
    data = f"{nickname}{salt}{var1}{var2}{var3}"

    # Hash it all a specific level in the game
    sha256 = hashlib.sha256(data.encode('utf-8')).hexdigest()

    return sha256, salt

def play_game(nickname, salt): # Keep the same salt 
    # What needs to be accomplished in the game to match pre_game_hash in the end
    print("Game on!")
    problem1 = input("1 + 1 = ")
    problem2 = input("2 + 2 = ")
    problem3 = input("3 + 3 = ")

    # Check if the answers are correct 
    if problem1 == "2" and problem2 == "4" and problem3 == "6":
        var1 = 10
        var2 = 20
        var3 = 30
    else:
        var1 = 0
        var2 = 0
        var3 = 0

    # Concatenate all elements
    data = f"{nickname}{salt}{var1}{var2}{var3}"

    # Hash the players nickname/salt/and reults of ingame tasks.
    sha256 = hashlib.sha256(data.encode('utf-8')).hexdigest()

    return sha256

# Get the nickname from the user
print("------------------------------------------------------------------------------")
nickname = input("::: > Nickname: ")

# Hash the nickname and print the result
hashed_nickname, salt = pre_game_hash(nickname)
print("------------------------------------------------------------------------------")
print("Pre game hash (truth):", hashed_nickname)
print("Salt:", salt[:2] + "*********" + salt[-2:])
print("Nickname:", nickname)
print("------------------------------------------------------------------------------")


# Use the player function with the same nickname and salt
player_hash = play_game(nickname, salt)
print("------------------------------------------------------------------------------")
print("Finished game hash:", player_hash)

# Check if the hashes match
if hashed_nickname == player_hash:
    print("------------------------------------------------------------------------------")
    print(colorama.Fore.GREEN + "::: Congratulations " + nickname + "! :::" + colorama.Style.RESET_ALL)
else:
    print("------------------------------------------------------------------------------")
    print(colorama.Fore.RED + "::: Hashes don't match, " + nickname + " are you cheating? Kicked out. :::\n\n>> IP-number log\n>> Timestamp log\n>> Session ID log\n...etc" + colorama.Style.RESET_ALL)
