// Create a function called fizzbuzz that prints the numbers from 1 to 100 and replaces multiples of 3 with “Fizz”, multiples of 5 with “Buzz” and multiples of both with “FizzBuzz”.

"""
 
A first attempt... (option #1 in copilot list)
func fizzbuzz() {
    for i in 1...100 {
        if i % 3 == 0 && i % 5 == 0 {
            print("FizzBuzz")
        }
        else if i % 3 == 0 {
            print("Fizz")
        }
        else if i % 5 == 0 {
            print("Buzz")
        }
        else {
            print(i)
        }
    }
}
"""

// A more Swift-y solution... (option #3 in copilot list)
func fizzbuzz() {
    for i in 1...100 {
        switch (i % 3, i % 5) {
        case (0, 0):
            print("FizzBuzz")
        case (0, _):
            print("Fizz")
        case (_, 0):
            print("Buzz")
        default:
            print(i)
        }
    }
}