# 2022-04-25 tm() return lap
# 2021-05-30 xlspcl создает pcl файл 
# 2020-09-21 инициализация поссредством import adds; from adds import * ; init()

global l,start, dfr
global display, HTML, reload
from pathlib import Path
global tm,ii, merge_OKVED,start, _log
from xlsxwriter.utility import xl_rowcol_to_cell


global plt, clear_output
from IPython.display import clear_output
import matplotlib.pyplot as plt


# global rjust
# from string import rjust

global adds

global requests
import requests


#2020-09-29 адресация к объекту через .
global _o
class _o:
    def __init__(self, **entries):
        self.__dict__.update(entries)

        
if 'dfr' in locals(): 1  
else: dfr = {}

global xlspcl
def xlspcl(fname, dfr_name = 'tmp'):

    plc_basename = os.path.basename(fname).replace('.xlsx','.pcl')
    plc_dirname = os.path.dirname(fname)+'\_pcl\\'
    
    plc_fname = plc_dirname + plc_basename
    
    if not os.path.exists(plc_dirname): os.makedirs(plc_dirname)
    
    if (os.path.isfile(plc_fname)):
        dfr_name = os.path.basename(fname) if dfr_name == 'tmp' else dfr_name
        dfr[plc_basename] = pd.read_pickle(plc_fname)
        tm('read_plc:' + plc_fname )
    else: 
        dfr[plc_basename] = df = pd.read_excel(fname)
        df.to_pickle(plc_fname) 
        tm('read_xls:' + fname + str(df.shape))

        
        
global disp
def disp(df):
    display(HTML(df.to_html()))
    


def tm(txt="", s=0):
    
    global l,start
    
    import time
    
    SUB = str.maketrans(":-+.0123456789", "╷₋₊.₀₁₂₃₄₅₆₇₈₉")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    
    txt = str(txt)
    
    if txt == "" or s==1: 
        l = start = time.time()
        print("*** Start at: %s %s %s %s"%(
              strftime("%H:%M:%S", time.localtime()),
              strftime("%Y-%m-%d", time.localtime()).translate(SUB), 
              str(txt),"*"*60)); 
    else: 
#           print("[%6s%6s]%s%s %s"%("%2.2f"%(time.time()-l) , 
#           ("%2.1f"%(time.time()-start)).translate(SUB),
#           strftime("%H:%M:%S ", time.localtime()),
#           strftime("%Y-%m-%d ", time.localtime()).translate(SUB),
#           str(txt) )); l = time.time()  
            
        lap_time = str(datetime.timedelta(seconds=(time.time()-l)))[:-3]
        from_start_time = str(datetime.timedelta(seconds=(time.time()-start)))[:-3].translate(SUB)

        print(lap_time,
        from_start_time,
        str(txt) );
        l = time.time()
    return l 


# 2020-08-26  file log

global _log

def _log(str_log = '', add_time = False, work_folder = r'tmp2/', fname = r'log.txt', p=False):
    
    Path(work_folder).mkdir(parents=True, exist_ok=True)
    
    if str_log=='' or add_time :
        str_log = strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' **************************' + str_log
    
    if (p): print (str_log)
    
    with open(work_folder + fname, 'a+') as original: data = original.read()
    with open(work_folder + fname, 'w') as modified: modified.write(str_log + data) 
        
global plt        

def init():
#     global dfr
    
    global time, gmtime, strftime, datetime,l,start, plt
    
    from time import gmtime, strftime
    import time
    import datetime
    
    global plt
    import matplotlib.pyplot as plt
    
    l = start = time.time()

    global display, HTML,reload
    from IPython.display import display, HTML
    from importlib import reload  # Python 3.4+ only.  reload lib
    
    global np,pd,glob
    import numpy as np
    import pandas as pd
    import glob

    global zipfile
    import zipfile
    
    global shutil
    import shutil
    
    global math
    import math
    
    global requests
    import requests
    
    global os,listdir,isfile,join
    from os import listdir
    import os,zipfile
    from os.path import isfile, join

    global tm, ii, tmpxls,tm,sizeof_fmt, _log, df_info, read_rmsp, merge_OKVED, dfr, disp
    
    global adds
    import adds
    adds = reload(adds)
    from adds import  tm, ii, tmpxls,tm,sizeof_fmt, _log , df_info, read_rmsp, merge_OKVED, dfr, grpp, disp, requests  # import adds functions
    

    # Параметры вывода данных на экран
    # pd.set_option('display.height', 1000)
    # pd.set_option('display.max_rows', 500)
    # pd.set_option('display.max_columns', 1500)
    # pd.set_option('display.width', 3000)
    # pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', 800)
    # pd.option_context('display.colheader_justify','left')

    tm('init()')

