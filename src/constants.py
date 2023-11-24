from playsound import playsound
playsound_file_path = {
    'หนึ่ง' : ('soundtrack/1.หนึ่ง.wav'),
    'สอง' : 'soundtrack/2.สอง.wav',
    'สาม' : 'soundtrack/3.สาม.wav',
    'สี่' : 'soundtrack/4.สี่.wav',
    'ห้า' : 'soundtrack/5.ห้า.wav',
    'หก' : 'soundtrack/6.หก.wav',
    'เจ็ด' : 'soundtrack/7.เจ็ด.wav',
    'แปด' : 'soundtrack/1.แปด.wav',
    'เก้า' : 'soundtrack/8.เก้า.wav',
    'beep' : 'soundtrack/X2Download.app - Censor beep sound effect (128 kbps).wav',
    'prepare' : 'soundtrack/1.เตรียมตัวพูดบรรทัดใหม่หล.wav',
    'repeat_same_line' : 'soundtrack/1.เริ่มการอัดเสียงในบรรทัด.wav',
    'initial' : 'soundtrack/1.พูดหลังเสียงสัญญาณได้เลย.wav',
    'yes_or_no' : 'soundtrack/10.ใช่หรือไม่.wav',
    'cannot_catch' : 'soundtrack/11.เราได้ยินคุณไม่ชัดกรุณาพ.wav',
    'got_your_voice' : 'soundtrack/2.ได้รับข้อมูลเสียงแล้วค่ะ.wav',
    'you_said' : 'soundtrack/9.คุณพูด.wav',
    'end_of_process' : 'soundtrack/1.สิ้นสุดกระบวนการวัดค่าสา.wav'
}

def playsound_util(path):
    playsound(path)
