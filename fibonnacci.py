
def finonacci_sequence(n: int): 
    """
    This function returns the fibonnacci sequence for an n number of entries
    
    Args:
        n (int): This is the number of elements in the fibonacci sequence
    return:
        answer (list): This is the fibonnacci sequence in a list
    """
    answer = [0,1]
    for i in range(n):
        if i > 1:
            answer.append(answer[i-2] + answer[i-1])
        elif n == 1:
            answer.pop()
            return answer
    return answer


# Tests
print(finonacci_sequence(22))
print(finonacci_sequence(2))
print(finonacci_sequence(5))