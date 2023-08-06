from interval_map import IntervalMap


def main():
    im = IntervalMap[int, int](0, [1, 4, 7], [2, 6, 10])
    
    im.slice_subtract(10, 13, 1)
    
    for i in range(8, 15):
        print(i, im[i])
    
    
if __name__ == "__main__":
    main()
