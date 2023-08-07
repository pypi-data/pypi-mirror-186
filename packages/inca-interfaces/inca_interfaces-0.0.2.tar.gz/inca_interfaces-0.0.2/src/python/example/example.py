
import sklearn
from dataclasses import dataclass
from typing import Any
from enum import Enum

@dataclass
class ChunkAnalysis:
    datc: Any

class ResearchDomain(Enum):
    TODO = 'todo'



def get_sklearn_version():
    return sklearn.__version__


