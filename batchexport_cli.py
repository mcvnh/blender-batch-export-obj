import bpy
import os


def run():
	# Deselect all objects
	for obj in bpy.context.selected_objects:
		obj.select_set(False) 

    # Iterate over all objects and export them
	objects = bpy.context.view_layer.objects
	for ob in objects:
		objects.active = ob
		ob.select_set(True)

		if ob.type == 'MESH':
			bpy.ops.export_scene.obj(filepath=os.path.join(os.environ['OBJ_EXPORT_PATH'], ob.name + '.fbx'), use_selection=True)

		ob.select_set(False)


if __name__ == "__main__":
	run()
