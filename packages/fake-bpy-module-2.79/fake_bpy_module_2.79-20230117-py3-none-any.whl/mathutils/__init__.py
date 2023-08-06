import sys
import typing
from . import kdtree
from . import geometry
from . import noise
from . import bvhtree
from . import interpolate

GenericType = typing.TypeVar("GenericType")


class Color:
    ''' This object gives access to Colors in Blender. :param rgb: (r, g, b) color values :type rgb: 3d vector
    '''

    b: float = None
    ''' Blue color channel.

    :type: float
    '''

    g: float = None
    ''' Green color channel.

    :type: float
    '''

    h: float = None
    ''' HSV Hue component in [0, 1].

    :type: float
    '''

    hsv: typing.Union[typing.Sequence[float], 'Vector'] = None
    ''' HSV Values in [0, 1].

    :type: typing.Union[typing.Sequence[float], 'Vector']
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    r: float = None
    ''' Red color channel.

    :type: float
    '''

    s: float = None
    ''' HSV Saturation component in [0, 1].

    :type: float
    '''

    v: float = None
    ''' HSV Value component in [0, 1].

    :type: float
    '''

    @staticmethod
    def copy() -> 'Color':
        ''' Returns a copy of this color.

        :rtype: 'Color'
        :return: A copy of the color.
        '''
        pass

    @staticmethod
    def freeze():
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        '''
        pass

    def __init__(self, rgb=(0.0, 0.0, 0.0)) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Color']
                ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Color']
                ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __truediv__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __radd__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __rsub__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __rtruediv__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __iadd__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __isub__(self, other: typing.Union[typing.Sequence[float], 'Color']
                 ) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Color']
        :rtype: 'Color'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass

    def __itruediv__(self, other: typing.Union[int, float]) -> 'Color':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Color'
        '''
        pass


class Euler:
    ''' This object gives access to Eulers in Blender. :param angles: Three angles, in radians. :type angles: 3d vector :param order: Optional order of the angles, a permutation of ``XYZ``. :type order: str
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    order: str = None
    ''' Euler rotation order.

    :type: str
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    x: float = None
    ''' Euler axis angle in radians.

    :type: float
    '''

    y: float = None
    ''' Euler axis angle in radians.

    :type: float
    '''

    z: float = None
    ''' Euler axis angle in radians.

    :type: float
    '''

    @staticmethod
    def copy() -> 'Euler':
        ''' Returns a copy of this euler.

        :rtype: 'Euler'
        :return: A copy of the euler.
        '''
        pass

    @staticmethod
    def freeze():
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        '''
        pass

    def make_compatible(self, other):
        ''' Make this euler compatible with another, so interpolating between them works as intended.

        '''
        pass

    def rotate(self,
               other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotates the euler by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    def rotate_axis(self, axis: str, angle: float):
        ''' Rotates the euler a certain amount and returning a unique euler rotation (no 720 degree pitches).

        :param axis: single character in ['X, 'Y', 'Z'].
        :type axis: str
        :param angle: angle in radians.
        :type angle: float
        '''
        pass

    def to_matrix(self) -> 'Matrix':
        ''' Return a matrix representation of the euler.

        :rtype: 'Matrix'
        :return: A 3x3 roation matrix representation of the euler.
        '''
        pass

    def to_quaternion(self) -> 'Quaternion':
        ''' Return a quaternion representation of the euler.

        :rtype: 'Quaternion'
        :return: Quaternion representation of the euler.
        '''
        pass

    def zero(self):
        ''' Set all values to zero.

        '''
        pass

    def __init__(self, angles=(0.0, 0.0, 0.0), order='XYZ') -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass


class Matrix:
    ''' This object gives access to Matrices in Blender, supporting square and rectangular matrices from 2x2 up to 4x4. :param rows: Sequence of rows. When ommitted, a 4x4 identity matrix is constructed. :type rows: 2d number sequence
    '''

    col: 'Matrix' = None
    ''' Access the matix by colums, 3x3 and 4x4 only, (read-only).

    :type: 'Matrix'
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_negative: bool = None
    ''' True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).

    :type: bool
    '''

    is_orthogonal: bool = None
    ''' True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).

    :type: bool
    '''

    is_orthogonal_axis_vectors: bool = None
    ''' True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only).

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    median_scale: float = None
    ''' The average scale applied to each axis (read-only).

    :type: float
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    row: 'Matrix' = None
    ''' Access the matix by rows (default), (read-only).

    :type: 'Matrix'
    '''

    translation: 'Vector' = None
    ''' The translation component of the matrix.

    :type: 'Vector'
    '''

    @classmethod
    def Identity(cls, size: int) -> 'Matrix':
        ''' Create an identity matrix.

        :param size: The size of the identity matrix to construct [2, 4].
        :type size: int
        :rtype: 'Matrix'
        :return: A new identity matrix.
        '''
        pass

    @classmethod
    def OrthoProjection(
            cls, axis: typing.Union[str, typing.Sequence[float], 'Vector'],
            size: int) -> 'Matrix':
        ''' Create a matrix to represent an orthographic projection.

        :param axis: ['X', 'Y', 'XY', 'XZ', 'YZ'], where a single axis is for a 2D matrix. Or a vector for an arbitrary axis
        :type axis: typing.Union[str, typing.Sequence[float], 'Vector']
        :param size: The size of the projection matrix to construct [2, 4].
        :type size: int
        :rtype: 'Matrix'
        :return: A new projection matrix.
        '''
        pass

    @classmethod
    def Rotation(cls, angle: float, size: int,
                 axis: typing.Union[str, typing.Sequence[float], 'Vector']
                 ) -> 'Matrix':
        ''' Create a matrix representing a rotation.

        :param angle: The angle of rotation desired, in radians.
        :type angle: float
        :param size: The size of the rotation matrix to construct [2, 4].
        :type size: int
        :param axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object (optional when size is 2).
        :type axis: typing.Union[str, typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: A new rotation matrix.
        '''
        pass

    @classmethod
    def Scale(
            cls, factor: float, size: int,
            axis: typing.Union[typing.Sequence[float], 'Vector']) -> 'Matrix':
        ''' Create a matrix representing a scaling.

        :param factor: The factor of scaling to apply.
        :type factor: float
        :param size: The size of the scale matrix to construct [2, 4].
        :type size: int
        :param axis: Direction to influence scale. (optional).
        :type axis: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: A new scale matrix.
        '''
        pass

    @classmethod
    def Shear(cls, plane: str, size: int, factor: float) -> 'Matrix':
        ''' Create a matrix to represent an shear transformation.

        :param plane: ['X', 'Y', 'XY', 'XZ', 'YZ'], where a single axis is for a 2D matrix only.
        :type plane: str
        :param size: The size of the shear matrix to construct [2, 4].
        :type size: int
        :param factor: The factor of shear to apply. For a 3 or 4 *size* matrix pass a pair of floats corresponding with the *plane* axis.
        :type factor: float
        :rtype: 'Matrix'
        :return: A new shear matrix.
        '''
        pass

    @classmethod
    def Translation(cls, vector: typing.Union[typing.Sequence[float], 'Vector']
                    ) -> 'Matrix':
        ''' Create a matrix representing a translation.

        :param vector: The translation vector.
        :type vector: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: An identity matrix with a translation.
        '''
        pass

    def adjugate(self):
        ''' Set the matrix to its adjugate.

        '''
        pass

    def adjugated(self) -> 'Matrix':
        ''' Return an adjugated copy of the matrix.

        :rtype: 'Matrix'
        :return: the adjugated matrix.
        '''
        pass

    def copy(self) -> 'Matrix':
        ''' Returns a copy of this matrix.

        :rtype: 'Matrix'
        :return: an instance of itself
        '''
        pass

    def decompose(self) -> 'Quaternion':
        ''' Return the translation, rotation and scale components of this matrix.

        :rtype: 'Quaternion'
        :return: trans, rot, scale triple.
        '''
        pass

    def determinant(self) -> float:
        ''' Return the determinant of a matrix.

        :rtype: float
        :return: Return the determinant of a matrix.
        '''
        pass

    @staticmethod
    def freeze():
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        '''
        pass

    def identity(self):
        ''' Set the matrix to the identity matrix.

        '''
        pass

    def invert(
            self,
            fallback: typing.Union[typing.Sequence[float], 'Matrix'] = None):
        ''' Set the matrix to its inverse.

        :param fallback: Set the matrix to this value when the inverse cannot be calculated (instead of raising a :exc:`ValueError` exception).
        :type fallback: typing.Union[typing.Sequence[float], 'Matrix']
        '''
        pass

    def invert_safe(self):
        ''' Set the matrix to its inverse, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, set to the identity matrix instead.

        '''
        pass

    def inverted(self, fallback: typing.Any = None) -> 'Matrix':
        ''' Return an inverted copy of the matrix.

        :param fallback: return this when the inverse can't be calculated (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: 'Matrix'
        :return: the inverted matrix or fallback when given.
        '''
        pass

    def inverted_safe(self) -> 'Matrix':
        ''' Return an inverted copy of the matrix, will never error. If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one. If tweaked matrix is still degenerated, return the identity matrix instead.

        :rtype: 'Matrix'
        :return: the inverted matrix.
        '''
        pass

    @staticmethod
    def lerp(other: typing.Union[typing.Sequence[float], 'Matrix'],
             factor: float) -> 'Matrix':
        ''' Returns the interpolation of two matrices.

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :rtype: 'Matrix'
        :return: The interpolated matrix.
        '''
        pass

    def normalize(self):
        ''' Normalize each of the matrix columns.

        '''
        pass

    def normalized(self) -> 'Matrix':
        ''' Return a column normalized matrix

        :rtype: 'Matrix'
        :return: a column normalized matrix
        '''
        pass

    def resize_4x4(self):
        ''' Resize the matrix to 4x4.

        '''
        pass

    def rotate(self,
               other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotates the matrix by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    def to_3x3(self) -> 'Matrix':
        ''' Return a 3x3 copy of this matrix.

        :rtype: 'Matrix'
        :return: a new matrix.
        '''
        pass

    def to_4x4(self) -> 'Matrix':
        ''' Return a 4x4 copy of this matrix.

        :rtype: 'Matrix'
        :return: a new matrix.
        '''
        pass

    def to_euler(self, order: str,
                 euler_compat: typing.Union[typing.Sequence[float], 'Euler']
                 ) -> 'Euler':
        ''' Return an Euler representation of the rotation matrix (3x3 or 4x4 matrix only).

        :param order: Optional rotation order argument in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
        :type order: str
        :param euler_compat: Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves.
        :type euler_compat: typing.Union[typing.Sequence[float], 'Euler']
        :rtype: 'Euler'
        :return: Euler representation of the matrix.
        '''
        pass

    def to_quaternion(self) -> 'Quaternion':
        ''' Return a quaternion representation of the rotation matrix.

        :rtype: 'Quaternion'
        :return: Quaternion representation of the rotation matrix.
        '''
        pass

    def to_scale(self) -> 'Vector':
        ''' Return the scale part of a 3x3 or 4x4 matrix.

        :rtype: 'Vector'
        :return: Return the scale of a matrix.
        '''
        pass

    def to_translation(self) -> 'Vector':
        ''' Return the translation part of a 4 row matrix.

        :rtype: 'Vector'
        :return: Return the translation of a matrix.
        '''
        pass

    def transpose(self):
        ''' Set the matrix to its transpose.

        '''
        pass

    def transposed(self) -> 'Matrix':
        ''' Return a new, transposed matrix.

        :rtype: 'Matrix'
        :return: a transposed matrix
        '''
        pass

    def zero(self):
        ''' Set all the matrix values to zero.

        '''
        pass

    def __init__(self,
                 rows=((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0),
                       (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0,
                                              1.0))) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __len__(self) -> int:
        ''' 

        :rtype: int
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float]) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Matrix'
        '''
        pass

    def __matmul__(
            self, other: typing.Union[typing.Sequence[float], 'Matrix', typing.
                                      Sequence[float], 'Vector']
    ) -> typing.Union['Matrix', 'Vector']:
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix', typing.Sequence[float], 'Vector']
        :rtype: typing.Union['Matrix', 'Vector']
        '''
        pass

    def __radd__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                 ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __rsub__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                 ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float]) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Matrix'
        '''
        pass

    def __rmatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float]) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Matrix'
        '''
        pass

    def __imatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Matrix':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Matrix'
        '''
        pass


