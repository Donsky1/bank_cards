# bank_cards

<i>Задание 2. Веб-приложение для управления базой данных бонусных карт </i>
<h2>Website Using Django</h2>
<p><b>bank_cards</b> - веб-приложение для управления базой данных бонусных карт(карт лояльности, кредитный карт и т.д) Приложение состоит исключительно из админки.</p>

<b><i>Используется встроенный способ создания структуры БД (makemigrations, migrate). Встроенный manage.py syncdb или миграции через South (являются устаревшими)</i></b>
<br><br><br>

Обзор:
<ul>
  <li><a href='#main'>Описание задания</a></li>
  <li><a href='#list_card'>Страница списка карточек</a></li>
  <li><a href='#generate'>Страница генерации карт</a></li>
  <li><a href='#history-sell'>Страница истории покупок по карте в профиле</a></li>
</ul>

<h2 id='main'>Описание задания</h2>
<br>
Функционал приложения<br><br>
<ol>
  <li>список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус </li>
  <li>поиск по этим же полям </li>
  <li>просмотр профиля карты с историей покупок по ней </li>
  <li>активация/деактивация карты </li>
  <li>удаление карты </li>
 </ol>

<h2 id='list_card'>Страница списка карточек</h2>
<br>
<p><img src='https://github.com/Donsky1/bank_cards/blob/master/card_project/cards/main.png' align="center"></p>
<br>
<br>

<h2 id='generate'>Страница генерации карт</h2>

Реализовать генератор карт:
- с указанием серии и количества генерируемых карт, 
- срок окончания активности ("1 год", "6 месяцев" "1 месяц"). 
<br>
<p><img src='https://github.com/Donsky1/bank_cards/blob/master/card_project/cards/generate.png' align="center"></p>
<br>

<h2 id='history-sell'>Страница истории покупок по карте в профиле</h2>
<p>Для того чтобы посмотреть список покупок по карте, нужно "провалиться" в профиль карты, сверху можно будет увидеть кнопку "история покупок"</p>
<br>
<p><img src='https://github.com/Donsky1/bank_cards/blob/master/card_project/cards/history-sell.png' align="center"></p>
<br>
<p>кликнув по ней, можно будет увидеть следующую страницу с <a href='#history-sell'>историей покупок </a>по данной карте</p>
<br>
<p><img src='https://github.com/Donsky1/bank_cards/blob/master/card_project/cards/history-sell-page.png' align="center"></p>
<br>
