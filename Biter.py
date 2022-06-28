import tkinter as tk
from sub import search
from sub import graph

def main():

    def bit(memory):#最適な値に計算
        if memory == 0:# 0byteの特例
            return "{0} Byte".format(memory)
        
        if memory < 8:# 8bit(1byte)以下
            memory = round(memory/8,2)#バイト単位に直す(1Byte = 8bit
            return "{0} Byte".format(memory)
        else:
            if memory < 2 ** (10):# 1000Byte(1KB)以下
                memory = round(memory/8,2)#バイト単位に直す(1Byte = 8bit)
                return "{0} Byte".format(memory)
            else:
                if memory < 2 ** (20):# 1000KB(1MB)以下
                    memory = round(memory/2**(10),2)#KB単位に直す(1KB = 1000Byte)
                    return "{0} KB".format(memory)
                else:
                    if memory < 2 ** (30):# 1000MB(1GB)以下
                        memory = round(memory/2**(20),2)#MB単位に直す(1MB = 1000KB)
                        return "{0} MB".format(memory)
                    else:
                        if memory < 2 ** (40):# 1000GB(1TB)以下
                            memory = round(memory/2**(30),2)#GB単位に直す(1GB = 1000MB)
                            return "{0} GB".format(memory)
                        else:
                            memory = round(memory/2**(40),2)#TB単位に直す(1TB = 1000GB)
                            return "{0} TB".format(memory)

    def makeGraph():
        print(textbox.get("1.0","end-1c"))

        files = [];capacity = []
        for i in range(len(mydict)):
            files.append(mydict[i][0])
            capacity.append(mydict[i][1])
        print("aaaaaaaaaaaa")
        graph.graph(files,capacity)

    def click_btn():
        txt = entry.get()#パスを取得
        textbox.delete("1.0","end")#textbox内をクリア
        mydict = search.main(txt)#searchにアクセス
        if mydict == 0:#エラーコード
            textbox.insert("1.0","[error] 不明なエラー。制作者までご連絡ください。: \"{0}\"".format(txt))#テキストボックスに出力
        elif mydict == 1:#エラーコード
            textbox.insert("1.0","[error] 指定されたパスが見つかりません。: \"{0}\"".format(txt))#テキストボックスに出力
        if mydict == 2:#エラーコード
            textbox.insert("1.0","[error] ファイル名、ディレクトリ名、またはボリューム ラベルの構文が間違ってい ます。: \"{0}\"".format(txt))#テキストボックスに出力
        else:#成功
            text = ""#出力変数
            for i in range(len(mydict)):
                fileName = mydict[i][0]#ファイル名
                memory1 = bit(mydict[i][1])#ファイル容量
                memory2 = mydict[i][1]#ファイル容量
                text = "{0} : {1}({2} bit)\n".format(fileName,memory1,memory2)#出力変数作成
                textbox.insert("1.0",text)#テキストボックスに出力
            print("捜査終了")#logに実行終了を通知
        #グラフ表示 ボタン設置(次回以降)
        #button2 = tk.Button(text="グラフ表示",command=makeGraph)#ボタン作成
        #button2.place(x=515,y=60)#設置

    root = tk.Tk()#window作成
    root.title("Biter")#タイトル
    root.geometry("640x480")#winのサイズ

    label = tk.Label(root,text="調べたいパスを入力してください。")#ラベル作成
    label.place(x=10,y=10)#設置

    entry = tk.Entry(width=93)#パス入力欄作成
    entry.place(x=10,y=35)#設置

    button = tk.Button(text="実行",command=click_btn)#ボタン作成
    button.place(x=10,y=60)#設置

    textbox = tk.Text(root,width=70,height=20,font=("",12))#テキストボックス作成
    textbox.place(x=10,y=90)#設置

    root.mainloop()#ループ

if __name__ == "__main__":
    main()