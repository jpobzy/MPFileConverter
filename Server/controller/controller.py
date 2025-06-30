from pathlib import Path
from moviepy.editor import *

class controller():
    def __init__(self):
        self.defaultConvertedPath = Path.cwd() / 'converted'
        self.defaultUploadPath = Path.cwd() / 'uploads'


    def saveFile(self, file, filename):
        """
        Saves file to uploads folder
        """
        file.save(os.path.join(self.defaultUploadPath, filename))
        return self.defaultUploadPath / filename


    def convertFileToMP3(self, src, filename, dst=None):
        """
        Converts file to MP3 and saves it in designated filelocation (dst)
        """
        filename = filename.replace('.mp4', '')
        
        if dst == None:
            dst =  self.defaultConvertedPath / f'{filename}.mp3'
        else:
            dst = Path(dst) / f'{filename}.mp3'

        if not Path(src).exists():
            return f'ERROR FILE {filename} DOES NOT EXIST IN THE ', 404
        
        video = AudioFileClip(str(src))
        video.write_audiofile(dst, codec='mp3', bitrate='192k')

        return 'Success', 200
        

    def convertFileToWAV(self, src, filename, wav, dst=None):
        """
        Converts file to WAV and saves it in designated filelocation (dst)
        Choose pcm_s16le for 16-bit wav and pcm_s32le for 32-bit wav.
        """
        filename = filename.replace('.mp4', '')
        if dst == None:
            dst =  self.defaultConvertedPath / f'{filename}.wav'
        else:
            dst = Path(dst) / f'{filename}.wav'

        if not Path(src).exists():
            return f'ERROR FILE {filename} DOES NOT EXIST IN THE ', 404

        if wav== '16bit':
            codec='pcm_s16le'
        else: # 32bit
            codec='pcm_s32le'

        
        video = AudioFileClip(str(src))
        video.write_audiofile(dst, codec=codec)

        return 'Success', 200
    
