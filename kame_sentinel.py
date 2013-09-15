#!/usr/bin/env python
# encoding: utf-8
import math

kame_map = [
      [None] * 17,
      [None] + [chr(x) for x in range(ord('A'),ord('L'))] + [None],
      [None] + [chr(x) for x in range(ord('L'),ord('W'))] + [None],
      [None] + ['W','X','Y','Z','a','b','c','d','e','f','g'] + [None],
      [None] + ['h','i','j'] + [None] * 5 + ['7','6','5'] + [None],
      [None] + ['k','l','m'] + [None] * 5 + ['4','3','2'] + [None],
      [None] + ['n','o','p'] + [None] * 5 + ['1','0','z'] + [None],
      [None] + ['q','r','s'] + [None] * 5 + ['y','x','w'] + [None],
      [None] + ['t','u','v'] + [None] * 5 + ['v','u','t'] + [None],
      [None] + ['w','x','y'] + [None] * 5 + ['s','r','q'] + [None],
      [None] + ['z','0','1'] + [None] * 5 + ['p','o','n'] + [None],
      [None] + ['2','3','4'] + [None] * 5 + ['m','l','k'] + [None],
      [None] + ['5','6','7'] + [None] * 5 + ['j','i','h'] + [None],
      [None] + ['g','f','e','d','c','b','a','Z','Y','X','W'] + [None],
      [None] + [chr(x) for x in range(ord('V'),ord('K'), -1)] + [None],
      [None] + [chr(x) for x in range(ord('K'),ord('@'), -1)] + [None],
      [None] * 17
      ]

class Kame(object):

   def __init__(self):
      self.x = 0
      self.y = 1
      self.angle = 0

   def execute(self, commands):
      """
      コマンドを一つずつ実行する
      """

      result = []
      for c in '1'+commands:
         if c == 'L':
            self.L()
         elif c == 'R':
            self.R()
         else:
            i = int(c, 16)
            result += self.forward(i)
            if '?' in result:
               break

      return "".join(result)

   def forward(self, i):
      result = []
      
      for num in range(0, i):
         self.x += int(round(math.cos(math.radians(self.angle))))
         self.y += int(round(math.sin(math.radians(self.angle))))
         if kame_map[self.y][self.x] is None:
            result.append('?')
            break

         result.append(kame_map[self.y][self.x])

      return result

   def L(self):
      self.angle -= 90

   def R(self):
      self.angle += 90

def test(commands, answer):
   kame = Kame()
   print(commands)
   result = kame.execute(commands)

   if result == answer:
      print(answer + " OK")
   else:
      print(answer + ' ' + result + ' NG')


if __name__ == "__main__":
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

