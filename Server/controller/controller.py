from pathlib import Path
from moviepy.editor import *
import shutil
import tempfile


class controller():
    def __init__(self):
        """
        Creates an uploads folder in the users temp directory for file uploads
        temp files will always get deleted after conversion
        """
        if Path(tempfile.gettempdir() +  '/uploads').exists() == False:
            os.mkdir(Path(tempfile.gettempdir() +  '/uploads'))

        self.temp = Path(tempfile.gettempdir() +  '/uploads')

    def saveFile(self, file, filename):
        """
        Saves file to uploads folder
        """
        file.save(os.path.join(self.temp, filename))
        return self.temp / filename


    def convertFileToMP3(self, src, filename, dst):
        """
        Converts file to MP3 and saves it in designated filelocation (dst)
        """
        filename = filename.replace('.mp4', '')
        

        if not Path(src).exists():
            return f'ERROR FILE {filename} DOES NOT EXIST IN THE ', 404
        
        # AudioFileClip(str(src)).write_audiofile( self.temp / f'{filename}.mp3', codec='mp3', bitrate='192k')
        print(f'dst: {dst}')
        if dst != 'undefined':
            if not Path(dst).exists():
                # shutil.move(self.temp / f'{filename}.mp3', Path.home() / 'Downloads')
                return f'ERROR PATH {dst} COULD NOT BE LOCATED, MOVING FILE TO DOWNLOADS FOLDER', 202
            # shutil.move(self.temp / f'{filename}.mp3', dst)
        else:
            # shutil.move(self.temp / f'{filename}.mp3', Path.home() / 'Downloads')
            pass

        # if Path(self.temp / f'{filename}.mp4').exists():
        #     os.remove(self.temp / f'{filename}.mp4') 
        return 'Success', 200
        

    def convertFileToWAV(self, src, filename, wav, dst):
        """
        Converts file to WAV and saves it in designated filelocation (dst)
        Choose pcm_s16le for 16-bit wav and pcm_s32le for 32-bit wav.
        """
        filename = filename.replace('.mp4', '')

        if not Path(src).exists():
            return f'ERROR FILE {filename} DOES NOT EXIST IN THE ', 404

        if wav== '16bit':
            codec='pcm_s16le'
        else: # 32bit
            codec='pcm_s32le'


        AudioFileClip(str(src)).write_audiofile(self.temp / f'{filename}.wav', codec=codec)

        if dst != 'undefined':
            if not Path(dst).exists():
                shutil.move(self.temp / f'{filename}.mp3', Path.home() / 'Downloads')
                return f'ERROR PATH {dst} COULD NOT BE LOCATED, MOVING FILE TO DOWNLOADS FOLDER',304
            shutil.move(self.temp / f'{filename}.wav', dst)
        else:
            shutil.move(self.temp / f'{filename}.mp3', Path.home() / 'Downloads')
        
        if Path(self.temp / f'{filename}.mp4').exists():
            os.remove(self.temp / f'{filename}.mp4') 
        return 'Success', 200
    
