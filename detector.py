# detector.py
# Usage 1: python detector.py --type image --input Testcases/Street.JPG
# Usage 2: python detector.py --type video --input Testcases/SampleV.mp4
# Authors: Nguyen Ngoc Lan Phuong <19520227@gm.uit.edu.vn>
#          Cao Hung Phu           <19520214@gm.uit.edu.vn>
#          Le Quang Nha           <19520195@gm.uit.edu.vn>

# %% Import library
from SocialDetection import *
import argparse
import os
import imutils
import ctypes

# %% Config
THRESHOLD = 120
OUT_HEIGHT = 1280
OUT_WIDTH = 720

# %% Main
if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='video')
    parser.add_argument('--input', type=str, default='Testcases/SampleV.mp4')

    # Get arguments
    args = parser.parse_args()
    detectType = args.type.lower()
    imFilename = args.input

    # Check arguments
    if detectType not in ['image', 'video']:
        print("Error type!!!")
        print("Type: image, video")
        print("Example 1: python detector.py --type image --input Testcases/Street.JPG")
        print("Example 2: python detector.py --type video --input Testcases/SampleV.mp4")
        exit()

    if not os.path.exists(imFilename):
        print("Error input: Input not found!!!")
        exit()

    # Detector
    detector = SocialDetection(THRESHOLD)

    # Clear console
    os.system('cls')

    # Show msgbox
    ctypes.windll.user32.MessageBoxW(0, "Press: Ctrl + C or press 'Esc' key to exit", "Notification!", 0)

    if detectType == 'video':
        # Read input video
        imReader = cv2.VideoCapture(imFilename)
        frWidth  = int(imReader.get(cv2.CAP_PROP_FRAME_WIDTH))
        frHeight = int(imReader.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frNumber = int(imReader.get(cv2.CAP_PROP_FRAME_COUNT))  # Number of frames
        frPS     = imReader.get(cv2.CAP_PROP_FPS)               # Frame per second

        # Print information
        print('=== CAPTURE INFORMATION ===')
        print('Path input      : {}'.format(imFilename))
        print('Frame size      : {} x {}'.format(frWidth, frHeight))
        print('Number of frame : {}'.format(frNumber))
        print('Frame per second: {}'.format(frPS))

        # Check valid input
        if not detector.validImageSize(frWidth * frHeight):
            raise 'Oops! What a lovely bug: Image quality lower than 480p'

        # Show output
        for frIndex in range(frNumber):
            _, image = imReader.read()
            if not _: raise 'Oops! What a lovely bug: Fail to capture image'
            frame_show = imutils.resize(detector.getResult(image), height=OUT_HEIGHT, width=OUT_WIDTH)
            cv2.imshow('CS117.L21 - Social Detection', frame_show)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        imReader.release()
        cv2.destroyAllWindows()

    else:
        # Read input image
        print('Path input      : {}'.format(imFilename))
        # Show output
        frame_show = imutils.resize(detector.getResult(cv2.imread(imFilename)), height=OUT_HEIGHT, width=OUT_WIDTH)
        cv2.imshow('CS117.L21 - Social Detection', frame_show)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




