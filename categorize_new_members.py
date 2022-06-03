def open_or_senior(data):
    n = 0
    results = []
    for i in data:
        if data[n][0] >= 55 and data[n][1] > 7:
            results.append('Senior')
            n += 1
        else:
            results.append('Open')
            n += 1
    return results