class Quaternion:
    ''' This object gives access to Quaternions in Blender. :param seq: size 3 or 4 :type seq: `Vector` :param angle: rotation angle, in radians :type angle: float The constructor takes arguments in various forms: (), *no args* Create an identity quaternion (*wxyz*) Create a quaternion from a ``(w, x, y, z)`` vector. (*exponential_map*) Create a quaternion from a 3d exponential map vector. .. seealso:: :meth:`to_exponential_map` (*axis, angle*) Create a quaternion representing a rotation of *angle* radians over *axis*. .. seealso:: :meth:`to_axis_angle`
    '''

    angle: float = None
    ''' Angle of the quaternion.

    :type: float
    '''

    axis: typing.Union[typing.Sequence[float], 'Vector'] = None
    ''' Quaternion axis as a vector.

    :type: typing.Union[typing.Sequence[float], 'Vector']
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    magnitude: float = None
    ''' Size of the quaternion (read-only).

    :type: float
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    w: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    x: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    y: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    z: float = None
    ''' Quaternion axis value.

    :type: float
    '''

    @staticmethod
    def conjugate():
        ''' Set the quaternion to its conjugate (negate x, y, z).

        '''
        pass

    @staticmethod
    def conjugated() -> 'Quaternion':
        ''' Return a new conjugated quaternion.

        :rtype: 'Quaternion'
        :return: a new quaternion.
        '''
        pass

    @staticmethod
    def copy() -> 'Quaternion':
        ''' Returns a copy of this quaternion.

        :rtype: 'Quaternion'
        :return: A copy of the quaternion.
        '''
        pass

    def cross(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
              ) -> 'Quaternion':
        ''' Return the cross product of this quaternion and another.

        :param other: The other quaternion to perform the cross product with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        :return: The cross product.
        '''
        pass

    def dot(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
            ) -> 'Quaternion':
        ''' Return the dot product of this quaternion and another.

        :param other: The other quaternion to perform the dot product with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        :return: The dot product.
        '''
        pass

    @staticmethod
    def freeze():
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        '''
        pass

    @staticmethod
    def identity():
        ''' Set the quaternion to an identity quaternion.

        '''
        pass

    @staticmethod
    def invert():
        ''' Set the quaternion to its inverse.

        '''
        pass

    @staticmethod
    def inverted() -> 'Quaternion':
        ''' Return a new, inverted quaternion.

        :rtype: 'Quaternion'
        :return: the inverted value.
        '''
        pass

    @staticmethod
    def negate():
        ''' Set the quaternion to its negative.

        '''
        pass

    @staticmethod
    def normalize():
        ''' Normalize the quaternion.

        '''
        pass

    @staticmethod
    def normalized() -> 'Quaternion':
        ''' Return a new normalized quaternion.

        :rtype: 'Quaternion'
        :return: a normalized copy.
        '''
        pass

    def rotate(self,
               other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotates the quaternion by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    @staticmethod
    def rotation_difference(
            other: typing.Union[typing.Sequence[float], 'Quaternion']
    ) -> 'Quaternion':
        ''' Returns a quaternion representing the rotational difference.

        :param other: second quaternion.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        :return: the rotational difference between the two quat rotations.
        '''
        pass

    @staticmethod
    def slerp(other: typing.Union[typing.Sequence[float], 'Quaternion'],
              factor: float) -> 'Quaternion':
        ''' Returns the interpolation of two quaternions.

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :rtype: 'Quaternion'
        :return: The interpolated rotation.
        '''
        pass

    def to_axis_angle(self) -> typing.Tuple['mathutils.Vector', float]:
        ''' Return the axis, angle representation of the quaternion.

        :rtype: typing.Tuple['mathutils.Vector', float]
        :return: axis, angle.
        '''
        pass

    def to_euler(self, order: str,
                 euler_compat: typing.Union[typing.Sequence[float], 'Euler']
                 ) -> 'Euler':
        ''' Return Euler representation of the quaternion.

        :param order: Optional rotation order argument in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
        :type order: str
        :param euler_compat: Optional euler argument the new euler will be made compatible with (no axis flipping between them). Useful for converting a series of matrices to animation curves.
        :type euler_compat: typing.Union[typing.Sequence[float], 'Euler']
        :rtype: 'Euler'
        :return: Euler representation of the quaternion.
        '''
        pass

    def to_exponential_map(self) -> 'Vector':
        ''' Return the exponential map representation of the quaternion. This representation consist of the rotation axis multiplied by the rotation angle. Such a representation is useful for interpolation between multiple orientations. To convert back to a quaternion, pass it to the `Quaternion` constructor.

        :rtype: 'Vector'
        :return: exponential map.
        '''
        pass

    def to_matrix(self) -> 'Matrix':
        ''' Return a matrix representation of the quaternion.

        :rtype: 'Matrix'
        :return: A 3x3 rotation matrix representation of the quaternion.
        '''
        pass

    def __init__(self, seq=(1.0, 0.0, 0.0, 0.0)) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __len__(self) -> int:
        ''' 

        :rtype: int
        '''
        pass

    def __getitem__(self, key: int) -> float:
        ''' 

        :param key: 
        :type key: int
        :rtype: float
        '''
        pass

    def __setitem__(self, key: int, value: float) -> float:
        ''' 

        :param key: 
        :type key: int
        :param value: 
        :type value: float
        :rtype: float
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
                ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Quaternion']
                ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float, typing.
                                          Sequence[float], 'Quaternion']
                ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[int, float, typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __matmul__(
            self, other: typing.Union[typing.Sequence[float], 'Vector', typing.
                                      Sequence[float], 'Quaternion']
    ) -> typing.Union['Vector', 'Quaternion']:
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector', typing.Sequence[float], 'Quaternion']
        :rtype: typing.Union['Vector', 'Quaternion']
        '''
        pass

    def __radd__(self,
                 other: typing.Union[typing.Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __rsub__(self,
                 other: typing.Union[typing.Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float, typing.
                                           Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[int, float, typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __rmatmul__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float, typing.
                                           Sequence[float], 'Quaternion']
                 ) -> 'Quaternion':
        ''' 

        :param other: 
        :type other: typing.Union[int, float, typing.Sequence[float], 'Quaternion']
        :rtype: 'Quaternion'
        '''
        pass

    def __imatmul__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass


class Vector:
    ''' This object gives access to Vectors in Blender. :param seq: Components of the vector, must be a sequence of at least two :type seq: sequence of numbers
    '''

    is_frozen: bool = None
    ''' True when this object has been frozen (read-only).

    :type: bool
    '''

    is_wrapped: bool = None
    ''' True when this object wraps external data (read-only).

    :type: bool
    '''

    length: float = None
    ''' Vector Length.

    :type: float
    '''

    length_squared: float = None
    ''' Vector length squared (v.dot(v)).

    :type: float
    '''

    magnitude: float = None
    ''' Vector Length.

    :type: float
    '''

    owner = None
    ''' The item this is wrapping or None (read-only).'''

    w: float = None
    ''' Vector W axis (4D Vectors only).

    :type: float
    '''

    ww = None
    ''' Undocumented'''

    www = None
    ''' Undocumented'''

    wwww = None
    ''' Undocumented'''

    wwwx = None
    ''' Undocumented'''

    wwwy = None
    ''' Undocumented'''

    wwwz = None
    ''' Undocumented'''

    wwx = None
    ''' Undocumented'''

    wwxw = None
    ''' Undocumented'''

    wwxx = None
    ''' Undocumented'''

    wwxy = None
    ''' Undocumented'''

    wwxz = None
    ''' Undocumented'''

    wwy = None
    ''' Undocumented'''

    wwyw = None
    ''' Undocumented'''

    wwyx = None
    ''' Undocumented'''

    wwyy = None
    ''' Undocumented'''

    wwyz = None
    ''' Undocumented'''

    wwz = None
    ''' Undocumented'''

    wwzw = None
    ''' Undocumented'''

    wwzx = None
    ''' Undocumented'''

    wwzy = None
    ''' Undocumented'''

    wwzz = None
    ''' Undocumented'''

    wx = None
    ''' Undocumented'''

    wxw = None
    ''' Undocumented'''

    wxww = None
    ''' Undocumented'''

    wxwx = None
    ''' Undocumented'''

    wxwy = None
    ''' Undocumented'''

    wxwz = None
    ''' Undocumented'''

    wxx = None
    ''' Undocumented'''

    wxxw = None
    ''' Undocumented'''

    wxxx = None
    ''' Undocumented'''

    wxxy = None
    ''' Undocumented'''

    wxxz = None
    ''' Undocumented'''

    wxy = None
    ''' Undocumented'''

    wxyw = None
    ''' Undocumented'''

    wxyx = None
    ''' Undocumented'''

    wxyy = None
    ''' Undocumented'''

    wxyz = None
    ''' Undocumented'''

    wxz = None
    ''' Undocumented'''

    wxzw = None
    ''' Undocumented'''

    wxzx = None
    ''' Undocumented'''

    wxzy = None
    ''' Undocumented'''

    wxzz = None
    ''' Undocumented'''

    wy = None
    ''' Undocumented'''

    wyw = None
    ''' Undocumented'''

    wyww = None
    ''' Undocumented'''

    wywx = None
    ''' Undocumented'''

    wywy = None
    ''' Undocumented'''

    wywz = None
    ''' Undocumented'''

    wyx = None
    ''' Undocumented'''

    wyxw = None
    ''' Undocumented'''

    wyxx = None
    ''' Undocumented'''

    wyxy = None
    ''' Undocumented'''

    wyxz = None
    ''' Undocumented'''

    wyy = None
    ''' Undocumented'''

    wyyw = None
    ''' Undocumented'''

    wyyx = None
    ''' Undocumented'''

    wyyy = None
    ''' Undocumented'''

    wyyz = None
    ''' Undocumented'''

    wyz = None
    ''' Undocumented'''

    wyzw = None
    ''' Undocumented'''

    wyzx = None
    ''' Undocumented'''

    wyzy = None
    ''' Undocumented'''

    wyzz = None
    ''' Undocumented'''

    wz = None
    ''' Undocumented'''

    wzw = None
    ''' Undocumented'''

    wzww = None
    ''' Undocumented'''

    wzwx = None
    ''' Undocumented'''

    wzwy = None
    ''' Undocumented'''

    wzwz = None
    ''' Undocumented'''

    wzx = None
    ''' Undocumented'''

    wzxw = None
    ''' Undocumented'''

    wzxx = None
    ''' Undocumented'''

    wzxy = None
    ''' Undocumented'''

    wzxz = None
    ''' Undocumented'''

    wzy = None
    ''' Undocumented'''

    wzyw = None
    ''' Undocumented'''

    wzyx = None
    ''' Undocumented'''

    wzyy = None
    ''' Undocumented'''

    wzyz = None
    ''' Undocumented'''

    wzz = None
    ''' Undocumented'''

    wzzw = None
    ''' Undocumented'''

    wzzx = None
    ''' Undocumented'''

    wzzy = None
    ''' Undocumented'''

    wzzz = None
    ''' Undocumented'''

    x: float = None
    ''' Vector X axis.

    :type: float
    '''

    xw = None
    ''' Undocumented'''

    xww = None
    ''' Undocumented'''

    xwww = None
    ''' Undocumented'''

    xwwx = None
    ''' Undocumented'''

    xwwy = None
    ''' Undocumented'''

    xwwz = None
    ''' Undocumented'''

    xwx = None
    ''' Undocumented'''

    xwxw = None
    ''' Undocumented'''

    xwxx = None
    ''' Undocumented'''

    xwxy = None
    ''' Undocumented'''

    xwxz = None
    ''' Undocumented'''

    xwy = None
    ''' Undocumented'''

    xwyw = None
    ''' Undocumented'''

    xwyx = None
    ''' Undocumented'''

    xwyy = None
    ''' Undocumented'''

    xwyz = None
    ''' Undocumented'''

    xwz = None
    ''' Undocumented'''

    xwzw = None
    ''' Undocumented'''

    xwzx = None
    ''' Undocumented'''

    xwzy = None
    ''' Undocumented'''

    xwzz = None
    ''' Undocumented'''

    xx = None
    ''' Undocumented'''

    xxw = None
    ''' Undocumented'''

    xxww = None
    ''' Undocumented'''

    xxwx = None
    ''' Undocumented'''

    xxwy = None
    ''' Undocumented'''

    xxwz = None
    ''' Undocumented'''

    xxx = None
    ''' Undocumented'''

    xxxw = None
    ''' Undocumented'''

    xxxx = None
    ''' Undocumented'''

    xxxy = None
    ''' Undocumented'''

    xxxz = None
    ''' Undocumented'''

    xxy = None
    ''' Undocumented'''

    xxyw = None
    ''' Undocumented'''

    xxyx = None
    ''' Undocumented'''

    xxyy = None
    ''' Undocumented'''

    xxyz = None
    ''' Undocumented'''

    xxz = None
    ''' Undocumented'''

    xxzw = None
    ''' Undocumented'''

    xxzx = None
    ''' Undocumented'''

    xxzy = None
    ''' Undocumented'''

    xxzz = None
    ''' Undocumented'''

    xy = None
    ''' Undocumented'''

    xyw = None
    ''' Undocumented'''

    xyww = None
    ''' Undocumented'''

    xywx = None
    ''' Undocumented'''

    xywy = None
    ''' Undocumented'''

    xywz = None
    ''' Undocumented'''

    xyx = None
    ''' Undocumented'''

    xyxw = None
    ''' Undocumented'''

    xyxx = None
    ''' Undocumented'''

    xyxy = None
    ''' Undocumented'''

    xyxz = None
    ''' Undocumented'''

    xyy = None
    ''' Undocumented'''

    xyyw = None
    ''' Undocumented'''

    xyyx = None
    ''' Undocumented'''

    xyyy = None
    ''' Undocumented'''

    xyyz = None
    ''' Undocumented'''

    xyz = None
    ''' Undocumented'''

    xyzw = None
    ''' Undocumented'''

    xyzx = None
    ''' Undocumented'''

    xyzy = None
    ''' Undocumented'''

    xyzz = None
    ''' Undocumented'''

    xz = None
    ''' Undocumented'''

    xzw = None
    ''' Undocumented'''

    xzww = None
    ''' Undocumented'''

    xzwx = None
    ''' Undocumented'''

    xzwy = None
    ''' Undocumented'''

    xzwz = None
    ''' Undocumented'''

    xzx = None
    ''' Undocumented'''

    xzxw = None
    ''' Undocumented'''

    xzxx = None
    ''' Undocumented'''

    xzxy = None
    ''' Undocumented'''

    xzxz = None
    ''' Undocumented'''

    xzy = None
    ''' Undocumented'''

    xzyw = None
    ''' Undocumented'''

    xzyx = None
    ''' Undocumented'''

    xzyy = None
    ''' Undocumented'''

    xzyz = None
    ''' Undocumented'''

    xzz = None
    ''' Undocumented'''

    xzzw = None
    ''' Undocumented'''

    xzzx = None
    ''' Undocumented'''

    xzzy = None
    ''' Undocumented'''

    xzzz = None
    ''' Undocumented'''

    y: float = None
    ''' Vector Y axis.

    :type: float
    '''

    yw = None
    ''' Undocumented'''

    yww = None
    ''' Undocumented'''

    ywww = None
    ''' Undocumented'''

    ywwx = None
    ''' Undocumented'''

    ywwy = None
    ''' Undocumented'''

    ywwz = None
    ''' Undocumented'''

    ywx = None
    ''' Undocumented'''

    ywxw = None
    ''' Undocumented'''

    ywxx = None
    ''' Undocumented'''

    ywxy = None
    ''' Undocumented'''

    ywxz = None
    ''' Undocumented'''

    ywy = None
    ''' Undocumented'''

    ywyw = None
    ''' Undocumented'''

    ywyx = None
    ''' Undocumented'''

    ywyy = None
    ''' Undocumented'''

    ywyz = None
    ''' Undocumented'''

    ywz = None
    ''' Undocumented'''

    ywzw = None
    ''' Undocumented'''

    ywzx = None
    ''' Undocumented'''

    ywzy = None
    ''' Undocumented'''

    ywzz = None
    ''' Undocumented'''

    yx = None
    ''' Undocumented'''

    yxw = None
    ''' Undocumented'''

    yxww = None
    ''' Undocumented'''

    yxwx = None
    ''' Undocumented'''

    yxwy = None
    ''' Undocumented'''

    yxwz = None
    ''' Undocumented'''

    yxx = None
    ''' Undocumented'''

    yxxw = None
    ''' Undocumented'''

    yxxx = None
    ''' Undocumented'''

    yxxy = None
    ''' Undocumented'''

    yxxz = None
    ''' Undocumented'''

    yxy = None
    ''' Undocumented'''

    yxyw = None
    ''' Undocumented'''

    yxyx = None
    ''' Undocumented'''

    yxyy = None
    ''' Undocumented'''

    yxyz = None
    ''' Undocumented'''

    yxz = None
    ''' Undocumented'''

    yxzw = None
    ''' Undocumented'''

    yxzx = None
    ''' Undocumented'''

    yxzy = None
    ''' Undocumented'''

    yxzz = None
    ''' Undocumented'''

    yy = None
    ''' Undocumented'''

    yyw = None
    ''' Undocumented'''

    yyww = None
    ''' Undocumented'''

    yywx = None
    ''' Undocumented'''

    yywy = None
    ''' Undocumented'''

    yywz = None
    ''' Undocumented'''

    yyx = None
    ''' Undocumented'''

    yyxw = None
    ''' Undocumented'''

    yyxx = None
    ''' Undocumented'''

    yyxy = None
    ''' Undocumented'''

    yyxz = None
    ''' Undocumented'''

    yyy = None
    ''' Undocumented'''

    yyyw = None
    ''' Undocumented'''

    yyyx = None
    ''' Undocumented'''

    yyyy = None
    ''' Undocumented'''

    yyyz = None
    ''' Undocumented'''

    yyz = None
    ''' Undocumented'''

    yyzw = None
    ''' Undocumented'''

    yyzx = None
    ''' Undocumented'''

    yyzy = None
    ''' Undocumented'''

    yyzz = None
    ''' Undocumented'''

    yz = None
    ''' Undocumented'''

    yzw = None
    ''' Undocumented'''

    yzww = None
    ''' Undocumented'''

    yzwx = None
    ''' Undocumented'''

    yzwy = None
    ''' Undocumented'''

    yzwz = None
    ''' Undocumented'''

    yzx = None
    ''' Undocumented'''

    yzxw = None
    ''' Undocumented'''

    yzxx = None
    ''' Undocumented'''

    yzxy = None
    ''' Undocumented'''

    yzxz = None
    ''' Undocumented'''

    yzy = None
    ''' Undocumented'''

    yzyw = None
    ''' Undocumented'''

    yzyx = None
    ''' Undocumented'''

    yzyy = None
    ''' Undocumented'''

    yzyz = None
    ''' Undocumented'''

    yzz = None
    ''' Undocumented'''

    yzzw = None
    ''' Undocumented'''

    yzzx = None
    ''' Undocumented'''

    yzzy = None
    ''' Undocumented'''

    yzzz = None
    ''' Undocumented'''

    z: float = None
    ''' Vector Z axis (3D Vectors only).

    :type: float
    '''

    zw = None
    ''' Undocumented'''

    zww = None
    ''' Undocumented'''

    zwww = None
    ''' Undocumented'''

    zwwx = None
    ''' Undocumented'''

    zwwy = None
    ''' Undocumented'''

    zwwz = None
    ''' Undocumented'''

    zwx = None
    ''' Undocumented'''

    zwxw = None
    ''' Undocumented'''

    zwxx = None
    ''' Undocumented'''

    zwxy = None
    ''' Undocumented'''

    zwxz = None
    ''' Undocumented'''

    zwy = None
    ''' Undocumented'''

    zwyw = None
    ''' Undocumented'''

    zwyx = None
    ''' Undocumented'''

    zwyy = None
    ''' Undocumented'''

    zwyz = None
    ''' Undocumented'''

    zwz = None
    ''' Undocumented'''

    zwzw = None
    ''' Undocumented'''

    zwzx = None
    ''' Undocumented'''

    zwzy = None
    ''' Undocumented'''

    zwzz = None
    ''' Undocumented'''

    zx = None
    ''' Undocumented'''

    zxw = None
    ''' Undocumented'''

    zxww = None
    ''' Undocumented'''

    zxwx = None
    ''' Undocumented'''

    zxwy = None
    ''' Undocumented'''

    zxwz = None
    ''' Undocumented'''

    zxx = None
    ''' Undocumented'''

    zxxw = None
    ''' Undocumented'''

    zxxx = None
    ''' Undocumented'''

    zxxy = None
    ''' Undocumented'''

    zxxz = None
    ''' Undocumented'''

    zxy = None
    ''' Undocumented'''

    zxyw = None
    ''' Undocumented'''

    zxyx = None
    ''' Undocumented'''

    zxyy = None
    ''' Undocumented'''

    zxyz = None
    ''' Undocumented'''

    zxz = None
    ''' Undocumented'''

    zxzw = None
    ''' Undocumented'''

    zxzx = None
    ''' Undocumented'''

    zxzy = None
    ''' Undocumented'''

    zxzz = None
    ''' Undocumented'''

    zy = None
    ''' Undocumented'''

    zyw = None
    ''' Undocumented'''

    zyww = None
    ''' Undocumented'''

    zywx = None
    ''' Undocumented'''

    zywy = None
    ''' Undocumented'''

    zywz = None
    ''' Undocumented'''

    zyx = None
    ''' Undocumented'''

    zyxw = None
    ''' Undocumented'''

    zyxx = None
    ''' Undocumented'''

    zyxy = None
    ''' Undocumented'''

    zyxz = None
    ''' Undocumented'''

    zyy = None
    ''' Undocumented'''

    zyyw = None
    ''' Undocumented'''

    zyyx = None
    ''' Undocumented'''

    zyyy = None
    ''' Undocumented'''

    zyyz = None
    ''' Undocumented'''

    zyz = None
    ''' Undocumented'''

    zyzw = None
    ''' Undocumented'''

    zyzx = None
    ''' Undocumented'''

    zyzy = None
    ''' Undocumented'''

    zyzz = None
    ''' Undocumented'''

    zz = None
    ''' Undocumented'''

    zzw = None
    ''' Undocumented'''

    zzww = None
    ''' Undocumented'''

    zzwx = None
    ''' Undocumented'''

    zzwy = None
    ''' Undocumented'''

    zzwz = None
    ''' Undocumented'''

    zzx = None
    ''' Undocumented'''

    zzxw = None
    ''' Undocumented'''

    zzxx = None
    ''' Undocumented'''

    zzxy = None
    ''' Undocumented'''

    zzxz = None
    ''' Undocumented'''

    zzy = None
    ''' Undocumented'''

    zzyw = None
    ''' Undocumented'''

    zzyx = None
    ''' Undocumented'''

    zzyy = None
    ''' Undocumented'''

    zzyz = None
    ''' Undocumented'''

    zzz = None
    ''' Undocumented'''

    zzzw = None
    ''' Undocumented'''

    zzzx = None
    ''' Undocumented'''

    zzzy = None
    ''' Undocumented'''

    zzzz = None
    ''' Undocumented'''

    @classmethod
    def Fill(cls, size: int, fill: float = 0.0):
        ''' Create a vector of length size with all values set to fill.

        :param size: The length of the vector to be created.
        :type size: int
        :param fill: The value used to fill the vector.
        :type fill: float
        '''
        pass

    @classmethod
    def Linspace(cls, start: int, stop: int, size: int):
        ''' Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param size: The size of the vector to be created.
        :type size: int
        '''
        pass

    @classmethod
    def Range(cls, start: int = 0, stop: int = -1, step: int = 1):
        ''' Create a filled with a range of values.

        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param step: The step between successive values in the vector.
        :type step: int
        '''
        pass

    @classmethod
    def Repeat(cls, vector, size: int):
        ''' Create a vector by repeating the values in vector until the required size is reached.

        :param tuple: The vector to draw values from.
        :type tuple: typing.Union[typing.Sequence[float], 'Vector']
        :param size: The size of the vector to be created.
        :type size: int
        '''
        pass

    @staticmethod
    def angle(other: typing.Union[typing.Sequence[float], 'Vector'],
              fallback: typing.Any = None) -> float:
        ''' Return the angle between two vectors.

        :param other: another vector to compare the angle with
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param fallback: return this when the angle can't be calculated (zero length vector), (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: float
        :return: angle in radians or fallback when given
        '''
        pass

    @staticmethod
    def angle_signed(other: typing.Union[typing.Sequence[float], 'Vector'],
                     fallback: typing.Any) -> float:
        ''' Return the signed angle between two 2D vectors (clockwise is positive).

        :param other: another vector to compare the angle with
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param fallback: return this when the angle can't be calculated (zero length vector), (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: float
        :return: angle in radians or fallback when given
        '''
        pass

    @staticmethod
    def copy() -> 'Vector':
        ''' Returns a copy of this vector.

        :rtype: 'Vector'
        :return: A copy of the vector.
        '''
        pass

    def cross(self, other: typing.Union[typing.Sequence[float], 'Vector']
              ) -> 'Vector':
        ''' Return the cross product of this vector and another.

        :param other: The other vector to perform the cross product with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: The cross product.
        '''
        pass

    def dot(self,
            other: typing.Union[typing.Sequence[float], 'Vector']) -> 'Vector':
        ''' Return the dot product of this vector and another.

        :param other: The other vector to perform the dot product with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: The dot product.
        '''
        pass

    @staticmethod
    def freeze():
        ''' Make this object immutable. After this the object can be hashed, used in dictionaries & sets.

        '''
        pass

    @staticmethod
    def lerp(other: typing.Union[typing.Sequence[float], 'Vector'],
             factor: float) -> 'Vector':
        ''' Returns the interpolation of two vectors.

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :rtype: 'Vector'
        :return: The interpolated vector.
        '''
        pass

    def negate(self):
        ''' Set all values to their negative.

        '''
        pass

    def normalize(self):
        ''' Normalize the vector, making the length of the vector always 1.0.

        '''
        pass

    def normalized(self) -> 'Vector':
        ''' Return a new, normalized vector.

        :rtype: 'Vector'
        :return: a normalized copy of the vector
        '''
        pass

    def orthogonal(self) -> 'Vector':
        ''' Return a perpendicular vector.

        :rtype: 'Vector'
        :return: a new vector 90 degrees from this vector.
        '''
        pass

    @staticmethod
    def project(
            other: typing.Union[typing.Sequence[float], 'Vector']) -> 'Vector':
        ''' Return the projection of this vector onto the *other*.

        :param other: second vector.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: the parallel projection vector
        '''
        pass

    def reflect(self, mirror: typing.Union[typing.Sequence[float], 'Vector']
                ) -> 'Vector':
        ''' Return the reflection vector from the *mirror* argument.

        :param mirror: This vector could be a normal from the reflecting surface.
        :type mirror: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        :return: The reflected vector matching the size of this vector.
        '''
        pass

    def resize(self, size=3):
        ''' Resize the vector to have size number of elements.

        '''
        pass

    def resize_2d(self):
        ''' Resize the vector to 2D (x, y).

        '''
        pass

    def resize_3d(self):
        ''' Resize the vector to 3D (x, y, z).

        '''
        pass

    def resize_4d(self):
        ''' Resize the vector to 4D (x, y, z, w).

        '''
        pass

    def resized(self, size=3) -> 'Vector':
        ''' Return a resized copy of the vector with size number of elements.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    @staticmethod
    def rotate(other: typing.Union[typing.Sequence[float], 'Euler', typing.
                                   Sequence[float], 'Quaternion', typing.
                                   Sequence[float], 'Matrix']):
        ''' Rotate the vector by a rotation value.

        :param other: rotation component of mathutils value
        :type other: typing.Union[typing.Sequence[float], 'Euler', typing.Sequence[float], 'Quaternion', typing.Sequence[float], 'Matrix']
        '''
        pass

    @staticmethod
    def rotation_difference(
            other: typing.Union[typing.Sequence[float], 'Vector']
    ) -> 'Quaternion':
        ''' Returns a quaternion representing the rotational difference between this vector and another.

        :param other: second vector.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Quaternion'
        :return: the rotational difference between the two vectors.
        '''
        pass

    @staticmethod
    def slerp(other: typing.Union[typing.Sequence[float], 'Vector'],
              factor: float,
              fallback: typing.Any = None) -> 'Vector':
        ''' Returns the interpolation of two non-zero vectors (spherical coordinates).

        :param other: value to interpolate with.
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :param factor: The interpolation value typically in [0.0, 1.0].
        :type factor: float
        :param fallback: return this when the vector can't be calculated (zero length vector or direct opposites), (instead of raising a :exc:`ValueError`).
        :type fallback: typing.Any
        :rtype: 'Vector'
        :return: The interpolated vector.
        '''
        pass

    def to_2d(self) -> 'Vector':
        ''' Return a 2d copy of the vector.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    def to_3d(self) -> 'Vector':
        ''' Return a 3d copy of the vector.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    def to_4d(self) -> 'Vector':
        ''' Return a 4d copy of the vector.

        :rtype: 'Vector'
        :return: a new vector
        '''
        pass

    def to_track_quat(self, track: str, up: str) -> 'Quaternion':
        ''' Return a quaternion rotation from the vector and the track and up axis.

        :param track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
        :type track: str
        :param up: Up axis in ['X', 'Y', 'Z'].
        :type up: str
        :rtype: 'Quaternion'
        :return: rotation from the vector and the track and up axis.
        '''
        pass

    def to_tuple(self, precision: int = -1) -> typing.Tuple:
        ''' Return this vector as a tuple with.

        :param precision: The number to round the value to in [-1, 21].
        :type precision: int
        :rtype: typing.Tuple
        :return: the values of the vector rounded by *precision*
        '''
        pass

    def zero(self):
        ''' Set all values to zero.

        '''
        pass

    def __init__(self, seq=(0.0, 0.0, 0.0)) -> typing.Any:
        ''' 

        :rtype: typing.Any
        '''
        pass

    def __len__(self) -> int:
        ''' 

        :rtype: int
        '''
        pass

    def __getitem__(self, key: int) -> float:
        ''' 

        :param key: 
        :type key: int
        :rtype: float
        '''
        pass

    def __setitem__(self, key: int, value: float) -> float:
        ''' 

        :param key: 
        :type key: int
        :param value: 
        :type value: float
        :rtype: float
        '''
        pass

    def __neg__(self) -> 'Vector':
        ''' 

        :rtype: 'Vector'
        '''
        pass

    def __add__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __sub__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __mul__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __truediv__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __matmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                   ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Vector'
        '''
        pass

    def __radd__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __rsub__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __rmul__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __rtruediv__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __rmatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Vector'
        '''
        pass

    def __iadd__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __isub__(self, other: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Vector'
        '''
        pass

    def __imul__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __itruediv__(self, other: typing.Union[int, float]) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[int, float]
        :rtype: 'Vector'
        '''
        pass

    def __imatmul__(self, other: typing.Union[typing.Sequence[float], 'Matrix']
                    ) -> 'Vector':
        ''' 

        :param other: 
        :type other: typing.Union[typing.Sequence[float], 'Matrix']
        :rtype: 'Vector'
        '''
        pass
