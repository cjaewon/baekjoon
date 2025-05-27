import re
import sys

input = lambda: sys.stdin.readline() #.rstrip()

class BrainkfuckInterpreter:
  bytes_arr: list[int]
  pointer: int
  code: str
  code_idx: int
  bracket_pair_idx: dict[int, int]

  def __init__(self, code: str):
    self.bytes_arr = [0 for _ in range(32768)]
    self.pointer = 0
    self.code = code
    self.code_idx = 0
    self.bracket_pair_idx = {}

    self.remove_comment()
    self.init_bracket()

  def remove_comment(self):
    pattern = re.compile(r"%[^\r\n]*")
    self.code = re.sub(pattern, "", self.code)

  def init_bracket(self):
    stack = []

    for i in range(len(self.code)):
      if self.code[i] == "[":
        stack.append(i)
      elif self.code[i] == "]":
        if not stack:
          raise RuntimeError("COMPILE ERROR")
        
        open_idx = stack.pop()

        self.bracket_pair_idx[open_idx] = i
        self.bracket_pair_idx[i] = open_idx

    if len(stack) > 0:
      raise RuntimeError("COMPILE ERROR")

  def run(self):
    i = 0

    while i < len(self.code):
      match self.code[i]:
        case ">":
          self.right_oper()
        case "<":
          self.left_oper()
        case "+":
          self.inc_oper()
        case "-":
          self.dec_oper()
        case ".":
          self.print_ascii()
        case "[":
          i = self.open_bracket(i)
        case "]":
          i = self.close_bracket(i)

      i += 1

  def left_oper(self):
    if self.pointer == 0:
      self.pointer = 32767
    else:
      self.pointer -= 1

  def right_oper(self):
    if self.pointer == 32767:
      self.pointer = 0
    else:
      self.pointer += 1

  def inc_oper(self):
    if self.bytes_arr[self.pointer] == 255:
      self.bytes_arr[self.pointer] = 0
    else:
      self.bytes_arr[self.pointer] += 1

  def dec_oper(self):
    if self.bytes_arr[self.pointer] == 0:
      self.bytes_arr[self.pointer] = 255
    else:
      self.bytes_arr[self.pointer] -= 1
  
  def print_ascii(self):
    print(chr(self.bytes_arr[self.pointer]), end="")

  def open_bracket(self, i):
    if self.bytes_arr[self.pointer] == 0:
      return self.bracket_pair_idx[i]
  
    return i

  def close_bracket(self, i):
    if self.bytes_arr[self.pointer] != 0:
      return self.bracket_pair_idx[i]
    
    return i

for i in range(int(input())):
  code = ""

  while (line := input()) != "end\n":
    code += line
  
  print(f"PROGRAM #{i + 1}:")

  try:
    interpreter = BrainkfuckInterpreter(code)

    interpreter.run()

    print()
  except RuntimeError as e:
    print(e)
