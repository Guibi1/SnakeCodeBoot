# Snake
snakeHead = """#000#463#463#6b3#6b3#6b3#6b3#6b3#463#463#000
#000#463#6b3#9d5#9d5#9d5#9d5#9d5#6b3#463#000
#000#6b3#9d5#9d5#9d5#9d5#9d5#9d5#9d5#6b3#000
#000#9d5#9d5#9d5#9d5#9d5#9d5#9d5#9d5#9d5#000
#000#9d5#fff#000#9d5#9d5#9d5#fff#000#9d5#000
#000#9d5#9d5#9d5#9d5#9d5#9d5#9d5#9d5#9d5#000
#000#000#fe3#9d5#6b3#9d5#6b3#9d5#fe3#000#000
#000#000#000#fe3#fe3#fe3#fe3#fe3#000#000#000
#000#000#000#000#000#e00#000#000#000#000#000
#000#000#000#000#e00#e00#e00#000#000#000#000
#000#000#000#000#e00#000#e00#000#000#000#000"""

snakeLine = """#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#9d5#463#463#463#9d5#000#000#000
#000#000#000#463#223#223#223#463#000#000#000
#000#000#000#223#223#223#223#223#000#000#000
#000#000#000#223#6b3#6b3#6b3#223#000#000#000
#000#000#000#6b3#9d5#9d5#9d5#6b3#000#000#000
#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000"""

snakeCorner = """#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#9d5#9d5#9d5#9d5#463#000#000#000
#000#000#000#9d5#9d5#463#463#223#223#000#000
#000#000#000#9d5#463#223#223#223#6b3#9d5#9d5
#000#000#000#463#223#223#223#6b3#9d5#9d5#9d5
#000#000#000#223#223#223#6b3#9d5#9d5#9d5#9d5
#000#000#000#000#223#6b3#9d5#9d5#9d5#9d5#9d5
#000#000#000#000#000#9d5#9d5#9d5#9d5#9d5#9d5
#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000"""

snakeTail = """#000#000#000#9d5#9d5#9d5#9d5#9d5#000#000#000
#000#000#000#6b3#9d5#9d5#9d5#6b3#000#000#000
#000#000#000#6b3#9d5#9d5#9d5#6b3#000#000#000
#000#000#000#000#6b3#9d5#6b3#000#000#000#000
#000#000#000#000#6b3#9d5#6b3#000#000#000#000
#000#000#000#000#000#6b3#000#000#000#000#000
#000#000#000#000#000#6b3#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000
#000#000#000#000#000#000#000#000#000#000#000"""

# Apple
apple = """#000#000#000#000#000#000#472#8d4#000#000#000
#000#000#c22#b22#000#6a3#6a3#8d4#c22#000#000
#000#d33#e55#e66#c22#6b3#7c4#d33#c22#d33#000
#000#d55#f77#e44#b22#b22#b22#d33#b22#b22#d33
#b22#e55#d33#b22#c22#b22#b22#b22#b22#b22#b22
#b22#b22#c22#c22#b22#b22#b22#b22#b22#b11#b22
#c22#b22#b22#b22#c22#b11#b22#b22#b22#b11#b22
#000#c22#c22#b11#b22#b11#b11#b11#b11#b11#b11
#000#b11#b22#c22#b11#b11#b11#b11#b11#b11#000
#000#000#b22#b11#b11#b11#b11#b11#b11#000#000
#000#000#000#b22#b11#000#b11#b11#000#000#000"""

gapple = """#000#000#000#fe3#000#000#472#8d4#000#000#000
#000#000#fe3#ff7#fe3#6a3#6a3#8d4#fd2#000#000
#000#fe7#fea#fe3#ffe#6b3#7c4#fd6#fd7#fe3#000
#000#fea#ffd#ffd#ffe#ffe#fec#fe9#fe3#ff7#fe3
#fd4#fe9#fea#ffd#ffd#ffd#fec#fe8#fd5#fe3#fd5
#fd6#fea#ffe#ffe#ffd#feb#feb#fd5#fd7#fd2#fd4
#fe8#fe9#ffd#fec#fe8#fe8#fd4#fd5#fd5#fd4#fd3
#000#fe8#fd2#fd7#fd7#fea#fe8#fd2#fd3#fd3#ec3
#000#fe3#fd6#fd4#fd5#fd7#fd3#fc3#fc2#fd2#000
#fe3#ff7#fe3#fd5#fd3#fd3#fc2#ec3#fc2#000#000
#000#fe3#000#fd4#fd2#000#fc1#fd3#000#000#000"""

