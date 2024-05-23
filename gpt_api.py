from flask import Flask, request, jsonify
import cv2
import pytesseract
import openai
import os
from werkzeug.utils import secure_filename
