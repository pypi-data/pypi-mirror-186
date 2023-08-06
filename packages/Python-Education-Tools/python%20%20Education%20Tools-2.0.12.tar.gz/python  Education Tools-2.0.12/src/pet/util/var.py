import pandas as pd

# 获取上海市地铁线路数据字典
def get_subway_lines_dict(filename='subway.xlsx'):
    df=pd.read_excel(filename)
    cls=df.columns
    k={c:df[c].dropna().values.tolist() for c in cls}

    return k




from random import shuffle


# 按要求生成n副扑克牌，每副牌有54张，然后洗牌
def gen_poker(shuffled=True, n=1):
    number = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
    kind = ['黑桃', '红桃', '梅花', '方块']
    pk = [j + '-' + i for i in number for j in kind] + ['King', 'Queen']
    pk = pk * n
    if shuffled: shuffle(pk)
    return pk

if __name__ == '__main__':
    d=get_subway_lines_dict()
    print(d.keys())
    print(d)

    t=gen_poker(shuffled=True, n=3)
    print(t)