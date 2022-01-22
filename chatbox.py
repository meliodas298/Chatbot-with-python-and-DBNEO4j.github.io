from flask import Flask, request
from pymessenger import Bot
from DB_NEO4J import *
from Return_CB import *

app = Flask(__name__)

VERIFY_TOKEN = 'Chatbot'
PAGE_ACCESS_TOKEN = 'EAAJBID5bvRoBAEQJyItgnlRehfiHzIJEhUQrtiIga1YDDHhtkrjWY5bn4lotiwEcBMfuCczug1bWzlB1AHi68DYp6cI6Wx2nUFwCSSiZAMfDFdhBDJyXiCyhROwNiXQnKz6AFVfCq6WJ7m3HhtCxzU0qkta9vSZADb8RAl6PfJk3QuEpC3tv3Q3LCDcZANEqvwGZCVfKdQZDZD'
                    #EAAJBID5bvRoBALd1taQh0BIsCVZCELgv5QL9e8r1Ck0aG9rw2h9NkC8OJpLfUUtuJ8Yk26FKmYWfhZBZBsxYTHNAiKbOA73ZBXUUBu6fDmOLJ6p0jN16mhqZCg0kJThsWFPhF53JYmPFwpKyZBESTWA7DqW0QBU7t8NV6927EdMgJkPHcqqydPKdmo2bdUcMYZA2NumKhg46gZDZD
bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "abc"
    elif request.method == "POST":
        payload = request.json
        app = App("bolt://localhost:7687", "Thongtin", "Tt123")
        print(payload)
        print(ID)
        print(ID_Chat)
        if 'postback' in payload['entry'][0]['messaging'][0]:
            event = payload['entry'][0]['messaging']
            for msg in event:
                text = msg['postback']['payload']
                sender_id = msg['sender']['id']
                for i, a in enumerate(ID):
                    if a == sender_id:
                        if text == "1":
                            response = "Hãy chọn một lĩnh vực Anh/Chị cần hỗ trợ:"
                            bot.send_text_message(sender_id, response)
                            bot.send_generic_message(sender_id, app.findLV())
                        elif text[0:2] == "LV":
                            maxtthc, response = app.find_TTHC(int(text[2]), 1)
                            response_text = "Anh/Chị Hãy chọn một Thủ tục hành chính cần hỗ trợ (nếu không tìm thấy vui lòng chọn qua trang):"
                            bot.send_text_message(sender_id, response_text)
                            bot.send_generic_message(sender_id, response)
                            ID_Chat[i] = list(ID_Chat[i])
                            ID_Chat[i][0] = text[2]
                            ID_Chat[i] = "".join(ID_Chat[i])
                        elif text[0:4] == "TTHC":
                            if len(text) ==5:
                                ID_Chat[i] = list(ID_Chat[i])
                                ID_Chat[i][2] = text[4]
                                ID_Chat[i] = "".join(ID_Chat[i])
                            else:
                                ID_Chat[i] = list(ID_Chat[i])
                                ID_Chat[i][1:3] = text[4:6]
                                ID_Chat[i] = "".join(ID_Chat[i])
                            response = "Chọn một nội dung cần hỗ trợ:"
                            bot.send_message(sender_id, return_text_ND(response))
                        elif(text == "CALL1022"):
                            bot.send_text_message(sender_id, return_1022())
                        elif(text == "Next"):
                            maxtthc, response = app.find_TTHC(int(ID_Chat[i][0]), 0)
                            bot.send_generic_message(sender_id, response)
                        elif (text == "Back"):
                            maxtthc, response = app.find_TTHC(int(ID_Chat[i][0]), 1)
                            bot.send_generic_message(sender_id, response)
                        elif text == "2":
                            response_text = "Cám ơn Anh/Chị đã ghé qua! Chúc Anh/Chị một ngày tốt lành!"
                            bot.send_text_message(sender_id, response_text)
                        break
        else:
            event = payload['entry'][0]['messaging']
            if 'attachments' in payload['entry'][0]['messaging'][0]['message']:
                for msg in event:
                    sender_id = msg['sender']['id']
                    for i, a in enumerate(ID):
                        if a == sender_id:
                            if ID_Chat[i][1:3] != "00":
                                response = "Bot đang phát triển tính năng này! Anh/Chị vui lòng chọn một trong các gợi ý dưới đây:"
                                bot.send_message(sender_id, return_text_ND(response))
                            elif ID_Chat[i][0] != "0":
                                maxtthc, response = app.find_TTHC(ID_Chat[i][0], 1)
                                response_text = "Bot đang phát triển tính năng này! Anh/Chị hãy chọn một Thủ tục hành chính cần hỗ trợ (nếu không tìm thấy vui lòng chọn qua trang):"
                                bot.send_text_message(sender_id, response_text)
                                bot.send_generic_message(sender_id, response)
                            else:
                                bot.send_text_message(sender_id, return_1022())
                                break
                    else:
                        ID.append(sender_id)
                        ID_Chat.append("00000")
                        text = "Anh/Chị có cần hỗ trợ gì không:"
                        bot.send_button_message(sender_id, text, return_Quest())
                        break
            else:
                for msg in event:
                    text = msg['message']['text']
                    sender_id = msg['sender']['id']
                    for i, a in enumerate(ID):
                        if a == sender_id:
                            if text == "Có" or text == "có":
                                response = "Hãy chọn một lĩnh vực Anh/Chị cần hỗ trợ:"
                                bot.send_text_message(sender_id, response)
                                bot.send_generic_message(sender_id, app.findLV())
                            elif text == "Không" or text == "không":
                                response_text = "Cám ơn Anh/Chị đã ghé qua! Chúc Anh/Chị một ngày tốt lành!"
                                bot.send_text_message(sender_id, response_text)
                            elif text == "Nộp trực tiếp":
                                response = "Trung tâm Phục vụ hành chính công tỉnh (Quầy số 08), Số 377, đường Hùng Vương, xã Đạo Thạnh, TP. Mỹ Tho, tỉnh Tiền Giang hoặc qua bưu điện."
                                bot.send_message(sender_id, return_text_ND(response))
                            elif text == "Nộp gián tiếp" or text == "nộp gián tiếp":
                                ID_Chat[i] = list(ID_Chat[i])
                                ID_Chat[i][3] = "2"
                                ID_Chat[i] = "".join(ID_Chat[i])
                                response = app.find_ND(int(ID_Chat[i][0:3]), int(ID_Chat[i][0:4]))
                                bot.send_message(sender_id, return_text_ND(response))
                            elif text == "Trình tự thực hiện" or text == "trình tự thực hiện":
                                ID_Chat[i] = list(ID_Chat[i])
                                ID_Chat[i][3] = "3"
                                ID_Chat[i] = "".join(ID_Chat[i])
                                response = app.find_ND(int(ID_Chat[i][0:3]), int(ID_Chat[i][0:4]))
                                bot.send_message(sender_id, return_text_ND(response))
                            elif text == "Hồ sơ" or text == "hồ sơ":
                                ID_Chat[i] = list(ID_Chat[i])
                                ID_Chat[i][3] = "4"
                                ID_Chat[i] = "".join(ID_Chat[i])
                                response = app.find_ND(int(ID_Chat[i][0:3]), int(ID_Chat[i][0:4]))
                                bot.send_message(sender_id, return_text_ND(response))
                            elif text == "Thời gian" or text == "thời gian":
                                ID_Chat[i] = list(ID_Chat[i])
                                ID_Chat[i][3] = "5"
                                ID_Chat[i] = "".join(ID_Chat[i])
                                response = app.find_ND(int(ID_Chat[i][0:3]), int(ID_Chat[i][0:4]))
                                bot.send_message(sender_id, return_text_ND(response))
                            elif text == "Xem thêm thông tin" or text == "xem thêm thông tin":
                                response = "Hãy chọn một lĩnh vực anh/chị cần hỗ trợ:"
                                bot.send_text_message(sender_id, response)
                                bot.send_generic_message(sender_id, app.findLV())
                            elif text == "Kết thúc" or text == "kết thúc":
                                response_text = "Cám ơn Anh/Chị đã tương tác với hệ thống! Anh/Chị có gì góp ý hoặc không hài lòng thì xin vui lòng góp ý với hệ thống thông qua mail:" \
                                                " thuan018101092@tgu.edu.vn. Mọi góp ý của Anh/Chị sẽ là động lực để hệ thống phát triển thêm."
                                bot.send_text_message(sender_id, response_text)
                            elif ID_Chat[i][1:3] != "00":
                                response = "Bot đang phát triển tính năng này! Anh/Chị vui lòng chọn một trong các gợi ý dưới đây:"
                                bot.send_message(sender_id, return_text_ND(response))
                            elif ID_Chat[i][0] != "0":
                                maxtthc, response = app.find_TTHC(ID_Chat[i][0], 1)
                                response_text = "Bot đang phát triển tính năng này! Anh/Chị hãy chọn một Thủ tục hành chính cần hỗ trợ (nếu không tìm thấy vui lòng chọn qua trang):"
                                bot.send_text_message(sender_id, response_text)
                                bot.send_generic_message(sender_id, response)
                            else:
                                bot.send_text_message(sender_id, return_1022())
                                print(text)
                            break
                        if i + 1 == len(ID):
                            # Lưu ID người dùng
                            ID.append(sender_id)
                            # Lưu và gán thông tin phản hồi người dùng dưới dạng 00000
                            ID_Chat.append("00000")
                            text = "Anh/Chị có cần hỗ trợ gì không:"
                            bot.send_button_message(sender_id, text, return_Quest())
                            # bot.send_generic_message(sender_id,return_elements())
                            break
        #    print(a, sender_id, i, len(ID))
        #    print(text, sender_id)
        #    print(ID, ID_Chat)
        #   response = process_messenge(text)
        #   bot.send_text_message(sender_id, response)
        return "message received."
    else:
        return 200


if __name__ == '__main__':
    ID = ["0"]
    ID_Chat = ["0"]
    app.run(debug=True)
# chatbox()
