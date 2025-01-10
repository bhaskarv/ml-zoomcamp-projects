import requests

url = "http://localhost:9696/predict"

booking  = {"hotel":1.0,"lead_time":222.0,"arrival_date_year":2015.0,"arrival_date_month":9.0,"arrival_date_week_number":38.0,"arrival_date_day_of_month":14.0,"stays_in_weekend_nights":1.0,"stays_in_week_nights":1.0,"adults":2.0,"children":0.0,"babies":0.0,"meal":2.0,"country":51.0,"market_segment":4.0,"distribution_channel":3.0,"is_repeated_guest":0.0,"previous_cancellations":0.0,"previous_bookings_not_canceled":0.0,"reserved_room_type":0.0,"assigned_room_type":0.0,"booking_changes":0.0,"deposit_type":0.0,"agent":68.0,"days_in_waiting_list":0.0,"customer_type":2.0,"adr":80.0,"required_car_parking_spaces":0.0,"total_of_special_requests":0.0}
booking1 = {"hotel":0.0,"lead_time":82.0,"arrival_date_year":2015.0,"arrival_date_month":7.0,"arrival_date_week_number":29.0,"arrival_date_day_of_month":16.0,"stays_in_weekend_nights":0.0,"stays_in_week_nights":3.0,"adults":2.0,"children":0.0,"babies":0.0,"meal":0.0,"country":135.0,"market_segment":6.0,"distribution_channel":3.0,"is_repeated_guest":0.0,"previous_cancellations":0.0,"previous_bookings_not_canceled":0.0,"reserved_room_type":0.0,"assigned_room_type":0.0,"booking_changes":0.0,"deposit_type":0.0,"agent":9.0,"days_in_waiting_list":0.0,"customer_type":2.0,"adr":76.5,"required_car_parking_spaces":0.0,"total_of_special_requests":0.0}

response = requests.post(url=url, json=booking).json()

print(response)