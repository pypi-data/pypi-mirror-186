import bpy
from .particle import Particle
from .setting import *


class Sphere(Particle):
    def __init__(
        self, name="sphere", position=([0, 0, 0]), rotation=([0, 0, 0]), scale=([1, 1, 1])
    ):
        super().__init__(name=name, position=position, rotation=rotation, scale=scale)
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=1,
            enter_editmode=False,
            align="WORLD",
            location=self._position,
            scale=self._scale,
        )
        bpy.context.object.name = self._name


class Vertice(Particle):
    def __init__(self, name="vertice", position=([0, 0, 0])):
        super().__init__(name=name, position=position)
        bpy.ops.mesh.primitive_vert_add()
        bpy.context.object.name = self._name
        set_object_mode("OBJECT")
        self.set_position(position)


class Mesh(Particle):
    def __init__(
        self,
        name="mesh",
        position=([0, 0, 0]),
        rotation=([0, 0, 0]),
        scale=([1, 1, 1]),
        vertices=[],
        edges=[],
        faces=[],
    ):
        super().__init__(name=name, position=position, rotation=rotation, scale=scale)
        self._vertices = vertices
        self._edges = edges
        self._faces = faces
        # vertices = bpy.context.active_object.data.vertices
        # edges = bpy.context.active_object.data.edges
        # faces = bpy.context.active_object.data.polygons
        mesh = bpy.data.meshes.new(self._name)
        obj = bpy.data.objects.new(self._name, mesh)
        col = bpy.data.collections.get("Collection")
        col.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        mesh.from_pydata(self._vertices, self._edges, self._faces)


class Path_curve(Particle):
    def __init__(self, name="path_curve", position=([0, 0, 0])):
        super().__init__(name=name, position=position)
        bpy.ops.curve.primitive_nurbs_path_add(
            radius=1,
            enter_editmode=False,
            align="WORLD",
            location=self._position,
            scale=self._scale,
        )
        bpy.context.object.name = self._name


class Bezier_curve(Particle):
    def __init__(
        self,
        name="bezier",
        position=([0, 0, 0]),
        rotation=([0, 0, 0]),
        scale=([1, 1, 1]),
    ):
        super().__init__(name=name, position=position, scale=scale)
        bpy.ops.curve.primitive_bezier_curve_add(
            radius=1,
            enter_editmode=False,
            align="WORLD",
            location=self._position,
            scale=self._scale,
        )
        bpy.context.object.name = self._name
        
        
class Camera(Particle):
    def __init__(
        self,
        name="camera",
        position=([0, 0, 0]),
        rotation=([0, 0, 0]),
        scale=([1, 1, 1]),
        focal_length=85,
    ):
        super().__init__(name=name, position=position, rotation=rotation, scale=scale)
        self.focal_length = focal_length
        bpy.ops.object.camera_add(
            enter_editmode=False,
            align="VIEW",
            location=self._position,
            rotation=self._rotation,
            scale=self._scale,
        )
        bpy.context.object.name = self._name
        bpy.context.object.data.lens = self.focal_length
        
        
class Timer(Particle):
    def __init__(
        self,
        name="timer",
        position=([0, 0, 0]),
        rotation=([0, 0, 0]),
        scale=([1, 1, 1]),
        frame=24,
    ):
        super().__init__(name=name, position=position, rotation=rotation, scale=scale)
        self.frame = frame
        bpy.ops.object.text_add(
            enter_editmode=False,
            align="WORLD",
            location=self._position,
            rotation=self._rotation,
            scale=self._scale,
        )
        bpy.ops.object.modifier_add(type="SOLIDIFY")
        bpy.context.object.modifiers["Solidify"].thickness = 0.02
        bpy.context.object.data.align_x = "CENTER"
        bpy.context.object.data.align_y = "CENTER"
        bpy.context.object.name = self._name
        scene = bpy.context.scene
        obj = scene.objects[self._name]

        def recalculate_text(scene):
            if scene.frame_current in range(0, 60 * self.frame):
                obj.data.body = (
                    str(int(bpy.context.scene.frame_current / self.frame)) + "s"
                )
            else:
                min = int(bpy.context.scene.frame_current / self.frame) // 60
                obj.data.body = (
                    str(min)
                    + "min  "
                    + str(int(bpy.context.scene.frame_current / self.frame) - 60 * min)
                    + "s"
                )

        bpy.app.handlers.frame_change_post.append(recalculate_text)




# if __name__ == "__main__":
#     # m = Mesh(
#     #     vertices=((0, 1, 0), (1, 0, 0), (0, 0, 1), (-1, 0, 0)),
#     #     edges=([0, 1], [1, 2], [0, 2], [0, 3], [2, 3]),
#     #     faces=([0, 1, 2], [2, 0, 3]),
#     # )

if __name__ == "__main__":
    
    
    mesh = Mesh(
        vertices = ((0,0,0),(1,1,0),(2,0,0)),
        edges=((0,1),(1,2))
    )
    
    set_keyframe_vertices("mesh", 0, 1)
    set_keyframe_vertices("mesh", 1, 1)
    set_keyframe_vertices("mesh", 2, 1)
    
    
    
    mesh.set_vertices((0,1,2), ((0,0,0), (1,0,0), (2,0,0)))
    
    set_keyframe_vertices("mesh", 0, 10)
    set_keyframe_vertices("mesh", 1, 10)
    set_keyframe_vertices("mesh", 2, 10)

# vertices = ((0,1,0),(1,0,0),(0,0,1),(-1,0,0))
# edges = ([0,1],[1,2],[0,2],[0,3],[2,3])
# faces = ([0,1,2],[2,0,3])

# name = "New Object"
# mesh = bpy.data.meshes.new(name)
# obj = bpy.data.objects.new(name, mesh)
# col = bpy.data.collections.get("Collection")
# col.objects.link(obj)
# bpy.context.view_layer.objects.active = obj
# mesh.from_pydata(vertices,edges,faces)
