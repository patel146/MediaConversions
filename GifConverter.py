import requests
import os
import subprocess

'''
For this script to work, you need to have ffmpeg installed in your system and added as a PATH variable. To check if this
is the case, open windows terminal (cmd) and type ffmpeg. If an error shows up, you either haven't installed it or you
don't have it as a PATH variable. 

If you need help this should do the trick: https://www.wikihow.com/Install-FFmpeg-on-Windows '''

if __name__ == '__main__':

    running = True

    while running:
        # Copy image address of gif
        uri = input('image address: ')

        # Pass a blank space into the image address to exit the program
        if uri != '':

            # enter a suitable name for the mp4 file
            name = input('Name of gif: ')
            
            # Saves gif to a temporary location for subsequent conversion, detail a temporary path below
            # Example: "C:/Users/yourName/tmp/tmp-gifs/"
            result_path = os.path.normpath("Enter path here" + name + ".gif")

            with open(result_path, 'wb') as f:
                f.write(requests.get(uri).content)

            target = os.path.normpath(r'"Same tmp path as line 28"' + '/' + name + '.gif')
            print(target)
            output = os.path.normpath(r'"Path of where you want the mp4s to go"' + '/' + name + '.mp4')

            subprocess.call(
                'ffmpeg -i ' + target + ' -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ' + output,
                shell=True
            )
        else:
            running = False
