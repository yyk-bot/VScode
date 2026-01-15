import numpy as np
import matplotlib.pyplot as plt
data_list = np.loadtxt('./Sample1.txt')
def plot_and_find_max(data, x_range=(349, 451)):
    wavelengths = [d for d in data]
    values = np.array([d[1:] for d in data])

    fig, ax = plt.subplots()
    ax.plot(wavelengths, values.T, 'o', label='Data Points')

    # 在指定范围内搜索第六列的最大值
    max_value_index = np.argmax(values[:, 5] > x_range) if x_range < x_range else None
    max_wavelength, max_value = wavelengths[max_value_index], values[max_value_index]

    if max_value_index is not None:
        ax.scatter(max_wavelength, max_value, marker='*', color='red', s=100, label=f'Max Value ({max_value})')
        ax.axvspan(max_wavelength - (x_range - x_range), max_wavelength + (x_range - x_range), alpha=0.2)

    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Value')
    ax.set_title('Wavelength vs. Data Values')
    ax.legend()
    plt.xlim(x_range)
    
    return fig

# 调用函数绘制图形并找到最大值
fig = plot_and_find_max(data_list)
plt.show()

# 最大值的相关信息

