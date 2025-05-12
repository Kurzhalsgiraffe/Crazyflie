factor = 10

with open("albsig_single_motion_coordinates.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        if len(l) > 1:
            x,y = l.split(" ")
            x,y = int(x[1:])/factor, int(y[1:])/factor
            coords = [x,y,1]
            print(coords, end="")
