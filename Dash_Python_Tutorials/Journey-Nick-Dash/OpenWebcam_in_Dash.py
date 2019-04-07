import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

from flask import Flask, Response
import cv2
import datetime
import time
import math

import detection
class VideoCamera(object):

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image, threshold = detection.detection(success,image)
        ret, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

    def get_frame_threshold(self):
        success, image = self.video.read()
        image, threshold = detection.detection(success,image)
        ret, jpeg = cv2.imencode('.jpg',threshold)
        return jpeg.tobytes()

def gen(camera):
    
    while True:
        frame = camera.get_frame()
        frame_threshold = camera.get_frame_threshold()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

@server.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

app.layout = html.Div([
    html.H1("Webcam Test"),
    html.Img(src="/video_feed"),
])
