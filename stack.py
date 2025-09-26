class DS_Stack: 

# The __init__ method is a special method called a constructor.
# It's automatically called when a new instance of the class is created.
# 'self' refers to the instance of the class itself.
    def __init__(self, stack_capacity): 
            self.capacity = stack_capacity 
            self.arr = [None] * int(stack_capacity)             
            self.top = -1
    
    def pop(self):
          if self.top == -1:
            return "Stack is empty"
          value = self.arr[self.top]
          self.arr[self.top] = None
          self.top -= 1
          return value
    
    def push(self, value):
          if self.top == int(self.capacity) - 1:
               return "Stack is full, cannot push"
         
          self.top += 1
          self.arr[self.top] = value
          return f"Item {value} pushed to the stack"
          
    def peek(self):
          if self.top == -1:
               return "Stack is empty"
          else:
               return self.arr[self.top]
          

if __name__ == "__main__":
    while True:
        input_raw = input("Enter the capacity of the stack or type '0' to quit:")
        if(input_raw == '0'):
            break
        if(input_raw.isdigit()):  
            input_capacity = int(input_raw)          
            stack = DS_Stack(input_capacity)
            break
        else:
            print("Invalid input, please enter a valid integer number for capacity. Or type '0' to quit.")

    while True:
        operation = input("Enter operation (push, pop, peek) or type 'exit' to quit: ").strip().lower()
        if operation == 'exit':
            break
        elif operation == 'push':
            value = input("Enter value to push: ")
            if value.isdigit():
                print(stack.push(int(value)))
            else:
                print("Invalid input, please enter a valid integer value.")
        elif operation == 'pop':
            print(stack.pop())
        elif operation == 'peek':
            print(stack.peek())
        else:
            print("Invalid operation. Please enter 'push', 'pop', 'peek', or 'exit'.")
