def check_bingo(bingo_card, selected_words):
    """ビンゴが達成しているかどうかを判定する関数

    引数
    ----------
    bingo_card : list型
        ビンゴカードの各行を要素とする2次元リスト　例：[[行1],[行2],[行3], ...]
    selected_words : list型
        選ばれた単語を要素とするリスト

    戻り値
    -------
     'yes'または'no' : str型
    """

    line_count = len(bingo_card)

    # ビンゴカードの全ての要素をFalseとするマーク用のカードを作成
    mark_card = [[False] * line_count for i in range(line_count)]

    # 選ばれた単語とビンゴカードの単語が一致した場合は、マーク用カードの該当要素をFalseからTrueに変える
    for word in selected_words:
        for i in range(line_count):
            for j in range(line_count):
                if bingo_card[i][j] == word:
                    mark_card[i][j] = True
                    break
            else:
                continue
            break

    # マーク用カードの各行に対しビンゴかどうか(全ての要素がTrueであるか)を判定する
    for i in range(line_count):
        if all(mark_card[i]):
            return "yes"

    # マーク用カードの各列に対しビンゴかどうか(全ての要素がTrueであるか)を判定する
    for j in range(line_count):
        column = [mark_card[i][j] for i in range(line_count)] # 縦列のリストを生成
        if all(column):
            return 'yes'

    # 左上から右下の斜めの列に対しビンゴかどうか(全ての要素がTrueであるか)を判定する
    diagonal1 = [mark_card[i][i] for i in range(line_count)] # 斜め列のリストを生成
    if all(diagonal1):
        return 'yes'

    # 左下から右上の斜めの列に対しビンゴかどうか(全ての要素がTrueであるか)を判定する
    diagonal2 = [mark_card[i][line_count-i-1] for i in range(line_count)] # 斜め列のリストを生成
    if all(diagonal2):
        return 'yes'

    return 'no'

# 入力処理
S = int(input())
bingo_card = [input().split() for i in range(S)]
N = int(input())
selected_words = [input() for i in range(N)]

# ビンゴ判定関数の実行
print(check_bingo(bingo_card, selected_words))
