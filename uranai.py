import re
import time
import random
import IPython
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://3.bp.blogspot.com/-qbORCFE5qhk/UmTBJwEYKjI/AAAAAAAAZYY/nbjieynFcLQ/s800/job_uranaishi.png'
YOUR_ICON = 'https://3.bp.blogspot.com/-nHZhTWISMxk/Vw5KxMQxRhI/AAAAAAAA5tQ/HR_btIW3k1ISG3GGNG1HFpsgk38wSuGzwCLcB/s800/nuigurumi_bear.png'

def run_chat(chat = chat, start='こんにちは!占いの館へようこそ!この館では、３つの占いを通してあなたを必ずハッピーにします!では早速、占いをはじめましょう!', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'Master')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)
    
  # フレーム 状態をもつ辞書
# 'name', 'birthday', 'asking'
frame = {}
TYPE = []

def number(x):
  number = list(x)
  number = [''.join( x for x in number if x not in '\n')]
  number = sum([[*word] for word in number], [])
  m = re.compile('^[0-9]+$')
  result = [s for s in number if m.match(s)]
  number = list(map(int, result))
  #sn = sum(int(c) for c in number) 
  return len(number)


def match(x):
  Match = list(x)
  Match = ''.join( x for x in Match if x not in '\n') 
  pattern = r'\d\d'
  result = re.match(pattern, Match)
  if result == None:
    return 'None'


def soulnumber(X):
  number = [''.join( x for x in X if x not in '\n')]
  number = sum([[*word] for word in number], [])
  m = re.compile('^[0-9]+$')
  result = [s for s in number if m.match(s)]
  number = list(map(int, result))
  sn = sum(int(c) for c in number)
  if sn % 11 == 0: # ゾロ目の時
    return sn
  if sn > 9: #２桁の時は
    return soulnumber(str(sn)) #再帰を使う
  return sn


