with open("blender_benchmark.log") as log:
    for line in log:
        if "Time: " in line:
            print(line[:-20])



datamatrix[0] = "Blender 2.7, Cube, CPU"
datamatrix[1] = "Blender 2.7, Cube, GPU"
datamatrix[2] = "Blender 2.8, Cube, CPU"
datamatrix[3] = "Blender 2.8, Cube, GPU"
datamatrix[4] = "Blender 2.8, Cube, CPU + GPU"
datamatrix[5] = "Blender 2.7, Bmw, CPU"
datamatrix[6] = "Blender 2.7, Bmw, GPU"
datamatrix[7] = "Blender 2.8, Bmw, CPU"
datamatrix[8] = "Blender 2.8, Bmw, GPU"
datamatrix[9] = "Blender 2.8, Bmw, CPU + GPU"
datamatrix[10] = "Blender 2.7, Classroom, CPU"
datamatrix[11] = "Blender 2.7, Classroom, GPU"
datamatrix[12] = "Blender 2.8, Classroom, CPU"
datamatrix[13] = "Blender 2.8, Classroom, GPU"
datamatrix[14] = "Blender 2.8, Classroom, CPU + GPU"
datamatrix[15] = "Blender 2.8, Attic, CPU"
datamatrix[16] = "Blender 2.8, Attic, GPU"
datamatrix[17] = "Blender 2.8, Attic, CPU + GPU"