from time import sleep
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class uc_easy(Chrome):
    def __init__(self,xxtimeout=20,timesleep=0,**kw):
        """
        :param xxtimeout: 显性等待超时时间，默认20s
        :param timesleep: 操作时间间隔，默认0s
        """
        super().__init__(use_subprocess=True,**kw)
        self.xxtimeout=xxtimeout
        self.timesleep=timesleep
        
    def fex(self,xpath):
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        sleep(self.timesleep)
        return self.find_element(By.XPATH, xpath)
        
    def fesx(self,xpath):
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        sleep(self.timesleep)
        return self.find_elements(By.XPATH, xpath)

    def feid(self,id):
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.ID, id)))
        sleep(self.timesleep)
        return self.find_element(By.ID, id)

    def fesid(self,id):
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.ID, id)))
        sleep(self.timesleep)
        return self.find_elements(By.ID, id)

    def fename(self,name):
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.NAME, name)))
        sleep(self.timesleep)
        return self.find_element(By.NAME, name)

    def fesname(self,name):
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.ID, name)))
        sleep(self.timesleep)
        return self.find_elements(By.NAME, name)

    def fel_t(self,l_t):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.LINK_TEXT, l_t)))
        return self.find_element(By.LINK_TEXT, l_t)

    def fesl_t(self,l_t):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.LINK_TEXT, l_t)))
        return self.find_elements(By.LINK_TEXT, l_t)

    def fep_l_t(self,p_l_t):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, p_l_t)))
        return self.find_element(By.PARTIAL_LINK_TEXT, p_l_t)

    def fesp_l_t(self,p_l_t):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, p_l_t)))
        return self.find_elements(By.PARTIAL_LINK_TEXT, p_l_t)

    def fec_s(self,c_s):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, c_s)))
        return self.find_element(By.CSS_SELECTOR, c_s)

    def fesc_s(self,c_s):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, c_s)))
        return self.find_elements(By.CSS_SELECTOR, c_s)

    def fec_n(self,c_n):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.CLASS_NAME, c_n)))
        return self.find_element(By.CLASS_NAME, c_n)

    def fesc_n(self,c_n):
        sleep(self.timesleep)
        WebDriverWait(self, self.xxtimeout).until(EC.visibility_of_element_located((By.CLASS_NAME, c_n)))
        return self.find_elements(By.CLASS_NAME, c_n)