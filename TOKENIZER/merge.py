def _merge_pair(ids: list[int], pair: tuple[int, int], new_id: int) -> list[int]:
    out = []
    i = 0
    a, b = pair
    while i < len(ids):
        if i + 1 < len(ids) and ids[i] == a and ids[i + 1] == b:
            out.append(new_id)
            i += 2
        else:
            out.append(ids[i])
            i += 1
    return out