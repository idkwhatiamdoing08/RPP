{% load static %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{% static 'main/css/navigation.css' %}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="{% static 'main/css/form.css' %}">
    <link rel="stylesheet" href="{% static 'main/css/data_table.css' %}">

</head>
    <body>
        {% include 'main/navigation.html' %}
        {% include 'main/registrationButtons.html' %}
        <div class="center_table">
            <form class="table_change_form" method="post">
                {% csrf_token %}
                {% for d in form %}
                    {% if forloop.counter == 1 %} <div class="name">{{names.0}}</div> {% endif %}
                    {% if forloop.counter == 2 %} <div class="name">{{names.1}}</div> {% endif %}
                    {% if forloop.counter == 3 %} <div class="name">{{names.2}}</div> {% endif %}
                    {% if forloop.counter == 4 %} <div class="name">{{names.3}}</div> {% endif %}
                    {% if forloop.counter == 5 %} <div class="name">{{names.4}}</div> {% endif %}
                    {% if forloop.counter == 6 %} <div class="name">{{names.5}}</div> {% endif %}
                    {% if forloop.counter == 7 %} <div class="name">{{names.6}}</div> {% endif %}
                    {% if forloop.counter == 8 %} <div class="name">{{names.7}}</div> {% endif %}
                    {% if forloop.counter == 9 %} <div class="name">{{names.8}}</div> {% endif %}
                    {{d}}
                {% endfor %}
                <div style="color: white;">{{error}}</div>
                <button class="confirm_button button" type="submit">Подтвердить</button>
            </form>
        </div>
    </body>
</html>
