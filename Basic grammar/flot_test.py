"""
정수 배열 (배열 INT)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오.
단, 시간 복잡도는 O (N).
정수 배열을 감안할 때, 요소의 가장 큰 연속 합계를 찾을 수 있습니다.
예제}
입력 : [-1, 3, -1, 5]
출력 : 7 // 3 + (-1) + (5)
입력 : [-5, -3, -1]
출력 : -1 // -1
입력 : [2, 4, -2, -3, 8]
출력 : 9 // 2 + 4 + (-2) + (-3) + (8)

이 문제는 두 개의 정수 변수로 현재의 합(current sum)과
전체의 제일 큰 합(max sum)을 저장해야 합니다. 각 원소마다(currrent sum+원소)
값을 원소 값이랑 비교하고, 더 큰 값이 current sum이 됩니다. max sum은 current sum이
바뀔때마다 체크하여 제일 큰 값을 저장하면 됩니다.
"""

input_list = [-5, -3, -1,5,6,7,8,9,-5,20,-25,-5]
current_sum = input_list[0]
sum_log = [input_list[0]]
result = " "

''' 최댓값 찾고 저장하는 부분 '''
for i in range (1,len(input_list)) :
    if current_sum+input_list[i] < input_list[i] :
        current_sum = input_list[i] ##누적이 음의 값일 때 버리는 부분.
    else :
        current_sum += input_list[i]
    sum_log.append(current_sum)

    print("Current_sum : {0} sum_log : {1} ".format(current_sum, sum_log))

sum_log.append(current_sum) ##마지막 부분합 저장.

max_end = sum_log.index(max(sum_log))

print("Current_sum : {0} sum_log : {1} ".format(current_sum, sum_log))

