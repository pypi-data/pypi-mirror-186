from typing import TypeVar, DefaultDict, Iterable
from collections import defaultdict, namedtuple

Group = namedtuple(typename="Group", field_names=("length", "distance", "elements"))

E = TypeVar("E")


def sortkey(index: int):
    return lambda e: e[index]


def iter_length_groups(__data: Iterable[E], key: E):
    le_map: DefaultDict[int, list[E]] = defaultdict(list[E])
    for e in __data:
        le_map[len(e)].append(e)

    ld_list = [(l, abs(l - len(key))) for l in le_map.keys()]
    ld_list.sort(key=sortkey(index=1))
    for (l, d) in ld_list:
        e = le_map[l]
        yield Group(l, d, e)


def levenshtein_neighbors(__values: tuple[E, E, int, int]) -> int:
    lhe, rhe, llen, rlen = __values
    dp = [[0] * (rlen + 1) for _ in range(llen + 1)]
    for i in range(llen + 1):
        dp[i][0] = i
    for j in range(rlen + 1):
        dp[0][j] = j
    for i in range(1, llen + 1):
        for j in range(1, rlen + 1):
            if lhe[i - 1] == rhe[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[llen][rlen]


def get_nearest(top: int, __data: Iterable[E], key: E):
    length = len(key)
    limit = length + 1
    heap = [[] for _ in range(0, limit)]
    for group in iter_length_groups(__data, key):
        if (sum(len(rgroup) for rgroup in heap) < top) and group.distance < length:
            for (e, d) in (
                ed
                for ed in (
                    (e, levenshtein_neighbors((e, key, group.length, length)))
                    for e in group.elements
                )
                if ed[1] < limit
            ):
                heap[d].append((d, e))
        else:
            break
    results = []
    extend = results.extend
    for h in heap:
        if len(results) < top:
            extend(h)
        else:
            break

    return results
