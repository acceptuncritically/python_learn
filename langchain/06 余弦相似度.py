import math
def get_dot(var_a, var_b):
    """
    计算相同长度的两个向量的数量积
    :param var_a: a向量
    :param var_b: b向量
    :return:
    """
    if len(var_a) != len(var_b):
        raise ValueError
    dot_sum=0
    for a,b in zip(var_a,var_b):
        #zip 是将两个向量按照一个一个插入重新排成适合向量乘积的形式
        #zip([1,2,3][4,5,6])---> [(1,4),(2,5),(3,6)]
        dot_sum+=a*b
    return dot_sum
def get_norm(var):
    """
    计算一个向量的模
    :param var: 传入的向量
    :return: 模
    """
    sum=0
    for v in var:
        sum+=v**2
    return math.sqrt(sum)
def cos(var_a, var_b):
    """
    计算余弦相似度
    :param var_a:
    :param var_b:
    :return:
    """
    result=get_dot(var_a, var_b)/(get_norm(var_a)*get_norm(var_b))
    return result
if __name__ == '__main__':
    var_a=[1,2,3,4,5,6]
    var_b=[1,2,3,5,4,6]
    cos(var_a, var_b)