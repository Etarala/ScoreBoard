paused = False

def pause():
    global paused

    paused = not paused


if not paused:
        turtle.clear()


print(paused)
pause()
print(paused)

pause()
print(paused)