import numpy as np
from typing import Dict
from Types import DataType


RatingType = Dict[str, float]


class AvarageMark():

        def __init__(self, data: DataType) -> None:
            self.data: DataType = data
            self.rating: RatingType = {}

        def calc(self) -> RatingType:
            for key in self.data:
                self.rating[key] = 0
                for subject in self.data[key]:
                    if subject[1] >= 90:
                        self.rating[key] += 1
            return self.rating



