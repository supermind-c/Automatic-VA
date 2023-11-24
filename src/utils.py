import numpy as np
from src.constants import *
def evaluation_score(ref_len, hyp_len, hyp_text, ref_text):
    checked_index = []
    correct = []
    if (ref_len == hyp_len):
        print("ref_len == hyp_len")
        for i, hyp in enumerate(hyp_text.split(" ")):
            if hyp in ref_text.split(" "):
                print("true")
                correct.append(hyp)
            else:
                print(f"sub @ index {i} by {hyp}")

    elif (ref_len < hyp_len):
        print("ref_len < hyp_len")
        for i, ref in enumerate(ref_text.split(" ")):
            for j, hyp in enumerate(hyp_text.split(" ")):
                if hyp in ref:
                    print(f"true {hyp}")
                    correct.append(hyp)
                    checked_index.append(j)
                    break
                elif (hyp not in ref) & (j>=i) & (j not in checked_index):
                    print(f"insert @ index {i} by {hyp}")


    #Unfinished for same number
    elif (ref_len > hyp_len):
        print("ref_len > hyp_len")
        for i, ref in enumerate(ref_text.split(" ")):
            for j, hyp in enumerate(hyp_text.split(" ")):
                if (hyp in ref):
                    print(f"true {hyp}")
                    correct.append(hyp)
                    checked_index.append(j)
                    break
                elif (hyp not in ref) & (j>=i) & (j not in checked_index):
                    print(f"Delete @ index {i} ")
    # print(expected == len(correct
    # print(expected, len(correct))
    print("=========================================")
    return correct

def check_score(n,score):
    if n > 3 :
        limit = np.ceil(n/2) - 1
    elif n == 3 :
        limit = 1
    else :
        limit = 0

    if limit >= (n - score) :
        if n == 8 :
            return False, (n - score)
        else :
            return True, (n - score)
    else :
        return False, (n - score)

def result_score(n, incorrect, line=None):
    if line == None :
        line = n
    base_line = numpy.floor(n/2)
    if incorrect > base_line:
        return (line-1), (n - incorrect)
    else :
        return line, -incorrect

def result(n, score, line=None) :
    stop, incorrect = check_score(n,score)
    if stop == False :
        end_line, note = result_score(n,incorrect)
    print(f"End @ line {end_line} with {note}")


def repeat_answer(hyp_text):
    playsound_util(playsound_file_path['you_said'])
    for i in hyp_text:
        play_num_sound(i)
    playsound_util(playsound_file_path['yes_or_no'])

def play_num_sound(num):
    playsound_util(playsound_file_path[f'{num}'])
    # key = ['หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า']
    # if num == key[0]:
    #     playsound_util(playsound_file_path['หนึ่ง'])
    #
    # elif num == key[1]:
    #     playsound_util(playsound_file_path['สอง'])
    #
    # elif num == key[2]:
    #     playsound_util(playsound_file_path['สาม'])
    #
    # elif num == key[3]:
    #     playsound_util(playsound_file_path['สี่'])
    #
    # elif num == key[4]:
    #     playsound_util(playsound_file_path['ห้า'])
    #
    # elif num == key[5]:
    #     playsound_util(playsound_file_path['หก'])
    #
    # elif num == key[6]:
    #     playsound_util(playsound_file_path['เจ็ด'])
    #
    # elif num == key[7]:
    #     playsound_util(playsound_file_path['แปด'])
    #
    # elif num == key[8]:
    #     playsound_util(playsound_file_path['เก้า'])
