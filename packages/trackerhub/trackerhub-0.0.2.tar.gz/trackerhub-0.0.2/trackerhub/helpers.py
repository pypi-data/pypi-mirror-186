import os
from pathlib import Path

import cv2

# limit the number of cpus used by high performance libraries
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

from trackerhub.track import load_detector_model, load_tracker_model, track_objects
from trackerhub.utils.config_utils import get_config
from torchyolo import YoloHub


config_path = 'trackerhub/configs/default_config.yaml'
tracker_prediction = track_objects(config_path)
    

        













