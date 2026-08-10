# # students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# # for i in students:
# #     print(i)

# if __name__ == '__main__':
#     a={}
#     scores=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         a[name]=score
#         scores.append(score)
#     scores.sort()
#     run=scores[1]
#     res=[]
#     for k,v in a.items():
#         if run==v:
#             res.append(k)
#     res.sort()
#     for i in res:
#         print(i)

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get unique scores and sort them
    scores = sorted(set(score for name, score in students))

    # Second lowest score
    second_lowest = scores[1]

    # Get names with the second lowest score
    names = sorted([name for name, score in students if score == second_lowest])

    # Print names
    for name in names:
        print(name)