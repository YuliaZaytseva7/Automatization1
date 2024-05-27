from adress import Address

from mailing import Mailing


to_address = Address("0012", "Yerevan", "Vahrama Papaziana", "27", "20")
from_address = Address("101000", "Moscow", "Golovinskoe shosse" ,"10Б","801")
mailing_delivery = Mailing(to_address, from_address, 200, "ASD378923020")

print("Отправление", mailing_delivery.track, "из", 
      f"{mailing_delivery.from_address.zip_code}, {mailing_delivery.from_address.town}, 
      {mailing_delivery.from_address.street}, {mailing_delivery.from_address.building_number} 
      - {mailing_delivery.from_address.room_number},"
      "в," 
      f"{mailing_delivery.to_address.zip_code}, {mailing_delivery.to_address.town}, 
      {mailing_delivery.to_address.srteet}, {mailing_delivery.to_address.building_number} 
      -{mailing_delivery.to_address.room_number}." 
      "Стоимость", mailing_delivery.cost, "рублей")