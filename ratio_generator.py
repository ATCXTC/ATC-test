import random

def generate_ratios(max_count=24):
    # Generate a random number of ratios (1 to max_count)
    num_ratios = random.randint(1, max_count)
    
    # Generate the specified number of ratios
    ratios = []
    for _ in range(num_ratios):
        # Generate random positive integers for numerator and denominator
        # Using range(1, 101) to keep numbers manageable
        numerator = random.randint(1, 100)
        denominator = random.randint(1, 100)
        ratios.append(f"{numerator}/{denominator}")
    
    # Write ratios to output file
    with open('ratios.txt', 'w') as f:
        for ratio in ratios:
            f.write(ratio + '\n')

if __name__ == "__main__":
    generate_ratios()