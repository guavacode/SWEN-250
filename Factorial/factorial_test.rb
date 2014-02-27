require_relative 'factorial' #We need to access our code to test
require 'test/unit'          #We need Ruby's unit testing library

class FactorialTest < Test::Unit::TestCase #This is a class. (It's ok if you don't know what those are yet)

  #Test methods MUST start with test_
  def test_normal
    assert_equal 24, factorial(4),"4! should be 24"
  end

  # Test for 5!
  def test_another_normal
    assert_equal 120, factorial(5),"5! should be 120"
  end

  # Test for 0!
  def test_zero
    assert_equal 1, factorial(0),"0! should be 1"
  end

  # Test for negative number -1!
  def test_negative
    assert_raise ArgumentError do   # We expect an exception to be raised
      factorial(-1)
    end
  end
  
  # Test for a non-numeric parameter for factorial
  def test_strin
    assert_raise ArgumentError do   # We expect an exception to be raised
      factorial("ghgg")
    end
  end

end
