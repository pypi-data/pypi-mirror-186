import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class UnifiedPaintPanel:
    def paint_settings(self, context):
        ''' 

        '''
        pass

    def prop_unified_color(self, parent, context, brush, prop_name, text):
        ''' 

        '''
        pass

    def prop_unified_color_picker(self, parent, context, brush, prop_name,
                                  value_slider):
        ''' 

        '''
        pass

    def prop_unified_size(self, parent, context, brush, prop_name, icon, text,
                          slider):
        ''' 

        '''
        pass

    def prop_unified_strength(self, parent, context, brush, prop_name, icon,
                              text, slider):
        ''' 

        '''
        pass

    def prop_unified_weight(self, parent, context, brush, prop_name, icon,
                            text, slider):
        ''' 

        '''
        pass

    def unified_paint_settings(self, parent, context):
        ''' 

        '''
        pass


class VIEW3D_MT_tools_projectpaint_clone(bpy_types.Menu, bpy_types._GenericUI):
    bl_label = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    def append(self, draw_func):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass_py(self):
        ''' 

        '''
        pass

    def draw(self, context):
        ''' 

        '''
        pass

    def draw_collapsible(self, context, layout):
        ''' 

        '''
        pass

    def draw_preset(self, _context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def is_extended(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_overridable_library(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_menu(self, searchpaths, operator, props_default, prop_filepath,
                  filter_ext, filter_path, display_name, add_operator):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def pop(self):
        ''' 

        '''
        pass

    def prepend(self, draw_func):
        ''' 

        '''
        pass

    def property_overridable_library_set(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def remove(self, draw_func):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


def brush_basic_gpencil_paint_settings(layout, _context, brush, compact):
    ''' 

    '''

    pass


def brush_basic_gpencil_sculpt_settings(layout, context, brush, compact):
    ''' 

    '''

    pass


def brush_basic_gpencil_weight_settings(layout, _context, brush, compact):
    ''' 

    '''

    pass


def brush_basic_sculpt_settings(layout, context, brush, compact):
    ''' 

    '''

    pass


def brush_basic_texpaint_settings(layout, context, brush, compact):
    ''' 

    '''

    pass


def brush_basic_vpaint_settings(layout, context, brush, compact):
    ''' 

    '''

    pass


def brush_basic_wpaint_settings(layout, context, brush, compact):
    ''' 

    '''

    pass


def brush_mask_texture_settings(layout, brush):
    ''' 

    '''

    pass


def brush_texpaint_common(panel, context, layout, brush, _settings, projpaint):
    ''' 

    '''

    pass


def brush_texpaint_common_clone(_panel, context, layout, _brush, settings,
                                projpaint):
    ''' 

    '''

    pass


def brush_texpaint_common_color(_panel, context, layout, brush, _settings,
                                projpaint):
    ''' 

    '''

    pass


def brush_texpaint_common_gradient(_panel, context, layout, brush, _settings,
                                   projpaint):
    ''' 

    '''

    pass


def brush_texpaint_common_options(_panel, _context, layout, brush, _settings,
                                  projpaint):
    ''' 

    '''

    pass


def brush_texture_settings(layout, brush, sculpt):
    ''' 

    '''

    pass
