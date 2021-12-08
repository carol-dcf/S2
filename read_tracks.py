import os
import json

def broadcasting_standard(input_path):
    a = "ffprobe -loglevel 0 -print_format json -show_format -show_streams " + input_path + " > output.json"
    #os.system(a)
    standards = {
        "DVB": [
            {"Video": ['MPEG2',  'h264']},
            {"Audio": ['AAC', 'AC-3', 'MP3']}
        ],
        "ISDB": [
            {"Video": ['MPEG2', 'h264']},
            {"Audio": ['AAC']}
        ],
        "ATSC": [
            {"Video": ['MPEG2', 'h264']},
            {"Audio": ['AC-3']}
        ],
        "DTMB": [
            {"Video": ['MPEG2', 'h264', 'AVS', 'AVS+']},
            {"Audio": ['AAC', 'AC-3', 'MP3', 'DRA']}
        ]
    }
    audio_standards = {
        "aac": ['DVB', 'ISDB', 'DTMB'],
        "ac3": ['DVB', 'ATSC', 'DTMB'],
        "mp3": ['DVB', 'DTMB'],
        "dra": ['DTMB']
    }
    video_standards = {
        "mpeg2video": ['DVB', 'ISDB', 'ATSC', 'DTMB'],
        "h264": ['DVB', 'ISDB', 'ATSC', 'DTMB'],
        "avs": ['DTMB'],
        "AVS+": ['DTMB']
    }

    compatible_standards = []
    audio_compatible_standards = []
    video_compatible_standards = []

    # read json
    with open('output.json') as f:
        data = json.load(f)
        streams = data['streams']
        for stream in streams:
            codec_name = stream['codec_name']
            codec_type = stream['codec_type']
            if codec_type == 'video':
                video_compatible_standards += video_standards[codec_name]
            elif codec_type == 'audio':
                audio_compatible_standards += audio_standards[codec_name]
        compatible_standards = list(set(video_compatible_standards) & set(audio_compatible_standards))

    if compatible_standards == []:
        compatible_standards = 'ERROR'
    return compatible_standards