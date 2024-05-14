import random, sys

def generate_requests(file_name, num_requests, max_cylinder, seed):
    if seed:
        random.seed(seed) # Add Seed if you want a fixed randomness.

    with open(file_name, 'w') as file:
        for i in range(num_requests):
            # Return random integer in range of 0 to max_cylinder, which includes 0 and max_cylinder
            request = random.randint(0, max_cylinder)
            # Write the file
            file.write(str(request) + '\n')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Allow the user to provide seed for a fixed randomness
        seed = int(sys.argv[1])
    else: seed = None

    # Determine file name
    file_name = "requests.txt"
    # The total produced line
    num_requests = 1000
    # The max number
    max_cylinder = 4999

    generate_requests(file_name, num_requests, max_cylinder, seed)