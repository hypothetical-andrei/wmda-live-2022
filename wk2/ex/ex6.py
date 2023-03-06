from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.set_window_size(800, 600)
    driver.get('https://www.imobiliare.ro/vanzare-garsoniere/bucuresti/berceni/garsoniera-de-vanzare-XAQN000V2?exprec=similare&rec_ref=home&sursa_rec=home&imoidviz=3956189975')
    element = driver.find_element(By.CSS_SELECTOR, '.pret.first.dl_infotip_pret_fix.tooltipstered')
    print(element.text.split('€')[0])
    driver.quit()

if __name__ == '__main__':
    main()