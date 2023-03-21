from pyfiglet import Figlet
import moviepy.editor
from pathlib import Path


def mp4_to_mp3():
    try:
        preview_text = Figlet(font='big')
        print(preview_text.renderText('MP4 ---> MP3'))
        video_path = input('Please, enter file name: ')
        if video_path.count('.mp4') >= 1:
            video_path.replace('.mp4', '')
        else:
            video_path += '.mp4'
        video_file = Path(f'{video_path}')
        video = moviepy.editor.VideoFileClip(f'{video_file}')
        audio = video.audio
        audio.write_audiofile(f'{video_file.stem}.mp3')
        print('The video has been successfully converted to mp3 file!')
    except Exception:
        print('Check the correctness of the entered file name!')


def main():
    mp4_to_mp3()


if __name__ == '__main__':
    main()
