# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:31:55 2018

@author: naitik
"""

def FirstFactorial(num):
	num = int(num)
	if(num == 1):
		return 1
	if(num == 2):
		return 2
    # code goes here
	return num*FirstFactorial(num-1)

# keep this function call here
print(FirstFactorial(4))



def FirstReverse(str):
	lis = [i for i in str]
	rev=[]
	j = len(lis)-1
	for i in range(len(lis)):
		rev.append(lis[j])
		j = j-1
    # code goes here
	return str(rev)

def FirstReverse(s):
	ar = bytearray(s, 'utf8')
	ar.reverse()
	return str(ar)

# keep this function call here
print(FirstReverse("I Love Code"))


def LetterChanges(str):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    vowel='aeoiu'
    #new_l=""
    new = [letter[ord(x)%32] if x in letter else x for x in str]
    new1 =[i.upper() if i in vowel else i for i in new]
    # code goes here
    return ''.join(new1)

# keep this function call here
print(LetterChanges("hello*3"))

[letter[ord(x)%32] for x in str]

def SimpleAdding(num):
	num=int(num)
	# code goes here
	if num==0:
		return 0
	return num+SimpleAdding(num-1)

# keep this function call here
print(SimpleAdding("8"))

def SimpleSymbols(str):
    zz = len(str)
    print(zz)
    for i in range(len(str)):
        print(str[i])
        if str[i].isalpha():
            if (i-1<0 or i+1>zz-1):
                print(str[i-1],str[i],str[i+1])
                print(i)
                return 'false1'
            if str[i-1] !="+" or str[i+1] !="+":
                print(str[i-1],str[i],str[i+1])
                return 'false2'
    return 'true'

print(SimpleSymbols("+a="))



from datetime import datetime
d = datetime.now()
d.date()

d1="08-01-2018"
d1.to_datetime()
d1.date()

def TimeConvert(num):
    hour = num/60
    min = num%60
    # code goes here
    return str(round(hour))+':'+str(min)

# keep this function call here
print(TimeConvert(126))



def CheckNums(num1,num2):
    if num2>num1: return 'true'
    # code goes here
    return 'false'

# keep this function call here
print(CheckNums(1,2))


def QuestionsMarks(str):
	num = 0
	ques = 0
	start_cnt = False
	start=False
	for i,n in enumerate(str):
		print(n)
		if n.isdigit():
			num = num+int(n)
			if num==10:
				if ques != 3:
					return 'false1'
				else:
					num = int(n)
					ques=0
					print("num=",num,ques)
				start_cnt = True
				print(start_cnt)
			start=True
		if (n =='?' and start):
			ques += 1
	# code goes here
	return 'true' if start_cnt else 'false2'

print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))


# keep this function call here
print(QuestionsMarks("9???1???9??1???9"))



def check(i,j,strArr):
    vowel = 'aeiou'
    try:
	    for k in range(0,2):
	        for l in range(0,2):
	            if not (strArr[i+k][j+l] in vowel):
	                return False
    except:
	    return False
    return True


def VowelSquare(strArr):
    vowel = 'aeiou'
    for i,row in enumerate(strArr):
        for j,col in enumerate(row):
            if col in vowel:
                if(check(i,j,strArr)):
                    return str(i)+'-'+str(j)
    return "not found"

# keep this function call here
print(VowelSquare(["one","two","three"]))


def PentagonalNumber(num):
    if num == 1:
        return 1
    # code goes here
    return 5*(num-1)+PentagonalNumber(num-1)

# keep this function call here
print(PentagonalNumber(3))






def check_square(matrix,i,j,m,n):
	area = 1
	if i==m or j==n: return 1
	for k in


def MaximalSquare(strArr):
	m = len(strArr)-1
	for i,row in enumerate(strArr):
		n = len(row)-1
		for j,column in enumerate(row):
			if column == 0:
				continue
			area = check_square(strArr,i,j,m,n)

	return area if area else 1

# keep this function call here
print(MaximalSquare("0111", "1111", "1111", "1111"))

