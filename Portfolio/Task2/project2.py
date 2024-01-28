import sys

def cat_log(file):
    """
    The function calculates the total cat visits, including time spent and average using the file provided through a command line argument to read.
    
    Parameters:
    - file (str): The path to the cat log file.
    """
    try:
        with open(file, 'r') as f:
            cat_visit = 0
            our_cat_time_spent = 0
            other_cat_visit = 0
            our_cat_average = []
            sum_our_cat = 0

            while True:
                line = f.readline().strip()  # Reads the file line by line and breaks if "END" in the file
                if 'END' in line:
                    break

                if 'OURS' in line:  # Calculates cat visits, time spent, and appends the our_cat_time_spent in our_cat_average list
                    cat_visit += 1
                    spliting = line.split(',')
                    slicing1 = int(spliting[1])
                    slicing2 = int(spliting[2])
                    our_cat_time_spent = slicing2 - slicing1
                    our_cat_average.append(our_cat_time_spent)

                elif 'THEIRS' in line:  # Calculates other cat visits
                    other_cat_visit += 1

        def format_time(minutes): 
            """The function formats time in a more readable format."""
            hours = minutes // 60
            minutes %= 60
            return f"{hours} Hours, {minutes} Minutes"

# For finding the sum
        for i in our_cat_average:
            sum_our_cat += i

# Calculates the average, longest and shortest stay of 'OURS' cat 
        average = int(sum_our_cat / len(our_cat_average))
        longest = max(our_cat_average)
        shortest = min(our_cat_average)

# Prints the values
        print('Log File Analysis')
        print('=' * 17)
        print('Cat visit', cat_visit)
        print('Other cat visit', other_cat_visit)
        print('\n')
        print('Total time in the house:', format_time(sum_our_cat))
        print('\n')
        print('Average:', format_time(average))
        print('Longest:', format_time(longest))
        print('Shortest:', format_time(shortest))

# Prints error message if the file is not found
    except FileNotFoundError:
        print(f'Cannot open "{file}"!')

# Check if a command line argument is provided
if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    file = sys.argv[1]
    cat_log(file)
