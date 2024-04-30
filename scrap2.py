from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def translate_text(text, source_lang='en', dest_lang='fr'):
    # Initialize Chrome WebDriver
    translator = webdriver.Chrome()
    translator.get(f"https://translate.google.com/?sl={source_lang}&tl={dest_lang}")
    
    # Locate the text input field
    text_input = WebDriverWait(translator, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".er8xn"))
    )
    
    # Enter the text to be translated
    text_input.clear()
    text_input.send_keys(text)
    
    # Wait for translation to appear
    WebDriverWait(translator, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ryNqvb"))
    )
    
    # Get the translated text
    translated_text_element = translator.find_element(By.CSS_SELECTOR, ".ryNqvb")
    translated_text = translated_text_element.text
    
    # Close the translator
    translator.quit()
    
    return translated_text

def main():
    # Read content from output.txt
    with open("output.txt", "r", encoding="utf-8") as output_file:
        output_content = output_file.read()
    
    # Translate the content
    translated_content = translate_text(output_content)
    
    # Append translated content to input.txt
    with open("input.txt", "a", encoding="utf-8") as input_file:
        input_file.write(f"Original:\n{output_content}\nTranslated:\n{translated_content}\n\n")
        # Append translated code
        input_file.write(translated_content)

if __name__ == "__main__":
    main()
