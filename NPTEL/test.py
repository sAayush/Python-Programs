def orangecap(d):
    scr = dict()
    for msc in d:
        for p in d[msc]:
            if p in scr:
                scr[p] += d[msc][p]
                print(scr)
            else:
                scr[p] = d[msc][p]
                print(scr)

    pn = str()
    tscr = 0
    for p in scr:
        if scr[p] > tscr:
            tscr = scr[p]
            pn = p

    return (pn, tscr)

d = {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
print(orangecap(d)) # ('player3', 100)


