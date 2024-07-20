def send_email(message, recipient, *, sender="university.help@gmail.com"):

    exam_1 = None
    exam_2 = None
    ends = [".com", ".ru", ".net"]
    end_1 = None
    end_2 = None

    if "@" in recipient:
        for i in range(len(ends)):
            if ends[i] in recipient:
                end_1 = 1
        if end_1 == 1:
            exam_1 = True
        else:
            exam_1 = False
    else:
        exam_1 = False


    if "@" in sender:
        for i in range(len(ends)):
            if ends[i] in sender:
                end_2 = 1
        if end_2 == 1:
            exam_2 = True
        else:
            exam_2 = False
    else:
        exam_2 = False

    if exam_1 == False or exam_2 == False:
        print("Невозможно отправить письмо с адреса", sender, " на адрес", recipient)

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient,".")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, " на адрес", recipient, ".")

send_email("example_1", "katrin@mail.ru", sender="git@gmail.com")
send_email("example_2", "katrin@mail.ru")
send_email("example_3", "university.help@gmail.com", sender="university.help@gmail.com")
send_email("example_4", "katrin")
send_email("example_5", "katrin@mail")
send_email("example_6", "katrin@mail.ru", sender="university.help@gmail")