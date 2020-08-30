
import pandas as pd
import os
import time
from datetime import datetime


path = "./intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    
    # make new 'data frame' with PANDA
    df = pd.DataFrame( columns = ['Date','Unix','Ticker','DE Ratio'] )

    statspath = path + '/_KeyStats'
    stock_list = [ x[0] for x in os.walk(statspath) ]

    #for x in os.walk(statspath):
        #print("x here", x[0]) >> x here ./intraQuarter/_KeyStats\aapl

    for each_dir in stock_list[1:]:
        
        # 'list' files in each folder
        each_file = os.listdir(each_dir)
        
        # get the 'ticker symbol' >> ['./intraQuarter/_KeyStats', 'aci']
        ticker = each_dir.split( "\\" ) [1]
        
        # checking the 'file length'
        if len(each_file) > 0:
            for file in each_file:
                datetime1 = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unixtime1 = time.mktime( datetime1.timetuple() )
                
                #print(datetime1, unixtime1)
            
            # get the full file path, ./intraQuarter/_KeyStats\aapl/20130811023032.html
            full_file_path = each_dir+'/'+file

            # open file 'read only'
            source_code = open(full_file_path, 'r').read()
            
            try: 
                value = float( source_code.split( gather + ':</td><td class="yfnc_tabledata1">' )[1].split('</td>')[0] ) 
                #print(ticker + ":" + value)
                
                # 'add' data to 'data frame'
                #df.append({'Date':datetime1, 'Unix':unixtime1, 'Ticker':ticker, 'DE Ratio':value}, ignore_index = True)
                df = df.append({'Date':datetime1, 'Unix':unixtime1, 'Ticker':ticker, 'DE Ratio':value} )

            except Exception as e:
                pass
            
    # this is just a really stupid way to make a file name, nothing speci al
    save_name = gather.replace(' ', '').replace(')', '').replace( '(', '').replace('/', '')+('.csv')
    
    # save data to '.csv' file
    df.to_csv(save_name)
    
            
# running function Key_Stats()
Key_Stats()

