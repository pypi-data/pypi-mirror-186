import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def open(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         filepath: typing.Union[str, typing.Any] = "",
         hide_props_region: typing.Union[bool, typing.Any] = True,
         check_existing: typing.Union[bool, typing.Any] = True,
         filter_blender: typing.Union[bool, typing.Any] = False,
         filter_backup: typing.Union[bool, typing.Any] = False,
         filter_image: typing.Union[bool, typing.Any] = False,
         filter_movie: typing.Union[bool, typing.Any] = False,
         filter_python: typing.Union[bool, typing.Any] = False,
         filter_font: typing.Union[bool, typing.Any] = False,
         filter_sound: typing.Union[bool, typing.Any] = False,
         filter_text: typing.Union[bool, typing.Any] = False,
         filter_archive: typing.Union[bool, typing.Any] = False,
         filter_btx: typing.Union[bool, typing.Any] = False,
         filter_collada: typing.Union[bool, typing.Any] = False,
         filter_alembic: typing.Union[bool, typing.Any] = True,
         filter_folder: typing.Union[bool, typing.Any] = True,
         filter_blenlib: typing.Union[bool, typing.Any] = False,
         filemode: typing.Optional[typing.Any] = 8,
         display_type: typing.Optional[typing.Any] = 'DEFAULT',
         sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA'):
    ''' Load a cache file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: typing.Union[bool, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_VERTICAL`` Short List, Display files as short list. * ``LIST_HORIZONTAL`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Name, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Modified Date, Sort files by modification time. * ``FILE_SORT_SIZE`` Size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    '''

    pass


def reload(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Update objects paths list with new data from the archive

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
