import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--inputdir', type=str, default='./videos2')
parser.add_argument('--outputdir', type=str, default='./output2')
parser.add_argument('--fps', type=float, default=1)
args = parser.parse_args()

if not os.path.exists(args.outputdir):
    os.makedirs(args.outputdir)

# Read the video from specified path
total_frames_saved = 0
print(os.listdir(args.inputdir))
for video in os.listdir(args.inputdir):
    cap = cv2.VideoCapture(os.path.join(args.inputdir, video))
    print("processing video ", video)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        frame_number += 1
        if ret:
            if (frame_number / video_fps) % (1 / args.fps) == 0:
                total_frames_saved += 1
                cv2.imwrite(os.path.join(args.outputdir, "frame_" + str(total_frames_saved) + ".jpg"), frame)
                print("saving frame")
        else:
            print("next video")
            break