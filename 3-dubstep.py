def song_decoder2(text):
    flag = 0
    st = []
    for sym in text.strip():
        if sym == ' ':
            flag += 1
            if flag > 1:
                continue
        else:
            flag = 0
        st.append(sym)
    return "".join(st)


def song_decoder(text):
    return " ".join(text.split())


assert song_decoder("A B C"), "A B C" == "1   should be replaced by 1 space"
assert song_decoder("A   B   C") == "A B C","2 multiples   should be replaced by only 1 space"
assert song_decoder(" A B C ") == "A B C","3 heading or trailing spaces should be removed"
assert song_decoder("Q QQ I  WW JOPJPBRH") == 'Q QQ I WW JOPJPBRH'