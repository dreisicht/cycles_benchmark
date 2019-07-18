import bpy
cycles_pref = bpy.context.preferences.addons['cycles'].preferences
cycles_pref.compute_device_type = 'CUDA'
print(cycles_pref)
cycles_pref.devices[0].use = True
bpy.context.scene.cycles.device = 'GPU'
bpy.ops.render.render(True)
