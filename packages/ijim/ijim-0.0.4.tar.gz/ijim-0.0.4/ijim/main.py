from interval_map import IntervalMap


def main():
    im = IntervalMap[int, int](
        0, 
        [],
        []
    )
    print(im)
    im.slice_sub(2, 4, 1)
    print(im)
    
    
if __name__ == "__main__":
    main()
