from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import TimeoutException



def solve_challenge():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://localhost")

    driver.find_element_by_css_selector("[data-test-id='render-challenge']").click()

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".challenge tr"))
    )

    rows = driver.find_elements_by_css_selector(".challenge tr")

    for row in rows:
        INDEX_FOUND = False
        elems = row.find_elements_by_tag_name("td")
        elem_list = list(map(lambda x: int(x.text), elems))

        for _i in range(len(elem_list)):
            print("\nelem_list[] {}".format(elem_list))
            print("[_i] {}".format(_i))
            print("elem_list[_i] {}".format(elem_list[_i]))
            print("elem_list[:_i] {} {}".format(str(elem_list[:_i]), str(sum(elem_list[:_i]))))
            print("elem_list[_i+1:] {} {}".format(str(elem_list[_i+1:]), str(sum(elem_list[_i+1:]))))

            if sum(elem_list[:_i]) == sum(elem_list[_i+1:]):  # Add try block to catch exception for last element
                INDEX_FOUND = True
                print("Balanced")
                break
            else:
                print("Unbalanced")

        print(_i) if INDEX_FOUND else print(None)
        print("\n" + "-" * 30 + "\n")

        driver.find_element_by_css_selector("[data-test-id='submit-{}']".format(rows.index(row) + 1)).send_keys(_i)

    driver.find_element_by_css_selector("[data-test-id='submit-4']").send_keys("Abhinav")

    driver.find_element_by_css_selector("[data-test-id='submitButton']").click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test-id='close-dialog']"))
        )
        print('\n\nSUCCESS!!')
    except TimeoutException:
        print('\n\nFAIL!')
    finally:
        driver.quit()

if __name__ == "__main__":
    solve_challenge()
