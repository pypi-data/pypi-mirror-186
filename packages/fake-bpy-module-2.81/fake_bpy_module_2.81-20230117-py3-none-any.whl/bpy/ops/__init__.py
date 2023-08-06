import sys
import typing
from . import palette
from . import image
from . import ed
from . import text
from . import view2d
from . import boid
from . import dpaint
from . import export_mesh
from . import gpencil
from . import cachefile
from . import import_scene
from . import wm
from . import import_anim
from . import buttons
from . import info
from . import surface
from . import render
from . import sculpt
from . import safe_areas
from . import scene
from . import anim
from . import cloth
from . import transform
from . import particle
from . import gizmogroup
from . import fluid
from . import collection
from . import uv
from . import file
from . import marker
from . import mball
from . import sound
from . import sequencer
from . import nla
from . import paintcurve
from . import mesh
from . import lattice
from . import ptcache
from . import import_mesh
from . import world
from . import graph
from . import poselib
from . import workspace
from . import ui
from . import rigidbody
from . import material
from . import import_curve
from . import camera
from . import font
from . import outliner
from . import node
from . import preferences
from . import script
from . import mask
from . import screen
from . import object
from . import console
from . import brush
from . import clip
from . import cycles
from . import paint
from . import view3d
from . import export_scene
from . import action
from . import texture
from . import constraint
from . import pose
from . import curve
from . import armature
from . import export_anim

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
