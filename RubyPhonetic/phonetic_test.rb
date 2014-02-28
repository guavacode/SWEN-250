require_relative 'phonetic'
require 'test/unit'

class PhoneticTest < Test::Unit::TestCase

  def test_rit_to_phonetic
    assert_equal 'ROMEO INDIA TANGO', to_phonetic('RIT')
  end

  def test_line_rit_to_phonetic
    assert_equal 'ROMEO INDIA TANGO', translate('A2P RIT')
  end

  def test_phonetic_to_rit
    assert_equal 'RIT', from_phonetic('ROMEO INDIA TANGO')
  end

  def test_line_phonetic_to_rit
    assert_equal 'RIT', translate('P2A ROMEO INDIA TANGO')
  end
end
