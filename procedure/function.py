from openpyxl import load_workbook
import math

def get_data_from_excel(filename):
    """

    """
    wb=load_workbook(filename)
    ws=wb.active
    g=ws.rows
    raw_data={}
    for name_cell, score_cell in g:
        raw_data[name_cell.value] = score_cell.value
    return raw_data

def get_average(scores):
    s=0.0
    for score in scores:
        s+=score
    return s/len(scores)

def get_variance(scores, avrg):
    s=0.0
    for score in scores:
        s+=(score-avrg)**2
    return round(s/len(scores), 1)

def get_std_dev(variance):
    return round(math.sqrt(variance), 1)
    
def evaluate_class(avrg, std_dev):
    """
        evaluate_class()
    """
    if avrg < 50 and std_dev > 20:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avrg > 50 and std_dev > 20:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avrg < 50 and std_dev < 20:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avrg > 50 and std_dev < 20:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')
