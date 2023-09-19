
# Юлия Мясникова, 8а поток - дипломный проект
import sender_stand_request

# Тест. Код ответа = 200 на запрос заказа по трек-номеру
def test_get_order_with_track_success():
    response = sender_stand_request.get_order_with_track()
    assert response.status_code == 200
