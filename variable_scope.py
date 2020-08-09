a = 5
def f():
  a = 2
  def x():
    nonlocal a
    a = a+1
    print("local a:",a)
  x()
  print("enclosing a:",a)
print("a before function execution:",a)
f()
print("a after function execution:",a)