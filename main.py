import ssl
import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt
import pyaudio
import audioop
import wave
from pythaiasr import asr
from playsound import playsound

im_1_path = 'pic_to_use/Screenshot 2566-09-12 at 08.07.24.png'
ssl._create_default_https_context = ssl._create_unverified_context

def recognize_text(img_path):
    '''loads an image and recognizes text.'''

    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)

result = recognize_text(im_1_path)
img_1 = cv2.imread(im_1_path)
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
plt.imshow(img_1)

def overlay_ocr_text(img_path, save_name):
    '''loads an image, recognizes text, and overlays the text on the image.'''

    #list for retrieve result
    global result_append
    result_append = []
    # loads image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    dpi = 80
    fig_width, fig_height = int(img.shape[0]/dpi), int(img.shape[1]/dpi)
    plt.figure()
    f, axarr = plt.subplots(1,2, figsize=(fig_width, fig_height))
    axarr[0].imshow(img)

    # recognize text
    result = recognize_text(img_path)

    # if OCR prob is over 0.5, overlay bounding box and text
    for (bbox, text, prob) in result:
        if prob >= 0.5:
            # display
            print(f'Detected text: {text} (Probability: {prob:.2f})')
            result_append.append(text)
            # get top-left and bottom-right bbox vertices
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

            # create a rectangle for bbox display
            cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)

            # put recognized text
            cv2.putText(img=img, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=8)

    # show and save image
    axarr[1].imshow(img)
    #plt.savefig(f'./output/{save_name}_overlay.jpg', bbox_inches='tight')

print(overlay_ocr_text(im_1_path, '1_carplate'))
print(result_append)

def get_audio():
    # Parameters for audio recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024  # The chunk size defines the length of time for each analysis frame.
    THRESHOLD = 1500  # Adjust this threshold to fit your environment and microphone sensitivity.
    SILENCE_LIMIT = 5  # Time in seconds to wait for silence before stopping recording.

    p = pyaudio.PyAudio()

    # Open the microphone stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []
    silence_frames = 0

    while True:
        try:
            data = stream.read(CHUNK)
            frames.append(data)
            rms = audioop.rms(data, 2)  # Calculate the RMS energy of the audio chunk.

            if rms < THRESHOLD:
                silence_frames += 1
            else:
                silence_frames = 0  # Reset silence counter if there's audio activity.

            if silence_frames > int(RATE / CHUNK) * SILENCE_LIMIT:
                print("Silence detected. Stopping recording.")
                break

        except KeyboardInterrupt:
            print("Recording stopped by user.")
            break

    # Close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
#     file_name = 'record_with_silence.wav'
#     # Save the recorded audio to a file
# # Save the recorded audio to a file
#     with wave.open(file_name, 'wb') as wf:
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))
#
#     print(f"Audio saved as {file_name}")
    return audio_data

#will be discarded later
def audio_visualization(audio):
    time = np.arange(len(audio))
    data = audio
    plt.figure(figsize=(10, 6))
    plt.plot(time, data, label='Data')
    plt.xlabel('Time')
    plt.ylabel('Data Value')
    plt.title('Data vs. Time')
    plt.grid(True)
    plt.legend()
    plt.show()

def get_text(audio_vector) -> str:
    text_sample = asr(audio_vector)
    return str(text_sample)

def process_text(text_sample: str) -> str:
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



def evaluation_score(ref_len, hyp_len, hyp_text, ref_text):
    checked_index = []
    checked_index2 = []
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

#process digit to thai words
def process_digit_thai(digits) -> str:
    digits = str(digits).strip()
    result_gathering = []
    digit_dict = {"1":'หนึ่ง',"2":'สอง',"3":'สาม',"4":'สี่',"5":'ห้า',"6":'หก',"7":'เจ็ด',"8":'แปด',"9":'เก้า'}
    for i_ in digits:
        result_gathering.append(digit_dict.get(i_,'0'))
    return " ".join(result_gathering)



if __name__ == '__main__':
    print(f"There are #{len(result_append)} lines ")
    soundtrack_instruction = 'soundtrack/poodka.wav'
    soundtrack_stop = 'soundtrack/yoodka.wav'

    correct = []
    for i in result_append:
        print(i)
        playsound(soundtrack_instruction)
        voice_recorded = get_audio()
        playsound(soundtrack_stop)
        #audio_visualization(voice_recorded)
        speech_text = get_text(voice_recorded)
        ref_text = process_digit_thai(i)
        hyp_text = process_text(speech_text)
        print(f"Speech text: {speech_text}")
        print(f"hyp_text: {hyp_text}")
        print(f"ref_text: {ref_text}")
        print("=========================================")
        evaluation_score(ref_len=len(ref_text), hyp_len=len(hyp_text), hyp_text=hyp_text, ref_text=ref_text)

    print(f"Score: {len(correct)}")
    print(correct)

