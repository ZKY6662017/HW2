{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199\n"
     ]
    }
   ],
   "source": [
    "#Question 1\n",
    "for i in range(2000,3201):\n",
    " if i%7 == 0 and i%5 != 0:\n",
    "    print(i,end=',')\n",
    "print(\"\\b\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40320\n"
     ]
    }
   ],
   "source": [
    "#Queation 2\n",
    "n = int(input())\n",
    "fact = 1 \n",
    "i = 1 \n",
    "while i <= n: \n",
    "    fact = fact * i; \n",
    "    i = i + 1 \n",
    "print(fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n"
     ]
    }
   ],
   "source": [
    "#Question 3\n",
    "n = int(input())\n",
    "ans={i : i*i for i in range(1,n+1)}\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['34', '67', '55', '33', '12', '98']\n",
      "('34', '67', '55', '33', '12', '98')\n"
     ]
    }
   ],
   "source": [
    "#Question 4?????\n",
    "\n",
    "\n",
    "t = input()\n",
    "d = t.split(',')                 # split（）函数按照所给参数分割序列\n",
    "\n",
    "r = tuple(d)                     # 转换为元组类型\n",
    "print(d)\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ICAR\n"
     ]
    }
   ],
   "source": [
    "#Question 5\n",
    "class InputOutputString():      \n",
    "    def __init__(self):\n",
    "        self.s = ''\n",
    "\n",
    "    def __getString__(self):\n",
    "        self.s = input()\n",
    "\n",
    "    def __printString__(self):\n",
    "        print(self.s.upper())       \n",
    "\n",
    "\n",
    "stringRan = InputOutputString()\n",
    "stringRan.__getString__()\n",
    "stringRan.__printString__()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18,22,24\n"
     ]
    }
   ],
   "source": [
    "#Question 6\n",
    "import math\n",
    "C = 50\n",
    "H = 30\n",
    "value = []      \n",
    "t = input()\n",
    "x = [i for i in t.split(',')]\n",
    "\n",
    "for d in x:\n",
    "    value.append(str(round(math.sqrt((2 * C * float(d)) / H)))) \n",
    "\n",
    "print(','.join(value))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]\n"
     ]
    }
   ],
   "source": [
    "#Question 7\n",
    "input_str = input()\n",
    "dimensions=[int(x) for x in input_str.split(',')]\n",
    "rowNum=dimensions[0]\n",
    "colNum=dimensions[1]\n",
    "multilist = [[0 for col in range(colNum)] for row in range(rowNum)]\n",
    "\n",
    "for row in range(rowNum):\n",
    "    for col in range(colNum):\n",
    "        multilist[row][col]= row*col\n",
    "\n",
    "print(multilist)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bag,hello,without,world\n"
     ]
    }
   ],
   "source": [
    "#Question 8\n",
    "temp = input()\n",
    "inputStr = temp.split(',')             \n",
    "inputStr.sort()                        \n",
    "print(','.join(inputStr)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO WORLD PRACTICE MAKES PERFECT \n"
     ]
    }
   ],
   "source": [
    "#Question 9\n",
    "lines = []\n",
    "while True:\n",
    "    s = input()\n",
    "    if s:\n",
    "        lines.append(s.upper())\n",
    "    else:\n",
    "        break\n",
    "\n",
    "for sentence in lines:\n",
    "    print(sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " again and hello makes perfect practice world\n"
     ]
    }
   ],
   "source": [
    "#Question 10\n",
    "s = input()\n",
    "words = [word for word in s.split(\" \")]\n",
    "print(\" \".join(sorted(list(set(words)))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "person's name is Allen\n",
      "person's name is Mark\n"
     ]
    }
   ],
   "source": [
    "#Question 25\n",
    "class Exp1:\n",
    "    name = 'person\\'s'\n",
    "\n",
    "    def __init__(self, name=None):      \n",
    "        self.name = name\n",
    "\n",
    "\n",
    "alan = Exp1('Allen')\n",
    "print('%s name is %s' % (Exp1.name, alan.name))            \n",
    "\n",
    "mark = Exp1()                                               \n",
    "mark.name = 'Mark'\n",
    "print('%s name is %s' % (Exp1.name, mark.name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n",
      "9\n",
      "16\n",
      "25\n",
      "36\n",
      "49\n",
      "64\n",
      "81\n",
      "100\n",
      "121\n",
      "144\n",
      "169\n",
      "196\n",
      "225\n",
      "256\n",
      "289\n",
      "324\n",
      "361\n",
      "400\n"
     ]
    }
   ],
   "source": [
    "#Question 35\n",
    "\n",
    "def printDict():\n",
    "    d=dict()\n",
    "    for i in range(1,21):\n",
    "        d[i]=i**2\n",
    "        print(d[i])    \n",
    "\n",
    "printDict()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "#Question 36\n",
    "def printDict():\n",
    "\td=dict()\n",
    "\tfor i in range(1,21):\n",
    "\t\td[i]=i**2\n",
    "\t\n",
    "\t\tprint(i)\n",
    "\n",
    "printDict()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]\n"
     ]
    }
   ],
   "source": [
    "#Question 37\n",
    "def printList():\n",
    "\tlist=[i**2 for i in range(1,21)]\n",
    "\tprint(list)\n",
    "\n",
    "printList()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "#Question 43\n",
    "tp = (1,2,3,4,5,6,7,8,9,10)\n",
    "\n",
    "n = list()\n",
    "\n",
    "for x in tp:\n",
    "\tif x<=len(tp)-1:\n",
    "\t\tif tp[x]%2==0:\n",
    "\t\t\tn.append(tp[x])\n",
    "\n",
    "print(n)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.American object at 0x000002C8A5FB8F88>\n",
      "<__main__.NewYorker object at 0x000002C8A5FB8F48>\n"
     ]
    }
   ],
   "source": [
    "#Question 51\n",
    "class American():\n",
    "    pass\n",
    "\n",
    "class NewYorker(American):\n",
    "    pass\n",
    "\n",
    "american = American()\n",
    "newyorker = NewYorker()\n",
    "\n",
    "print(american)\n",
    "print(newyorker)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32\n"
     ]
    }
   ],
   "source": [
    "#Question 53\n",
    "class Rectangle():\n",
    "    def __init__(self,l,w):\n",
    "        self.length = l\n",
    "        self.width = w\n",
    "\n",
    "    def area(self):\n",
    "        return self.length*self.width\n",
    "\n",
    "\n",
    "rect = Rectangle(4,8)\n",
    "print(rect.area())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n"
     ]
    }
   ],
   "source": [
    "#Question 54\n",
    "\n",
    "class Shape():\n",
    "    def __init__(self):\n",
    "        pass\n",
    "\n",
    "    def area(self):\n",
    "        return 0\n",
    "\n",
    "class Square(Shape):\n",
    "    def __init__(self,length = 0):\n",
    "        Shape.__init__(self)\n",
    "        self.length = length\n",
    "\n",
    "    def area(self):\n",
    "        return self.length*self.length\n",
    "\n",
    "Asqr = Square(5)\n",
    "print(Asqr.area())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "division by zero!\n"
     ]
    }
   ],
   "source": [
    "#Question 56\n",
    "def divide():\n",
    "    return 5/0\n",
    "\n",
    "try:\n",
    "    divide()\n",
    "except ZeroDivisionError as ze:\n",
    "    print(\"division by zero!\")\n",
    "except:\n",
    "    print('Caught an exception')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12, 24, 35, 88, 120, 155]\n"
     ]
    }
   ],
   "source": [
    "#Question 94\n",
    "li = [12,24,35,24,88,120,155,88,120,155]\n",
    "n = list(set(li))\n",
    "n.sort()\n",
    "print(n)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7.4 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "7bdfec4e4745230aa72b6b3b9f6cf04179ed160966ad1f3d6706347769a5dbdb"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
