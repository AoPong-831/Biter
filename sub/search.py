import os

def getFolderCapa(path_):
    capa = 0
    try:#[エラー]アクセス拒否の対処
        with os.scandir(path_) as it:#フォルダを開く
            for entry in it:
                if entry.is_file():#ファイルの場合、容量を記録(追加)
                    capa += entry.stat().st_size
                elif entry.is_dir():#フォルダの場合、さらに中のファイルを開く
                    try:#[エラー]アクセス拒否の対処
                        capa += getFolderCapa(entry.path)
                    except(PermissionError):
                        print("アクセスが拒否されました。[{0}]".format(path_))
                        next#飛ばして続きから
    except(PermissionError):
        print("アクセスが拒否されました。[{0}]".format(path_))
        next
    return capa

def getCapa(files,path):
    capacity = []
    for i in files:
        capa = 0
        path_ = path +"\\"+ i#フォルダの中身のパス取得
        if os.path.isfile(path_):#ファイルの容量取得
            capa = os.path.getsize(path_)
        else:#フォルダの容量取得
            capa = getFolderCapa(path_)
        capacity.append(capa)
    return capacity

def println(mydict,files,capacity):
    for i in mydict:
        print(*i)
        
def main(path):
    #for i in range(1):
    #    path = input("input path >")#ファイルパスを入力
    try:
        files = os.listdir(path)
        print()
        print("pass : " + path)
        capacity = getCapa(files,path)#フォルダ内のファイル名と容量をリスト化
    except(FileNotFoundError):
        print("[error] 指定されたパスが見つかりません。",path)
        return 1 #エラーコード
    except(OSError):
        print("[error] ファイル名、ディレクトリ名、またはボリューム ラベルの構文が間違ってい ます。",path)
        return 2 #エラーコード
    except:
        print("[error] 不明なエラー",path)
        return 0 #エラーコード 
    mydict = {}
    for j in range(len(files)):#ファイル名と容量を辞書に入れる
        mydict[files[j]] = capacity[j]
    mydict = sorted(mydict.items(),key=lambda x:x[1])#容量の昇順に整列
    println(mydict,files,capacity)#一覧表示
    
    return mydict