# you can use conditionals and like modulo and stuff how do you 
# even do this without that bruh idek

num_students = int(input("how many students in the course? "))
group_size = int(input("desired group size? "))

#model solution:
groups_formed = (num_students + group_size - 1) // group_size

# how does this work
#groups_formed = -(-num_students//group_size)
print(f"Number of groups formed:", groups_formed)
