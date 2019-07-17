import os
import subprocess
import time

print("Preparing Benchmark.")

def render(version, filename, processor):
    base_string = "{} -b ./blends/{}.blend -P {} -o ./img/{} -f {}"
    
    command_str_tmp = base_string.format(version, filename[0], processor, filename[0]+"_##.png", filename[1])
    command_str = command_str_tmp.replace("./", cwd)
    print("--> Command String: ", command_str)
    subprocess.Popen(command_str)

cwd = os.getcwd().replace("\\", "/") +"/"

blender27 = "./blender/blender-2.79b/blender.exe"
blender28 = "./blender/blender-2.80rc1/blender.exe"

cpu = "./scripts/cpu.py"
gpu = "./scripts/gpu.py"

attic = ("attic_2.8", 1)
bmw = ("bmw_2.7", 1)
classroom = ("classroom_2.7", 1)
cube27 = ("default_cube_2.7", 1)
cube28 = ("default_cube_2.8", 1)

render(blender27, cube27, cpu)
render(blender27, cube27, cpu)