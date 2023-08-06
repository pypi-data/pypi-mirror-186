def make_pretty(ax, title='', xTitle='', yTitle=''):
    ax.spines['left'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['right'].set_color('black')

    ax.spines['left'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    
    ax.set_title(title, fontsize = 20)
    ax.set_xlabel(xTitle, fontsize=16)
    ax.yaxis.set_label_coords(-0.15, 0.5)
    ax.set_ylabel(yTitle, rotation = 'horizontal', fontsize = 16)
    
    ax.tick_params(axis='both', labelsize = 16)
    
    ax.grid(True)
    return


def scatter_bygroup(ax, x,y,col,colmap='hot'):
    '''
    Purpose:
        - Plot y against x in a scatterplot, where the points are coloured by a third variable, col.

    Input:
        - ax  (matplotlib axis) : The axis on which to add the scatter plot
        - x   (array/float)     : The data for the x-axis of the scatterplot
        - y   (array/float)     : The data for the y-axis of the scatterplot
        - col (list)            : A list of values of some variable which will correspond to groups. This 
                                  value is used to determine the colour of a point. Points with the same 
                                  'col' value will have the same colour.
        - colmap (str)          : A colormap for determining the group colours. Default to 'hot'.
    '''


    # Set the color map to match the number of species
    uniq = list(set(col))
    z    = range(1,len(uniq))
   
    cNorm  = colors.Normalize(vmin=0, vmax=len(uniq))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=colmap)

    
    # Plot each group
    for i in range(len(uniq)):
        indx = (col == uniq[i])
        ax.scatter(x[indx], y[indx], s=150, color=scalarMap.to_rgba(i), label=uniq[i])


    
    return