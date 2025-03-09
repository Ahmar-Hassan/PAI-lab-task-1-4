def waterjugproblem_dfs(c1, c2, goal):
    stack = []  
    visited = set()
    
    stack.append((0, 0))
    visited.add((0, 0))

    while stack:
        jug1, jug2 = stack.pop()  
        print(jug1, jug2)  

        if jug1 == goal or jug2 == goal:
            print("Solution found")
            for state in visited:
                print(state)
            return True

        
        rules = [
            (c1, jug2), 
            (jug1, c2), 
            (0, jug2),   
            (jug1, 0),   
            (jug1 - min(jug1, c2 - jug2), jug2 + min(jug1, c2 - jug2)),  
            (jug1 + min(jug2, c1 - jug1), jug2 - min(jug2, c1 - jug1))   
        ]

        for rule in rules:
            if rule not in visited:
                visited.add(rule)
                stack.append(rule) 

    print("No solution found.")
    return False


waterjugproblem_dfs(4, 3, 2)
