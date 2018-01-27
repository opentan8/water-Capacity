# water-Capacity
破解倒水解谜游戏的算法

编写语言：python3

./water.py 

修改__init__中的前三行数据定义：

    water_capacity: (当前容量, 最大容量), .....
    expects: [(第n个瓶子, 期待容量), .....]   其中n从0开始，与water_capacity对应。
    limits: [0, 1, ...]   选中的瓶子不可以移动

生成结果：
  可生成所有步骤，以及每个步骤的结果;
  每个步骤的结果都是用最少步数的。
