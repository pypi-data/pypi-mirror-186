import bpy


def get_frame() -> int:
    return bpy.context.scene.frame_current

def set_frame(frame) -> None:
    return bpy.context.scene.frame_set(frame)    
     
def set_keyframe(name, data_path="location", frame = None) -> None:
    """It puts a keyframe
    Args:
        name (_type_): The name of the object
        frame (_type_): The frame
        data_path (str, optional): It can be "location", "rotation_euler", "scale", "hide_render". Defaults to 'location'.
    """
    bpy.data.objects[name].keyframe_insert(data_path = data_path, frame = frame)


def set_keyframe_vertices(name, vertice_id, frame = get_frame()) -> None:
    bpy.data.objects[name].data.vertices[vertice_id].keyframe_insert("co", frame = frame)
    return None


def delete_keyframe():
    pass
