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
        :return: A 3x3 rotation matrix representation of the euler.
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
    ''' This object gives access to Matrices in Blender, supporting square and rectangular matrices from 2x2 up to 4x4. :param rows: Sequence of rows. When omitted, a 4x4 identity matrix is constructed. :type rows: 2d number sequence
    '''

    col: 'Matrix' = None
    ''' Access the matrix by columns, 3x3 and 4x4 only, (read-only).

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
    ''' Access the matrix by rows (default), (read-only).

    :type: 'Matrix'
    '''

    translation: 'Vector' = None
    ''' The translation component of the matrix.

    :type: 'Vector'
    '''

    @classmethod
    def Diagonal(cls, vector: typing.Union[typing.Sequence[float], 'Vector']
                 ) -> 'Matrix':
        ''' Create a diagonal (scaling) matrix using the values from the vector.

        :param vector: The vector of values for the diagonal.
        :type vector: typing.Union[typing.Sequence[float], 'Vector']
        :rtype: 'Matrix'
        :return: A diagonal matrix.
        '''
        pass

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
        ''' Return the translation, rotation, and scale components of this matrix.

        :rtype: 'Quaternion'
        :return: tuple of translation, rotation, and scale
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
        ''' Returns the interpolation of two matrices. Uses polar decomposition, see "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.

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
            ) -> float:
        ''' Return the dot product of this quaternion and another.

        :param other: The other quaternion to perform the dot product with.
        :type other: typing.Union[typing.Sequence[float], 'Quaternion']
        :rtype: float
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
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    www = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wwzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wxzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wywx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wywy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wywz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wyzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    wzzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    x: float = None
    ''' Vector X axis.

    :type: float
    '''

    xw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xwzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xxzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xywx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xywy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xywz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xyzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    xzzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    y: float = None
    ''' Vector Y axis.

    :type: float
    '''

    yw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    ywzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yxzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yywx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yywy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yywz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yyzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    yzzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    z: float = None
    ''' Vector Z axis (3D Vectors only).

    :type: float
    '''

    zw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zwzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zxzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zywx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zywy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zywz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zyzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzww = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzwx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzwy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzwz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzxw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzxx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzxy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzxz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzyw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzyx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzyy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzyz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzzw = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzzx = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzzy = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

    zzzz = None
    ''' Undocumented `contribute <https://developer.blender.org/T51061>`'''

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
