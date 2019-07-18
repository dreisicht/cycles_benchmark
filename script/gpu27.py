import bpy

currentScene = bpy.context.scene.name

bpy.context.scene.render.engine = 'CYCLES'
bpy.data.scenes[currentScene].cycles.device = 'GPU'
bpy.context.scene.cycles.device = 'GPU'

bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = "CUDA"
bpy.context.user_preferences.addons['cycles'].preferences.devices[0].use = True
bpy.context.user_preferences.addons['cycles'].preferences.devices[1].use = True
