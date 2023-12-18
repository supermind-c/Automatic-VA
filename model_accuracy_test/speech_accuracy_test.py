from src.speech_recognition import Speech_recognition
from src.audio_processing import Audio_processing



if __name__ == '__main__':
    SPEECH_processor = Speech_recognition()
    AUDIO_processor = Audio_processing()
    ground_truth_speech = []
    with open('/Users/printfnack/Desktop/Automatic-VA/model_accuracy_test/ground_truth_label/ground_truth_speech.txt', 'r') as file:
        # Read the lines
        lines = file.readlines()

        # Count and loop through non-empty lines
        data_line_count = 0
        for line in lines:
            # Strip to remove whitespace and check if line is not empty

            if line.strip():
                data_line_count += 1
                ground_truth_speech.append(line)
                # Process the line here
                #print(f"Line {data_line_count}: {line.strip()}")
    for i in ground_truth_speech:
        print(i)
        voice_recorded = AUDIO_processor.record_audio()
        speech_text = SPEECH_processor.get_text(voice_recorded)
        print(speech_text)

        print(speech_text == i)