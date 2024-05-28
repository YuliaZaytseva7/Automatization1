from adress import Address

from mailing import Mailing


to_address = Address("0012", "Yerevan", "Vahrama Papaziana", "27", "20")
from_address = Address("101000", "Moscow", "Golovinskoe shosse" ,"10Б","801")
mailing_delivery = Mailing(to_address, from_address, 200, "ASD378923020")



print(f"Отправление {mailing_delivery.track}. Из {mailing_delivery.from_address.zip_code}, "
      f"{mailing_delivery.from_address.town}, {mailing_delivery.from_address.street}, "
      f"{mailing_delivery.from_address.building_number} - {mailing_delivery.from_address.room_number}, В "
      f"{mailing_delivery.to_address.zip_code}, {mailing_delivery.to_address.town}, "
      f"{mailing_delivery.to_address.street}, {mailing_delivery.to_address.building_number}"
      f"-{mailing_delivery.to_address.room_number}.  Стоимость: {mailing_delivery.cost} рублей.")