#     tmp_dir = r'C:/!data/tmp//'    
    tmp_dir = r'tmp//'    

    _log('00.Big-RMSP init\n',1)    
    
    lst = dir(adds)
        
    n = 16
    
    display(HTML(pd.DataFrame ( [lst[i:i+n] for i in range(0,len(lst),n)], 
                              columns = [z+1 for z in range(n)]).fillna('-').to_html()))
    
    
#     print (["".join([x.rjust(10,' ')+',' for x in lst[i:i+n]]) for i in range(0, len(lst), n)])
    

    
# 2020-09-15 

def merge_OKVED(df):
    f = ['ОКВЭД',r'C:\!data\04.Справочники\ОКВЭД2_2020.xlsx',
         {'ОКВЭД_Класс_Код':str},
         ['ОКВЭД_Класс_Код','ОКВЭД_Класс_Наим','ОКВЭД_Раздел_Код','ОКВЭД_Раздел_Наим','ОКВЭД_Вид']]
     
    dfr[f[0]] = pd.read_excel(f[1], converters=f[2], usecols=f[3] )
    
    dfr[f[0]].drop_duplicates(inplace=True)
    
    df['ОКВЭД_Класс_Код'] = df['Основной вид деятельности'].str[0:2]
    
    df = pd.merge(df, dfr['ОКВЭД'], on='ОКВЭД_Класс_Код', how='left')

    df["ОКВЭД_Класс_Код_Наим"] = df["ОКВЭД_Класс_Код"] + '. '+ df["ОКВЭД_Класс_Наим"]

    return df

    
# 2020-09-15 читаем rmsp
    
def read_rmsp(mode=3,fname_csv='data.csv',fname_pcl='rmsp.pcl'):
    
    d = 'r'
    dir_path = r'C:\!data\02.fns\02.03.gnivc8m\\'
    
    
#     print ('****\n',fname_pcl,'\n',fname_csv,'\n***')
    
    usecols = ['№ п/п',
            'ИНН',
            'ОГРН',
            'Индивидуальный предприниматель / юридическое лицо',
            'Полное наименование / Ф.И.О.',
            'Дата создания',
            'Дата прекращения деятельности',
            'Дата включения в РСМП',
            'Дата исключения из РСМП',
            'Категория субъекта МСП',
            'Основной вид деятельности',
            'Категория субъекта МСП до исключения',
            'Федеральный округ',
            'Субъект Российской Федерации',
            'Муниципальное образование',
            'Моногород ',
            'Вновь созданный субъект МСП',
            'Сельскохозяйственный кооператив',
            'Крестьянское (фермерское) хозяйство',
            'Признак КГН',
            'УСН',
            'ЕСХН',
            'ЕНВД',
            'СРП',
            'ССЧР',
            'Доход',
            'Расход',
            'Уплаченные налоги',
            'Задолженность',
            'Нарушения', 
    #                                           'Unnamed: 19'
           ]   
    
    dupcols = ['Признак КГН',
                'УСН',
                'ЕСХН',
                'ЕНВД',
                'СРП',
                'ССЧР',
                'Доход',
                'Расход',
                'Уплаченные налоги',
                'Задолженность',
                'Нарушения']

    modes = ['in keys','read_zip','read_pickle']    
    
    if mode == 3:
        if d in dfr.keys():
            df = dfr[d]
            mode = 0
        elif os.path.isfile(dir_path+fname_pcl): mode = 2
        else: mode = 1  # обрабатываем zip 
    
    tm('1. read_rmsp() mode='+str(mode)+' ' + modes[mode])

    if mode == 1:   # загрузка из исходника 
    
        with zipfile.ZipFile(dir_path+'rmsp.zip', 'r') as zip_ref:
            zip_ref.extractall(dir_path)
            fname_csv =  dir_path +  zip_ref.infolist()[0].filename
            
            num_lines = sum(1 for line in open(fname_csv))

            tm ('2. unzip '+str(num_lines)+' lines')
        
        
        df = pd.read_csv(   fname_csv, 
                            sep = '\t',
#                             nrows = nr, 
                            index_col=0,
                            header = 0, 
                            low_memory=False,
                            converters = {'ИНН':str,'ОГРН':str, 'ИНН субъекта МСП':str },  
                            encoding = 'cp1251'
                            )
        
        tm ('3. read '+str(fname_csv))
        
        df.columns = [ ('2017_' + x if x in dupcols else ('2018_' + x[:-2] if x[-2:] == '.1' else x) ) for x in df.keys()] 
        
        [( df.drop(c , axis=1, inplace=True) if 'Unnamed' in c else c )  for c in df.keys()]

        for c in df.keys():
            if 'Unnamed' in c: del df[c]

