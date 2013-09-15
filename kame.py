#!/usr/bin/env python
# encoding: utf-8


class Kame(object):
   """
   道なりの亀
   """

   class Node(object):
      """
      各文字が入るノード
      ノードはそれぞれ上下左右の枝を持つ
      """

      def __init__(self, value):
         """
         nodeのコンストラクタ
         """
         self.value = value
         self.top = None   
         self.bottom = None
         self.right = None
         self.left  = None

      def set_nodes(self, top=None, bottom=None, right=None, left=None):
         """
         上下左右のnodeを設定する
         """
         self.top = top
         self.bottom = bottom
         self.right = right
         self.left = left

      def next_node(self, num):
         """
         次に進むnodeを取得する
         """
         # PythonにSwith case文なんてモノはない
         if num == 0 or num == -4:
            return self.right
         elif num == 1 or num == -3:
            return self.bottom
         elif num == 2 or num == -2:
            return self.left
         elif num == 3 or num == -1:
            return self.top
         else:
            raise ValueError('無効な値')

      @staticmethod
      def make_nodes():
         """
         今回問題となる地図を作成する
         """
         data1 = [Kame.Node(x) for x in "ABCDEFGHIJK"]
         data2 = [Kame.Node(x) for x in "LMNOPQRSTUV"]
         data3 = [Kame.Node(x) for x in "WXYZabcdefg"]
         data4 = [Kame.Node(x) for x in "hij"]
         data5 = [Kame.Node(x) for x in "klm"]
         data6 = [Kame.Node(x) for x in "nop"]
         data7 = [Kame.Node(x) for x in "qrs"]
         data8 = [Kame.Node(x) for x in "tuv"]
         data9 = [Kame.Node(x) for x in "wxy"]
         data10 = [Kame.Node(x) for x in "z01"]
         data11 = [Kame.Node(x) for x in "234"]
         data12 = [Kame.Node(x) for x in "567"]
         
         for i in range(0, len(data1)):
            left  = None if i == 0 else data1[i-1]
            right = None if (i+1) == len(data1) else data1[i+1]
            data1[i].set_nodes(left=left, bottom=data2[i], right=right)

         for i in range(0, len(data2)):
            left = None if i == 0 else data2[i-1]
            right = None if (i+1) == len(data2) else data2[i+1]
            data2[i].set_nodes(top=data1[i], left=left, bottom=data3[i], right=right)

         for i in range(0, len(data3)):
            left = None if i == 0 else data3[i-1]
            right = None if (i+1) == len(data3) else data3[i+1]
            bottom = None
            if i in range(0, 3):
               bottom = data4[i]
            elif i in range(len(data3)-3, len(data3)):
               bottom = data12[len(data3)-i-1]

            data3[i].set_nodes(top=data2[i], left=left, bottom=bottom, right=right)

         for i in range(0, len(data4)):
            left = None if i == 0 else data4[i-1]
            right = None if (i+1) == len(data4) else data4[i+1]
            bottom = data5[i]
            top = data3[i]

            data4[i].set_nodes(top=top, left=left, bottom=bottom, right=right)
            
         for i in range(0, len(data5)):
            left = None if i == 0 else data5[i-1]
            right = None if (i+1) == len(data5) else data5[i+1]
            bottom = data6[i]
            top = data4[i]

            data5[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         for i in range(0, len(data6)):
            left = None if i == 0 else data6[i-1]
            right = None if (i+1) == len(data6) else data6[i+1]
            bottom = data7[i]
            top = data5[i]

            data6[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         for i in range(0, len(data7)):
            left = None if i == 0 else data7[i-1]
            right = None if (i+1) == len(data7) else data7[i+1]
            bottom = data8[i]
            top = data6[i]

            data7[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         for i in range(0, len(data8)):
            left = None if i == 0 else data8[i-1]
            right = None if (i+1) == len(data8) else data8[i+1]
            bottom = data9[i]
            top = data7[i]

            data8[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         for i in range(0, len(data9)):
            left = None if i == 0 else data9[i-1]
            right = None if (i+1) == len(data9) else data9[i+1]
            bottom = data10[i]
            top = data8[i]

            data9[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         for i in range(0, len(data10)):
            left = None if i == 0 else data10[i-1]
            right = None if (i+1) == len(data10) else data10[i+1]
            bottom = data11[i]
            top = data9[i]

            data10[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         for i in range(0, len(data11)):
            left = None if i == 0 else data11[i-1]
            right = None if (i+1) == len(data10) else data11[i+1]
            bottom = data12[i]
            top = data10[i]

            data11[i].set_nodes(top=top, left=left, bottom=bottom, right=right)
         
         for i in range(0, len(data12)):
            left = None if i == 0 else data12[i-1]
            right = None if (i+1) == len(data12) else data12[i+1]
            bottom = data3[len(data3)-1 - i]
            top = data11[i]

            data12[i].set_nodes(top=top, left=left, bottom=bottom, right=right)

         return data1[0]
  
   # Kame クラス
   def __init__(self):
      """
      コンストラクタ
      """
      self.now_node = Kame.Node.make_nodes()
      self.next_direction = 0

   def execute(self, commands):
      """
      コマンドを一つずつ実行する
      """

      result = [self.now_node.value]
      for c in commands:
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
      """
      i分だけ進む方向に前進する
      """
      result = []

      for num in range(0, i):
         prev_node = self.now_node
         self.now_node = self.now_node.next_node(self.next_direction)
         if self.now_node is None:
            result.append('?')
            break

         result.append(self.now_node.value)
         if self.__is_bottom_to_bottom(prev_node):
            # 移動前のnodeとbottomでつながっている場合は進む方向を反転する
            self.__turn()

      return result

   def R(self):
      """
      右に90度回転
      """
      self.next_direction += 1
      if self.next_direction is 4:
         self.next_direction = 0

      self.next_node = self.now_node.next_node(self.next_direction)

   def L(self):
      """
      左に90度回転
      """
      self.next_direction -= 1
      if self.next_direction is -5:
         self.next_direction = 3

      self.next_node = self.now_node.next_node(self.next_direction)

   def __turn(self):
      """
      方向を現在の進行方向から反転する
      """
      self.L()
      self.L()

   def __is_bottom_to_bottom(self, prev_node):
      """
      bottomとbottomがつながっているnode間で移動があった場合trueを返す
      """
      return self.now_node is not None \
            and self.now_node.value in ['e','f','g','5','6','7'] \
            and self.now_node.bottom is prev_node

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


