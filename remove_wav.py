#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# python remove_wav.py
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import soundfile as sf
import os

root_folder = "/data1/usermessage/zqy/work/data"


bad_file = []
audio_files = []

for root, dirs, files in os.walk(root_folder):
    # 遍历当前目录下的所有文件
    for file in files:
        if file.endswith(".wav"):
            file_path = os.path.join(root, file)  # 获取文件路径
            audio_files.append(file_path)  # 将文件路径添加到audio_files列表中

for file in audio_files:
    try:
        audio, samplerate = sf.read(file)
        duration_in_sec = len(audio) / samplerate  # 获取音频长度（以秒为单位）
        if duration_in_sec <= 1:
            bad_file.append(os.path.abspath(file))
            os.remove(file)  # 删除小于1秒的文件
    except Exception as e:
        print(f"Error: {e}")
        bad_file.append(os.path.abspath(file))
        os.remove(file)  # 删除出错的文件

with open("/data1/usermessage/zqy/work/data/wrong_data/wrong_wav1.txt", "w") as f:
    f.write("\n".join(bad_file))
