import os

def burn_subtitles(input_path, subtitles_url):
    output_path = "subtitled_" + input_path
    subtitles = "My_own_subtitles.srt"
    subtitles_command = "ffmpeg -i " + input_path + " -vf subtitles=" + subtitles + " " + output_path
    os.system(subtitles_command)
    return