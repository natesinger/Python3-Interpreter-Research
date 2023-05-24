import timeit

def loopy_native():
    for i in range(int(1e9)): x = i / 5

if __name__ == "__main__":
    # run the native version
    print(f"Time taken by native implementation is {timeit.timeit(loopy_native, number=1)} seconds")

    # run the optomized library
    stmt = "loopy_optimized.loopy_optimized()"
    execution_time = timeit.timeit(stmt, setup="import loopy_optimized", number=1)
    print(f"Time taken by optimized implementation is {execution_time} seconds")
