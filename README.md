# water-Capacity
破解倒水解谜游戏的算法

执行方式：命令行执行
./water.py args


参数格式如下：

args[1]		瓶子个数n

args[2, 2+n)	每个瓶子的最大容量

args[2+n, last]	倒水目标：每两个一组，将x升水装入容量为y的瓶子中


如：./water.py 3 8 34 3 2 8 1 34


表示：

  一共有3个瓶子，容量分别为8,34,3

  需要将2倒入容量为8的瓶子，并把1倒入容量为34的瓶子


生成结果：

  可生成所有步骤，以及每个步骤的结果
  每个步骤的结果都是用最少步数的
