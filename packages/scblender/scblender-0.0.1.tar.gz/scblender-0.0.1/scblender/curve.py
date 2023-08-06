import bpy
from .particle import Particle


class Path_curve(Particle):
    def __init__(self, name="path_curve", position=(0, 0, 0)) -> None:
        super().__init__(name=name, position=position)
        bpy.ops.curve.primitive_nurbs_path_add(
            radius=1,
            enter_editmode=False,
            align="WORLD",
            location=self._position,
            scale=self._scale,
        )
        bpy.context.object.name = self._name
        return None


class Bezier_curve(Particle):
    def __init__(
        self,
        name="bezier",
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=(1, 1, 1),
    ) -> None:
        super().__init__(name=name, position=position, scale=scale)
        bpy.ops.curve.primitive_bezier_curve_add(
            radius=1,
            enter_editmode=False,
            align="WORLD",
            location=self._position,
            scale=self._scale,
        )
        bpy.context.object.name = self._name
        return None

