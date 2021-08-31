# output.py
# Usage: python output.py --input input/video_1.mp4 --output output/video_1.mp4
# Authors: Nguyen Ngoc Lan Phuong <19520227@gm.uit.edu.vn>
#          Cao Hung Phu           <19520214@gm.uit.edu.vn>
#          Le Quang Nha           <19520195@gm.uit.edu.vn>

# %% Import library
from SocialDetection import *
import argparse
from tqdm import tqdm

# %% Threshold
THRESHOLD = 120

# %% Main
if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input/video_1.mp4')
    parser.add_argument('--output', type=str, default='output/video_1.avi')

    # Detector
    detector = SocialDetection(THRESHOLD)
    
    # Get arguments
    args = parser.parse_args()
    imFilename = args.input
    omFilename = args.output

    # Read input
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
    
  
  
  
