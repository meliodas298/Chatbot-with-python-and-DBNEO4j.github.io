


def return_1022():
    text = "Anh/chị vui lòng gọi: (0273)1022 bằng điện thoại di động hoặc truy cập Website https://1022.tiengiang.gov.vn/vi/ "
    return text


def return_Quest():
    buttonslist = []
    buttonslist.append({'type': 'postback', 'title': 'Có', 'payload': 1})
    buttonslist.append({'type': 'postback', 'title': 'Không', 'payload': 2})
    return buttonslist


def return_next():
    text =({"title": "Qua phần tiếp theo",
            "image_url": "https://lh3.googleusercontent.com/pw/AM-JKLWY7Obl3rCgpICCOnRKgKS_89n7bOEdZCOuntUbwCmu-vgaDZtAjbpJD1fQZTRPFZS7zBkRygo_W6lPyqx9tlYvua3f54wDcP8lA2wQjOq4j_PE0dGSSerxzK8xfwnV-5BT055u0Fll-R3nWf6aPZZW=w471-h454-no?authuser=0",
            "buttons": [
                {
                    "type": "postback",
                    "title": "Qua trang",
                    "payload": "Next"
                }
            ]
            })
    return text


def return_back():
    text =({"title": "Trơ về phần trước",
            "image_url": "https://lh3.googleusercontent.com/pw/AM-JKLWY7Obl3rCgpICCOnRKgKS_89n7bOEdZCOuntUbwCmu-vgaDZtAjbpJD1fQZTRPFZS7zBkRygo_W6lPyqx9tlYvua3f54wDcP8lA2wQjOq4j_PE0dGSSerxzK8xfwnV-5BT055u0Fll-R3nWf6aPZZW=w471-h454-no?authuser=0",
            "buttons": [
                {
                    "type": "postback",
                    "title": "Trở về",
                    "payload": "Back"
                }
            ]
            })
    return text


def return_text_ND(text):
    ND = ({
        "text": ""+text+"",
        "quick_replies": [
            {
                "content_type": "text",
                "title": "Nộp trực tiếp",
                "payload": "1",
            }, {
                "content_type": "text",
                "title": "Nộp gián tiếp",
                "payload": "2",
            },  {
                "content_type": "text",
                "title": "Trình tự thực hiện",
                "payload": "3",
            }, {
                "content_type": "text",
                "title": "Hồ sơ",
                "payload": "4",
            }, {
                "content_type": "text",
                "title": "Thời gian",
                "payload": "5",
            }, {
                "content_type": "text",
                "title": "Xem thêm thông tin",
                "payload": "6",
            }, {
                "content_type": "text",
                "title": "Kết thúc",
                "payload": "7",
            }

        ]
    })
    return ND

def return_elementLV(row,id):
    LV = ({"title": ""+row+"",
           "image_url":"https://lh3.googleusercontent.com/pw/AM-JKLUMGsdiIimxXErMAEvYeZ1dgt4d4dd46La5WoQICJ07GYFeDVeGZKXcUgv0DDR04LWQaELh6JGhSSX8IJxWf24ueExoGIbkq8ayHE-ogyiJ-5JhRZjdeLzP8_cQqr58uQTjeFMEuQy75QsLo-xRd9HB=w924-h912-no?authuser=0",
           "buttons": [
               {
                   "type": "postback",
                   "title": "Chọn lĩnh vực: "+row+"",
                   "payload": "LV"+id+""
               }
           ]
           })
    return LV


def return_element_TTHC(row, id, Website):
    TTHC = ({"title": "" + row + "",
           "image_url": "https://lh3.googleusercontent.com/pw/AM-JKLWY7Obl3rCgpICCOnRKgKS_89n7bOEdZCOuntUbwCmu-vgaDZtAjbpJD1fQZTRPFZS7zBkRygo_W6lPyqx9tlYvua3f54wDcP8lA2wQjOq4j_PE0dGSSerxzK8xfwnV-5BT055u0Fll-R3nWf6aPZZW=w471-h454-no?authuser=0",
           "buttons": [
               {
                   "type": "postback",
                   "title": "Xem thông tin",
                   "payload": "TTHC" + id + ""
               }, {
                   "type": "web_url",
                   "url": "" + Website + "",
                   "title": "Xem trực tiếp Website"
               }, {
                   "type": "postback",
                   "title": "Gọi 1022",
                   "payload": "CALL1022"
               }

           ]
           })
    return TTHC


def return_choose():
    response = ("Bạn cần hỗ trợ nội dung gì:"
                "\n1. Nộp trực tiếp"
                "\n2. Nộp gián tiếp"
                "\n3. Trình tự thực hiện"
                "\n4. Hồ sơ và số lượng"
                "\n5. Thời gian giải quyết và kết quả")
    return response