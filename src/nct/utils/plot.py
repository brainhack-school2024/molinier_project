import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def save_violin(data, outpath, x_names=['data'], x_axis='data', y_axis='values'):
    '''
    Create violin plot
    '''
    if isinstance(data[0],list):
        if (len(data) != len(x_names)):
            raise ValueError('Missing x names')
    else:
        if len(x_names) != 1:
            raise ValueError('Only one 1 name should be used for the x axis')
        else:
            data = [data]
    
    plot_dict = {'data' : [], 'values' : []}
    for name, d in zip(x_names, data):
        plot_dict['data'] += [name]*len(d)
        plot_dict['values'] += d
    
    plot_df = pd.DataFrame(data=plot_dict)
    sns.set(style="darkgrid")

    # Make the plot 
    plt.figure(figsize = (10, 10))
    sns.violinplot(x="data", y="values", hue="data", data=plot_df, width=0.5, cut=0)
    plt.title(f'{y_axis} violin plot')
    plt.xlabel(x_axis, fontsize = 25)
    plt.ylabel(y_axis, fontsize = 25)
    plt.title(y_axis, fontsize = 30)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    
    # Save plot
    plt.savefig(outpath)