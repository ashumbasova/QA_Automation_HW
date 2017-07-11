#HW2_Task_9

def song(znak, stroki = 3, raz = 3):
    if znak == 0:
        punkZnak = "."
    elif znak == 1:
        punkZnak = "!"
    else: punkZnak = ""
    newLine = []
    while raz > 0:
        newLine.append("la")
        raz -= 1
    finalNewLine = "-".join(newLine)
    song = (finalNewLine + "\n") * stroki
    finalSong = song.rstrip("\n") + punkZnak
    return finalSong
print(song(1))
