#Extended tileset exporter for godot
import bpy
import copy
import os 

def getMeshes():
    export_list = []
    for ob in bpy.data.objects:
        if(ob.type == "MESH"):
            export_list.append(ob)
    return export_list

def main():
    meshes = getMeshes()
    print(str(len(meshes))+" objects found")
    for obj in meshes:
        pos = moveToZero(obj)
        bpy.context.scene.objects.active = obj
        obj.select = True
        
        filepath = bpy.data.filepath
        directory = os.path.dirname(filepath)
        expath = str(directory)+"/objs/"+obj.name+".obj"
        print("exporting ... {}".format(expath))
        bpy.ops.export_scene.obj(filepath=expath, check_existing=True, filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_edges=True, use_normals=False, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=False, keep_vertex_order=False, global_scale=1.0, axis_forward='-Z', axis_up='Y', path_mode='AUTO')
        obj.select = False
        
        moveBack(obj,pos)
        
def moveToZero(obj):
    pos = copy.copy(obj.location)
    obj.location = (0.0,0.0,0.0)
    return pos

def moveBack(obj,pos):
    obj.location = pos
    
def createRotDuplicates(obj):
    dirs = {0:"d",180:"u",90:"r",-90:"l"}
    pass

main()

