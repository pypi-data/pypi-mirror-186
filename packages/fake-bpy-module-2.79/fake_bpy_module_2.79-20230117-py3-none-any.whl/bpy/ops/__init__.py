import sys
import typing
from . import gpencil
from . import sequencer
from . import image
from . import node
from . import scene
from . import cachefile
from . import font
from . import constraint
from . import mesh
from . import script
from . import outliner
from . import import_mesh
from . import export_scene
from . import file
from . import info
from . import world
from . import anim
from . import armature
from . import mball
from . import import_scene
from . import text
from . import paint
from . import poselib
from . import paintcurve
from . import surface
from . import mask
from . import import_curve
from . import safe_areas
from . import action
from . import view3d
from . import buttons
from . import transform
from . import fluid
from . import graph
from . import cycles
from . import uv
from . import curve
from . import render
from . import pose
from . import import_anim
from . import particle
from . import camera
from . import brush
from . import group
from . import export_mesh
from . import nla
from . import lattice
from . import export_anim
from . import wm
from . import sketch
from . import object
from . import marker
from . import view2d
from . import rigidbody
from . import sound
from . import clip
from . import time
from . import screen
from . import ptcache
from . import dpaint
from . import palette
from . import boid
from . import sculpt
from . import material
from . import cloth
from . import texture
from . import console
from . import ed
from . import logic
from . import lamp
from . import ui

GenericType = typing.TypeVar("GenericType")


class BPyOps:
    pass


class BPyOpsSubMod:
    pass


class BPyOpsSubModOp:
    def get_instance(self):
        ''' 

        '''
        pass

    def get_rna(self):
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
