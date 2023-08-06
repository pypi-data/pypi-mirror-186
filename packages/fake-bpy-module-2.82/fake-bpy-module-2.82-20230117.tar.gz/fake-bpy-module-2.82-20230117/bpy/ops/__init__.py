import sys
import typing
from . import lattice
from . import collection
from . import mask
from . import fluid
from . import file
from . import paintcurve
from . import preferences
from . import ed
from . import surface
from . import view2d
from . import material
from . import sound
from . import armature
from . import import_scene
from . import buttons
from . import cycles
from . import workspace
from . import uv
from . import rigidbody
from . import texture
from . import palette
from . import boid
from . import image
from . import curve
from . import world
from . import camera
from . import particle
from . import render
from . import ptcache
from . import script
from . import scene
from . import console
from . import node
from . import constraint
from . import view3d
from . import screen
from . import font
from . import outliner
from . import export_scene
from . import info
from . import mesh
from . import pose
from . import action
from . import import_curve
from . import safe_areas
from . import paint
from . import cachefile
from . import text
from . import nla
from . import graph
from . import import_anim
from . import clip
from . import gpencil
from . import export_anim
from . import ui
from . import sculpt
from . import anim
from . import transform
from . import import_mesh
from . import brush
from . import marker
from . import export_mesh
from . import poselib
from . import gizmogroup
from . import wm
from . import object
from . import cloth
from . import mball
from . import sequencer
from . import dpaint

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
