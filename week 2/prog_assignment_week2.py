#______________________QUESTIONS__________________
# A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

# Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. (If m is not positive, your function should return False.)

# Here are some examples of how your function should work.

# >>> primepartition(7)
# True

# >>> primepartition(185)
# False

# >>> primepartition(3432)
# True
# Write a function nestingdepth(s) that takes as input a string s and computes the maximum nesting depth of brackets if s has properly nested brackets. If the string is not properly matched, your function should return -1.

# Hint: Use the function matched() from the practice assignment.

# Here are some examples to show how your function should work.

 
# >>> nestingdepth("zb%78")
# 0

# >>> nestingdepth("(7)(a")
# -1

# >>> nestingdepth("a)*(?")
# -1

# >>> nestingdepth("((jkl)78(A)&l(8(dd(FJI:),):)?)")
# 4
# A list rotation consists of taking the first element and moving it to the end. For instance, if we rotate the list [1,2,3,4,5], we get [2,3,4,5,1]. If we rotate it again, we get [3,4,5,1,2].

# Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k rotations. If k is not positive, your function should return l unchanged. Note that your function should not change l itself, and should return the rotated list.

# Here are some examples to show how your function should work.

# >>> rotatelist([1,2,3,4,5],1)
# [2, 3, 4, 5, 1]

# >>> rotatelist([1,2,3,4,5],3)
# [4, 5, 1, 2, 3]

# >>> rotatelist([1,2,3,4,5],12)
# [3, 4, 5, 1, 2]

#_________________________ANSWERS______________________
def isP(n):
    if n==2:
        return True
    if n%2==0:
        return False
    return all(n%x>0 for x in range(3, int(n**0.5)+1, 2))
 
def genP(n):
    p = [2]
    p.extend([x for x in range(3, n+1, 2) if isP(x)])
    return p
def primepartition(n):
    p = genP(n)
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if p[i]+p[j]==n:
                return True
    return False

def rotatelist(l,k):
  m=l[:]
  for i in range(k):
    t=m.pop(0)
    m.append(t)
    
  return((m))


def matched(s):
  c=0
  for i in s:
    if i == "(":
      c+=1
    elif i==")":
      if c==0:
        return False
      c-=1	      
  if(c==0):
    return True
  else:
    return False

