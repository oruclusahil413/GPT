def encode(self, text: str) -> list[int]:
    ids = list(text.encode("utf-8"))
    for merge_index, pair in enumerate(self.merges):
        ids = self._merge_pair(ids, pair, 256 + merge_index)
    return ids


def decode(self, ids: list[int]) -> str:
    pieces = {i: bytes([i]) for i in range(256)}
    for merge_index, (a, b) in enumerate(self.merges):
        pieces[256 + merge_index] = pieces[a] + pieces[b]