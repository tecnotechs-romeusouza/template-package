/**
 *
 * @abstract Imagens, resultados e histograms
 * @author Romeu Souza
 * @category biblioteca pyplot
*/

import matplotlib.pyplot as plt 

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap = 'gray')
    plt.axis('off')
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows = 1, ncols = number_images, figsize = (12, 4))
    names_list = ["image {}".format(i) for i in range(1, number_images)]
    names_list.append('Result')
    for ax, name, image in zip(axis, names_list, args):
        ax.set_title(name)
        ax.imshow(image, cmap = 'gray')
        ax.axis('off')    
    fig.tight_layout() 
    plt.show()


def plot.histogram(image):
    fig, axis = plt.subplots(nrows = 1, ncols =  3, figsize = (12, 4), sharey=True)
    color_list = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{}.histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins = 256, color = color, alpha = 0.0)
    fig.tight_layout()
    plt.show()        