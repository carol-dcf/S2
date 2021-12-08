from broadcasting import MPEG

if __name__ == "__main__":
    # create instance
    semi2 = MPEG("BBB.mp4", "cut_bbb.mp4")

    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. Analyse video" + "\n\t 2. New container" + "\n\t 3. Broadcasting Standard" + "\n\t 4. Add Subtitles" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")
            semi2.video_motion_vectors()

        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")
            semi2.new_container()

        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")
            print(semi2.broadcasting_standard())

        elif (ex == 4):
            #### 4 #####
            print("\n\033[1mEXERCISE 4\033[0m")
            semi2.burn_subtitles("https://raw.githubusercontent.com/carol-dcf/S2/main/my_own_subtitles.srt")

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")