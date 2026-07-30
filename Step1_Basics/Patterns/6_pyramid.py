def triangle7(n):
    for i in range(n):
        print("  "*(n-i)+"* "*(2*i+1))

triangle7(4)

"""
4
        * 
      * * * 
    * * * * *
  * * * * * * *
"""