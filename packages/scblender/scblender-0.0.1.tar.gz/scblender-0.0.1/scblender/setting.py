import bpy

def set_frame_format(format=[1920, 1080]):
    """
    This function defines the format of the scene frame,
    by default the format is 1920 by 1800
    """
    bpy.context.scene.render.resolution_x = format[0]
    bpy.context.scene.render.resolution_y = format[1]


def __purge_orphans():
    if bpy.app.version >= (3, 0, 0):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
    else:
        # call __purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            __purge_orphans()


def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene
    """
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        select_particle(obj.name)

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    __purge_orphans()


def set_timeline(timeline):
    """
    It puts the time line at some position
    """
    bpy.context.scene.frame_set(timeline)


def transform_pivot_point(type):
    """This function change the transformation pivot point

    Args:
        type (str): bounding box center, cursor, individual origins, median point, active element
    """
    if type == "bounding box center":
        bpy.context.scene.tool_settings.transform_pivot_point = "BOUNDING_BOX_CENTER"

    elif type == "cursor":
        bpy.context.scene.tool_settings.transform_pivot_point = "CURSOR"

    elif type == "individual origins":
        bpy.context.scene.tool_settings.transform_pivot_point = "INDIVIDUAL_ORIGINS"

    elif type == "median point":
        bpy.context.scene.tool_settings.transform_pivot_point = "MEDIAN_POINT"

    elif type == "active element":
        bpy.context.scene.tool_settings.transform_pivot_point = "ACTIVE_ELEMENT"


def transform_orientation(type):
    """This function change the transformation orientation

    Args:
        type (str): global, local, normal, gimbal, view, cursor
    """
    if type == "global":
        bpy.context.scene.transform_orientation_slots[0].type = "GLOBAL"

    elif type == "local":
        bpy.context.scene.transform_orientation_slots[0].type = "LOCAL"

    elif type == "normal":
        bpy.context.scene.transform_orientation_slots[0].type = "NORMAL"

    elif type == "gimbal":
        bpy.context.scene.transform_orientation_slots[0].type = "GIMBAL"

    elif type == "view":
        bpy.context.scene.transform_orientation_slots[0].type = "VIEW"

    elif type == "cursor":
        bpy.context.scene.transform_orientation_slots[0].type = "CURSOR"


def select_particle(name, deselect_others=True, select=True, active=True):
    """It select and activate objects

    Args:
        name (str): name of the object
        deselect_others (bool, optional): if it should deselect all the others objects. Defaults to True.
        select (bool, optional): Defaults to True.
        active (bool, optional): Defaults to True.
    """
    if deselect_others:
        bpy.ops.object.select_all(action="DESELECT")
    bpy.data.objects[name].select_set(select)
    if active:
        bpy.context.view_layer.objects.active = bpy.data.objects[name]


def set_particle_visibility(
    name,
    hide_select=False,
    hide_in_viewport=False,
    globally_viewport=False,
    hide_render=False,
    particle_in_object_mode=True,
):
    """It controls the visibility of the object

    Args:
        name (str): the name of the object
        hide_select (bool, optional): disable the posibility of select the object . Defaults to False.
        hide_in_viewport (bool, optional): Defaults to False.
        globally_viewport (bool, optional): Defaults to False.
        hide_render (bool, optional): Defaults to False.
        particle_in_object_mode (bool, optional): at the end it puts on the object mode. Defaults to True.
    """
    select_particle(name)  # calling the function select_particle

    bpy.data.objects[name].hide_select = hide_select
    bpy.context.active_object.hide_set(hide_in_viewport)
    bpy.context.active_object.hide_viewport = globally_viewport
    bpy.data.objects[name].hide_render = hide_render

    if particle_in_object_mode and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()


def set_object_mode(mode="object"):
    """It change the object mode

    Args:
        mode (str, optional): this variable can be 'object', 'edit' 'sculpt', 'vertex_paint',
        'WEIGHT_PAINT' or 'TEXTURE_PAINT'. Defaults to 'OBJECT'.
    """
    bpy.ops.object.mode_set(mode=mode.upper())


def apply_transformations(name, location=True, rotation=True, scale=True):
    """
    This function reset informations about position, rotation and scale of the particle
    """
    set_particle_visibility(name)

    bpy.ops.object.transform_apply(location=location, rotation=rotation, scale=scale)
    try:
        name._position = ([0, 0, 0]) if location else name._position
        name._rotation = ([0, 0, 0]) if rotation else name._rotation
        name._scale = ([0, 0, 0]) if scale else name._scale
    except:
        pass


def create_collection(collection_name):
    """It creates a collection if it doesn't exist yet

    Args:
        collection_name (str)
    """
    exist = False
    for c in list(bpy.data.collections):
        if c.name == collection_name:
            exist = True
            break
    if exist is False:
        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)


def delete_object(name):
    """It delets particles

    Args:
        name (str): the name of the particle you want to delete
    """
    try:
        select_particle(name)
        bpy.ops.object.delete()
    except:
        pass


def move_to_collection(object_name, collection_name):
    """It link an object to a specific collection

    Args:
        object_name (str)
        collection_name (str)
    """
    try:
        bpy.data.collections[collection_name].objects.link(
            bpy.data.objects[object_name]
        )
        bpy.data.scenes["Scene"].collection.objects.unlink(
            bpy.data.objects[object_name]
        )
    except:
        pass

    for c in list(bpy.data.collections):
        if c.name != collection_name:
            try:
                c.objects.unlink(bpy.data.objects[object_name])
            except:
                pass



# def set_keyframe_vertices():
#     bpy.data.window_managers["WinMan"].animall_properties.key_points = True
#     bpy.context.scene.animall_properties.key_point_location = True
#     bpy.context.scene.animall_properties.key_radius = True
#     bpy.context.scene.animall_properties.key_tilt = True
#     bpy.context.scene.animall_properties.key_material_index = True
#     bpy.context.scene.animall_properties.key_shape_key = True
#     bpy.ops.anim.insert_keyframe_animall()
#     return None


def delete_keyframe():
    pass


def change_cursor_position(position):
    bpy.context.scene.cursor.location = position


def render():
    pass
