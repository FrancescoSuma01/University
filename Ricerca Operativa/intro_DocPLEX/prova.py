import docplex.mp.model as cplex

# creation of the model
m = cplex.Model("telephone_production")  # Model for optimizing telephone production

# creation of the two continuous variables useful for constraint creation
desk = m.continuous_var(name='desk')
cell = m.continuous_var(name='cell')

# write constraints
# constraint 1: desk production is greater than or equal to 100
m.add_constraint(desk >= 100, 'minimum_desks')

# constraint 2: cell production is greater than or equal to 100
m.add_constraint(cell >= 100, 'minimum_cells')

# constraint 3: assembly time limit
m.add_constraint(0.2 * desk + 0.4 * cell <= 400, 'ct_assembly')

# constraint 4: painting time limit
m.add_constraint(0.5 * desk + 0.4 * cell <= 490, 'ct_painting')

# objective function definition
# maximize profit: $12 per desk and $20 per cell
m.maximize(12 * desk + 20 * cell)

# prints information about the model, such as number and type of variables, constraints, etc.
m.print_information()

# solving the model
sol = m.solve(log_output=True)

# check if a solution exists
if sol is not None:
    # retrieve the objective value (total profit)
    fo = m.objective_value
    
    print("--------------------------------------------")    
    print()
    print("Total profit: ", fo)
    print()

    # retrieve and print the values of decision variables
    print("Produce", desk.solution_value, "desk")
    
    print()
    print("Produce", cell.solution_value, "cell")
    print()
    
else:
    print("No solution found for the model.")

# print solution details
print(m.solve_details)
