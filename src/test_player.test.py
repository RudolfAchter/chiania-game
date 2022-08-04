import chiania

player=chiania.player()

cmd=""
print ("enter '!quit' to exit")
while cmd != "!quit":
    cmd=input("command: ")
    player.command(cmd)
    print(player.character.message)
    player.character.look()
    print(player.character.message)