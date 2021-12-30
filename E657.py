import time
import sys
import json
from PIL import Image, ImageDraw,ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# E657系

def LED_display(form_json,stalist_json):

    #パラメータを保存
    parameters = json.loads(form_json)
    stalist = json.loads(stalist_json)
    
    # 使用するLEDのパラメーター(この辺はgithubのサンプルのコピペです)
    options = RGBMatrixOptions()
    options.rows = 32
    options.chain_length = 4
    options.parallel = 1
    options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
    matrix = RGBMatrix(options = options)

    Path = 'E657/pics/'
    Jpn = 'Japanese/'
    Eng = 'English/'
    Typ = 'type/'
    Des = 'destination/'
    Nst = 'next_sta/'
    Set = 'seat/'
    png = '.png'

    if (str(parameters['train_number']) == ""):
        print("種別単体表示") #未実装
        img_typ_jpn = Image.open(str(Path + Typ + Jpn + parameters['type'] + png))
    elif (str(parameters['type']) == "003" or str(parameters['type']) == "004"):
        if (int(parameters['train_number']) < 10):
            img_typ_jpn = Image.open(str(Path + Typ + Jpn + parameters['type'] + "-1" + png))  # 入力に応じた日本語種別の画像を開く
        else:
            img_typ_jpn = Image.open(str(Path + Typ + Jpn + parameters['type'] + "-2" + png))  # 入力に応じた日本語種別の画像を開く
    else:
        img_typ_jpn = Image.open(str(Path + Typ + Jpn + parameters['type'] + png))  # 入力に応じた日本語種別の画像を開く
    
    img_set_jpn = Image.open(str(Path + Set + Jpn + parameters['seat'] + png))  # 入力に応じた日本語席種の画像を開く
    img_des_jpn = Image.open(str(Path + Des + Jpn + parameters['destination'] + png))  # 入力に応じた日本語行先の画像を開く
    img_typ_eng = Image.open(str(Path + Typ + Eng + parameters['type'] + png))  # 入力に応じた英語種別の画像を開く
    img_set_eng = Image.open(str(Path + Set + Eng + parameters['seat'] + png))  # 入力に応じた英語席種の画像を開く
    img_des_eng = Image.open(str(Path + Des + Eng + parameters['destination'] + png))  # 入力に応じた英語行先の画像を開く

    if(len(str(parameters['train_number'])) == 0):
        print("種別単体表示")
    else:
        font_nojp = ImageFont.truetype('E657/fonts/E657numJP.ttf',16)
        font_noen = ImageFont.truetype('E657/fonts/E657numEN.ttf',16)
        draw_nojp = ImageDraw.Draw(img_typ_jpn)
        draw_noen = ImageDraw.Draw(img_typ_eng)
        if(str(parameters['type']) == "001"): # ときわの号数設定
            if(int(parameters['train_number']) <10): # 号数が一けたのとき
                draw_nojp.multiline_text((96,1)," " + str(parameters['train_number']),fill=(243,152,0),font=font_nojp)
                draw_noen.multiline_text((99,2),str(parameters['train_number']),fill=(243,152,0),font=font_noen)
            else: # 号数が二けたのとき
                draw_nojp.multiline_text((96,1),str(parameters['train_number']),fill=(243,152,0),font=font_nojp)
                draw_noen.multiline_text((99,2),str(parameters['train_number']),fill=(243,152,0),font=font_noen)
        elif(str(parameters['type']) == "002"): # ひたちの号数設定
            if(int(parameters['train_number']) <10):
                draw_nojp.multiline_text((96,1)," " + str(parameters['train_number']),fill=(0,127,255),font=font_nojp)
                draw_noen.multiline_text((100,2),str(parameters['train_number']),fill=(0,127,255),font=font_noen)
            else:
                draw_nojp.multiline_text((96,1),str(parameters['train_number']),fill=(0,127,255),font=font_nojp)
                draw_noen.multiline_text((100,2),str(parameters['train_number']),fill=(0,127,255),font=font_noen)
        elif(str(parameters['type']) == "003"): # フレッシュひたちの号数設定
            if(int(parameters['train_number']) < 10):
                draw_nojp.multiline_text((101,1)," " + str(parameters['train_number']),fill=(243,152,0),font=font_nojp)
                draw_noen.multiline_text((118,2),str(parameters['train_number']),fill=(243,152,0),font=font_noen)
            else:
                draw_nojp.multiline_text((102,1),str(parameters['train_number']),fill=(243,152,0),font=font_nojp)
                draw_noen.multiline_text((115,2),str(parameters['train_number']),fill=(243,152,0),font=font_noen)
        elif(str(parameters['type']) == "004"): # スーパーひたちの号数設定
            if(int(parameters['train_number']) <10):
                draw_nojp.multiline_text((101,1)," " + str(parameters['train_number']),fill=(0,127,255),font=font_nojp)
                draw_noen.multiline_text((118,2),str(parameters['train_number']),fill=(0,127,255),font=font_noen)
            else:
                draw_nojp.multiline_text((100,1),str(parameters['train_number']),fill=(0,127,255),font=font_nojp)
                draw_noen.multiline_text((115,2),str(parameters['train_number']),fill=(0,127,255),font=font_noen)

    img1 = Image.new("RGB",(128,32),(0,0,0))  # 1枚目(日本語,行先)
    img1.paste(img_typ_jpn,(0,0))
    img1.paste(img_set_jpn,(0,16))
    img1.paste(img_des_jpn,(48,16))

    img2 = Image.new("RGB",(128,32),(0,0,0))  # 2枚目(英語,行先)
    img2.paste(img_typ_eng,(0,0))
    img2.paste(img_set_eng,(0,16))
    img2.paste(img_des_eng,(48,16))

    if (parameters['departure'] == '0'):
        img_next_sta_jpn = Image.open(str(Path + Nst + Jpn + parameters['next_sta'] + png))  # 入力に応じた日本語次駅の画像を開く
        img3 = Image.new("RGB",(128,32),(0,0,0))  # 3枚目(日本語,次駅)
        img3.paste(img_typ_jpn,(0,0))
        img3.paste(img_set_jpn,(0,16))
        img3.paste(img_next_sta_jpn,(48,16))
    
    elif (parameters['departure'] == '1'):  # スクロールする場合

        fig_stop_sta = len(parameters['stop_sta'])
        start = '停車駅：'  # スクロールする文章の生成
        end = '終点　' + stalist.get(str(parameters['destination'])) + 'です。'
        text = start
        # 行先の駅番号が次駅番号より大きい場合(下り),番号が小さい方から駅を追加
        if int(parameters['destination']) >= int(parameters['next_sta']):
            i = 0
            for i in range(len(parameters['stop_sta'])):
                if (int(parameters['stop_sta'][i]) >= int(parameters['destination'])):  # 次に追加する駅が行先の場合追加を終了
                        break
                if(int(parameters['stop_sta'][i]) >= int(parameters['next_sta'])): # 下りの場合は次駅以北の駅を文章に追加
                    text = text + stalist.get(str(parameters['stop_sta'][i])) + '、'

        # 行先の駅番号が次駅番号より小さい場合(上り),番号が大きい方から駅を追加
        else:
            i = 0
            for i in range(len(parameters['stop_sta'])):
                if (int(parameters['stop_sta'][fig_stop_sta-1-i]) <= int(parameters['destination'])):  # 次に追加する駅が行先の場合追加を終了
                        break
                if(int(parameters['stop_sta'][fig_stop_sta-1-i]) <= int(parameters['next_sta'])): # 上りの場合は次駅以南の駅を文章に追加
                    text = text + stalist.get(str(parameters['stop_sta'][fig_stop_sta-1-i])) + '、'
    
        text = text + end
        leng_text_pic = len(text) * 16
        print(text)

        scroll_images = []
        i = 0
        j = 0
        sc_font = ImageFont.truetype('E657/fonts/msx-font.TTF',16)
        img_scroll = Image.new("RGB",(leng_text_pic+128,16),(0,0,0))
        draw_s = ImageDraw.Draw(img_scroll)
        draw_s.multiline_text((0,0),text,fill=(255,255,0),font=sc_font)
        while True :  # スクロール画像を生成
            ims_base = Image.new("RGB",(128,32),(0,0,0))
            ims_base.paste(img_scroll,(128-i,16))
            ims_base.paste(img_typ_jpn,(0,0))
            ims_base.paste(img_set_jpn,(0,16))
            scroll_images.append(ims_base)
            i += 1
            if i == int(leng_text_pic) + 128:
                break
        
        print(len(scroll_images))

    try:
        if (parameters['departure'] == '0'):
            while True:
                matrix.SetImage(img1)  # 1枚目を表示
                time.sleep(3)
                matrix.SetImage(img2)  # 2枚目を表示
                time.sleep(3)
                matrix.SetImage(img3)  # 3枚目を表示
                time.sleep(3)
        elif (parameters['departure'] == '1'):
            while True:
                matrix.SetImage(img1)  # 1枚目を表示
                time.sleep(3)
                matrix.SetImage(img2)  # 2枚目を表示
                time.sleep(3)
                for im_scroll in scroll_images:  # スクロール表示
                    matrix.SetImage(im_scroll)
                    time.sleep(0.016)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    form_json = '{"series": "002", "type": "002", "destination": "041", "next_sta": "005", "seat": "002", "train_number": "3", "departure": "1", "stop_sta": ["001", "002", "003", "005", "013", "018", "019", "022", "025", "027", "028", "029", "030", "031", "033", "034", "035", "036", "037", "038", "041"]}'
    stalist_json = '{"001":"品川","002":"東京","003":"上野","004":"日暮里","005":"柏","006":"我孫子","007":"取手","008":"佐貫","009":"龍ケ崎市","010":"牛久","011":"ひたち野うしく","012":"荒川沖","013":"土浦","014":"石岡","015":"友部","016":"赤塚","017":"偕楽園","018":"水戸","019":"勝田","020":"東海","021":"大甕","022":"常陸多賀","023":"日立","024":"高萩","025":"磯原","026":"大津港","027":"勿来","028":"泉","029":"湯本","030":"いわき","031":"広野","032":"Jヴィレッジ","033":"富岡","034":"大野","035":"双葉","036":"浪江","037":"原ノ町","038":"相馬","039":"亘理","040":"岩沼","041":"仙台"}'
    LED_display(form_json,stalist_json)