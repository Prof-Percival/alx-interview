#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    max_num = max(nums)
    primes_list = [True for _ in range(1, max_num + 1, 1)]
    primes_list[0] = False
    for p, is_prime in enumerate(primes_list, 1):
        if p == 1 or not is_prime:
            continue
        for j in range(p + p, max_num + 1, p):
            primes_list[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, max_num in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes_list[0: max_num])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
