# Dependencies
import os
from time import gmtime
from time import strftime
import json
import requests

class MPEG:
    # Class constructor
    def __init__(self, input_path, short_input_path):
        self.input_path = input_path
        self.short_input_path = short_input_path # same input video but shorter for faster computations
        self.compatible_standards = [] # list of compatible broadcasting standards
        self.output_folder = "Results/"
        # create output folder if it does not exist yet
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

    # exercise 1: macroblocks and motion vectors
    def video_motion_vectors(self):
        """
        Get motionvectors from each macroblock of an input video
        :return: output_path -> path of the created video (motionvectors in this case)
        """
        output_path = self.output_folder + "analysis_" + self.short_input_path
        analysis_command = "ffmpeg -flags2 +export_mvs -i " + self.short_input_path + " -vf codecview=mv=pf+bf+bb " + output_path
        print("\n" + analysis_command + "\n")
        os.system(analysis_command)
        return output_path

    def cut_N_seconds(self, start, N):
        """
        Cut video of some length into just the first N seconds starting from second "start"
        :param input_path: (str) path of the video file to be cutted
        :param start: (int) in which second you start
        :param N: (int) seconds to cut from video
        :return:
        """
        start_time = strftime("%H:%M:%S", gmtime(start))
        final_time = strftime("%H:%M:%S", gmtime(N + start))
        output_path = self.output_folder + "cut_" + str(N) + "_" + self.input_path
        cut_command = "ffmpeg -ss " + start_time + " -i " + self.input_path + " -to " + final_time + " -c copy " + output_path
        print("\n" + cut_command + "\n")
        os.system(cut_command)
        return output_path

    # exercise 2: new container
    def new_container(self):
        """
        Create a new container from video, takes the (1 min) video and ads two different audio tracks (AAC and MP3)
        :return: output_path -> path of the created video (new container in this case)
        """
        ## Cut video
        input_path = self.cut_N_seconds(0, 60)

        ## Extract .mp3
        mp3_audio_path = self.output_folder + "mp3_audio_bbb.mp3"
        mp3_audio_command = "ffmpeg -i " + input_path + " -f mp3 -ac 2 -vn " + mp3_audio_path
        print("\n" + mp3_audio_command + "\n")
        os.system(mp3_audio_command)

        ## Extract .aac
        aac_audio_path = self.output_folder + "aac_audio_bbb.m4a"
        aac_audio_command = "ffmpeg -i " + input_path + " -c:a libfdk_aac -vbr 2 " + aac_audio_path
        print("\n" + aac_audio_command + "\n")
        os.system(aac_audio_command)

        ## Package
        output_path = self.output_folder + "multiple_BBB.mp4"
        package_command = "ffmpeg -i " + input_path + " -i " + mp3_audio_path + " -i " + aac_audio_path + " \
        -map 0:v -map 1:a -map 2:a \
        -metadata:s:a:0 title=\"MP3\" \
        -metadata:s:a:1 title=\"AAC\" \
        -c:v copy -c:a libopus " + output_path
        print("\n" + package_command + "\n")
        os.system(package_command)
        return output_path

    # exercise 3: assign broadcasting standard
    def broadcasting_standard(self):
        """
        Read tracks from a mp4 container and output the broadcasting standard(s) that would fit
        :return: compatible_standards -> list of fitting standard(s)
        """
        output_path = self.output_folder + "video_tracks.json"
        tracks_command = "ffprobe -loglevel 0 -print_format json -show_format -show_streams " + self.short_input_path + " > " + output_path
        os.system(tracks_command)

        ## Dictionary to map audio codec to compatible broadcast standard
        audio_standards = {
            "aac": ['DVB', 'ISDB', 'DTMB'],
            "ac3": ['DVB', 'ATSC', 'DTMB'],
            "mp3": ['DVB', 'DTMB'],
            "dra": ['DTMB']
        }
        ## Dictionary to map video codec to compatible broadcast standard
        video_standards = {
            "mpeg2video": ['DVB', 'ISDB', 'ATSC', 'DTMB'],
            "h264": ['DVB', 'ISDB', 'ATSC', 'DTMB'],
            "avs": ['DTMB']
        }

        ## lists to add multiple compatible standards for a given video
        audio_compatible_standards = []
        video_compatible_standards = []

        # read json
        with open(output_path) as f:
            data = json.load(f)
            streams = data['streams'] # read multiple streams (audio and video)
            for stream in streams:
                codec_name = stream['codec_name'] # get codec (aac, mp3, h264...)
                codec_type = stream['codec_type'] # get type (video or audio)
                # append standard to list
                if codec_type == 'video':
                    video_compatible_standards += video_standards[codec_name]
                elif codec_type == 'audio':
                    audio_compatible_standards += audio_standards[codec_name]
            ## get final compatible standard(s) (intersection between lists)
            self.compatible_standards = list(set(video_compatible_standards) & set(
                audio_compatible_standards))

        ## in case it does not fit any standard
        if self.compatible_standards == []:
            self.compatible_standards = 'ERROR'

        return self.compatible_standards

    # exercise 4: burn subtitles into video
    def burn_subtitles(self, subtitles_url):
        """
        Download subtitles from url and burn them into video
        :param subtitles_url: link to subtitles file (.srt)
        :return: output_path -> path of the created video (video + integrated subtitles in this case)
        """
        output_path = self.output_folder + "subtitled_" + self.short_input_path
        ## download subtitles
        r = requests.get(subtitles_url, allow_redirects=True)
        subtitles_path = self.output_folder + "my_own_subtitles.srt"
        open(subtitles_path, 'wb').write(r.content)
        ## integrate subtitles into video
        subtitles_command = "ffmpeg -i " + self.short_input_path + " -vf subtitles=" + subtitles_path + " " + output_path
        print("\n" +  subtitles_command + "\n")
        os.system(subtitles_command)
        return output_path