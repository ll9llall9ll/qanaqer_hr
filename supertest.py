import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def translate_text(text, source_lang='hy', dest_lang='en'):  
    translator = webdriver.Chrome()
    translator.get(f"https://translate.google.com/?sl={source_lang}&tl={dest_lang}")
    
    text_input = WebDriverWait(translator, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".er8xn"))
    )
    
    text_input.clear()
    text_input.send_keys(text)
    
    WebDriverWait(translator, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ryNqvb"))
    )
    
    translated_text_element = translator.find_element(By.CSS_SELECTOR, ".ryNqvb")
    translated_text = translated_text_element.text
    
    text_input.clear()
    text_input.send_keys(translated_text)
    
    translator.quit()
    
    return translated_text

def main():
    translated_lines_count = 0
    with open("output.txt", "r", encoding="utf-8") as output_file, \
         open("input.txt", "a", encoding="utf-8") as input_file:
             
        for line in output_file:
            translated_line = translate_text(line.strip(), source_lang='hy', dest_lang='en')
            
            input_file.write(f"Armenian:\n{line}\nEnglish:\n{translated_line}\n\n")
            input_file.write(translated_line + '\n')  
            
            translated_lines_count += 1
            
            # Check if 3 lines have been translated, then add a separator to input.txt
            if translated_lines_count % 3 == 0:
                input_file.write("------\n\n")
            
            time.sleep(1)

if __name__ == "__main__":
    main()
