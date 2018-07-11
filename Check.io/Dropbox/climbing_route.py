import pdb

'''
This isn't correct, but I kinda dig it. This just checks for a shortest path
in the given elevation map with the constraints of the problem
'''

class Route():
    def __init__(self, row, col, num_steps):
        self.row = row
        self.col = col
        self.num_steps = num_steps

    def __str__(self):
        return 'row: {}, col: {}, num_steps: {}'.format(self.row, self.col, self.num_steps)

def climbing_route(elevation_map):
    def find_candidates(route):
        row = route.row
        col = route.col
        elev = int(elevation_map[row][col])
        num_steps = route.num_steps

        # Determine if we can move down one
        if row < end_r:
            d_elev = int(elevation_map[row+1][col])

            if elev - 1 <= d_elev <= elev + 1:
                d_route = Route(row+1, col, num_steps+1)

                q.append(d_route)

        # Determine if we can move one up
        if row > 0:
            d_elev = int(elevation_map[row-1][col])

            if elev - 1 <= d_elev <= elev + 1:
                d_route = Route(row-1, col, num_steps+1)

                q.append(d_route)

        # Determine if we can move to the right
        if col < end_r:
            r_elev = int(elevation_map[row][col+1])

            if elev - 1 <= r_elev <= elev + 1:
                r_route = Route(row, col+1, num_steps+1)

                q.append(r_route)

        # Determine if we can move to the left
        if col > 0:
            r_elev = int(elevation_map[row][col-1])

            if elev - 1 <= r_elev <= elev + 1:
                r_route = Route(row, col-1, num_steps+1)

                q.append(r_route)

    route = Route(0, 0, 0)
    end_r = len(elevation_map) - 1
    end_c = len(elevation_map[0]) - 1

    q = [route]

    while len(q) != 0:
        route = q.pop(0)

        row = route.row
        col = route.col
        num_steps = route.num_steps

        if row == end_r and col == end_c:
            return route.num_steps

        find_candidates(route)

    return None

def main():
    mountain = [
        '012',
        '232',
        '100']

    sol = climbing_route(mountain)
    print(sol)

if __name__ == '__main__':
    main()
