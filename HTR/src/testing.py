import sys 

CSV_FILE = '../../Results/results.csv'

def get_args():
    ''' takes test file name as argument '''

    instance = sys.argv[1].removeprefix('test_').removesuffix('.png')
    return instance

def get_res_prob():
    '''
    looks at the output cut from running the model on the test image
    '''
    with open('./cut_output.dump') as out:
        output_rows = [row.removesuffix('\n') for row in out]

    result = output_rows[0]
    prob = output_rows[1]

    return result, prob

def read_file_lines(file_path):
    ''' reads file lines '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

#print(csv_lines)
#print(instance)
#print(result, prob)

csv_lines = read_file_lines(CSV_FILE)
instance = get_args()
result, prob = get_res_prob()
lines = []

def file_line_rewritter():
    ''' rewrites the instance in the line by appending result and prob '''
    for line in csv_lines:
        line = line.removesuffix('\n')
        line = line.rstrip()
        if line.startswith(f'{instance},'):
            updated_line = f'{line} {result}, {float(prob)*100}%, '
            line = updated_line
        lines.append(line+ '\n')
    with open(CSV_FILE, 'w') as file:
        file.writelines(lines)

file_line_rewritter()