# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 18:24:08 2025

@author: Affan
"""

import subprocess
import os
import sys
project_path = r"C:\Users\Affan\OneDrive\Music Recomendation app"
app_file = "main.py"

os.chdir(project_path)
preprocessed_file = r"C:\Users\Affan\OneDrive\Music Recomendation app\preprocessed.py"

# Run the file using the current Python interpreter
subprocess.run([sys.executable, preprocessed_file])
subprocess.run(f'streamlit run {app_file}', shell=True)
