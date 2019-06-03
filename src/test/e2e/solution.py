from selenium import webdriver   


def solve_challenge():
    driver = webdriver.Chrome()

    driver.maximize_window()                                                                     

    driver.get("http://localhost:3000")                                                          

    driver.find_element_by_css_selector("[data-test-id='render-challenge']").click() 

    rows = driver.find_elements_by_css_selector(".challenge tr")

    for row in rows:
        INDEX_FOUND = False
        elems = row.find_elements_by_tag_name("td")
        elem_list = list(map(lambda x: int(x.text), elems))

        for _i in range(len(elem_list)):
            if sum(elem_list[:_i-1]) == sum(elem_list[_i:]):
                INDEX_FOUND = True
                break
        
        print(_i - 1) if INDEX_FOUND else print(None)

if __name__ == "__main__":
    solve_challenge()
