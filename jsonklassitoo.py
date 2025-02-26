import json
import re

# Функция для проверки правильности email
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email)

# Ввод данных
company_name = input("Sisesta oma ettevõtte nimi: ")
contact_email = input("Sisesta oma isiklikk email address: ")

# Проверка email
while not is_valid_email(contact_email):
    print("Sisestatud e-posti aadress ei ole korrektne. Palun proovige uuesti.")
    contact_email = input("Sisesta oma isiklikk email address: ")

data_collection_type = input("Millised andmed salvestame: ")
data_usege = input("Kuidas andmed kasutatakse: ")
data_storage_limit = input("Kui kaua andem salvestatakse: ")

# Данные конфиденциальности
privacy_data = {
    "company_name": company_name,
    "contact_email": contact_email,
    "data_collection_type": data_collection_type,
    "data_usege": data_usege,
    "data_storage_limit": data_storage_limit
}

# Сохранение данных в JSON файл
with open("privacy_template.json", "w", encoding="utf-8") as file:
    json.dump(privacy_data, file, indent=4)
print("Kõik on salvestatud")

# HTML шаблон с улучшенными стилями и добавлением проверки cookies
html_template = """
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privaasuspooliitika</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f9;
        }
        h1 {
            color: #333;
            font-size: 2em;
        }
        h2 {
            color: #444;
            font-size: 1.5em;
            margin-top: 20px;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6em;
            color: #555;
        }
        #cookie-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
            text-align: center;
            padding: 10px;
            display: none;
        }
        #cookie-banner button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Poliitika pühendanud ettevõttele - {company_name}</h1>
    <p>Kontakt: <a href="mailto:{contact_email}">{contact_email}</a></p>
    <h2>Millised andmed kogume?</h2>
    <p>{data_collection_type}</p>
    <h2>Kuidas andmed kasutatakse</h2>
    <p>{data_usege}</p>
    <h2>Kui kaua andmed salvestatakse</h2>
    <p>{data_storage_limit}</p>

    <!-- Баннер cookies -->
    <div id="cookie-banner">
        <p>Me kasutame küpsiseid. Palun nõustuge meie küpsiste poliitikaga.</p>
        <button id="accept-cookies">Nõustun</button>
    </div>

    <script>
        // Проверка наличия cookies
        window.onload = function() {
            if (!getCookie("cookies-accepted")) {
                document.getElementById("cookie-banner").style.display = "block";
            }
        };

        // Установка cookie при согласии
        document.getElementById("accept-cookies").onclick = function() {
            setCookie("cookies-accepted", "true", 365); // Сохранить cookie на 365 дней
            document.getElementById("cookie-banner").style.display = "none";
        };

        // Функции для работы с cookies
        function setCookie(name, value, days) {
            var expires = "";
            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + (value || "") + expires + "; path=/";
        }

        function getCookie(name) {
            var nameEQ = name + "=";
            var ca = document.cookie.split(';');
            for (var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0) == ' ') c = c.substring(1, c.length);
                if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
            }
            return null;
        }
    </script>
</body>
</html>
"""

# Форматирование HTML-шаблона с данными
privacy_policy = html_template.format(**privacy_data)

# Сохранение HTML файла
with open("privacy_template.html", "w", encoding="utf-8") as file:
    file.write(privacy_policy)

print("HTML fail on edukalt genereeritud")
