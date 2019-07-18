import os
import subprocess
import time

print("Preparing Benchmark.")

def render(version, filename, processor):
    base_string = "{} -b ./blends/{}.blend -P {} -o ./img/{} -f {}"

    # TODO make sure meta data is in blender enabled
    if processor == 0 and version == "./blender/blender-2.79b/blender.exe":
        renderscript = "./script/cpu27.py"
    elif processor == 1 and version == "./blender/blender-2.79b/blender.exe":
        renderscript = "./script/gpu27.py"
    elif processor == 0 and version == "./blender/blender-2.80rc1/blender.exe":
        renderscript = "./script/cpu28.py"
    elif processor == 1 and version == "./blender/blender-2.80rc1/blender.exe":
        renderscript = "./script/gpu28.py"
    elif processor == 2 and version == "./blender/blender-2.80rc1/blender.exe":
        renderscript = "./script/gpucpu28.py"
    
    opt = create_opt_str(version, filename, processor)
    command_str_tmp = base_string.format(version, filename[0], renderscript, opt, filename[1])
    command_str = command_str_tmp.replace("./", cwd)
    print("--> Command String: ", command_str)
    process = subprocess.run(
        command_str, encoding='utf-8', stdout=subprocess.PIPE)
    for line in process.stdout.split('\n'):
        print(line)

def create_opt_str(version, filename, processor):
    if version == "./blender/blender-2.79b/blender.exe":
        version_tmp = "2.79"
    elif version == "./blender/blender-2.80rc1/blender.exe":
        version_tmp = "2.80"

    if processor == 0:
        processor_tmp = "cpu"
    elif processor == 1:
        processor_tmp = "gpu"
    elif processor == 2:
            processor_tmp = "cpugpu"

    return filename[0]+"-"+processor_tmp+"-"+version_tmp+"_#.png"


cwd = os.getcwd().replace("\\", "/") +"/"

blender27 = "./blender/blender-2.79b/blender.exe"
blender28 = "./blender/blender-2.80rc1/blender.exe"

cpu = 0
gpu = 1
cpugpu = 2

attic = ("attic_2.8", 1)
bmw = ("bmw_2.7", 1)
classroom = ("classroom_2.7", 1)
cube27 = ("default_cube_2.7", 1)
cube28 = ("default_cube_2.8", 1)

render(blender27, cube27, cpu)
# render(blender28, cube27, cpu)
