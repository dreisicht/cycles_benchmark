import os
import subprocess
import time

print("Preparing Benchmark.")

blender27 = "./blender/blender-2.79b/blender.exe"
blender28 = "./blender/blender-2.80rc1/blender.exe"

cpu = "./scripts/cpu.py"
gpu = "./scripts/gpu.py"

attic = "attic_2.8"
bmw = "bmw_2.7"
classroom = "classroom_2.7"
cube27 = "default_cube_2.7"
cube28 = "default_cube_2.8"

base_string = "{} -b ./blends/{}.blend -P {} -o ./img/ -a"

subprocess.Popen(base_string.format(blender27, cube27, cpu))
