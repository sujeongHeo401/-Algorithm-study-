def solution(board, moves):
    answer = 0
    new_arr = [[] for _ in range(len(board))]
    box = []
    for i in board:
        for idx, value in enumerate(i):
            if value != 0:
                new_arr[idx].append(value)
            
    for ele in moves: 
        if ele - 1 < 0:
            return # wrong indx
        if len(new_arr[ele - 1]) != 0:
            curr_target = new_arr[ele - 1].pop(0) 
            if len(box) == 0: 
                box.append(curr_target)
            elif curr_target == box[-1]:
                box.pop(-1)
                answer += 2
            elif curr_target != box[-1]:
                box.append(curr_target)
                
    print("answer: ", answer)
    return answer
        
        
        
    
#     answer = 4
#     return answer


# # 스택
# # 0 처리
#  1 2 3 4 5                              [1,5,3,5,1,2,1,4]
# [0,0,0,0,0],
# [0,0,1,0,3],
# [0,2,5,0,1],
# [4,2,4,4,2],
# [3,5,1,3,1]     [4, 3, 1, 1,(1지워짐), 3, 2(2지워짐),1줄 없음, 4]

# # ex) 1, 5, 3, 5