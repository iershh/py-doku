def random_literal(cnf):
    literals = []
    # loop through cnf to get the literals
    for clause in cnf:
        for literal in clause:
            literals.append(literal)
    # get random literal        
    return random.choice(literals)