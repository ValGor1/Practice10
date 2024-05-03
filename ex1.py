if __name__ == "__main__":
    input = 'input.txt'
    output = 'output.txt'
    upper(input, output)

def upper(input, output):
    with open(input 'r') as input_file:
        data = input_file.read()

    with open(output, 'w') as output_file:
        converted_data = data.upper()
        output_file.write(converted_data)

