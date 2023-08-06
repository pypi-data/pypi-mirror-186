import sys
import typing
from . import import_scene
from . import boid
from . import render
from . import nla
from . import collection
from . import fluid
from . import armature
from . import world
from . import script
from . import ui
from . import gpencil
from . import anim
from . import material
from . import view3d
from . import surface
from . import sequencer
from . import camera
from . import sculpt
from . import console
from . import ptcache
from . import file
from . import particle
from . import poselib
from . import cycles
from . import object
from . import image
from . import screen
from . import cloth
from . import clip
from . import ed
from . import curve
from . import view2d
from . import node
from . import constraint
from . import preferences
from . import lattice
from . import export_anim
from . import import_mesh
from . import sound
from . import text
from . import uv
from . import outliner
from . import pose
from . import buttons
from . import mask
from . import import_anim
from . import marker
from . import action
from . import mball
from . import palette
from . import paintcurve
from . import brush
from . import cachefile
from . import texture
from . import graph
from . import paint
from . import mesh
from . import scene
from . import import_curve
from . import transform
from . import workspace
from . import safe_areas
from . import export_mesh
from . import dpaint
from . import info
from . import wm
from . import gizmogroup
from . import font
from . import export_scene
from . import rigidbody

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
