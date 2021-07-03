import subprocess
import cv2
import os
import numpy
from scipy.ndimage import rotate
import json
from face_detection.detect_faces import detect_face


NUM_OF_FRAMES = 30
file_name = 'frame_record.txt'
video_dir = os.getcwd() + '/datasets/videos/'
print(video_dir)

with open(file_name) as json_file:
    content = json.load(json_file) 

def extract_frames(video, id):
    content.update({id:id})
    with open(file_name, 'w')as file:
        json.dump(content, file, indent=4, sort_keys=True)
    i = 0
    cam = cv2.VideoCapture(video)
    while True:
        ret, im = cam.read()

        if ret:
            result_from_face_detection = detect_face(im)
            print("Detection result for {} is {} : {}".format(i,result_from_face_detection,len(result_from_face_detection)))
            if len(result_from_face_detection) == 0:
                break
            else:
                classpath = os.path.join('datasets/raw',str(id))
                if not os.path.exists(classpath):
                    os.mkdir(classpath)
                i += 1
                cv2.imwrite(os.path.join(classpath, str(id) + str(i) + ".jpg"), im)
            if i > NUM_OF_FRAMES:
                break

        else:
            break

def frames(video_dir, file_name):
    try:
        with open(file_name) as json_file:
            content = json.load(json_file)
    except:
        with open(file_name, 'w')as json_file:
            json.dump({}, json_file)
            content = json.load(json_file)
        raise

    for root in os.listdir(video_dir):
        vid_file = root.split('.')[0]
        # import pdb;pdb.set_trace()
        video_path = os.path.join(video_dir,root)
        print("Extracting frames for {}".format(video_path))
        if vid_file not in content:
            import pdb;
            pdb.set_trace()
            extract_frames(video_path, vid_file)

if __name__== "__main__":
    frames(video_dir,file_name)