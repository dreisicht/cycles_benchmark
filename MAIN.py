import os
import subprocess
import datetime

prestart = datetime.datetime.now()
print("Preparing Benchmark.")

global last_time
last_time = datetime.datetime.now()

def render(version, filename, processor):
    base_string = "{} --enable-autoexec -b ./blends/{}.blend -P {} -o ./img/{} -f {}"

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
        renderscript = "./script/cpugpu28.py"

    opt = create_opt_str(version, filename, processor)
    command_str_tmp = base_string.format(
        version, filename[0], renderscript, opt, filename[1])
    command_str = command_str_tmp.replace("./", cwd)
    print("--> Launching new Test: ", command_str)
    process = subprocess.run(
        command_str, encoding='utf-8', stdout=subprocess.PIPE)

    # print(process.stdout)
    f = open("blender_benchmark.log", "a")
    f.write(process.stdout)
    # for line in process.stdout.split('\n'):
    # print(line)


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

def delta_timer():
    '''Function to get quick delta timing'''
    global last_time
    deltat = datetime.datetime.now() - last_time
    last_time = datetime.datetime.now()
    print(deltat)
    return deltat

# Static declarations


cwd = os.getcwd().replace("\\", "/") + "/"

blender27 = "./blender/blender-2.79b/blender.exe"
blender28 = "./blender/blender-2.80rc1/blender.exe"

cpu = 0
gpu = 1
cpugpu = 2

attic = ("attic_2.8", 1)
bmw = ("bmw_2.7", 1)
classroom = ("classroom_2.7", 1)
cube = ("default_cube_2.7", 1)
timeList = []

# Main Program

# Delete Contents of log file
f = open("blender_benchmark.log", "w")
f.write("")
f.close()


print("Preparation: ", delta_timer())
# Matrix



render(blender27, cube, cpu)
timeList.append(delta_timer())

render(blender27, cube, gpu)
timeList.append(delta_timer())

render(blender28, cube, cpu)
timeList.append(delta_timer())

render(blender28, cube, gpu)
timeList.append(delta_timer())

render(blender28, cube, cpugpu)
timeList.append(delta_timer())


# render(blender27, bmw, cpu)
timeList.append(delta_timer())

# render(blender27, bmw, gpu)
timeList.append(delta_timer())

# render(blender28, bmw, cpu)
timeList.append(delta_timer())

# render(blender28, bmw, gpu)
timeList.append(delta_timer())

# render(blender28, bmw, cpugpu)
timeList.append(delta_timer())


# render(blender27, classroom, cpu)
timeList.append(delta_timer())

# render(blender27, classroom, gpu)
timeList.append(delta_timer())

# render(blender28, classroom, cpu)
timeList.append(delta_timer())

# render(blender28, classroom, gpu)
timeList.append(delta_timer())

# render(blender28, classroom, cpugpu)
timeList.append(delta_timer())


# render(blender28, attic, cpu)
timeList.append(delta_timer())

# render(blender28, attic, gpu)
timeList.append(delta_timer())

# render(blender28, attic, cpugpu)
timeList.append(delta_timer())


# Printing of proper Benchmark


datamatrix = []

datamatrix.append("Blender 2.7, Default cube, CPU,")
datamatrix.append("Blender 2.7, Default cube, GPU,")
datamatrix.append("Blender 2.8, Default cube, CPU,")
datamatrix.append("Blender 2.8, Default cube, GPU,")
datamatrix.append("Blender 2.8, Default cube, CPU + GPU,")
datamatrix.append("Blender 2.7, Bmw, CPU,")
datamatrix.append("Blender 2.7, Bmw, GPU,")
datamatrix.append("Blender 2.8, Bmw, CPU,")
datamatrix.append("Blender 2.8, Bmw, GPU,")
datamatrix.append("Blender 2.8, Bmw, CPU + GPU,")
datamatrix.append("Blender 2.7, Classroom, CPU,")
datamatrix.append("Blender 2.7, Classroom, GPU,")
datamatrix.append("Blender 2.8, Classroom, CPU,")
datamatrix.append("Blender 2.8, Classroom, GPU,")
datamatrix.append("Blender 2.8, Classroom, CPU +, GPU")
datamatrix.append("Blender 2.8, Attic, CPU,")
datamatrix.append("Blender 2.8, Attic, GPU,")
datamatrix.append("Blender 2.8, Attic, CPU + GPU,")

j = 0
with open("blender_benchmark.log") as log:
    for line in log:
        if "Time: " in line:
            print(datamatrix[j], line[:-20], ",  ", timeList[j])
            j += 1