def uranai(input_text):
  global frame # 外部の状態を参照する
  if 'asking' in frame:  # asking から更新する
    frame[frame['asking']] = input_text
    del frame['asking']

  if 'name' not in frame:
    frame['asking'] = 'name' # 名前をたずねる  
    return 'あなたの名前は？'

  if frame['name'] == '\n':
    del frame['name']
    frame['asking'] = 'name'
    return '名前が入力されていないようです。もう一度、あなたのお名前を入力してください。'

  if 'name' in frame and 'year' not in frame:
    frame['asking'] = 'year' # 誕生年をたずねる    
    return 'あなたの生まれた年を西暦(４桁)で教えてください(ex:平成12年生まれの場合は2000と入力)。'

  if 'name' in frame and (number(frame['year']) != 4 or match(frame['year']) == 'None'):
    del frame['year']
    frame['asking'] = 'year' # 誕生年をたずねる    
    return '正しく入力されていないようです。もう一度、あなたの生まれた年を西暦(４桁)で教えてください(ex:平成12年生まれの場合は2000と入力)。'
  
  if 'name' in frame and 'year' in frame and 'month' not in frame:
    frame['asking'] = 'month' # 誕生月をたずねる    
    return 'あなたの生まれた月を２桁で教えてください(ex:1月生まれの場合は01と入力)。'

  if 'name' in frame and 'year' in frame and (number(frame['month']) != 2 or match(frame['month']) == 'None'):
    del frame['month']
    frame['asking'] = 'month' # 誕生月をたずねる    
    return '正しく入力されていないようです。もう一度、あなたの生まれた月を２桁で教えてください(ex:1月生まれの場合は01と入力)。'

  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' not in frame:
    frame['asking'] = 'day' # 誕生日をたずねる    
    return 'あなたの生まれた日を２桁で教えてください(ex:1日生まれの場合は01と入力)。'

  if 'name' in frame and 'year' in frame and 'month' in frame and (number(frame['day']) != 2 or match(frame['day']) == 'None'):
    del frame['day']
    frame['asking'] = 'day' # 誕生日をたずねる    
    return '正しく入力されていないようです。もう一度、あなたの生まれた日を２桁で教えてください(ex:1日生まれの場合は01と入力)。'  

  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and 'type' not in frame: # 占います
    frame['asking'] = 'type'
    return 'この館では、計算したソウルナンバーをもとに３つの占いができます!Aでは性格やタイプを、Bでは同じソウルナンバーを持つ有名人を、Cではラッキーカラーを診断します！！！A,B,Cのうちどれか１文字を入力してください。'

  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and frame['type'] != '\nA' and frame['type'] != '\nB' and frame['type'] != '\nC': # 占います
    del frame['type']
    frame['asking'] = 'type'
    return '正しく入力されていないようです。もう一度、A,B,Cのうちどれか１文字を入力してください。'


  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and 'type' in frame and 'manzoku' not in frame:
    if frame['type'] == '\nA':
      #number = list(frame['year']) + list(frame['month']) + list(frame['day'])
      TYPE.append('A')
      soul = soulnumber(list(frame['year']) + list(frame['month']) + list(frame['day']))
      if soul == 1:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが1のあなたは、素晴らしい行動力の持ち主で、頭の回転が速く、周りからも頼られる存在ですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 2:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが2のあなたは、さっぱりした兄貴肌・姉貴肌的な性格で、バランス調整力が高い人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 3:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが3のあなたは、平和主義者で洞察力が高く、周りからも慕われる存在のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 4:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが4のあなたは、外向的で積極的なリーダー気質で、周りに影響力を与えられるような存在のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 5:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが5のあなたは、真面目で曲がったことが嫌いで、自分の道を突き進む人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 6:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが6のあなたは、社交的で、情け深く、頭の回転が速い人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 7:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが7のあなたは、優しく、家庭的で、探求心が強い人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 8:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが8のあなたは、穏やかな性格で純粋な人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 9:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが9のあなたは、さびしがり屋さんで、やんちゃな部分もある、憎めない人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 11:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが11のあなたは、直感が鋭い人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 22:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが22のあなたは、判断力が強く、諦めない人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 33:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが33のあなたは、天才肌な人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      else:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが44のあなたは、問題解決能力が高く、リーダー気質で、考えが鋭い人のようですね!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'

    if frame['type'] == '\nB':
      #number = list(frame['year']) + list(frame['month']) + list(frame['day'])
      TYPE.append('B')
      soul = soulnumber(list(frame['year']) + list(frame['month']) + list(frame['day']))
      if soul == 1:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ1のソウルナンバーを持つ有名人には、お笑いタレントの春日俊彰さんや俳優の成田凌さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 2:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ2のソウルナンバーを持つ有名人には、歌手の和田アキ子さんや俳優の山﨑賢人さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 3:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ3のソウルナンバーを持つ有名人には、俳優の生瀬勝久さんや女優の天海祐希さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 4:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ4のソウルナンバーを持つ有名人には、お笑いタレントの渡辺直美さんや女優の米倉涼子さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 5:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ5のソウルナンバーを持つ有名人には、予備校講師の林修先生やタレントの国分太一さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 6:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ6のソウルナンバーを持つ有名人には、女優の深田恭子さんや歌手の米津玄師さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 7:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ7のソウルナンバーを持つ有名人には、女優の新垣結衣さんや長澤まさみさんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 8:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ8のソウルナンバーを持つ有名人には、プロフィギュアスケーターの浅田真央さんやプロ野球選手の大谷翔平選手など多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 9:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ9のソウルナンバーを持つ有名人には、女優の北川景子さんやお笑いタレントの松本人志さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 11:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ11のソウルナンバーを持つ有名人には、お笑いタレントの上田晋也さんや女優の杉咲花さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 22:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ22のソウルナンバーを持つ有名人には、お笑いタレントの博多大吉さんや女優の小池栄子さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 33:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ33のソウルナンバーを持つ有名人には、俳優の福山雅治さんや歌手のあいみょんさんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      else:
        frame['asking'] = 'manzoku'
        return 'あなたと同じ44のソウルナンバーを持つ有名人には、アイドルの岸優太さんや女優の中村静香さんなど多くの有名人がいらっしゃいます!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'

    if frame['type'] == '\nC':
      TYPE.append('C')
      soul = soulnumber(list(frame['year']) + list(frame['month']) + list(frame['day']))
      if soul == 1:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが1のあなたのラッキーカラーは、レッドです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 2:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが2のあなたのラッキーカラーは、ホワイト、オレンジ、ブルーです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 3:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが3のあなたのラッキーカラーは、イエローです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 4:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが4のあなたのラッキーカラーは、グリーン、ブラウン、ブルーです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 5:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが5のあなたのラッキーカラーは、グリーンとピンクです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 6:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが6のあなたのラッキーカラーは、ピンクです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 7:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが7のあなたのラッキーカラーは、ネイビーです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 8:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが8のあなたのラッキーカラーは、オレンジです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 9:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが9のあなたのラッキーカラーは、パープルとホワイトです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 11:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが11のあなたのラッキーカラーは、シルバーです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 22:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが22のあなたのラッキーカラーは、ゴールド、シルバー、グリーンです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      elif soul == 33:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが33のあなたのラッキーカラーは、レインボーです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'
      else:
        frame['asking'] = 'manzoku'
        return 'ソウルナンバーが44のあなたのラッキーカラーは、ブラウンです!参考にしてみてください!この占い結果に満足できた場合はYを、満足できなかった場合はNを入力してください。'

  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and 'type' in frame and frame['manzoku'] != '\nY' and frame['manzoku'] != '\nN':
    del frame['manzoku']
    frame['asking'] = 'manzoku'
    return '正しく入力されていないようです。もう一度、YかNのどちらか１文字を入力してください。'

  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and 'type' in frame and frame['manzoku'] == '\nY':
    return 'よかったです!また占いしにきてくださいね!'
  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and 'type' in frame and frame['manzoku'] == '\nN' and len(TYPE) < 3:
    #TYPE.append(frame['type'])
    del frame['type']
    del frame['manzoku']
    frame['asking'] = 'type'
    return 'ではもう１度、A(性格やタイプ)、B(同じナンバーを持つ有名人)、C(ラッキーカラー)を選択し、A,B,Cのうちどれか１文字を入力してください。次の占いであなたをハッピーにさせてみせます!'
  
  if 'name' in frame and 'year' in frame and 'month' in frame and 'day' in frame and 'type' in frame and frame['manzoku'] == '\nN' and len(TYPE) >= 3:
    return 'A,B,Cの占いであなたをハッピーにさせることができずに申し訳ないです。でも占いでは見つけることのできなかったあなたの魅力は必ずあるはずです!!元気を出してください!!!'
  
  
  return output_text

def start():
  run_chat(chat=uranai)
