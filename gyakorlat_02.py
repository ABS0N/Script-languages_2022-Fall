#!/usr/bin/env python3

from re import A


def main():

#tobbsoros string
    html = """
<html>
<body>
<h1>Hello!</h1>
</body>
</html>
""".strip()
    print("'" + html + "'")

# raw string
    s = "py\nthon"
    print(len(s))
    s = r"py\nthon"
    print(len(s))

a = 5
++a #semmi 
--a #semmi
---a # -5
a += 1 # 6
a -= 1 # 5


##############################################

if __name__ == "__main__":
    main()