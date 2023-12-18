import easyocr
import cv2
import matplotlib.pyplot as plt
class Image_processing():

    def __init__(self):
        pass

    def pre_process(self):
        pass

    def split_digits(self,ocr_result):
        """Split OCR results into single digits."""
        bbox, number, _ = ocr_result
        return [(bbox, digit) for digit in number if digit.isdigit()]

    def is_on_same_line(self,bbox1, bbox2, threshold=40):
        """Check if two bounding boxes are on the same line."""
        y1_center = (bbox1[0][1] + bbox1[2][1]) / 2
        y2_center = (bbox2[0][1] + bbox2[2][1]) / 2
        return abs(y1_center - y2_center) <= threshold
    
    def process_ocr_results(self,ocr_results, previous_texts, repeat_threshold=3):
        """Process OCR results to get unique numbers in lines."""
        # Split digits and flatten list
        all_digits = [item for result in ocr_results for item in self.split_digits(result)]
    
        line_groups = []
        for bbox1, digit1 in all_digits:
            added_to_line = False
            for line in line_groups:
                if any(self.is_on_same_line(bbox1, bbox2) for bbox2, _ in line):
                    line.append((bbox1, digit1))
                    added_to_line = True
                    break
            if not added_to_line:
                line_groups.append([(bbox1, digit1)])
    
        # Convert line groups to text lines
        lines = [''.join(digit for _, digit in line) for line in line_groups]
    
        # Check for repeated results based on text lines
        if lines == previous_texts:
            self.repeat_count += 1
            if self.repeat_count >= repeat_threshold and lines:
                return None
        else:
            self.repeat_count = 0
    
        return lines
        
    def return_ocr_result(self):
        self.repeat_count = 0

        # Read the image
        cap = cv2.VideoCapture(0)
        
        # Instance text detection
        reader = easyocr.Reader(["en"], gpu=False)
        
        # Detect text on image
        threshold = 0.1
        previous_texts = []
        actual_output = []
        while True:
            try:
                ret, frame = cap.read()
                text_raw = reader.readtext(frame)
                current_results = [(bbox, text, score) for bbox, text, score in text_raw if score > threshold]
                
                # Process OCR results
                output = self.process_ocr_results(current_results, previous_texts)
                actual_output.append(output)
                if output is None:
                    print("Repeated results. Breaking loop.")
                    break
            
                # Draw bounding boxes and texts
                for bbox, text, score in current_results:
                    if score > threshold:
                        cv2.rectangle(frame, bbox[0], bbox[2], (0, 255, 0), 5)
                        cv2.putText(frame, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
                # Update previous texts
                previous_texts = output
                print(output)
               # cv2.imshow("Text Recognition", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                    
            except Exception as e:
                print("ERROR OCCUR", e)
        
        cap.release()
        cv2.destroyAllWindows()
        final_output = []
        
        for i in actual_output[-2]:
            final_output.append(list(i))
        
    
        return final_output

