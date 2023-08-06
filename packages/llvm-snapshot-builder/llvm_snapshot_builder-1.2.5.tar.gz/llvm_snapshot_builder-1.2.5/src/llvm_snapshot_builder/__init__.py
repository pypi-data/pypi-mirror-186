"""
llvm_snapshot_builder provides classes to interact with Copr.
"""
from importlib.metadata import version
# read version from installed package
__version__ = version("llvm_snapshot_builder")

from .actions import *
from .mixins import *
from .copr_project_ref import CoprProjectRef
