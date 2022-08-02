import os

# ファイル名をCLIで取得
path = ""
while 1:
    file_name = input("ファイル名を入力してください: ")
    path= "./"+file_name+".bat"
    command = input(path+"でよろしいですか？[y/n]")
    if command == 'y':
        break

# 拡張機能を入力された分だけ取得
print("拡張機能を改行ありで貼り付けて下さい\n[Enterで入力終了します]")
exts = []
tmp = "true"
while tmp:
    tmp = input()
    if not tmp:
        break
    exts.append(tmp)

exts_n = len(exts)
print("入力された機能数は"+str(exts_n)+"でした")

# バッチファイルに書き込む内容の作成
body = "@echo off\necho start to install VSCode extentions.\n"
for i in range(exts_n):
    body+="code --install-extension "+exts[i].replace("\"", "")+" & "
    if i==exts_n-1:
        body+="echo finish installing... & pause\n"
body+="exit"

# file作成, 書き込み, 終了
file = open(path, 'w')
file.write(body)
file.close()
print(path+"にファイルを生成しました。")