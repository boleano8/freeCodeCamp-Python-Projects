# Proyecto: Elegancia_Aritmética
# Descripción: Formatea problemas aritméticos de manera elegante y vertical.
** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        # Split the problem into its components
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format"
        
        num1, operator, num2 = parts

        # Validate the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate that numbers only contain digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."  

        # Validate the length of numbers
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits." 

        # Calculate the width needed for this problem
        width = max(len(num1), len(num2)) + 2  # +2 for operator and space

        # Format the lines
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dash_line.append('-' * width)

        # Calculate the answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line.append(answer.rjust(width))

    # Combine all lines
    result = '    '.join(first_line) + '\n'
    result += '    '.join(second_line) + '\n'
    result += '    '.join(dash_line)

    # Add answers if requested
    if show_answers:
        result += '\n' + '    '.join(answer_line)

    return result

# Llamada a la función para probar (fuera de la definición)
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))

** end of main.py **

