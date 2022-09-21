import requests

def fetch(url, params):
  headers = params["headers"]
  body = params["body"]
  if params["method"] == "POST":
  # отправили post запрос на url, приложив к нему headers и тело запроса
    response = requests.post(url, headers=headers, data=body)
  else:
    response = requests.get(url, headers=headers)
  return response

def get_lambos(year_from, year_to):
  lambo_response = fetch("https://auto.ru/-/ajax/desktop/listing/", {
    "headers": {
      "accept": "*/*",
      "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
      "content-type": "application/json",
      "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"macOS\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "same-origin",
      "sec-fetch-site": "same-origin",
      "x-client-app-version": "155.0.10041033",
      "x-client-date": "1663699067540",
      "x-csrf-token": "d0c4221ac15f246b50b2c9e202d866597d1c43e99226c3eb",
      "x-page-request-id": "78796908f6145d6a026049e7b9c0e438",
      "x-requested-with": "XMLHttpRequest",
      "x-retpath-y": "https://auto.ru/moskovskaya_oblast/cars/lamborghini/all/?year_to=2019&year_from=2005",
      "cookie": "suid=c0320a1d952962effbef097ada56b017.72bf3b905ff71bf4c810ea79e1d508da; _csrf_token=d0c4221ac15f246b50b2c9e202d866597d1c43e99226c3eb; autoru_sid=a%3Ag632703f42lhg5cdg4vlvj6aps0777u7.4deec2cbe712655bd807634af41d8bad%7C1663501300669.604800.UnPPzhnX2DZ9coAh56sWww.o4jrAU4WVTz7A84WEPIDptdSP9ROg4vZ7imaomzngS0; autoruuid=g632703f42lhg5cdg4vlvj6aps0777u7.4deec2cbe712655bd807634af41d8bad; counter_ga_all7=1; yuidlt=1; yandexuid=4508204351568733777; my=YwA%3D; gdpr=0; _ym_uid=1663501301690692461; spravka=dD0xNjYzNTAxMzE2O2k9OTUuMTYxLjIzNS4xNTI7RD04REUwQzVDNjU3NjVCQUU1OEQ2NTlFRjZDOEI3QkIyQkRBRkY0NDJDMzUzM0E1OThBMkNCQTRBQzMwODM4QTFBMEI5OEVEODE7dT0xNjYzNTAxMzE2MzU3NTQzNjk3O2g9OWNlMGJjMWY0YTU0ZjlmMDE3NDIwZTkxMDNhMzI1ZjU=; crookie=AVTGKphB2I997JrfXV6AU4ZaD/cNmfZ6FkDjTW8yrRYLMJ1f3Ld6aqrObOzt25LH0HkBrBK3s9J0QJajWjW8Ev3b4mE=; cmtchd=MTY2MzUwMTMxNzIyNA==; yandex_login=; i=LH+2H7FX0yBnkv9F7r4aDigiucJVED+AW7TqhV0WvZsei0Ej8eh6a9cfzr1pyGp4CE9neor71hVKs6TcDxeBv5QmgLs=; los=1; bltsr=1; Session_id=noauth:1663691979; ys=udn.cDprb3Ntb3N0YXI5cg%3D%3D%23c_chck.1562940119#c_chck.2705818414; mda2_beacon=1663691979362; _ym_isad=1; from=direct; _yasc=08lMmd6IuT9w87MlncTN8qiJ3PdIRXgcaw2IXWsyl1pIfIgh; layout-config={\"win_width\":663,\"win_height\":821}; from_lifetime=1663699062256; _ym_d=1663699063",
      "Referer": "https://auto.ru/moskovskaya_oblast/cars/lamborghini/all/?year_to=2019&year_from=2005",
      "Referrer-Policy": "no-referrer-when-downgrade"
    },
    "body": "{\"year_from\":" + str(year_from)+ ",\"year_to\":" + str(year_to) +",\"catalog_filter\":[{\"mark\":\"LAMBORGHINI\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_id\":[1]}",
    "method": "POST"
  })

  response_json = lambo_response.json()
  return response_json["offers"]


lambos = get_lambos(2005, 2019)

for lambo in lambos:
  mark_info = lambo["vehicle_info"]["mark_info"]["name"]
  model_info = lambo["vehicle_info"]["model_info"]["name"]
  price = lambo["price_info"]["RUR"]
  print(f'Автомобиль {mark_info} {model_info} стоит {price} руб.')