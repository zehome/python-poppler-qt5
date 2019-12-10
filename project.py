import os

from pyqtbuild import PyQtBindings, PyQtProject, QmakeBuilder
from sipbuild import Option, Project
from sipbuild import Option


class Poppler(Project):
    def __init__(self):
        super().__init__()
        self.qml_debug = False
        # /Users/admin/.conan/data//poppler/0.80.0/clarisys/stable/package/630d44cde0674cd46a6832f68a09065394c5d148/include/poppler
        self.py_pylib_dir = None
        self.builder_factory = QmakeBuilder
#        self.bindings_factories = [PopplerBinding]

    def get_options(self):
        options = super().get_options()
        inc_dir_option = Option('poppler_include_dir',
                help="the directory containing qt5/poppler.h", metavar="DIR")
        options.append(inc_dir_option)
        lib_dir_option = Option('poppler_library_dir',
                help="the directory containing the poppler library",
                metavar="DIR")
        options.append(lib_dir_option)
        return options

    def apply_user_defaults(self, tool):
        if self.poppler_include_dir is not None:
            self.poppler_include_dir = os.path.abspath(self.poppler_include_dir)

        # Ensure any user supplied library directory is an absolute path.
        if self.poppler_library_dir is not None:
            self.library_dir = os.path.abspath(self.poppler_library_dir)

        # Apply the defaults for the standard options.
        super().apply_user_defaults(tool)

    def update(self, tool):
        poppler_bindings = self.bindings['popplerqt5']
        if self.poppler_include_dir is not None:
            poppler_bindings.include_dirs = [self.poppler_include_dir]
        if self.poppler_library_dir is not None:
            poppler_bindings.library_dirs = [self.poppler_library_dir]

#class PopplerBinding(PyQtBindings):
#    def __init__(self, project):
#        super().__init__(project, 'popplerqt5', sip_file='popplerqt5mod.sip')

