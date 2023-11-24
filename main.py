from src.constants import *
from src.image_processing import Image_processing
from src.audio_processing import Audio_processing
from src.text_processing import Text_processing
from src.speech_recognition import Speech_recognition
from src.utils import *


if __name__ == '__main__':
    #Create instance of each class.
    IMG_processor = Image_processing()
    AUDIO_processor = Audio_processing()
    TEXT_processor = Text_processing()
    SPEECH_processor = Speech_recognition()

    #testing image
    im_paths = ['pic_to_use/Screenshot 2566-09-12 at 08.07.24.png']

    #preprocess
    # result = recognize_text(im_1_path)
    # img_1 = cv2.imread(im_1_path)
    # img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    #plt.imshow(img_1)
    # print(overlay_ocr_text(im_1_path, '1_carplate'))

    YES = ['ถูกต้อง', 'ถูกต้องครับ', 'ถูกต้องค่ะ','ใช่','ใช่ครับ']
    NO = ['ผิด', 'ผิดค่ะ', 'ผิดครับ','ไม่ใช่','ไม่','ไม่ใช่ครับ']

    for im_path in im_paths:
        result_append = IMG_processor.overlay_ocr_text(im_path, '1_carplate')
        print(result_append)
        print(f"There are #{len(result_append)} lines ")
        total_score = 0
        for i in result_append:
            print(i)
            playsound_util(playsound_file_path['initial'])
            playsound_util(playsound_file_path['beep'])
            voice_recorded = AUDIO_processor.record_audio()
            playsound_util(playsound_file_path['got_your_voice'])
            #audio_visualization(voice_recorded)
            speech_text = SPEECH_processor.get_text(voice_recorded)

            ref_text = TEXT_processor.process_digit_thai(i)
            #print(speech_text)
            hyp_text = TEXT_processor.process_text(speech_text)

            repeat_answer(hyp_text.split(" "))
            playsound_util(playsound_file_path['beep'])

            while True:
                #repeat_answer(hyp_text)

                res_rec = AUDIO_processor.record_audio()
                res_text = SPEECH_processor.get_text(res_rec)
                print(res_text)
                user_respond = TEXT_processor.process_user_respond(res_text)
                #debug
                print(user_respond)
                print(user_respond in YES, user_respond in NO)
                playsound_util(playsound_file_path['beep'])
                if (user_respond in YES):
                    playsound_util(playsound_file_path['prepare'])
                    break

                elif (user_respond in NO):
                    playsound_util(playsound_file_path['repeat_same_line'])
                    playsound_util(playsound_file_path['initial'])
                    playsound_util(playsound_file_path['beep'])
                    voice_recorded = AUDIO_processor.record_audio()
                    speech_text = SPEECH_processor.get_text(voice_recorded)
                    hyp_text = TEXT_processor.process_text(speech_text)
                    playsound_util(playsound_file_path['got_your_voice'])
                    repeat_answer(hyp_text.split(" "))

                else:
                    playsound_util(playsound_file_path['cannot_catch'])
                    playsound_util(playsound_file_path['beep'])

            playsound_util(playsound_file_path['end_of_process'])
            print(f"Speech text: {speech_text}")
            print(f"hyp_text: {hyp_text}")
            print(f"ref_text: {ref_text}")
            print("=========================================")
            evaluation_result = evaluation_score(ref_len=len(ref_text), hyp_len=len(hyp_text), hyp_text=hyp_text, ref_text=ref_text)
            total_score += len(evaluation_result)
            #result(len(i),len(correct))
            break
        print(f"Score: {total_score}")
    #print(f"Score: {len(correct)}")
    #print(correct)
