from collections import deque
from time import time, sleep

import pytest

from ..ttl_dict import TTLDict


@pytest.mark.benchmark
def test_ttl_dict_performance(performance_test):

    def _test_get(num, size):
        ttl = TTLDict(zip(range(size), range(size)))
        t0 = time()
        deque((ttl[n % size] for n in range(num)), maxlen=0)
        t1 = time()
        return t1 - t0, num

    def _test_dict_get(num, size):
        normal_dict = dict(zip(range(size), range(size)))
        t0 = time()
        deque((normal_dict[n % size] for n in range(num)), maxlen=0)
        t1 = time()
        return t1 - t0, num

    def _test_set(num, size):
        ttl = TTLDict(zip(range(size), range(size)))
        t0 = time()
        deque((ttl.__setitem__(n % size, n) for n in range(num)), maxlen=0)
        t1 = time()
        return t1 - t0, num

    def _test_dict_set(num, size):
        normal_dict = dict(zip(range(size), range(size)))
        t0 = time()
        deque((normal_dict.__setitem__(n % size, n) for n in range(num)), maxlen=0)
        t1 = time()
        return t1 - t0, num

    def _test_len(num, size):
        ttl = TTLDict(zip(range(size), range(size)))
        t0 = time()
        deque((ttl.__len__() for _ in range(num)), maxlen=0)
        t1 = time()
        return t1 - t0, num

    def _test_dict_len(num, size):
        normal_dict = dict(zip(range(size), range(size)))
        t0 = time()
        deque((normal_dict.__len__() for _ in range(num)), maxlen=0)
        t1 = time()
        return t1 - t0, num

    num, runs = 3000, 3
    sizes = [10, 100, 1000]

    print(f'\n\nTesting TTL dict performance ({num} cycles, {runs} runs)...\n')

    print(f'\tGET:')
    for size in sizes:
        dt, counter, rps = performance_test(_test_get, args=(num, size), runs=runs)
        dt2, counter2, rps2 = performance_test(_test_dict_get, args=(num, size), runs=runs)
        percent = round(100 * rps / rps2, 1)
        print(f'\t{size:>4} {int(rps):>10} sec^-1 | {percent}%')
    print()

    print(f'\tSET:')
    for size in sizes:
        dt, counter, rps = performance_test(_test_set, args=(num, size), runs=runs)
        dt2, counter2, rps2 = performance_test(_test_dict_set, args=(num, size), runs=runs)
        percent = round(100 * rps / rps2, 1)
        print(f'\t{size:>4} {int(rps):>10} sec^-1 | {percent}%')
    print()

    print(f'\tLENGTH:')
    for size in sizes:
        dt, counter, rps = performance_test(_test_len, args=(num, size), runs=runs)
        dt2, counter2, rps2 = performance_test(_test_dict_len, args=(num, size), runs=runs)
        percent = round(100 * rps / rps2, 1)
        print(f'\t{size:>4} {int(rps):>10} sec^-1 | {percent}%')
    print()


@pytest.mark.unit
def test_ttl_dict(logger):

    fixture = {'a': 42}

    logger.info('Testing basic operation.')

    ttl = TTLDict(**fixture)
    assert dict(ttl) == fixture
    assert list(ttl.items()) == list(fixture.items())
    assert list(ttl.values()) == list(fixture.values())
    assert dict(**ttl) == fixture
    assert ttl.pop('a') == fixture['a']
    assert len(ttl) < len(fixture)
    assert not ttl
    ttl['b'] = 42
    assert 'b' in ttl

    logger.info('Testing ttl operations.')

    with pytest.raises(ValueError):
        ttl.set_ttl(-1)

    ttl.set_ttl(1)
    ttl['k'] = 1
    sleep(1.1)
    assert 'k' not in ttl
    assert ttl.get('k') is None

    logger.info('Finished tests.')
