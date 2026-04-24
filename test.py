import os

# cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
# data_path = os.path.join(cur_dir, 'data/medical.json')
#
# print(os.path.abspath(__file__))
# print(os.path.abspath(__file__).split('/'))
# print(os.path.abspath(__file__).split('/')[:-1])
# print(data_path)
# print(cur_dir)

# class QuestionClassifier:
#     def __init__(self):
#         cur_dir = './'
#         #　特征词路径
#         self.disease_path = os.path.join(cur_dir, 'dict/disease.txt')
#         self.department_path = os.path.join(cur_dir, 'dict/department.txt')
#         self.check_path = os.path.join(cur_dir, 'dict/check.txt')
#         self.drug_path = os.path.join(cur_dir, 'dict/drug.txt')
#         self.food_path = os.path.join(cur_dir, 'dict/food.txt')
#         self.producer_path = os.path.join(cur_dir, 'dict/producer.txt')
#         self.symptom_path = os.path.join(cur_dir, 'dict/symptom.txt')
#         self.deny_path = os.path.join(cur_dir, 'dict/deny.txt')
#         # 加载特征词
#         self.disease_wds= [i.strip() for i in open(self.disease_path,encoding='utf-8') if i.strip()]
#         self.department_wds= [i.strip() for i in open(self.department_path,encoding='utf-8') if i.strip()]
#         self.check_wds= [i.strip() for i in open(self.check_path,encoding='utf-8') if i.strip()]
#         self.drug_wds= [i.strip() for i in open(self.drug_path,encoding='utf-8') if i.strip()]
#         self.food_wds= [i.strip() for i in open(self.food_path,encoding='utf-8') if i.strip()]
#         self.producer_wds= [i.strip() for i in open(self.producer_path,encoding='utf-8') if i.strip()]
#         self.symptom_wds= [i.strip() for i in open(self.symptom_path,encoding='utf-8') if i.strip()]
#         self.region_words = set(self.department_wds + self.disease_wds + self.check_wds + self.drug_wds + self.food_wds + self.producer_wds + self.symptom_wds)
#
#
# question = QuestionClassifier()
# print(question.region_words)

i = [(1, (21640, '感冒'))]

print(i[0][1][1])

args = {'感冒': ['disease']}

for arg, types in args.items():
    print( arg, types)