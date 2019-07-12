import bpy
import os


bl_info = {
    "name": "Batch Export",
    "category": "Import-Export",
    "version": (1, 0),
    "location": "Info > File > Export > OBJ Batch Export",
    "author": "Anh Mac"
}

def register():
    bpy.utils.register_class(BatchExport)
    bpy.types.INFO_MT_file_export.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BatchExport)
    bpy.types.INFO_MT_file_export.remove(menu_func)

def menu_func(self, context):
    self.layout.operator(BatchExport.bl_idname)


class BatchExport(bpy.types.Operator):
    bl_idname = "file.obj_batch_export"
    bl_label = "OBJ Batch Export"
    bl_options = {'REGISTER'}

    filepath = bpy.props.StringProperty(
            name="File Path",
            maxlen=1024,
            subtype="DIR_PATH",
            )

    def execute(self, context):
        # deselect all objects
        bpy.ops.object.select_all(action='DESELECT')    

        # loop through all the objects in the scene
        for ob in context.scene.objects:
            # make the current object active and select it
            context.scene.objects.active = ob
            ob.select = True

            # make sure that we only export meshes
            if ob.type == 'MESH':
                # export the currently selected object to its own file based on its name
                bpy.ops.export_scene.obj(filepath=os.path.join(self.filepath, ob.name + '.obj'), use_selection=True)

            # deselect the object and move on to another if any more are left
            ob.select = False

        return {'FINISHED'}

    def invoke(self, context, event):
        self.filepath = ""
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


if __name__ == "__main__":
    register()

