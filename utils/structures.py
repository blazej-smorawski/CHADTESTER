from typing import List, Tuple


class Question:
    def __init__(self, q: str, a: List[Tuple], c: List[str]):
        self.q = q
        self.a = a
        self.c = c
