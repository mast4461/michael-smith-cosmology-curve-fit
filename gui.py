import os

import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import scipy.optimize as optimize
import numpy as np

from settings import curve_fit_parameter_settings
from models.ST_D_L import ST_D_L
from models.InterST_D_L import InterST_D_L
from models.InterDE_D_L import InterDE_D_L

datasets = os.listdir('data')
models = [
    ST_D_L,
    InterST_D_L,
    InterDE_D_L,
    # 'logDE_mag',
    # 'logInterST_mag',
    # 'logST_mag'
]

root = tk.Tk()
widgetFrame = ttk.Frame(root)
widgetFrame.pack(side=tk.LEFT)


############################
# Plot
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)

def run_regression():
    model = get_model()
    data_frame = get_dataset()

    x = data_frame['ExpFact']
    d = data_frame['D_L']
    ed = data_frame['Err_D_L']

    ax.clear()
    ax.errorbar(x, d, ed, fmt='.', label='data', capsize=5)
    ax.autoscale(enable=True)

    popt, pcov = optimize.curve_fit(model, x, d, sigma=ed, **curve_fit_parameter_settings)
    xf = np.linspace(x.min(), x.max(), num=50)
    ax.plot(xf, model(xf, *popt), 'g--',
            label='fit: Hubble=%5.3f, Matter=%5.3f' % (popt[0], popt[1]))

    ax.set_title('Model: %s' % (model.__name__))
    ax.set_xlabel('Expansion factor')
    ax.set_ylabel('D_L')
    ax.legend()
    figure.canvas.draw()

lambda_run_regression = lambda x: run_regression()

############################
# Model selector
modelSelectorFrame = ttk.Labelframe(widgetFrame, text="Model")
modelSelectorFrame.pack(side=tk.TOP)

modelSelector = ttk.Combobox(
    modelSelectorFrame,
    values=[model.__name__ for model in models],
    state='readonly'
)
modelSelector.current(0)
modelSelector.pack(side=tk.TOP)
modelSelector.bind("<<ComboboxSelected>>", lambda_run_regression)

def get_model():
    return models[modelSelector.current()]

############################
# Dataset selector
datasetSelectorFrame = ttk.Labelframe(widgetFrame, text="Dataset")
datasetSelectorFrame.pack(side=tk.TOP)

datasetSelector = ttk.Combobox(
    datasetSelectorFrame,
    values=datasets,
    state='readonly'
)
datasetSelector.current(0)
datasetSelector.pack(side=tk.TOP)
datasetSelector.bind("<<ComboboxSelected>>", lambda_run_regression)

def get_dataset():
    file_name = datasets[datasetSelector.current()]
    data_frame = pd.read_csv('data' + os.path.sep + file_name)

    # Enforce non-zero error to avoid NaN in least squares resulting as product of inf and 0
    data_frame['Err_D_L'].mask(lambda e: e == 0, 1e-9, inplace=True)

    return data_frame

run_regression()
root.mainloop()