#         df.rename(columns = {'ИНН':'inn'}, inplace=True)

        
        df=merge_OKVED(df)
        tm('4. add OKVED')
        
        f1 = dir_path+'20200910_rmsp_('+str(num_lines)+').pcl'
        f2 = dir_path+'rmsp.pcl'
        
        df.to_pickle(f1)
        tm('5. to 20200910_rmsp_('+str(num_lines)+').pcl')
        
        shutil.copy2(f1,f2 )

        tm('6. to rmsp.pcl')


    elif mode == 2:  # загрузка из pcl
        df = pd.read_pickle(dir_path+fname_pcl)
    else: 
        df = dfr[d]
        s = '\nmode:'+str(mode)+'\n'+d+"\n" + str(df.shape); 
        tm(s); 
        return

    s = '\nmode:'+str(mode)+'\n'+d+"\n" + str(df.shape); 
    tm(s)

    dfr[d] = df
    return (mode)


# 2021-05-29 полей с переводом строки
# 2020-03-20 ii() вывод в HTML 
         
def ii(dii='', k = 0, pref='', sep='\t'):    
    
    dii = dfr if dii=='' else dii
    
    dfo = pd.DataFrame(columns=['name','rows','cols','memory','keys'])
    
    styler = dfo.style
    styler = styler.format("{:,.0f}")
    styler = styler.set_properties(**{'width': '220px', 'text-align': 'left'})
    styler.set_table_styles(
    [dict(selector="td", props=[("text-align", "left")])]   
    )
#     print(memus(dfr, deep = 0))
    for i in dii.keys(): 
#         print(type(dii[i]),i)
        if type(dii[i]) is pd.DataFrame:
#             if k == 1: print(dii[i].keys())
#             print ("[%s]:\t\t"%i , dii[i].shape, "{0:,}".format( dii[i].memory_usage(deep=0).sum()))
            dfo = dfo.append({
#                     'name': "dfr['" +pref+''+i+"']", 
                    'name': "df = dfr['"+i+"']", 
                    'rows': dii[i].shape[0], 
                    'cols': dii[i].shape[1], 
                    'memory': "{0:,}".format( dii[i].memory_usage(deep=0).sum()),
                    'keys': "['" + ("'," + sep + "'").join( dii[i].keys().astype('str') )+"']" if k == 1 else str(len(dii[i].keys()))
                    }, ignore_index=True)
            
        elif isinstance(dii[i], dict):
#             print (i)
            dfo = dfo.append(ii(dii=dii[i], pref= str(i)+"']['", k = k))
    
    def text_left(s):  return ['text-align: left; width:200px' for v in s]
    def col_width(s):  return ['text-align: left; width:800px' for v in s]
    def float_format(s): return ["{0:,}".format(s) for v in s]
    def highlight_max(s): 
        os = s # highlight the maximum in a Series yellow.
        is_max = s == s.max()       
        return ['background-color: #fff0cc; width:80px' if v else '' for v in is_max]

    dfo_html = dfo.style \
    .apply(text_left, subset=['name']) \
    .apply(col_width, subset=['keys']) \
    .apply(highlight_max, subset=['memory','rows'])
    
    html = (dfo_html)
#                      )
# , subset=['B', 'C', 'D']
    display(html)
#     return dfo





# 2020-09-10 new

