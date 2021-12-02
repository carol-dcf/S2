import macroblocks_motionvectors as mb

if __name__ == "__main__":
    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. Analyse video" + "\n\t 2. YUV histogram" + "\n\t 3. Resize video" + "\n\t 4. Change audio" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")
            mb.video_motion_vectors("cut_bbb.mp4")

        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")

        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")

        elif (ex == 4):
            #### 4 #####
            print("\n\033[1mEXERCISE 4\033[0m")

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")