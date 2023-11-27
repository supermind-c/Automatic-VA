from src.constants import *
from src.image_processing import Image_processing
from src.audio_processing import Audio_processing
from src.text_processing import Text_processing
from src.speech_recognition import Speech_recognition
from src.utils import *
import time

if __name__ == '__main__':
    #Create instance of each class.
    IMG_processor = Image_processing()
    AUDIO_processor = Audio_processing()
    TEXT_processor = Text_processing()
    SPEECH_processor = Speech_recognition()

    #testing image
    

    #preprocess
    # result = recognize_text(im_1_path)
    # img_1 = cv2.imread(im_1_path)
    # img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    #plt.imshow(img_1)
    # print(overlay_ocr_text(im_1_path, '1_carplate'))

    YES = ['ถูกต้อง', 'ถูกต้องครับ','ถูกต้องคับ', 'ถูกต้องค่ะ','ใช่','ใช่ครับ','ใช่คับ','ใช่ค่ะ','ใช่คะ','ใช่จ้า'] 
    NO = ['ผิด', 'ผิดค่ะ', 'ผิดครับ','ไม่ใช่','ไม่','ไม่ใช่ครับ','ไม่ใช่คับ','ไม่ครับ','ไม่คับ','ไม่ค่ะ','ไม่คะ']
    total_score = 0
    num_pic = 1
    total_pic = 0
    conclude_score = []
    for i in range(num_pic):
        playsound_util(playsound_file_path['process_pic'])
        result_append = IMG_processor.return_ocr_result()
        #result_append = [['6', '5'], ['2', '3', '9']]
        print(result_append)
        print(f"There are #{len(result_append)} lines ")
        count_line = 0
        total_pic += 1
        for i in result_append:
            print(i)
            playsound_util(playsound_file_path['initial'])
            voice_recorded = AUDIO_processor.record_audio()
            playsound_util(playsound_file_path['got_your_voice'])
            #audio_visualization(voice_recorded)
            speech_text = SPEECH_processor.get_text(voice_recorded)
    
            ref_text = TEXT_processor.process_digit_thai(i)
            #print(speech_text)
            hyp_text = TEXT_processor.process_text(speech_text)
    
            repeat_answer(hyp_text.split(" "))
            correct_test = 0
            #playsound_util(playsound_file_path['beep'])
            count_line += 1
            while hyp_text == '':
                voice_recorded = AUDIO_processor.record_audio()
                playsound_util(playsound_file_path['got_your_voice'])
                #audio_visualization(voice_recorded)
                print("TEST SI")
                speech_text = SPEECH_processor.get_text(voice_recorded)
        
                ref_text = TEXT_processor.process_digit_thai(i)
                #print(speech_text)
                hyp_text = TEXT_processor.process_text(speech_text)
        
                repeat_answer(hyp_text.split(" "))
                
            while True:
                #repeat_answer(hyp_text)
    
                res_rec = AUDIO_processor.record_audio()
                res_text = SPEECH_processor.get_text(res_rec)
                print(res_text)
                user_respond = TEXT_processor.process_user_respond(res_text)
                #debug
                print(user_respond)
                print(user_respond in YES, user_respond in NO)
                #playsound_util(playsound_file_path['beep'])
                
                if (user_respond in YES):
                    if count_line != len(result_append):
                        playsound_util(playsound_file_path['prepare'])
                        time.sleep(1)
                    break
    
                elif (user_respond in NO):
                    playsound_util(playsound_file_path['repeat_same_line'])
                    playsound_util(playsound_file_path['initial'])
                    voice_recorded = AUDIO_processor.record_audio()
                    #playsound_util(playsound_file_path['beep'])
                    speech_text = SPEECH_processor.get_text(voice_recorded)
                    hyp_text = TEXT_processor.process_text(speech_text)
                    playsound_util(playsound_file_path['got_your_voice'])
                    repeat_answer(hyp_text.split(" "))
                    
                    while hyp_text == ['']:
                        voice_recorded = AUDIO_processor.record_audio()
                        playsound_util(playsound_file_path['got_your_voice'])
                        #audio_visualization(voice_recorded)
                        speech_text = SPEECH_processor.get_text(voice_recorded)
                
                        ref_text = TEXT_processor.process_digit_thai(i)
                        #print(speech_text)
                        hyp_text = TEXT_processor.process_text(speech_text)
                
                        repeat_answer(hyp_text.split(" "))
                   
    
                else:
                    playsound_util(playsound_file_path['cannot_catch'])
                    playsound_util(playsound_file_path['yes_or_no'])
                    #playsound_util(playsound_file_path['beep'])
                    
    
            
            print(f"Speech text: {speech_text}")
            print(f"hyp_text: {hyp_text}")
            print(f"ref_text: {ref_text}")
            print("=========================================")
            evaluation_result = evaluation_score(ref_len=len(ref_text), hyp_len=len(hyp_text), hyp_text=hyp_text, ref_text=ref_text)
            total_score += len(evaluation_result)
            conclude_score.append((f"picture_number_{num_pic}",result(len(i),correct_test)))
        if total_pic != num_pic:
            playsound_util(playsound_file_path['change_pic'])
        time.sleep(5)
    playsound_util(playsound_file_path['end_of_process'])
    print(f"Score: {total_score}")
    print(conclude_score)
#print(f"Score: {len(correct)}")
#print(correct)