def df_info(df,samp=False):
    if (samp): display(HTML(df.sample(3).to_html()))
    display(HTML(pd.merge(df.count().reset_index(),df.dtypes.reset_index(),on='index').to_html()))

# 2020-09-10 add colmult

def tmpxls(o,
           fn,
           cs={}, 
           fdir = 'tmp/', 
           count_list = ['inn', 'ИНН','налогоплательщика','ОГРН','okpd2','OGRN'], 
           link_list=['Ссылка'],
           verb=0,
           colmult = 1
          ):
    
    import errno
    
    try:
        os.mkdir(fdir)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        print ("tmpxls err:" + str(exc.errno)+ str(exc) +  fdir+fn)
        pass

    
        
    
    from xlsxwriter.utility import xl_rowcol_to_cell
    
    if (verb): tm('Старт запись в xls:  '+fdir+fn+'.xlsx')

    path = fdir+fn+'.xlsx'
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    workbook  = writer.book

    format1 = workbook.add_format({'color':'black','font_size':11, 'text_wrap':True, 'valign':'top'})
    f_link = workbook.add_format({'color':'blue','font_size':11, 'text_wrap':True, 'valign':'top'})
    format_inn = workbook.add_format({'color':'black','font_size':10, 'bold':True, 'bg_color':'#e0f0ff', 'valign':'top'})
    total_fmt = workbook.add_format({'color':'black','font_size':12, 'bold':True, 'bg_color':'#ff9900', 'align':'center'})
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
         'font_size':9,
        'valign': 'vcenter',
        'align': 'center',
        'fg_color': '#88c0e8',
        'border': 1})
    
    if (type(o)!=dict):    # если dict записываем 
        o = {'Список':o}
        
    for key, df in o.items():

        key = key[:10]
        
        df.to_excel(writer, sheet_name = key, index=False,  startcol=0, startrow=1)
        worksheet = writer.sheets[key]

        # Write the column headers with the defined format.
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(1, col_num, value, header_format)

            cnt,inn_idx = 0,0 
            dsz = df.notna().sample(1000) if df.notna().shape[0] > 1000 else df.notna()

        link_col = -1

        for k in df.keys():

            mask = (df[k].astype(str).str.len() > 0 )
            
            if( k in cs.keys()):
                width = cs[k] 
                print('***',k,width)
            else:    
                width = df.loc[mask]
                width = width[k].astype(str).str.len().mean()+1
                width = width if width < 80 else 80
                width = width if (width > 5) and  ~math.isnan(width)  else 5

            if (verb): print(("%0.0f."%width).rjust(7),k)
            
            width = width*colmult

            if len( [ s for s in count_list if ~k.find(s) ] ) > 0  :
                start_range = xl_rowcol_to_cell(2, cnt)
                end_range = xl_rowcol_to_cell(df.shape[0]+2, cnt)

                
                # Construct and write the formula
                formula = "=SUBTOTAL(3,{:s}:{:s})".format(start_range, end_range)
                f = format_inn
                
# Set the column width and format.
                worksheet.set_column(cnt,cnt, width , f )   
                worksheet.write_formula(0, cnt, formula, total_fmt)
            elif k in link_list:
                worksheet.set_column(cnt,cnt, 20 , f_link )   # Set the column width and format.
#             link_col = cnt
            else:
                f = format1 
                worksheet.set_column(cnt,cnt, width , f )   # Set the column width and format.
            cnt += 1

        worksheet.freeze_panes(2, 3)
        worksheet.autofilter(1,0,df.shape[0]+1, df.shape[1]-1)
        worksheet.set_zoom(90)
    
    writer.save()
    writer.close()
    if (verb): tm('>>>')    

        

global sizeof_fmt

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

global grpp # 2020-09-23 
def grpp(df,grps,colcnt='ИНН',disp=False):
    dfg = df.groupby(grps)[colcnt].count().reset_index().sort_values([colcnt], ascending=False)
    dfg['%'] = dfg[colcnt]/dfg['ИНН'].sum()*100
    display(HTML(dfg.to_html())) if disp else 1
    return dfg

global Struct # 2022-01-06 

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

global draw_l        
        
def draw_l (**kwargs):
    print (kwargs.items())
    s = Struct(**kwargs)
    d = {}
    
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))

        # print("{} = {}".format(key, value))
    print (s.color)    