toxicApple = """#000#000#000#000#000#000#323#343#000#000#000
#000#000#000#000#000#453#453#683#a7b#000#000
#000#000#000#000#546#343#a8b#656#97a#a7b#000
#000#000#000#000#333#546#222#656#545#869#747
#000#000#000#213#111#435#222#111#435#869#425
#000#000#213#111#111#545#222#222#324#647#424
#313#213#a8b#667#556#435#424#324#424#647#869
#000#a7b#a8b#a7b#435#859#859#424#758#758#536
#212#869#869#868#647#424#425#637#868#536#000
#000#000#748#868#868#868#868#868#868#000#000
#000#212#000#536#536#000#536#757#000#000#000"""

chronoApple = """#000#000#000#000#000#000#472#8d4#000#000#000
#000#000#ddd#ddd#000#444#6a3#8d4#ccc#000#000
#000#444#ddd#ccc#ddd#444#7c4#ddd#ccc#444#000
#000#eee#444#ddd#ccc#ddd#eee#ccc#444#ccc#ccc
#ddd#ddd#ddd#ddd#444#ddd#ddd#eee#ccc#ccc#ccc
#444#444#ccc#ddd#444#444#ddd#ddd#ddd#444#444
#ccc#ccc#ddd#ddd#ddd#000#ddd#ddd#ccc#ccc#eee
#000#ddd#ddd#444#ddd#ddd#444#ddd#eee#ccc#ddd
#000#eee#444#ddd#ddd#ddd#ccc#444#ddd#eee#000
#000#000#ddd#ddd#ddd#444#ddd#ddd#ddd#000#000
#000#000#000#eee#ddd#000#ddd#ddd#000#000#000"""

# Levels
grass = """#463#250#361#250#453#361#250#250#361#352#462
#453#250#463#352#361#462#454#453#473#462#361
#454#462#462#250#352#453#473#573#462#564#473
#361#361#361#352#453#454#462#250#462#250#454
#361#250#473#453#453#454#564#463#250#250#361
#352#361#462#462#462#454#361#453#250#454#250
#462#462#462#473#453#361#361#453#564#361#361
#250#250#361#462#462#250#463#462#462#361#361
#250#352#462#462#462#250#462#250#462#462#250
#462#361#361#250#250#462#462#454#453#250#361
#454#473#462#462#250#463#352#250#361#361#250"""

grassFlower = """#463#250#361#250#453#361#250#250#b11#352#462
#453#250#463#352#361#462#454#c11#ff7#a33#361
#454#462#462#250#352#453#473#573#d55#ff7#c11
#361#d33#361#352#453#454#462#250#462#c33#454
#b11#ff7#711#453#453#454#564#463#250#250#361
#352#a33#462#462#462#454#361#453#250#454#250
#462#462#462#473#453#361#361#453#564#361#361
#250#250#611#462#462#250#463#462#c11#361#361
#250#a33#fe6#b33#462#250#462#911#ff7#c11#250
#462#361#a11#250#250#462#462#454#911#250#361
#454#473#462#462#250#463#352#250#361#361#250"""

fence = """#ca5#ca5#000#000#000#000#000#000#000#a84#984
#b95#ca5#ca5#b95#db6#ca5#b95#973#b94#b95#cb6
#db6#db6#983#ca5#a94#973#a84#a94#a84#db6#b95
#a84#ca5#000#000#000#000#000#000#000#db6#984
#984#b94#000#000#000#000#000#000#000#db6#b94
#db6#b95#db6#ca5#db6#db6#db6#ca5#a84#db6#b95
#ca5#db6#db6#db6#b95#a84#db6#db6#db6#b95#cb6
#b94#a94#000#000#000#000#000#000#000#cb5#db6
#cb5#a84#000#000#000#000#000#000#000#a84#a94
#ba5#a84#000#000#000#000#000#000#000#ca5#cb6
#a84#b94#000#000#000#000#000#000#000#ca5#983"""

levels = {
    "grass": {
        "normal": grass,
        "special": grassFlower,
        "block": fence,
    }
}
