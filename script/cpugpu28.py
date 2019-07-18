import bpy
cycles_pref = bpy.context.preferences.addons['cycles'].preferences
cycles_pref.compute_device_type = 'CUDA'

bpy.context.scene.cycles.device = 'GPU'
print(bpy.context.scene.cycles.device)
bpy.ops.render.render(True)

for device in cycles_pref.devices:
    if "GeForce" in str(device.name):
        device.use = True
    if "GHz" in str(device.name):
        device.use = True

    print(device.name, device.use)
