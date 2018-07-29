# 러시아 농부 곱셈법 또는 고대 이집트 곱셈법이라고도 불린다.
# 1. 곱하려는 숫자(예 19와 254)를 적고 두 숫자 사이에 선을 하나 긋자. 작은 수를 앞에 적는 것이 계산이 더 빠르다.
# 2. 왼쪽에 있는 숫자를 2로 나눈다. 이때 나머지 값은 버리고 결과만 아래쪽에 적는다. 결과값이 1이 나올때까지 계속해서 2로 나누어준다.
# 3. 왼쪽의 계산이 끝이 났다면, 오른쪽으로 넘어간다. 오른쪽에는 2를 곱해서 끝까지 계산한다.
# 4. 만약 왼쪽에 짝수가 있다면 같은 줄의 오른쪽 값들은 지운다.
# 5. 남은 숫자를 합하면 곱셈의 닶이 나온다.

def Russia_multiplication():
    inData = input("enter two numbers: ")
    inData = inData.split(" ")
    f_inData = int(inData[0])
    s_inData = int(inData[1])
    
    result = 0
    while True:
        if f_inData < 1:
            break
        if f_inData % 2 == 0:
            setType = "struck"
        else:
            setType = "keep"
            
        print("{}\t{}\t{}".format(f_inData, s_inData, setType))
        
        if setType == "keep":
            result = result + s_inData
            
        f_inData = f_inData // 2
        s_inData = s_inData * 2
        
    print("The result is {}".format(result)) 
    
# 실행     
Russia_multiplication()

#####################################################################################################

# 이집트 곱셈법과 농부 곱셈법
# 첫 번째 수를 2의 거듭제곱들의 합으로 분해하고, 두 번째 수의 2의 거듭제곱에 대한 표를 만들어 첫 번째 수와 두 번째 수의 곱을 구한다

# 2의 거듭제곱들의 합으로 분해한 list 가져오기
def getCheckNum(tmp_num,tmp_checklist):
    _num = 1
    _rmNum = 0
    _cnt = 0   
    while True:
        _rmNum = tmp_num - _num
        _num = _num * 2
        if _num > tmp_num:
            _result = 2**_cnt          
            break
        _cnt += 1
    
    if _rmNum == 0:
        tmp_checklist.append(_result)
        return tmp_checklist
    else:
        tmp_checklist.append(_result)
        getdataaa(_rmNum,tmp_checklist)  

# 이집트 곱셈법
def ethiopia_multiplication():
    inData = input("enter two numbers: ")
    inData = inData.split(" ")
    inDataCnt = len(inData)
    
    # 숫자2개유무체크
    if inDataCnt != 2:
        print('숫자는 2개만 입력해 주세요.')
        ethiopia_multiplication()  
    
    # 큰수, 작은수 구분
    if int(inData[0]) >= int(inData[1]):
        bigNum = int(inData[0])
        smallNum = int(inData[1])
    else:
        bigNum = int(inData[1])
        smallNum = int(inData[0])
    
    # 큰수 : 2의 거듭제곱들의 합으로 분해한 list 가져오기 
    tmp_checklist = []
    getCheckNum(bigNum,tmp_checklist)
    tmp_checklist

    # 작은수 배수 list 가져오기
    tmp_list = []
    plusNum = 1
    while True:        
        tmp_row_list = []
        tmp_row_list.append(plusNum)
        tmp_row_list.append(smallNum)
        tmp_list.append(tmp_row_list)  
        plusNum = plusNum * 2
        smallNum= smallNum * 2 # 작은수는 2배 증가       
        if plusNum > bigNum:
            break
            
    # keep 한 값 더해서 가져오기        
    keep_list = []
    for kk in tmp_list:            
#         print("{} {}".format(kk[0],kk[1]))
        for jj in tmp_checklist:
            if jj == kk[0]:
                keep_list.append(kk[1]) 

    print("The result is {}".format(sum(keep_list)))

# 실행     
ethiopia_multiplication()