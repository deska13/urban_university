from pprint import pprint

import matplotlib.lines as lines
import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image


def get_content(url, *, params=None, timeout=10):
    response = requests.get(url, params=params, timeout=timeout)
    pprint(response.json())


def post_content(url, *, data, timeout=10):
    response = requests.post(url, data=data, timeout=timeout)
    pprint(response.json())


def delete_content(url, *, timeout=10):
    response = requests.delete(url, timeout=timeout)
    pprint(response.json())


def read_img(img_name):
    img = Image.open(img_name)
    return img


def imshow_img(img_name):
    img = read_img(img_name)
    plt.imshow(img)
    plt.show()


def imshow_gray_img(img_name):
    img = read_img(img_name)
    img = img.convert("LA")
    plt.imshow(img)
    plt.show()


def imshow_rotate_img(img_name, degree):
    img = read_img(img_name)
    img = img.rotate(degree)
    plt.imshow(img)
    plt.show()


def example_stat_work_matplotlib():
    fig = plt.figure()
    fig.subplots_adjust(top=0.8)
    ax1 = fig.add_subplot(211)
    ax1.set_ylabel("Voltage [V]")
    ax1.set_title("A sine wave")

    t = np.arange(0.0, 1.0, 0.01)
    s = np.sin(2 * np.pi * t)
    ax1.plot(t, s, color="blue", lw=2)

    np.random.seed(19680801)

    ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
    ax2.hist(np.random.randn(1000), 50, facecolor="yellow", edgecolor="yellow")
    ax2.set_xlabel("Time [s]")
    plt.show()


def example_line_plot_matplotlib():
    fig = plt.figure()

    l1 = lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
    l2 = lines.Line2D([0, 1], [1, 0], transform=fig.transFigure, figure=fig)
    fig.lines.extend([l1, l2])

    plt.show()


if __name__ == "__main__":
    get_content("https://httpbin.org/get")
    post_content("https://httpbin.org/post", data={"key": "value"})
    delete_content("https://httpbin.org/delete")

    imshow_img("libraries/libraries/img.jpg")
    imshow_gray_img("libraries/libraries/img.jpg")
    imshow_rotate_img("libraries/libraries/img.jpg", 90)

    example_stat_work_matplotlib()
    example_line_plot_matplotlib()
