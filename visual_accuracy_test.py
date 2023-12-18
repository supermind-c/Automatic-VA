from src.utils import *
from src.speech_recognition import Speech_recognition
from src.image_processing import Image_processing
from src.text_processing import Text_processing

if __name__ == '__main__':
    IMG_processor = Image_processing()
    #AUDIO_processor = Audio_processing()
    TEXT_processor = Text_processing()
    SPEECH_processor = Speech_recognition()
    accuracy = []
    ground_truth = []
    # Open the file
    with open('model_accuracy_test\ground_truth_label\gTruth.txt', 'r') as file:
        # Read the lines
        lines = file.readlines()

        # Count and loop through non-empty lines
        data_line_count = 0
        for line in lines:
            # Strip to remove whitespace and check if line is not empty

            if line.strip():
                data_line_count += 1
                ground_truth.append(line)
                # Process the line here
                #print(f"Line {data_line_count}: {line.strip()}")
        def split_into_digits(s):
            return [char for char in s if char.isdigit()]

        # Convert the string representation to the desired format
        result = []
        for item in ground_truth:
            # Remove the brackets, newline, and split by comma
            numbers = item.strip()[1:-1].split(',')
            # Split each number into its digits
            digit_groups = [split_into_digits(num) for num in numbers]
            result.append(digit_groups)

        # result now contains the converted data
        # data_int now contains the converted data


        for i in range(len(result)):
            result_append = IMG_processor.return_ocr_result()
            print(result_append in ground_truth)
            print(accuracy)
            print("Change picture")
    print(f"Image to Text Accuracy: {(sum(accuracy)/len(accuracy)) * 100} %")



