# output.py
# Usage 1: python output.py --type image --input Testcases/Street.JPG --output Results/Street.JPG
# Usage 2: python output.py --type video --input Testcases/SampleV.mp4 --output Results/SampleV.avi
# Authors: Nguyen Ngoc Lan Phuong <19520227@gm.uit.edu.vn>
#          Cao Hung Phu           <19520214@gm.uit.edu.vn>
#          Le Quang Nha           <19520195@gm.uit.edu.vn>

# %% Import library
from SocialDetection import *
import argparse
import os
from tqdm import tqdm


# %% Threshold
THRESHOLD = 120

# %% Main
if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='video')
    parser.add_argument('--input', type=str, default='Testcases/SampleV.mp4')
    parser.add_argument('--output', type=str, default='Results/SampleV.avi')
    
    # Get arguments
    args = parser.parse_args()
    detectType = args.type.lower()
    imFilename = args.input
    omFilename = args.output
    
    # Check arguments
    if detectType not in ['image', 'video']:
        print("Error type!!!")
        print("Type: image, video")
        print("Example 1: python output.py --type image --input Testcases/Street.JPG --output Results/Street.JPG")
        print("Example 2: python output.py --type video --input Testcases/SampleV.mp4 --output Results/SampleV.avi")
        exit()
        
    if not os.path.exists(imFilename):
        print("Error input: Input not found!!!")
        exit()
    
    # Detector
    detector = SocialDetection(THRESHOLD)
    
    # Clear console
    os.system('cls')
    
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
        print('Path output     : {}'.format(omFilename))
        print('Frame size      : {} x {}'.format(frWidth, frHeight))
        print('Number of frame : {}'.format(frNumber))
        print('Frame per second: {}'.format(frPS))
        
        # Check valid input
        if not detector.validImageSize(frWidth * frHeight):
            raise 'Oops! What a lovely bug: Image quality lower than 480p'
            
        # Write output
        imWriter = cv2.VideoWriter(omFilename, cv2.VideoWriter_fourcc(*'XVID'), frPS, (frWidth, frHeight))
        for frIndex in tqdm(range(frNumber)):
            _, image = imReader.read()
            if not _: raise 'Oops! What a lovely bug: Fail to capture image'
            image_result = detector.getResult(image)
            imWriter.write(image_result)
            
    else:
        # Read input image
        print('Path input      : {}'.format(imFilename))
        image = cv2.imread(imFilename)
        # Write output image
        cv2.imwrite(omFilename, detector.getResult(image))
        print('Path output     : {}'.format(omFilename))
  
  
  
