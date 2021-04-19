if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    arr = student_marks[query_name]
    ans = 0
    
    for i in range(len(arr)):
        ans += arr[i]
    
    a = ans / 3
    print('%.2f' %a)