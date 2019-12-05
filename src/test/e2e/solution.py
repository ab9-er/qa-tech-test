from selenium import webdriver


def solve_challenge():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://localhost")

    driver.find_element_by_css_selector("[data-test-id='render-challenge']").click()

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

if __name__ == "__main__":
    solve_challenge()
