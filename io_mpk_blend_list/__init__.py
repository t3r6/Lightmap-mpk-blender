from bpy_extras.io_utils import (
    ExportHelper,
)
from bpy.props import (
    BoolProperty,
    StringProperty,
)

import bpy
bl_info = {
   "name": "Painkiller blendlist export",
    "author": "dilettante",
    "version": ( 1, 0, 0 ),
    "blender": ( 4, 0, 0 ),    
    "location": "File > Import-Export",
    "description": "Painkiller blendlist export",
    "doc_url": "https://github.com/max-ego/PK_tools/",
    "category": "Import-Export",
}

class ExportBlendList(bpy.types.Operator, ExportHelper):
    bl_idname = "export_blend_list.txt"
    bl_label = 'Export blendlist'
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".txt"
    filter_glob: StringProperty(default="*.txt", options={'HIDDEN'})

    def execute(self, context):
        keywords = self.as_keywords(ignore=("filter_glob",
                                            "check_existing",
                                            ))
		
        save_txt(context, **keywords)

        return {'FINISHED'}

    def draw(self, context):
        pass

# Add to a menu
def menu_func_export(self, context):
    self.layout.operator(ExportBlendList.bl_idname, text="Painkiller blendlist (.txt)")


def register():
    bpy.utils.register_class(ExportBlendList)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportBlendList)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()


def save_txt(context, filepath=""):

    print("exporting blendlist: %r..." % (filepath), end="")

    file = open(filepath, 'w')

    writeTXT(file, context)

    file.close()

    if bpy.ops.object.select_all.poll():
        bpy.ops.object.select_all(action='DESELECT')


def writeTXT(file, context):
    view_layer = context.view_layer
    objects = [obj for obj in view_layer.objects if obj.visible_get(view_layer=view_layer)]
    for object in objects:
        if object.type == 'MESH':
            # mesh name
            file.write( object.name + "\n" )
            # Offset/Tile colorMap
            file.write( "0.000000\n0.000000\n1.000000\n1.000000\n" )
            colls = object.users_collection
            # lightMap name
            file.write(("\n" , colls[0].name + "\n")[len(colls) > 0 and len( object.data.uv_layers ) > 1])
            # blendMap name
            file.write( "\n" )
            # Offset/Tile blendMap
            file.write( "0.000000\n0.000000\n1.000000\n1.000000\n" )
            # alphaMap name
            file.write( "\n" )
