import os

def video_motion_vectors(input_path):
    output_path = "analysis_" + input_path
    analysis_command = "ffmpeg -flags2 +export_mvs -i " + input_path + " -vf codecview=mv=pf+bf+bb " + output_path
    os.system(analysis_command)
    return