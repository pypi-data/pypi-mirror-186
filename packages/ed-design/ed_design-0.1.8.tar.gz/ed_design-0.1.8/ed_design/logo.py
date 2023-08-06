# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os
#%%

def ed_logo(kind='print'):
    """
    Load EnviDan logo for use in for example a Matplotlib figure
    
    Use:
        Put logon in Matplotlib figures by adding an axes.
        
        logo = logo()
        ax_logo = fig.add_axes([0.75,0.94,0.16,0.20], anchor='NE', zorder=-1)
        ax_logo.imshow(logo)
        ax_logo.axis('off')

    Parameters
    ----------
    kind : str, optional
        Kind of logo to load. The default is 'print'.

    Returns
    -------
    logo : Array of uint8
        Array of uint8 number representing the image.

    """
    
    dir_path = os.path.dirname(__file__)

    if kind == 'print':
        logo = plt.imread(f'{dir_path}/_media/ed_logo_blue_print.jpg')
    elif kind == 'web':
        logo = plt.imread(f'{dir_path}/_media/ed_logo_blue_web.png')
    else:
        raise NameError(f'{kind} is unknown')
    return logo

