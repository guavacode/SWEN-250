require_relative 'factorial' #We need to access our code to test
require 'test/unit'          #We need Ruby's unit testing library

class FactorialTest < Test::Unit::TestCase #This is a class. (It's ok if you don't know what those are yet)

  #Test methods MUST start with test_
  def test_normal
    assert_equal 24, factorial(4),"4! should be 24"
  end

  # Add many other test methods here
  #

  def test_five
    assert_equal 120, factorial(5),"5! should be 120"
  end

  def test_large
    assert_equal 3628800, factorial(10),"10! should be 3628800"
  end
end
