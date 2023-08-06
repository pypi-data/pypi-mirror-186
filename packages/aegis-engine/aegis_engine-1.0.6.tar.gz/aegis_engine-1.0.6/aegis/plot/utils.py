import matplotlib.pyplot as plt

def plot(id, series):
    plt.figure(id)

    # Put a single series argument into a list of 1 length so it 
    # still works for iteration --> allows any number of series to
    # be used without worrying about plotting
    if len(series) == 1:
        series = [series]

    for data in series:
        x = data.index
        y = data.values
        plt.plot(x,y)

    plt.title(id)
    plt.show()