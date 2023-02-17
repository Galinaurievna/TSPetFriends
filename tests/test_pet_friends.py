from api import PetFriends
import settings
import os

pf = PetFriends()


# Тест №1
def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='43421754000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', pet_photo='images/beznazvaniya.jpeg'):
    """Проверяем что можно добавить питомца со слишком большим значением в параметрах"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# Тест №2
def test_add_new_pet_without_valid_data(name='Барбоскин', animal_type='',
                                     age='', pet_photo='images/beznazvaniya.jpeg'):
    """Проверяем что можно добавить питомца без данных"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# Тест №3
def test_add_new_pet_with_invalid_form_data(name='Барбоскин', animal_type='двортерьер',
                                     age='четыре', pet_photo='images/beznazvaniya.jpeg'):
    """Проверяем что можно добавить питомца с некорректной формой даных данных"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# Тест №4
def test_get_api_key_for_invalid_user_email(email=settings.valid_email*2, password=settings.valid_password):
    """ Проверяем что запрос api ключа, при неверном email возвращает статус 403"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


# Тест №5
def test_get_api_key_for_invalid_user_password(email=settings.valid_email, password=settings.valid_password*2):
    """ Проверяем что запрос api ключа, при неверном password возвращает статус 403"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


# Тест №6
def test_add_new_pet_without_foto(name='Барбоскин', animal_type='двортерьер', age='5'):
    """Проверяем что можно добавить питомца без фото """
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


# Тест №7
def test_add_pet_photo(pet_photo='images/Piksi.jpeg'):
    """Проверяем, что можно добавить фото питомца по ID"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем список "мои питомцы", если он пустой, добавляем питомца
    if len(my_pets["pets"]) == 0:
        pf.add_new_pet_simple(auth_key, "Piksi", "кот", "2")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём ID первого питомца и отправляем запрос на добавление к нему фото.
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_pet_set_photo(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result["pet_photo"] != ""

# Тест №8
def test_replace_pet_photo(pet_photo='images/Piksi.jpeg'):
    """Проверяем, что можно заменить фото питомца по ID"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    pf.add_new_pet(auth_key, 'Барбоскин', 'двортерьер', 'четыре', 'images/beznazvaniya.jpeg')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём ID первого питомца и отправляем запрос на добавление к нему фото.
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_pet_set_photo(auth_key, pet_id, pet_photo)
    assert status == 200


# Тест №9
def test_add_pet_photo_with_invalid_ID(pet_photo='images/Piksi.jpeg'):
    """Проверяем, что можно добавить фото питомца по неверному ID"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём ID первого питомца, меняем его и отправляем запрос на добавление к нему фото.
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_pet_set_photo(auth_key, pet_id*15, pet_photo)
    assert status == 500


# Тест №10
def test_get_list_of_my_pets(filter='my_pets'):
    """Проверяем возможность запроса списка Мои питомцы"""
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(settings.valid_email, settings.valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    
