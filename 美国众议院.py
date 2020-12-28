import pandas as pd
import numpy as np
import operator
from efficient_apriori import apriori
#读取数据
data = pd.read_csv("voting-records.csv",header=None)
#得到频繁项集及关联规则
itemsets, rules = apriori(data.values.tolist(), min_support=0.5,  min_confidence=0.9,max_length=10)
#分别根据置信度、支持度、提升度对规则进行排序
confidence = dict()
support = dict()
lift = dict()
for rule in rules:
    confidence[rule] = rule.confidence
    support[rule] = rule.support
    lift[(rule)] = rule.lift
    #rule.lhs,rule.rhs可用作提取规则的前件、后件
rules_sortbycon = sorted(confidence.items(),key=operator.itemgetter(1),reverse = True)
rules_sortbysup = sorted(support.items(),key=operator.itemgetter(1),reverse = True)
rules_sortbylift = sorted(lift.items(),key=operator.itemgetter(1),reverse = True)
print(rules_sortbycon)