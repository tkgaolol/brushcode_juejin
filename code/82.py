def solution(n, m, citizens, locations):
    # Function to calculate Manhattan distance between two points
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    min_total_distance = float('inf')
    best_location = None
    
    # For each possible location
    for location in locations:
        total_distance = 0
        # Calculate total distance from all citizens to this location
        for citizen in citizens:
            total_distance += manhattan_distance(citizen, location)
        
        # Update best location if current total distance is smaller
        # or if it's equal but current location comes first
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_location = location
    
    return best_location if best_location is not None else [-1, -1]

if __name__ == "__main__":
    #  You can add more test cases here
    citizens1 = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    locations1 = [[3, 2], [1, 0], [0, 0]]
    print(solution(4, 3, citizens1, locations1) == [1, 0])