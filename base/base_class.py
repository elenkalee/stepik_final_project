class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод получения текущей URL"""
        get_url = self.driver.current_url
        print(f"Current URL is {get_url}")

    def assert_url(self, result_url):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print(get_url)
        assert get_url == result_url
        print("URL is match")

    def assert_word(self, word, result_word):
        """Метод проверки слов"""
        value_word = word.text
        print(value_word)
        assert value_word == result_word
        print("Words match")
