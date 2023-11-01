class Text_processing():
    def __init__(self):
        pass
    def process_text(self,text_sample: str) -> str:
        key = ['หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า']
        result = []
        text, *_ = text_sample[0]
        for i, word in enumerate(text_sample.split(" ")):
            if word in key:
                result.append(word)
        #result = ['หนึ่ง', 'สอง', 'สาม', 'สี่']
        hyp_text = ""
        for i, word in enumerate(result):
            if(i < (len(result) - 1)):
                hyp_text += word + " "
            else:
                hyp_text += word
        #print(f"ASR hypothesis: {hyp_text}")
        return hyp_text

    def process_user_respond(self,text_sample: str) ->str:
        key = ['ใช่','ไม่']
        result = []
        text, *_ = text_sample[0]
        for i, word in enumerate(text_sample.split(" ")):
            if word in key:
                result.append(word)
        #result = ['ใช่']
        res_text = ""
        for i, word in enumerate(result):
            if(i < (len(result) - 1)):
                res_text += word + " "
            else:
                res_text += word
        #print(f"ASR hypothesis: {hyp_text}")
        return res_text

    #process digit to thai words
    def process_digit_thai(self,digits) -> str:
        digits = str(digits).strip()
        result_gathering = []
        digit_dict = {"1":'หนึ่ง',"2":'สอง',"3":'สาม',"4":'สี่',"5":'ห้า',"6":'หก',"7":'เจ็ด',"8":'แปด',"9":'เก้า'}
        for i_ in digits:
            result_gathering.append(digit_dict.get(i_,'0'))
        return " ".join(result_gathering)