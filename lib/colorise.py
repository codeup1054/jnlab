palettes  = {
    "speed":{'#993402': 5,
     '#fe0100': 10,
     '#fea000': 20,
     '#fbff00': 30,
     '#03ff00': 40,
     '#00b47b': 50,
     '#04cbd9': 60,
     '#1c65c9': 80,
     '#5006da': 100,
     '#555555': 300
    },
    
    "scooter":{'#bb2202':2,
     '#FE0100':5,
     '#FEA000':10,
     '#FED000':15,
     '#FBFF00':20,
     '#03FF00':25,
     '#00B47B':30,
     '#04CBD9':35,
     '#358AFF':40,
     '#DC01FE':45,
     '#999999':60
    },
    
    "parking_price":
    {'#aaaa': 10,
        '#cc0202':  20,
        '#FE5500':  40,
        '#dd7700':  40,
        '#BB7700':  50,
        '#FECA00':  60,
        '#ccee00':  70,
        '#03bb00':  80,
        '#00B499': 100,
        '#04AAD9': 150,
        '#256Add': 200,
        '#7755cc': 380,
        '#772222': 450
    }
}


# https://seaborn.pydata.org/tutorial/color_palettes.html

import seaborn as sns


def colorise(x, palette = palettes['parking_price']):
    
    return [i[1:] for i in palette if float(palette[i]) >= float(x) ][0]


def colorise_palettes():
    import matplotlib.pyplot as plt
    from io import BytesIO
    import base64
    from IPython.core.display import display, HTML

    img_html = ''
    pal_name = "Paired, magma, deep, muted, pastel, bright, dark, colorblind, rocket, rocket_r, flare, mako, crest, cubehelix, viridis, icefire, ch:s=-.2,r=.6, Spectral, coolwarm".split(", ")
    
    print(pal_name)
    
    for p in pal_name:
        colors = [c for c in sns.color_palette(p,13).as_hex()]
        palettes[p] = dict(zip(colors,range(1,len(colors))))
    
    for k in palettes:
        figfile = BytesIO()
        
        plen = len(palettes[k])

        fig, ax = plt.subplots(figsize=(3.5, 0.31*plen))
        x,y = list(palettes[k].keys()),list(palettes[k].values())
        barlist = ax.barh(x, y, height=1,color = x )
        for i,b in enumerate(barlist):
#             print(y[i],b.xy[1],y[i])
            ax.text(y[i],b.xy[1],y[i])
        
        plt.subplots_adjust(left=0.2, right=0.95, top=0.99, bottom=0.2)
    
        fig.savefig(figfile, format='png')
        figdata_png = base64.b64encode(figfile.getvalue())


        plt.close()
        
        pl = "".join(["<tr ><td>%s</td><td>%s</td><td >%s</td></tr>"%(i,p,palettes[k][p]) for i,p in enumerate(palettes[k])][::-1])
        
        img_html = img_html + '''
                                    <div class='pall' style='width:350px; 
                                    height:300px; 
                                    line-height: 1.1; 
                                    border: red solid 0px; 
                                    background-position: top 52px left 95px;
                                    background-repeat: no-repeat;
                                    background-image:url(data:image/png;base64,%s&#10;)'><hr><b>%s</b><br><br><table class=tab>%s</table></div>
                                 '''%(figdata_png.decode("utf-8"),k,pl) 
        
    
#     print (img_html)
    display(HTML('''<style>.tab td {padding:1px 2px; border: red solid 0px; font-size:11px;  }</style><h1>Palettes</h1><a href ='https://seaborn.pydata.org/tutorial/color_palettes.html'>seaborn.pydata.org</a><div style='display: flex; flex-wrap:wrap;'>'''+img_html+"</div>"))

