class Student(object):
    def __init__(self, line_array):
        self.id = line_array[0]
        self.name = line_array[1]
        self.sex = line_array[2]
        self.province = line_array[3]
        self.city = line_array[4]
        self.district = line_array[5]
        self.gaokao = line_array[6]
        self.sustech = line_array[7]
        self.gpa = line_array[8]
        self.plan = line_array[9]
        self.abroadCountry = line_array[10]
        self.abroadUniversity = line_array[11]
        self.abroadMajor = line_array[12]
        self.domesticUniversity = line_array[13]
        self.domesticMajor = line_array[14]
        self.workProvince = line_array[15]
        self.workCity = line_array[16]
        self.degree = line_array[17]
        self.firm = line_array[18]
        self.salary = line_array[19]


# 学生来源
def count_resident(students):
    # 列表存储所有的省市区
    pro = []
    city = []
    dist = []
    # 集合存储去重的省市区
    pro_set = set()
    city_set = set()
    dist_set = set()
    # 字典建立省市，市区关系
    p_c = {}
    c_d = {}
    for s in students:
        pro_set.add(s.province.replace('省', ''))
        city_set.add(s.city.replace('市', ''))
        dist_set.add(s.district.replace('区', ''))
        pro.append(s.province.replace('省', ''))
        city.append(s.city.replace('市', ''))
        dist.append(s.district.replace('区', ''))
    for p in pro_set:
        if p == '':
            continue
        p_c[p] = set()
    for c in city_set:
        if c == '':
            continue
        c_d[c] = set()
    for i in range(len(pro)):
        if pro[i] == '' or city[i] == '':
            continue
        p_c[pro[i]].add(city[i])
    for i in range(len(city)):
        if city[i] == '' or dist[i] == '':
            continue
        c_d[city[i]].add(dist[i])
    for p in pro_set:
        if p == '':
            continue
        print("--{}-- ({})".format(p, pro.count(p)))
        for c in p_c[p]:
            print("------{}-- ({})".format(c, city.count(c)))
            for d in c_d[c]:
                print("----------{}-- ({})".format(d, dist.count(d)))


# 毕业去向
def count_plan(students):
    plans = []
    for s in students:
        plans.append(s.plan)
    x = plans.count('出国深造')
    y = plans.count('国内读研')
    z = plans.count('毕业工作')
    print(x, y, z)


# 国外留学及回国年份
def count_abroad(students):
    nat = set()
    uni = set()
    for s in students:
        nat.add(s.abroadCountry)
        uni.add(s.abroadUniversity)