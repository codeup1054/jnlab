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
    "speed2":{'#993402':5,
     '#FE0100':10,
     '#FEA000':20,
     '#FED000':30,
     '#FBFF00':40,
     '#03FF00':50,
     '#00B47B':60,
     '#04CBD9':80,
     '#358AFF':100,
     '#DC01FE':120,
     '#999999':300,
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




def colorise(x, palette = palettes['parking_price']):
    return [i[1:] for i in palette if palette[i] >= x ][0]


def palettes_sample():
    import matplotlib.pyplot as plt

    for k in palettes:
        print(k)
        x,y = list(palettes[k].keys()),list(palettes[k].values())
        plt.figure(figsize=(10,4))
        barlist = plt.barh(x, y, color = x )
        plt.bar_label(barlist)
        plt.show()