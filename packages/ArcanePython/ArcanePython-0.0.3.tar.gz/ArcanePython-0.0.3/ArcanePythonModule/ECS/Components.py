from ArcanePythonModule.Maths import Vector3

class TransformComponent:
    def __init__(self, pos: Vector3, scale: Vector3) -> None:
        self.__position = pos 
        self.__scale = scale
