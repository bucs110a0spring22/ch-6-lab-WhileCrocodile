import turtle

def seq3np1(n):
  """
  Print the 3n+1 sequence from n, terminating when it reaches 1.
  args: n (int) starting value for 3n+1 sequence
  return: None
  """
  count = 0
  while(n != 1):
    count += 1
    if(n % 2) == 0:        # n is even
      n = n // 2
    else:                 # n is odd
      n = n * 3 + 1
  return count

def seqgraph(upper_bound):
  graphpen = turtle.Turtle()
  writerpen = turtle.Turtle()
  xpen = turtle.Turtle()
  ypen = turtle.Turtle()
  wn = turtle.Screen()
  
  wn.setworldcoordinates(llx=0, lly=0, urx=10, ury=10)
  max_so_far = 0
  ypen.left(90)
  writerpen.left(90)
  
  for start in range(1, upper_bound+1):
    result = seq3np1(start)
    if result > max_so_far:
      max_so_far = result
    wn.setworldcoordinates(llx=0, lly=0, urx=start+10, ury=max_so_far+10)
    xpen.goto(start+10, 0)
    ypen.goto(0, max_so_far)
    writerpen.clear()
    writerpen.goto(0, max_so_far)
    label = "Maximum so far: " + str(start) + " " + str(max_so_far)
    writerpen.write(label)
    graphpen.goto(start, result)
  wn.exitonclick()

def main():
  upper_bound = int(input("Choose an upper bound: "))
  if upper_bound > 0:
    print("start", "\t", "iterations")
    for start in range(1, upper_bound+1):
      print(start, "\t\t", seq3np1(start))
    for start in range(1, upper_bound+1):
      seqgraph(upper_bound)  
  else:
    print("Upper bound was not a positive integer. Ending program.")
  

main()
