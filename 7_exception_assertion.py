# -*- coding: utf-8 -*-

#%%
test = [1, 2, 3]
test[3]

#%% 7.1 例外の処理　

# 未処理例外 
#%% try-except
try:
    numSuccesses = 1
    numFailures = 0
    successFailureRatio = numSuccesses / float(numFailures)
    print 'The success / failure ratio is ', successFailureRatio
except ZeroDivisionError:
    print 'No failures sor the success/failure ratio is undefined.'
print 'Now here'

#%% 指練習
def sumDigits(s):
    """sを文字列とする.
       sの中の数字の合計を返す.
       例えば, sが'a2b3c'ならば5を返す"""
    
    sum = 0
    for v in s:
        try:
            sum += int(v)
        except ValueError:
            sum
    
    return sum

sumDigits('123')
sumDigits('a2b3c')
    
#%% 多相的

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg + ' ')
        try:
            val = valType(val)
            return val
        except ValueError:
            print val, errorMsg
    
readVal(int, 'Enter an integer:', 'is not an integer')

# 未処理例外が起こったときにプログラムが止まるのは良いこと
# 顕在的なバグ

#%% 複数の例外の処理 

try:
    raise ValueError
    raise TypeError
except (ValueError, TypeError):
    print 'error'
except: # すべての例外をキャッチ
    
#%% 7.2 フロー制御機構としての例外 
#%% raise文
raise ValueError('hoge')
#%%　指練習 
def findAnEven(I):
    """ Iをint型の要素を持つリストとする。
        Iに最初に現れる偶数を返す
        Iが偶数を含まなければValueErrorを引き起こす"""
    for i in I:
        if(i % 2 == 0):
            return i
    
    raise ValueError('No even value.')
    
findAnEven([1])
findAnEven([2])

#%% getRatios 
def getRatios(vect1, vect2):
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

getRatios([1.0, 2.0, 7., 6.], [1., 2., 0., 3.])
getRatios([], [])
getRatios([1., 2.], [3.])
getRatios([1], [2, 3])

#%% 7.3 アサーション

assert False
assert False, 'message'