
def smooth(series, window):
    series = series.rolling(window = window).mean()
    return series