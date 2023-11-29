"""
name: Muhammad Shike
"""

from math import gcd
from functools import reduce


def blocks_solver(blocks, total_target):
    factor = reduce(gcd, blocks)
    new_target, remainder = divmod(total_target, factor)
    if remainder:
        raise ValueError("Cannot make the target with the given blocks")
    blocks = [block // factor for block in blocks]

    # Dynamic programming phase
    memo = [(0, None)] + [None] * new_target
    for target in range(1, new_target + 1):
        min_ans = float('inf')
        min_idx = None
        for idx in range(len(blocks) - 1, -1, -1):
            next_target = target - blocks[idx]
            if next_target < 0:
                continue
            ans, _ = memo[next_target]
            if ans < min_ans:
                min_ans = ans
                min_idx = idx

        ret = (min_ans + 1, min_idx)
        memo[target] = ret

    total_blocks, next_block = memo[new_target]
    if total_blocks == float("inf"):
        raise ValueError("Cannot make the target with the given blocks")

    # Solution building phase
    counts = [0] * len(blocks)
    remaining_target = new_target
    while next_block is not None:
        remaining_target -= blocks[next_block]
        counts[next_block] += 1
        _, next_block = memo[remaining_target]

    return total_blocks, counts


def main():
    blocks = [int(num) for num in input().split()]
    target = int(input())
    min_blocks, blocks_used = blocks_solver(blocks, target)
    for block, num in zip(blocks, blocks_used):
        print(num, "of length", block)
    print(min_blocks, "rocket sections minimum")


if __name__ == "__main__":
    main()
