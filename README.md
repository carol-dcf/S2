# S2
## S2 of SCAV subject
In this project you can see applied some functionalities of the ffmpeg software into the BBB video. All the functions can be applied to any other video if the input_path is changed in the *main.py* file.

To run the program, run the *main.py* and a fully interactive menu will appear. There, you can navigate trough the different proposed exercises.

Instructions are really clear once you are running the files, however, here's a quick guide on how to use it.

| Num | Title         | Short explanation of the function                                                                                                                |
|-----|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Analyse video     | Given an input file, outputs a video that shows the motionvectors of each macroblock (note that on the latest ffmpeg version macroblocks per se cannot be visualized.) |
| 2   | New container | Given an input file, cut the video into 1 min, export audio into 2 different codecs (MP3 and AAC) and package everything into a MP4. |
| 3   | Broadcasting standard  | Given an input file, propose broadcasting standard(s) that would fit.               |
| 4   | Add subtitles  | Given an input video file and subtitles, burn them into the video track. |
| 0   | Exit          | Close application. |

(All the files generated in the different exercises on the BBB video can be seen in the Results folder)
