import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
caffe_model = os.path.join(ROOT, "res10_300x300_ssd_iter_140000.caffemodel")
prototxt_file = os.path.join(ROOT, "deploy.prototxt.txt")
confidence_value = 0.5