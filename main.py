import macroblocks_motionvectors as mb
import create_container as cc
import read_tracks as rt
import subtitles as sub

if __name__ == "__main__":
    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. Analyse video" + "\n\t 2. BBB container" + "\n\t 3. Broadcasting Standard" + "\n\t 4. Add Subtitles" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")
            mb.video_motion_vectors("cut_bbb.mp4")

        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")
            cc.new_container("BBB.mp4")

        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")
            print(rt.broadcasting_standard("cut_bbb.mp4"))

        elif (ex == 4):
            #### 4 #####
            print("\n\033[1mEXERCISE 4\033[0m")
            sub.burn_subtitles("cut_bbb.mp4", "ws")

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")