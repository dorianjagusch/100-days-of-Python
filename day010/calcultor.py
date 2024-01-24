import art

print(art.logo)

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def divide(a, b):
  if (b != 0):
    return a / b

operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": divide
}

def calc_result(a, b, op):
  result = operations[op](a,b)
  return result

in_calc = True

while in_calc:

  first_number = float(input("Whats's the first number?: "))
  continue_flag = 'y'
  print("+\n-\n*\n/")
  while continue_flag == 'y':

    operation = input("Pick an operation: ")
    second_number = float(input("Whats's the next number?: "))

    result = calc_result(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {result}")

    continue_flag = ""
    while continue_flag != "y" and continue_flag != "n":
      continue_flag = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new caluclation: ")

    if continue_flag == 'y':
      first_number = result