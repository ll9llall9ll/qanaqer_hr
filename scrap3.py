import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def translate_text(translator, text, source_lang='hy', dest_lang='en'):
    translator.get(f"https://translate.google.com/?sl={source_lang}&tl={dest_lang}")
    
    text_input = WebDriverWait(translator, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".er8xn"))
    )
    
    text_input.clear()
    text_input.send_keys(text)
    
    WebDriverWait(translator, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@jsname = 'toZopb']"))
    )
    
    translated_text_element = translator.find_element(By.XPATH, "//span[@jsname = 'toZopb']")
    translated_text = translated_text_element.text


    
    return f'{text} - {translated_text} - ({translated_text_element})'

translator = webdriver.Chrome()
with open("output.txt", "a", encoding="utf-8") as output_file, open("input.txt", "r", encoding="utf-8") as input_file:
    for line in input_file:
        translated_line = translate_text(translator, line.strip(), source_lang='en', dest_lang='hy')
        
        output_file.write(translated_line)
        time.sleep(1)

