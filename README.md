<h3>Версия 1 
<h3>Основной тестовый сценарий:</h3>

* С главной страницы перейти на страницу "Dresses"
* Выбрать фильтры:
  * Категория: summer dresses
  * размер S
  * цвет: Yellow и Orange
  * сортировка по цене: от низкой к высокой
  * диапазон цены 'до' изменен на -20 px
* Добавить первый товар
* Продолжить покупки
* Добавить второй товар
* Перейти к оплате
* На странице Summary нажать на proceed to Checkout
* На странице Sign in авторизоваться с данными пользователя 

email: elena.42rus@yandex.ru 

password: Test1234
* На странице Addresses нажать на Proceed to checkout
* На странице Shipping отметить checkbox с Terms of service и нажать на Proceed to checkout
* На странице Payment выбрать способ платежа Pay by bank wire
* На странице с информацией о Bank-wire payment нажать I confirm my order
* На финальной странице проверить, что заказ принят в обработку по фразе "Your order on My Store is complete."

В процессе выполнения возникли вопросы в файле **dresses_page.py** раздел **Actions**:
Как вызвать ранее сформированные геттеры, используя класс Actions? Пока сделала с поиском элементов внутри этих функций
* def check_summer_dresses_checkbox(self)
* def check_size_s_checkbox(self)
* def move_price_range_slider(self)
* def click_add_to_cart_btn_item_1(self)
* def click_add_to_cart_btn_item_2(self)


_Ассерты и скрины пока не делала_

