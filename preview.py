# %%
### 【法一】一个线性规划问题的求解
### 电气1807 张从佳 U201811816
# 调用scipy库解决
from scipy import optimize
import numpy as np

# 目标函数系数
z = np.array([5.24,7.30 ,8.34 ,4.18])

# 约束条件Ax<=b 系数A
a = np.array([[1.5 ,1.0 ,2.4 ,1.0],[1.0 ,5.0 ,1.0 ,3.5],[1.5 ,3.0 ,3.5 ,1.0]])

# 约束条件Ax<=b 系数b
b = np.array([2000 ,8000 ,5000])

# 决策变量取值范围
x1_bound = x2_bound = x3_bound = x4_bound = (0,None)

# 求解
res = optimize.linprog(-z,A_ub=a,b_ub=b,bounds=(x1_bound,x2_bound,x3_bound,x4_bound))

# 显示结果
print(res)

# %%
### 【法二】一个线性规划问题的求解
### 电气1807 张从佳 U201811816
# pip install pulp
# 调用pulp库
from pulp import *

# 定义求解的问题
prob = LpProblem('problem1',LpMaximize)

# 定义决策变量，连续型，范围从0到正无穷
x1 = LpVariable('x1',0,None,LpContinuous)
x2 = LpVariable('x2',0,None,LpContinuous)
x3 = LpVariable('x3',0,None,LpContinuous)
x4 = LpVariable('x4',0,None,LpContinuous)

# 定义目标函数
prob += 5.24*x1 + 7.30*x2 + 8.34*x3 + 4.18*x4

# 定义约束条件
prob += 1.5*x1 + 1.0*x2 + 2.4*x3 + 1.0*x4 <= 2000
prob += 1.0*x1 + 5.0*x2 + 1.0*x3 + 3.5*x4 <= 8000
prob += 1.5*x1 + 3.0*x2 + 3.5*x3 + 1.0*x4 <= 5000

# 将问题写进文件
# prob.writeLP('probelm1.lp')
# 求解
prob.solve()

## 显示结果
# 显示求解状态
print('\n','status:',LpStatus[prob.status],'\n')

# 显示各个决策变量取值
for v in prob.variables():
    print('\t',v.name,'=',v.varValue,'\n')

# 显示目标函数最大值
print('Maximun =',value(prob.objective))

# %%
### 【法三】一个线性规划问题的求解
### 电气1807 张从佳 U201811816
### 运用字典的方法
# 调用pulp库
from pulp import *

# 将相应的系数写入字典
keys = {'x1','x2','x3','x4'}
obj = {
    'x1':5.24,
    'x2':7.30,
    'x3':8.34,
    'x4':4.18
}
M1 = {
    'x1':1.5,
    'x2':1.0,
    'x3':2.4,
    'x4':1.0
}
M2 = {
    'x1':1.0,
    'x2':5.0,
    'x3':1.0,
    'x4':3.5
}
M3 = {
    'x1':1.5,
    'x2':3.0,
    'x3':3.5,
    'x4':1.0
}

# 定义求解的问题
prob = LpProblem('problem2',LpMaximize)

# 定义决策变量，连续型，范围从0到正无穷
var = LpVariable.dicts('key',keys,0,None,LpContinuous)

# 定义目标函数
prob += lpSum([obj[i]*var[i] for i in keys])

# 定义约束条件
prob += lpSum([M1[i]*var[i] for i in keys]) <= 2000
prob += lpSum([M2[i]*var[i] for i in keys]) <= 8000
prob += lpSum([M3[i]*var[i] for i in keys]) <= 5000

# 将问题写进文件
# prob.writeLP('problem2.lp')
# 求解
prob.solve()

## 显示结果
# 显示求解状态
print('\n','status:',LpStatus[prob.status],'\n')

# 显示各个决策变量取值
for v in prob.variables():
    print('\t',v.name,'=',v.varValue,'\n')

# 显示目标函数最大值
print('Maximun =',value(prob.objective))
