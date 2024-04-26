import matplotlib.pyplot as plt

def generate_image():
    labels = ['A', 'B', 'C']
    values = [200,50,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('grafico.png')
    plt.close()