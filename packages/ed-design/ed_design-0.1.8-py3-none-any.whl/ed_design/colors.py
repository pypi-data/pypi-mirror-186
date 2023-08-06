# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

# %%

class Colors(object):
    
    def __init__(self):
        
        self.colors = {'blues': ['#003778', '#006EB7', '#A3CCEE', '#DFEAF8'],
                       'greens': ['#125428', '#1D893A', '#B5D8AF', '#E1EFE3'],
                       'reds': ['#7B282E', '#C14246', '#F7BCBB', '#FCE4E0'],
                       'yellows': ['#6D4104', '#F7A823', '#FDD5A5', '#FEEBDA'],
                       'browns': ['#4A372C', '#7D604B', '#D4C1B2', '#F1E9E4'],
                       'purples': ['#53234e', '#82387B', '#DBBFDD', '#F2E1F0']
                       }
        
        self.palettes = {'dark': [self.colors[key][0] for key in self.colors.keys()],
                         'normal': [self.colors[key][1] for key in self.colors.keys()],
                         'pastel': [self.colors[key][2] for key in self.colors.keys()],
                         'light': [self.colors[key][3] for key in self.colors.keys()],
                         
                         'pair': [val for sublist in [v[:2] for v in self.colors.values()] for val in sublist],
                         'triple': [val for sublist in [v[:3] for v in self.colors.values()] for val in sublist],
                         'seq': [val for sublist in [v[:4] for v in self.colors.values()] for val in sublist]
                         }
        
        self.colormaps = {'BlWh': mcolors.LinearSegmentedColormap.from_list('BlGr',
                                                                            [self.colors['blues'][1],
                                                                             '#FFFFFF'],                                                                                   
                                                                            N=256),
                          'GrWh': mcolors.LinearSegmentedColormap.from_list('GrWh',
                                                                            [self.colors['greens'][1],
                                                                             '#FFFFFF'],                                                                                   
                                                                            N=256),
                          'BlGr': mcolors.LinearSegmentedColormap.from_list('BlGr',
                                                                            [self.colors['blues'][1],
                                                                             '#FFFFFF',
                                                                             self.colors['greens'][1]],                            
                                                                            N=256),
                          'BlRe': mcolors.LinearSegmentedColormap.from_list('BlRe',
                                                                            [self.colors['blues'][1],
                                                                             '#FFFFFF',
                                                                             self.colors['reds'][1]],
                                                                            N=256)}

    def get_palette(self, palette='normal'):
        if palette in self.colors.keys():
            cmap = self.colors[palette]
        elif palette in self.palettes.keys():
            cmap = self.palettes[palette]
        else:
            raise NameError('Palette not found')
        return cmap
    
    def get_cmap(self, cmap='BlWh'):
        if cmap in self.colormaps.keys():
            cmap = self.colormaps[cmap]
            return cmap
        else:
            raise NameError('Colormap not found')
        
    def create_cmap(self, *colors, n_colors=256):       
        cmap = mcolors.LinearSegmentedColormap.from_list('mycmap',
                                                         *colors,                                                                                 
                                                         N=n_colors)
        return cmap
            
    # def _palette_dict_check(self, palette):
    #     if palette not in self.palettes.keys() and palette not in self.colors.keys() and palette not in self.colormaps.keys():
    #         raise NameError('Palette doees not exist')
    #     return

    def _plot(self, palette, label):
        fig, ax = plt.subplots(figsize=(4, 0.5))
        plt.colorbar(
            mpl.cm.ScalarMappable(cmap=palette),
            cax=ax,
            orientation='horizontal',
            )
        plt.title(f'{label}')
        ax.set_xticks([]),
        ax.set_xticklabels([])
        plt.show()
        return
       
    def show_palette(self, palette='all'):
        if palette != 'all' and palette not in self.colors.keys() and palette not in self.palettes.keys():
            raise NameError('Palette does not exist!')
            
        elif palette in self.colors.keys():
            cmap = mcolors.ListedColormap(self.colors[palette])
            self._plot(cmap, label=palette)    
            
        elif palette in self.palettes.keys():
            cmap = mcolors.ListedColormap(self.palettes[palette])
            self._plot(cmap, label=palette)
            
        elif palette == 'all':
            for palette in self.colors.keys():
                cmap = mcolors.ListedColormap(self.colors[palette])
                self._plot(cmap, label=palette)
            
            for palette in self.palettes.keys():
                cmap = mcolors.ListedColormap(self.palettes[palette])
                self._plot(cmap, label=palette)
        return
    
    def show_cmap(self, cmap='all'):
        if cmap != 'all' and cmap not in self.colormaps.keys():
            raise NameError('Colormap not found')
        elif cmap in self.colormaps.keys():
            colormap = self.colormaps[cmap]
            self._plot(colormap, label=cmap)
        elif cmap == 'all':
            for cmap in self.colormaps.keys():
                colormap = self.colormaps[cmap]
                self._plot(colormap, label=cmap)
        return
    
    def show_all(self):
        self.show_palette('all')
        self.show_cmap('all')
            
