import bpy
# bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
# bpy.context.user_preferences.addons['cycles'].preferences.device[0].use = True
bpy.context.scene.cycles.device = 'CPU'
bpy.ops.render.render(True)
