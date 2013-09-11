#!/usr/bin/env ruby
# encoding: utf-8
#
# 道なりの亀（番兵使用）
#


$map = [
  [nil] * 17,
  [nil] + %w(A B C D E F G H I J K) + [nil],
  [nil] + %w(L M N O P Q R S T U V) + [nil],
  [nil] + %w(W X Y Z a b c d e f g) + [nil],
  [nil] + %w(h i j ) + ([nil] * 5) + %w(7 6 5) + [nil],
  [nil] + %w(k l m ) + ([nil] * 5) + %w(4 3 2) + [nil],
  [nil] + %w(n o p ) + ([nil] * 5) + %w(1 0 z) + [nil],
  [nil] + %w(q r s ) + ([nil] * 5) + %w(y x w) + [nil],
  [nil] + %w(t u v ) + ([nil] * 5) + %w(v u t) + [nil],
  [nil] + %w(w x y ) + ([nil] * 5) + %w(s r q) + [nil],
  [nil] + %w(z 0 1 ) + ([nil] * 5) + %w(p o n) + [nil],
  [nil] + %w(2 3 4 ) + ([nil] * 5) + %w(m l k) + [nil],
  [nil] + %w(5 6 7 ) + ([nil] * 5) + %w(j i h) + [nil],
  [nil] + %w(g f e d c b a Z Y X W) + [nil],
  [nil] + %w(V U T S R Q P O N M L) + [nil],
  [nil] + %w(K J I H G F E D C B A) + [nil],
  [nil] * 17
]

class Kame

  def initialize
    @x = 1
    @y = 1
    @rad = 0.0
    @once = true
  end 

  def execute(command)
    return '' if $map[@y][@x].nil?

    case command
    when /[1-9a-f]/
      i = command.to_i(16)
      forward(i)
    when 'R'
      R()
    when 'L'
      L()
    else
      raise 'Invalid command'
    end
  end

  def forward(i)
    result = @once ? [$map[@y][@x]] : []
    @once = false

    i.times do |index|
      @x += Math.cos(@rad).round
      @y += Math.sin(@rad).round
      if $map[@y][@x].nil?
        result.push '?'
        return result.join('')
      end
      result.push $map[@y][@x] 
    end
    
    result.join('')
  end

  def L
    @rad -= Math::PI/2    
    return ''
  end

  def R
    @rad += Math::PI/2    
    return ''
  end
end


def test(test, answer)
  kame = Kame.new

  commands = test
  result = ''
  commands.split(//).each do |command|
    result += kame.execute(command)
  end

  if answer == result 
    puts "#{answer} OK!"
  else
    puts "#{answer} #{result} NG"
  end
end

test( "2RcL3LL22", "ABCNYjmpsvy147edcbcdef" )
test( "L3R4L5RR5R3L5", "A?" )
test( "2ReLLe", "ABCNYjmpsvy147eTITe741yvspmjYNC" )
test( "1ReRRe", "ABMXilorux036fUJUf630xuroliXMB" )
test( "ReRRe", "ALWhknqtwz25gVKVg52zwtqnkhWLA" )
test( "f", "ABCDEFGHIJK?" )
test( "Rf", "ALWhknqtwz25gVK?" )
test( "1Rf", "ABMXilorux036fUJ?" )
test( "2Rf", "ABCNYjmpsvy147eTI?" )
test( "aR1RaL1LaR1R2L1L2", "ABCDEFGHIJKVUTSRQPONMLWXYZabcdefg567432" )
test( "2R1R2L1L2R1R2L1L2R1R2L1L2R1R2L1L2", "ABCNMLWXYjihklmponqrsvutwxy" )
test( "2R4R2L4L2R4R2L4L2R4R2L4L2", "ABCNYjmlknqtwxy147efgVK?" )
test( "R1L2R4R2L4L2R4R2L4L2R4R2L4L2", "ALMNYjmponqtwz0147eTUVK?" )
test( "R2L2R4R2L4L2R4R2L4L2R4R2L4L2", "ALWXYjmpsrqtwz2347eTIJK?" )
test( "R3L2R4R2L4L2R4R2L4L2R4R2L4L2", "ALWhijmpsvutwz2567eTI?" )
test( "R5L2L5L1LaR1L4L5", "ALWhknopmjYNCBMXilorux0325gVKJIHGF" )
test( "1R2L4L2R4R2L4L2R4", "ABMXYZabQFGHIJUfg?" )
test( "2R2L4L2R4R2L4L2R4", "ABCNYZabcRGHIJKVg?" )
test( "3R2L4L2R4R2L4L2R4", "ABCDOZabcdSHIJK?" )
test( "4R2L4L2R4R2L4L2R4", "ABCDEPabcdeTIJK?" )
test( "5R2L4L2R4R2L4L2R4", "ABCDEFQbcdefUJK?" )
test( "LLL1RRR1LLL1RRR2R1", "ALMXYZ?" )
test( "R3RRR3", "ALWhij?" )
test( "1LLL4RRR1LR1RL1", "ABMXilm?" )
test( "R2L1R2L1R3R4", "ALWXilmpsvut?" )
test( "7R4f47LLLc6R9L", "ABCDEFGHSd?" )
test( "5RR868L8448LL4R6", "ABCDEFEDCBA?" )
test( "42Rd1RLLa7L5", "ABCDEFGRc?" )
test( "RRLL6RLR1L5d12LaLRRL529L", "ABCDEFGRSTUV?" )
test( "RLR7L6LL1LRRRcRL52R", "ALWhknqtuv?" )
test( "1RLR8RLR1R437L99636R", "ABMXiloruxwtqnkhWLA?" )
test( "LLL2L3La9Le5LRR", "ALWXYZOD?" )
test( "R1LcRR491", "ALMNOPQRSTUV?" )
test( "R8L1R1R512L8RLLReRf", "ALWhknqtwx0z?" )
test( "1RcL8f1L29a5", "ABMXilorux036fedcbaZYXW?" )
test( "R822LeL46LL39LL", "ALWhknqtwz25gfedcbaZYXW?" )
test( "9R3L5LRRLb5R3L7cLLLR4L", "ABCDEFGHIJUf65?" )
test( "7LLRRR2R3R69Lf76eR2L", "ABCDEFGHSdcbaPE?" )
test( "8RRRLL3Le", "ABCDEFGHITe765?" )
test( "8R5RLL6LbL4LL5bL", "ABCDEFGHITe7410z?" )
test( "6LR2R1LR5LRLRL484L63", "ABCDEFGHITe741yxw?" )

