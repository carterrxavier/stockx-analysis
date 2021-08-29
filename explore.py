import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import itertools

def get_distribution(df):
    '''
    plots countplot distributions for specified columns in df
    '''
    #set up loop
    for i in df.columns:
        #set figure size
        plt.figure(figsize=(20,9))
        #put title
        plt.title('{} Distribution'.format(i))
        #label x axis
        plt.xlabel(i)
        #label y axis as count
        plt.ylabel('count')
        #create countplot
        sns.countplot(data=df, x=i)
        #show the plot
        plt.show()
        
def compare_to_target(df, target):
    '''
    compare_to_target will compare specified columns to a target variable
    '''
    
    #initiate loop
    for i in df:
        #if target is continuous, plot scatter plot
        if  df[target].dtype == np.float64:
            #set figure size
            plt.figure(figsize=(16,9))
            #set title
            plt.title('{} vs {}'.format(i,target))
            #plot scatterplot
            sns.scatterplot(data=df , y = target, x = i)
            #show graph
            plt.show()
        #if target is not continuous, plot countplot   
        else:
            #set figure size
            plt.figure(figsize=(16,9))
            #set title
            plt.title('{} Distribution'.format(i))
            #set x axis title
            plt.xlabel(i)
            #set y axis title
            plt.ylabel('count')
            #make countplot
            sns.countplot(data=df , x=i, hue=target)
            #show
            plt.show()
        
           
def get_heatmap(df, target):
    '''
    This method will return a heatmap of all variables and there relation to churn
    '''
    plt.figure(figsize=(15,12))
    color = sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)
    heatmap = sns.heatmap(df.corr()[[target]].sort_values(by=target, ascending=False), annot=True, cmap=color)
    heatmap.set_title('Feautures Correlating to {}'.format(target))
    plt.show()
    return heatmap


    
def plot_variable_pairs(df, cont_vars = 2):
    combos = itertools.combinations(df,cont_vars)
    for i in combos:
        plt.figure(figsize=(20,12))
        sns.regplot(data=df, x=i[0], y =i[1],line_kws={"color":"black"},scatter_kws={"color":'pink','alpha':0.5})
        plt.show()
        



def plot_cat_and_cont(cat_var, con_var, df):
    for i in cat_var:
        for j in con_var:
            plt.figure(figsize=(20,12))
            plt.subplot(131)
            sns.swarmplot(x=i, y=j, data=df)
            plt.subplot(132)
            sns.boxplot(x=i, y=j, data=df)
            plt.subplot(133)
            sns.barplot(x=i, y=j, data=df)
            plt.show()
        

