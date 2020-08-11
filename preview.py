# %%
### 【法一】调用scipy库解决线性规划问题
### 电气1807 张从佳 U201811816
from scipy import optimize
import numpy as np

obj = np.array([5.24 ,7.30 ,8.34 ,4.18])
constraints_A = np.array([[1.5 ,1.0 ,2.4 ,1.0],[1.0 ,5.0 ,1.0 ,3.5],[1.5 ,3.0 ,3.5 ,1.0]])
constraints_b = np.array([2000 ,8000 ,5000])
x1_bound = x2_bound = x3_bound = x4_bound = (0 ,None)

result = optimize.linprog(-obj,A_ub=constraints_A,b_ub=constraints_b,bounds=(x1_bound,x2_bound,x3_bound,x4_bound))
print(result)

# %%
### 【法二】调用pulp库解决线性规划问题
### 电气1807 张从佳 U201811816
# pip install pulp
from pulp import *

prob = LpProblem('problem1',LpMaximize)
x1 = LpVariable('x1',0,None,LpContinuous)
x2 = LpVariable('x2',0,None,LpContinuous)
x3 = LpVariable('x3',0,None,LpContinuous)
x4 = LpVariable('x4',0,None,LpContinuous)
prob += 5.24*x1 + 7.30*x2 + 8.34*x3 + 4.18*x4  # 目标函数
prob += 1.5*x1 + 1.0*x2 + 2.4*x3 + 1.0*x4 <= 2000  # 约束条件
prob += 1.0*x1 + 5.0*x2 + 1.0*x3 + 3.5*x4 <= 8000
prob += 1.5*x1 + 3.0*x2 + 3.5*x3 + 1.0*x4 <= 5000

prob.writeLP('probelm1.lp') # 将问题写进文件
prob.solve()
print('\n','status:',LpStatus[prob.status],'\n')  # 求解状态
for v in prob.variables():  # 生产计划
    print('\t',v.name,'=',v.varValue,'\n')
print('Maximun =',value(prob.objective))  # 最大利润

# %%
### 【法三】调用pulp库解决线性规划问题（改进）
### 电气1807 张从佳 U201811816
from pulp import *

keys = {'x1','x2','x3','x4'}
obj = {'x1':5.24,'x2':7.30,'x3':8.34,'x4':4.18}
constraints1 = {'x1':1.5,'x2':1.0,'x3':2.4,'x4':1.0}
constraints2 = {'x1':1.0,'x2':5.0,'x3':1.0,'x4':3.5}
constraints3 = {'x1':1.5,'x2':3.0,'x3':3.5,'x4':1.0}
constraints_b = (2000 ,8000 ,5000)

prob = LpProblem('problem2',LpMaximize)
var = LpVariable.dicts('key',keys,0,None,LpContinuous)  # 决策变量
prob += lpSum([obj[i]*var[i] for i in keys])  # 目标函数
prob += lpSum([constraints1[i]*var[i] for i in keys]) <= constraints_b[0]  # 约束条件
prob += lpSum([constraints2[i]*var[i] for i in keys]) <= constraints_b[1]
prob += lpSum([constraints3[i]*var[i] for i in keys]) <= constraints_b[2]

prob.writeLP('problem2.lp')  # 将问题写进文件
prob.solve()
print('\n','status:',LpStatus[prob.status],'\n')  # 求解状态
for v in prob.variables():  # 生产计划
    print('\t',v.name,'=',v.varValue,'\n')
print('Maximun =',value(prob.objective))  # 最大利润
