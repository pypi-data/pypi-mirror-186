import numpy
import bpy

class Particle:
    """This class create a particle with the following characteristics:
    Parameters
    ----------
    name : string
    position : array (x,y,z)
    rotation : array (yz,zx,xy)
    scale : array (sx,sy,sz)
    collection : string : (It is the name of the collection to which the particle belongs)
    """

    def __init__(self, name="particle", position=None, rotation=None, scale=None) -> None:
        self._name = name

        try:
            self._position = (
                position
                if position != None
                else [bpy.data.objects[self._name].location[i] for i in range(3)]
            )
            self._rotation = (
                rotation
                if rotation != None
                else [bpy.data.objects[self._name].rotation_euler[i] for i in range(3)]
            )
            self._scale = (
                scale
                if scale != None
                else [bpy.data.objects[self._name].scale[i] for i in range(3)]
            )
        except:
            pass

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        bpy.data.objects[self._name].name = name
        self._name = name
        return None

    def get_position(self) -> list:
        return [bpy.data.objects[self._name].location[i] for i in range(3)]

    def set_position(self, position: list) -> None:
        if self._checking_the_type_and_the_dimensionality(position):
            bpy.data.objects[self._name].location = position
            self._position = position
        return None

    def get_rotation(self) -> list:
        return [bpy.data.objects[self._name].rotation_euler[i] for i in range(3)]

    def set_rotation(self, rotation: list) -> None:
        if self._checking_the_type_and_the_dimensionality(rotation):
            bpy.data.objects[self._name].rotation_euler = rotation
            self._rotation = rotation
        return None

    def get_scale(self) -> list:
        return [bpy.data.objects[self._name].scale[i] for i in range(3)]

    def set_scale(self, scale: list) -> None:
        if self._checking_the_type_and_the_dimensionality(scale):
            bpy.data.objects[self._name].scale = scale
            self._scale = scale
        return None

    def get_vertices(self) -> list:
        """
        Returns:
            array: It returns an array with the position of the vertices
        """
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[self._name].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[self._name]
        return [v.co for v in bpy.context.active_object.data.vertices]

    def set_vertices(self, vertice_id: int, new_coordinate: list) -> None:
        if bpy.context.active_object.mode == "EDIT":
            bpy.ops.object.editmode_toggle()
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[self._name].select_set(True)
        bpy.context.active_object.data.vertices[vertice_id].co = new_coordinate
        return None

    @staticmethod
    def _checking_the_type_and_the_dimensionality(greatness) -> bool:
        """ This function check if the things that are being pass 
        for the methods involving position, rotation and scale
        are an array of dimension three  

        Args:
            greatness (any): what we want to check

        Returns:
            bool: It return three if it is and 3 dimension array and false otherwise
        """
        if (len(greatness) == 3) and (
            isinstance(greatness, list) or isinstance(greatness, np.ndarray)
        ):
            return True
        else:
            print("You must provide as input a list or a numpy array of length 3!")
            return False




