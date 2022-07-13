import os
import subprocess

'''
For this script to work, you need to have ffmpeg installed in your system and added as a PATH variable. To check if this
is the case, open windows terminal (cmd) and type ffmpeg. If an error shows up, you either haven't installed it or you
don't have it as a PATH variable. 

If you need help this should do the trick: https://www.wikihow.com/Install-FFmpeg-on-Windows '''

# Make sure your folders don't have spaces in their names. It's still possible but will take extra work not included in
# this script.

folder_of_gifs = os.path.normpath(r'C:\Users\patel\WorkingFiles\Gifs')
# example of proper path: r'C:\Users\YourName\SomeFolderWithGifs'


for gif in os.listdir(folder_of_gifs):
    output = os.path.normpath(r'C:\Users\patel\WorkingFiles\mp4converttest' + '\\' + gif[:-3] + 'mp4')
    # example of proper path: r'C:\Users\YourName\PutMP4Here'

    # This is the code where ffmpeg actually is run. Not sure if this works on Mac or linux :(
    subprocess.call(
        'ffmpeg -i ' + folder_of_gifs + '\\' + gif + ' -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ' + output,
        shell=True)
