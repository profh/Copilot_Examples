# Create a function called fizzbuzz that prints the numbers from 1 to 100 and replaces multiples of 3 with “Fizz”, multiples of 5 with “Buzz” and multiples of both with “FizzBuzz”.

def fizzbuzz
  (1..100).each do |i|
    if i % 3 == 0 and i % 5 == 0
      puts "FizzBuzz"
    elsif i % 3 == 0 
      puts "Fizz"
    elsif i % 5 == 0 
      puts "Buzz"
    else
      puts i
    end
  end
end

fizzbuzz