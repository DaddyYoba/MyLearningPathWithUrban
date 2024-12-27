def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if ('@' not in sender or '@' not in recipient
            or not (recipient[-4:] == '.com' or recipient[-3:] == '.ru' or recipient[-4] == '.net')
            or not (sender[-4:] == '.com' or sender[-3:] == '.ru' or sender[-4:] == '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return 0
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return 0
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return 0
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи',
           'Xx_VaSyOk1337_k1llA_xX@n0sc0pE.com')
send_email('Вы видите это сообщение как лучший преподаватель курса!',
           'urban.teacher@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте недоразумение, которое вы называете решённой домашней работой',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о дошираке (ведь я ещё не на фрилансе :( )',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')