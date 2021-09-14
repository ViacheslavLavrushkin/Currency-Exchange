# from time import sleep
#
# CACHE = {}
#
#
# def slow_function(sleep_time, mult=1):
#     cache_key = f'slow_function_{sleep_time}_{mult}'
#
#     if cache_key in CACHE:
#         return CACHE[cache_key]
#
#     sleep(sleep_time)
#     result = sleep_time * 2 * mult
#     CACHE[cache_key] = result
#     return result
#
# print(slow_function(3, 2))
# print(slow_function(3, 3))
# # print(slow_function2(3))
# # print(slow_function2(3))
# print(CACHE)
#
#
# '''
# def slow_function2(sleep_time):
#     cache_key = f'slow_function2_{sleep_time}'
#
#     if cache_key in CACHE:
#         return CACHE[cache_key]
#
#     sleep(sleep_time)
#     result = sleep_time * 3
#     CACHE[cache_key] = result
#     return result
# '''


cached = list(range(10_000))

if 9_999 in cached:
    print()

if 9_999 in cached:
    print()

if 9_999 in list(range(10_000)):
    print()

if 9_999 in list(range(10_000)):
    print()
