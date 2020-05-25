import cProfile
def solution(l):
    # Get length of input list
    l_size = len(l)
    # Return 0 if length is less than triple
    if len(l) < 3:
        return 0

    # Initialize count
    count = (int)(0)

    # Iterate over possible indices of middle element y: 1 to len-2
    for i in range(1, l_size - 1):

        y = l[i]

        # For given y, find x which divides y
        x_cnt = len([x for x in l[:i] if y % x == 0])

        # For given y, find z which is divisible by y
        if x_cnt != 0:
            z_cnt = len([z for z in l[i+1:] if z % y == 0])

            # Add intersection of x,y,z values to total count
            count += x_cnt * z_cnt

    return (count)

if __name__ == "__main__":


    l = [1] * 2000
    cProfile.run("p = solution(l)")
    print(hex(p))