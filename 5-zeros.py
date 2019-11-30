def move_zeros(array):
    new_array = []
    zero_array = []
    for line in array:
        if 'False' in str(line):
            new_array.append(line)
            continue
        elif line == 0:
            zero_array.append(0)
            continue
        elif "0" == str(line):
            zero_array.append("0")
            continue
        new_array.append(line)

    new_array.extend(zero_array)
    return new_array


move_zeros([-4, 0, -5, -3, 3, 0, -1, '0', 'c', 8, -9, 0, -7, 'b', 8, 0, 6, '0', -7, 7, 3, 0, 10, False, -7, 'z', 0, 0, -5])


assert move_zeros([1,2,0,1,0,1,0,3,0,1]) == [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
assert move_zeros(["a","b"]) == ["a","b"]
assert move_zeros(["a"]) == ["a"]
assert move_zeros([0,0]) == [0,0]
assert move_zeros([0]) == [0]
assert move_zeros([False]) == [False]
assert move_zeros([]) == []