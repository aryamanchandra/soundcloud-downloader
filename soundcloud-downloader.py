import os

url = input("Enter the url ")
type = int(
    input(
        "Enter the number for the required type"
        + "\n"
        + "[1:all songs, 2:playlist, 3:single track]"
    )
)

try:
    if type == 1:
        os.system(f'cmd /k "scdl -l {url} -a "')
        print("All Songs Downloaded")
    elif type == 2:
        os.system(f'cmd /k "scdl -l {url}"')
        print("Playlist Downloaded")
    else:
        os.system(f'cmd /k "scdl -l {url}"')
        print("Song Downloaded")
except:
    print("error occured")

print("Task completed")
