from PySide6.QtCore import *
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWebEngineCore import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWidgets import *
from importlib.metadata import version
from urllib import request
from pkg_resources import parse_version
from pathlib import Path
from datetime import datetime
import subprocess
from sys import platform
from shutil import copytree, ignore_patterns
from plyer import notification
from functools import cached_property
from string import Template
import json
import time
import os
import sys
import re
from . import *
from pyshortcuts import make_shortcut
