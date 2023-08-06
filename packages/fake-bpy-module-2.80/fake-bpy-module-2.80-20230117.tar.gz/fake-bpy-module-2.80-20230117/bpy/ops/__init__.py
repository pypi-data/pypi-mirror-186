import sys
import typing
from . import cycles
from . import uv
from . import action
from . import graph
from . import console
from . import view3d
from . import ed
from . import text
from . import workspace
from . import palette
from . import world
from . import import_curve
from . import transform
from . import constraint
from . import object
from . import lattice
from . import mesh
from . import texture
from . import screen
from . import gpencil
from . import particle
from . import paintcurve
from . import collection
from . import surface
from . import file
from . import ptcache
from . import camera
from . import render
from . import sculpt
from . import import_anim
from . import material
from . import preferences
from . import paint
from . import poselib
from . import brush
from . import scene
from . import curve
from . import sound
from . import cachefile
from . import boid
from . import view2d
from . import nla
from . import outliner
from . import mball
from . import export_anim
from . import export_mesh
from . import import_scene
from . import marker
from . import gizmogroup
from . import cloth
from . import import_mesh
from . import info
from . import pose
from . import clip
from . import armature
from . import script
from . import anim
from . import node
from . import safe_areas
from . import buttons
from . import sequencer
from . import mask
from . import dpaint
from . import export_scene
from . import font
from . import fluid
from . import wm
from . import image
from . import rigidbody
from . import ui

GenericType = typing.TypeVar("GenericType")


class BPyOps:
    pass


class BPyOpsSubMod:
    pass


class BPyOpsSubModOp:
    def get_rna_type(self):
        ''' 

        '''
        pass

    def idname(self):
        ''' 

        '''
        pass

    def idname_py(self):
        ''' 

        '''
        pass

    def poll(self, args):
        ''' 

        '''
        pass
