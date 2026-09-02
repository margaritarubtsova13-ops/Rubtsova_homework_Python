from lesson_07.pages.calculator_page import CalculatorPage

def test_slow_calculator(driver):
    page = CalculatorPage(driver)
   
    page.open()
   
    page.set_delay(25)
    
    buttons = ["7", "+", "8", "="]
    for label in buttons:
        page.click_button(label)
   
    result = page.get_result()
    
    assert result == "7+8", f"Ожидалось 7+8, получено: {result}"
