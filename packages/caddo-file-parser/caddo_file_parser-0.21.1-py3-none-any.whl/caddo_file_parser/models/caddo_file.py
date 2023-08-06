from caddo_file_parser.models.index_set import IndexSet
import pandas as pd

from caddo_file_parser.models.run import Run
from caddo_file_parser.settings.generation_settings import GenerationSettings


class CaddoFile:
    def __init__(self, runs: [Run], data: pd.DataFrame, settings: GenerationSettings):
        self.runs = runs
        self.data = data
        self.settings = settings

