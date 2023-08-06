# Параметры товара

| Ключ | Описание | Раздел |
| --- | --- | --- |
| price_supplier | закупочная | price |
| price_buy | себестоимость | price |
| price_base | базовая | price |
| price_general | ходовая | price |
| price_sale_10 | со скидкой, 10% | price |
| price_sale_20 | со скидкой, 20% | price |
| price_sale_30 | со скидкой, 30% | price |
| photo_general | фото на лошади | media |
| photo_collection | фото коллекции | media |
| photo_size | фото с сантиметром | media |
| photo_additional | фоток дополнительные | media |
| video_reals | видео рилс | media |
| video_description | видео подробное с голосом | media |
| video_general | основное видео | media |
| description_materials | Материалы / Состав | description |
| description_color | Цвет | description |
| description_measurement | ШиринаxГлубинаxВысота (мм) | description |
| description_title | Название на русском | description |
| description_collection | Коллекция | description |
| description_brand | Бренд | description |
| description_notes | Примечания | description |
| description_size | Размер | description |
| description_short | Короткое описание | description |
| description_weight | Вес (кг) | description |

# Параметры выгрузки

**Используется скриптами (изменять, только если понимаешь, что ты делаешь и зачем)** для выгрузки товаров во внешние платформы. Этот блок должен быть 1. В нем хранятся уникальные настройки выгрузки этого товара

## Примеры настроек:

- Если нужно изменить список платформ, на которые выгружается товар
- Сделать уникальную цену для конкретной платформы
- Добавить фотографии или видео для конкретной платформы или для всех платформ

## Комментарии от ботов

Для установки команд ботам, можно использовать комментарии к блоку [base_settings]. При выполнении задач, боты будут писать в комментарии свои метки

## Правило генерации SKU

Категория.Бренд.Цена_покупки.месяц_добавления.год_добавления.случайные_4_числа