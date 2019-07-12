import bpy
import os


def run():
    # deselect all objects
    bpy.ops.object.select_all(action='DESELECT')    

    objects = bpy.context.scene.objects 
    for ob in objects:
        objects.active = ob
        ob.select = True

        if ob.type == 'MESH':
            bpy.ops.export_scene.obj(filepath=os.path.join(os.environ['OBJ_EXPORT_PATH'], ob.name + '.obj'), use_selection=True)

        ob.select = False


if __name__ == "__main__":
    run()

