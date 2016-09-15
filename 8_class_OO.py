# -*- coding: utf-8 -*-

#%% 第8章 クラスとオブジェクト指向プログラミング

#%% 8.1 抽象データ型とクラス 

#抽象データ型 

class IntSet(object):
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

print type(IntSet), type(IntSet.insert)
s = IntSet()