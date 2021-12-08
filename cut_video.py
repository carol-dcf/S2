import os
from time import gmtime
from time import strftime

def cut_N_seconds(input_path, start, N):
    """
    Cut video of some length into just the first N seconds starting from second "start"
    :param input_path: (str) path of the video file to be cutted
    :param start: (int) in which second you start
    :param N: (int) seconds to cut from video
    :return:
    """
    start_time = strftime("%H:%M:%S", gmtime(start))
    final_time = strftime("%H:%M:%S", gmtime(N + start))
    output_path = "cut_" + str(N) + "_" + input_path
    cut_command = "ffmpeg -ss " + start_time + " -i bbb.mp4 -to " + final_time + " -c copy " + output_path
    print(cut_command)
    os.system(cut_command)
    return