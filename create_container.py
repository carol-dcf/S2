import os
import cut_video as cv

def new_container(input_path):
    ## Cut video
    cv.cut_N_seconds(input_path, 0, 60)

    ## Extract .mp3
    input_path = "cut_60_BBB.mp4"
    mp3_audio_path = "mp3_audio_bbb.mp3"
    mp3_audio_command = "ffmpeg -i " + input_path + " -f mp3 -ac 2 -ab 192000 -vn " + mp3_audio_path
    print("\n" + mp3_audio_command)
    os.system(mp3_audio_command)

    ## Extract .aac
    aac_audio_path = "aac_audio_bbb.m4a"
    aac_audio_command = "ffmpeg -i " + input_path + " -c:a libfdk_aac -b:a 128k " + aac_audio_path
    print("\n" + aac_audio_command)
    os.system(aac_audio_command)

    ## Package
    package_command = "ffmpeg -i cut_60_BBB.mp4 -i " + mp3_audio_path + " -i " + aac_audio_path + " \
    -map 0:v -map 1:a -map 2:a \
    -metadata:s:a:0 title=\"MP3\" \
    -metadata:s:a:1 title=\"AAC\" \
    -c:v copy -c:a libopus multiple_BBB.mp4"
    print("\n" + package_command)
    os.system(package_command)
    return
