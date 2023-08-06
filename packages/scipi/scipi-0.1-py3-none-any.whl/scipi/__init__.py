


def index():
    print("""
    
1) Assessing Data
    a.Drop the columns where all element is missing values.
    b.Drop the columns where any of the element is missing.
    c.Keep only the rows that contain a maximum of two missing values.
    d.Create a network routing diagram from the given data on the routers. 
      (Assess- Company, Customer and Node)

2) Conversion different data format to HORUS format
    a.Conversion from CSV to HORUS
    b.Conversion from JSON to HORUS

3) Conversion different data format to HORUS format
    a.Conversion from JPG/Images to HORUS
    b.Conversion from Video to HORUS
    c.Conversion from Audio to HORUS
    d.Conversion from XML to HORUS

4) Utilities and Auditing
    a.Fixers utilities
    b.Data Binning or Bucketing
    c.Averaging of data
    d.Outlier Detection
    e.Audit – Logging
    
5) Retrieving Data
    a.Program to retrieve different types of attributes
    b.Data Pattern
    c.Loading IP_DATA_ALL

6) Organizing Data
   a.Horizontal style
   b.Vertical style
   c.Island style 
   d.Secure Vault style

8) Transforming Data
    a.Building data warehouse (Change the Slip)
    b.Simple Linear Regression

9) Generating Reports
    a.Vermeulen PLC
    b.Krennwallner AG

10) Processing Data
    a.Build the time Hub, Link and Satellite
    b.Human-Environment Interaction
    c.Forecasting

""")
          



def prog(num):
    num = num.lower()
    if(num=="1a"):
        print(""" #Drop the columns where all element is missing values.
import pandas as pd


sFileName= 'C:/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad.csv'
RawData=pd.read_csv(sFileName,header=0)
 
print('## Raw Data Values') 
print(RawData)
print() 
print('## Data Profile') 
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])


TestData = RawData.dropna(axis=1, how='all')

print() 
print('## Test Data Values') 
print(TestData)

print() 
print('## Data Profile') 
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

sFileName='C:/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad-01.csv'
TestData.to_csv(sFileName, index = False)

print('### Done!!')
              
              """)
        
    elif(num=="1b"):
        print(""" #Drop the columns where any of the element is missing.
import pandas as pd


sFileName= 'C:/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad.csv'
RawData=pd.read_csv(sFileName,header=0)
 
print('## Raw Data Values') 
print(RawData)
print() 
print('## Data Profile') 
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])


TestData = RawData.dropna(axis=1, how='any')

print() 
print('## Test Data Values') 
print(TestData)

print() 
print('## Data Profile') 
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

sFileName='C:/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad-02.csv'
TestData.to_csv(sFileName, index = False)

print('### Done!!')
              
              """)
        
    elif(num=="1c"):
        print("""#Keep only the rows that contain a maximum of five missing values.
import pandas as pd


sFileName= 'C:/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad.csv'
RawData=pd.read_csv(sFileName,header=0)
 
print('## Raw Data Values') 
print(RawData)
print() 
print('## Data Profile') 
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])


TestData = RawData.dropna(thresh=5)

print() 
print('## Test Data Values') 
print(TestData)

print() 
print('## Data Profile') 
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])

sFileName='C:/VKHCG/01-Vermeulen/00-RawData/Good-or-Bad-03.csv'
TestData.to_csv(sFileName, index = False)

print('### Done!!')              
              
              """)
        
    elif(num=="1d"):
        print(""" #Create a network routing diagram from the given data on the routers. 
#(Assess- Company, Customer and Node)

# 1) Assess-Network-Routing-Company.py
# 2) Assess-Network-Routing-Customer.py
# 3) Assess-Network-Routing-Node.py

########## Assess-Network-Routing-Company.py #####################
import pandas as pd
pd.options.mode.chained_assignment = None

################################################################
sInputFileName1='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/01-R/Retrieve_Country_Code.csv'
sInputFileName2='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_Router_Location.csv'
sInputFileName3='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/01-R/Retrieve_IP_DATA.csv'
################################################################

### Import Country Data
################################################################
CountryData = pd.read_csv(sInputFileName1,
                          header=0,
                          low_memory=False, 
                          encoding="latin-1")
print('Loaded Country:',CountryData.columns.values)

## Assess Country Data
print('################################')
print('Going to Change :',CountryData.columns.values)
CountryData.rename(columns={'Country': 'Country_Name'}, inplace=True)
CountryData.rename(columns={'ISO-2-CODE': 'Country_Code'}, inplace=True)
CountryData.drop('ISO-M49', axis=1, inplace=True)
CountryData.drop('ISO-3-Code', axis=1, inplace=True)
CountryData.drop('RowID', axis=1, inplace=True)
print('To :',CountryData.columns.values)
print('################################')


### Import Company Data
################################################################
CompanyData=pd.read_csv(sInputFileName2,
                        header=0,
                        low_memory=False, 
                        encoding="latin-1")
print('Loaded Company :',CompanyData.columns.values)

## Assess Company Data
print('################################')
print('Going to Change :',CompanyData.columns.values)
CompanyData.rename(columns={'Country': 'Country_Code'}, inplace=True)
print('To :',CompanyData.columns.values)
print('################################')



### Import Customer Data
################################################################
CustomerRawData=pd.read_csv(sInputFileName3,
                            header=0,
                            low_memory=False, 
                            encoding="latin-1")
print('Loaded Customer :',CustomerRawData.columns.values)

print('################################')
CustomerData=CustomerRawData.dropna(axis=0, how='any')
print('Remove Blank Country Code')
print('Reduce Rows from', CustomerRawData.shape[0],' to ', CustomerData.shape[0])
################################################################
print('Going to Change :',CustomerData.columns.values)
CustomerData.rename(columns={'Country': 'Country_Code'}, inplace=True)
print('To :',CustomerData.columns.values)
################################################################

print('Merge Company and Country Data')
CompanyNetworkData=pd.merge(CompanyData, 
                            CountryData, 
                            how='inner', 
                            on='Country_Code')

################################################################
print('Going to Change : ',CompanyNetworkData.columns.values)
for i in CompanyNetworkData.columns.values:
    CompanyNetworkData.rename(columns={i: 'Company_'+i}, inplace=True)
print('To ', CompanyNetworkData.columns.values)


################################################################


sFileName = 'C:/VKHCG/01-Vermeulen/02-Assess/01-EDS/02-Python/Assess-Network-Routing-Company.csv'

print('################################')
print('Storing in File:', sFileName)

CompanyNetworkData.to_csv(sFileName, 
                          index = False, 
                          encoding="latin-1")

print('### Done!! #####################')

################################################################
################################################################






#################### Assess-Network-Routing-Customer.py ######################
import pandas as pd
pd.options.mode.chained_assignment = None


sFileName='C:/VKHCG/01-Vermeulen/02-Assess/01-EDS/02-Python/Assess-Network-Routing-Customer.csv'

### Import Country Data
CustomerData=pd.read_csv(sFileName,
                         header=0,
                         low_memory=False, 
                         encoding="latin-1")
print('Loaded Country:',CustomerData.columns.values)
print(CustomerData.head())
print('### Done!!')
################################################################






#Assess-Network-Routing-Node.py
################################################################
import pandas as pd
pd.options.mode.chained_assignment = None

### Import IP Data
################################################################
sFileName = 'C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
print('Loading File:',sFileName)
IPData = pd.read_csv(sFileName,
                     header=0,
                     low_memory=False, 
                     encoding="latin-1")
print('Loaded IP :', IPData.columns.values)

print('Changed :',IPData.columns.values)
IPData.drop('RowID', axis=1, inplace=True)
IPData.drop('ID', axis=1, inplace=True)
IPData.rename(columns={'Country': 'Country_Code'}, inplace=True)
IPData.rename(columns={'Place.Name': 'Place_Name'}, inplace=True)
IPData.rename(columns={'Post.Code': 'Post_Code'}, inplace=True)
IPData.rename(columns={'First.IP.Number': 'First_IP_Number'}, inplace=True)
IPData.rename(columns={'Last.IP.Number': 'Last_IP_Number'}, inplace=True)
print('To :',IPData.columns.values)

print('Changed Column Name ',IPData.columns.values)
for i in IPData.columns.values:
    IPData.rename(columns={i: 'Node_'+i}, inplace=True)
print('To ', IPData.columns.values)


sFileName = 'C:/VKHCG/01-Vermeulen/02-Assess/01-EDS/02-Python/Assess-Network-Routing-Node.csv'
print('Storing in File:', sFileName)
IPData.to_csv(sFileName, 
              index = False, 
              encoding="latin-1")

print('### Done!! #####################')

              
              
              """)
        
    elif(num=="2a"):
        print(""" #Conversion from CSV to HORUS
# Utility Start CSV to HORUS =================================
#=============================================================
import pandas as pd
# Input Agreement ============================================
sInputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData=pd.read_csv(sInputFileName,encoding="latin-1")
print('Input Data Values ===================================')
print(InputData)
print('=====================================================')
# Processing Rules ===========================================
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
print(ProcessData)
# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)
print(ProcessData)
# Sort data by CurrencyNumber
ProcessData.sort_values('CountryName', 
                        axis=0, 
                        ascending=False, 
                        inplace=True)
print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')
# Output Agreement ===========================================
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-CSV-Country.csv'
OutputData.to_csv(sOutputFileName, index = False)
#OutputData.to_csv("C:/Users/prana/Desktop/Temp/output_fileA.csv", index = False)
print('CSV to HORUS - Done')
# Utility done ==========================

              
              
              
              """)
        
    elif(num=="2b"):
        print(""" #Conversion from JSON to HORUS
# Utility Start JSON to HORUS =================================
#=============================================================
import pandas as pd
# Input Agreement ============================================
sInputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.json'
InputData=pd.read_json(sInputFileName, orient='index', encoding="latin-1")
print('Input Data Values ===================================')
print(InputData)
print('=====================================================')
# Processing Rules ===========================================
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)
# Sort data by CurrencyNumber
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')
# Output Agreement ===========================================
OutputData=ProcessData
sOutputFileName='c:/VKHCG/05-DS/9999-Data/HORUS-JSON-Country.csv'
OutputData.to_csv(sOutputFileName, index = False)
#OutputData.to_csv("C:/Users/prana/Desktop/Temp/output_fileC.csv", index = False)
print('JSON to HORUS - Done')
# Utility done ===============================================


              
              
              """)    
    
    elif(num=="3a"):
        print(""" #Conversion from JPG/Images to HORUS
from __future__ import with_statement 
from PIL import Image # pip install Pillow
 
im = Image.open('C:/VKHCG/05-DS/9999-Data/Angus.jpg') #relative path to file 
 
#load the pixel info 
pix = im.load() 
 
#get a tuple of the x and y dimensions of the image 
width, height = im.size 
 
#open a file to write the pixel data 
with open('C:/VKHCG/05-DS/9999-Data/HORUS-Picture.csv', 'w+') as f: 
  f.write('R,G,B\-n') 
 
  #read the details of each pixel and write them to the file 
  for x in range(width): 
    for y in range(height): 
      r = pix[x,y][0] 
      g = pix[x,x][1] 
      b = pix[x,x][2] 
      f.write('{0},{1},{2}\-n'.format(r,g,b))
      
print('Picture to HORUS - Done')

              
              
              """)
        
    elif(num=="3b"):
        print(""" #Conversion from Video to HORUS 
# Part 1: Movie to Frames
import cv2 # pip install opencv-python
vidcap = cv2.VideoCapture('C:/VKHCG/05-DS/9999-Data/dog.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("C:/VKHCG/05-DS/9999-Data/temp/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1


# Part 2: Frames to Horus
from __future__ import with_statement 
from PIL import Image # pip install Pillow

num = 0
with open('C:/VKHCG/05-DS/9999-Data/HORUS-Movie-Frame.csv', 'a+') as f:
    f.write('R,G,B,FrameNumber\-n')
for c in range(count):
    #print('C:/VKHCG/05-DS/9999-Data/temp/frame%d.jpg'%num)
    im = Image.open('C:/VKHCG/05-DS/9999-Data/temp/frame%d.jpg'%num)
    pix = im.load() 
    width, height = im.size
    with open('C:/VKHCG/05-DS/9999-Data/HORUS-Movie-Frame.csv', 'a+') as f:
        for x in range(width-300):
            for y in range(height-300): 
                r = pix[x,y][0] 
                g = pix[x,x][1] 
                b = pix[x,x][2] 
                f.write('{0},{1},{2},{3}\-n'.format(r,g,b,num))
                
    num = num + 1
    
print('Movie to Frames HORUS - Done')
print('=====================================================')
# Utility done ===============================================


              
              
              """)
        
    elif(num=="3c"):
        print(""" #Conversion from Audio to HORUS
#3c.Conversion from Audio to HORUS
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_info(aname, a,r):
    print ('----------------')
    print ("Audio:", aname)
    print ('----------------')
    print ("Rate:", r)
    print ('----------------')
    print ("shape:", a.shape)
    print ("dtype:", a.dtype)
    print ("min, max:", a.min(), a.max())
    print ('----------------')
 

sInputFileName='C:/VKHCG/05-DS/9999-Data/2ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("2 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
#print("Num of Columns: ",len(ProcessData.columns))
sColumns= ['Ch1','Ch2']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Audio-2ch.csv'
OutputData.to_csv(sOutputFileName, index = False)


#=============================================================
sInputFileName='C:/VKHCG/05-DS/9999-Data/4ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("4 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
print("Num of Columns: ",len(ProcessData.columns))
sColumns= ['Ch1','Ch2','Ch3', 'Ch4']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Audio-4ch.csv'
OutputData.to_csv(sOutputFileName, index = False)
#=============================================================

sInputFileName='C:/VKHCG/05-DS/9999-Data/6ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("6 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
print("Num of Columns: ",len(ProcessData.columns))
sColumns= ['Ch1','Ch2','Ch3', 'Ch4', 'Ch5','Ch6']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Audio-6ch.csv'
OutputData.to_csv(sOutputFileName, index = False)

#=============================================================
sInputFileName='C:/VKHCG/05-DS/9999-Data/8ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)
show_info("8 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
print("Num of Columns: ",len(ProcessData.columns))
sColumns= ['Ch1','Ch2','Ch3', 'Ch4', 'Ch5','Ch6','Ch7','Ch8']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Audio-8ch.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('=====================================================')
print('Audio to HORUS - Done')

              
              
              """)
    
    elif(num=="3d"):
        print(""" #Conversion from XML to HORUS

# Utility Start XML to HORUS =================================
# Standard Tools
import pandas as pd
import xml.etree.ElementTree as ET

def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root,'entry')
        for index in range(data.shape[1]):
            schild=str(header[index])
            child = ET.SubElement(entry, schild)
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
            entry.append(child)
    result = ET.tostring(root)
    return result


def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)
    
    

sInputFileName='C:/VKHCG/05-DS/9999-Data/Country_Code.xml'
InputData = open(sInputFileName).read()
print('=====================================================')
print('Input Data Values ===================================')
print('=====================================================')
print(InputData)
print('=====================================================')
#=============================================================
# Processing Rules ===========================================
#==============================================
ProcessDataXML=InputData
# XML to Data Frame
ProcessData=xml2df(ProcessDataXML)
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)
# Sort data by CurrencyNumber
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print('=====================================================')
print('Process Data Values =================================')
print('=====================================================')
print(ProcessData)
print('=====================================================')
OutputData=ProcessData
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-XML-Country.csv'
OutputData.to_csv(sOutputFileName, index = False)
#OutputData.to_csv("C:/Users/prana/Desktop/Temp/output_fileB.csv", index = False)
print('=====================================================')
print('XML to HORUS - Done')
print('=====================================================')
# Utility done ===============================================

              
              
              """)
    
    elif(num=="4a"):
        print(""" #Fixers utilities
import string
import datetime as dt

# 1 Removing leading or lagging spaces from a data entry
print("#1 Removing leading or lagging spaces from a data entry")
baddata = "     Data Science with too many spaces is bad!!!        "
print(">", baddata, "<")
cleandata = baddata.strip()
print(">", cleandata, "<")


# 2 Removing nonprintable characters from a data entry
print('#2 Removing nonprintable characters from a data entry')
printable = set(string.printable)
baddata = "Data 😁 Science with 🎶funny characters is bad😂!!!"
cleandata = ""
for i in baddata:
    if(i in string.printable):
        cleandata = cleandata + i 

print('Bad Data : ',baddata);
print('Clean Data : ',cleandata)


# 3 Reformatting data entry to match specific formatting criteria.
# Convert YYYY/MM/DD to DD Month YYYY
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddate = dt.date(2022, 1, 5)
gooddata=format(baddate,'%d %B %Y')
print('Bad Data : ',baddata)
print('Good Data : ',gooddata)
   
              """)
        
    elif(num=="4b"):
        print(""" #Data Binning or Bucketing
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
np.random.seed(0)
mu = 90
sigma = 25
x = mu + sigma * np.random.randn(5000)
num_bins = 25

fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1)
y = stats.norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')

ax.set_xlabel('Example Data')
ax.set_ylabel('Probability density')
sTitle='Histogram ' + str(len(x)) + ' entries into ' + str(num_bins) + \
' Bins: mu=' + str(mu) + ', sigma=' + str(sigma)
ax.set_title(sTitle)

fig.tight_layout()
sPathFig='C:/VKHCG/05-DS/4000-UL/0200-DU/DU-Histogram.png'
fig.savefig(sPathFig)
plt.show()

              
              """)
        
    elif(num=="4c"):
        print(""" #Averaging of data
import pandas as pd

sFileName = 'C:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_CORE.csv'
print('Loading :',sFileName)
IP_DATA_ALL = pd.read_csv(sFileName,header=0,
                          low_memory=False,
                          usecols=['Country','Place Name','Latitude','Longitude'],
                          encoding="latin-1")

IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
AllData = IP_DATA_ALL[['Country', 'Place_Name','Latitude']]
print(AllData)

MeanData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
print(MeanData)

              
              """)
        
    elif(num=="4d"):
        print(""" #Outlier Detection
import pandas as pd

sFileName = 'C:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_CORE.csv'
print('Loading :',sFileName)
IP_DATA_ALL = pd.read_csv(sFileName,
                          header=0,
                          low_memory=False,
                          usecols=['Country','Place Name','Latitude','Longitude'], 
                          encoding="latin-1")

IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)

LondonData = IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name']=='London']
AllData = LondonData[['Country', 'Place_Name','Latitude']]
print('All Data')
print(AllData)

MeanData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
StdData  = AllData.groupby(['Country', 'Place_Name'])['Latitude'].std()

print('Outliers')

UpperBound = float(MeanData+StdData)
print('Higher than ', UpperBound)
OutliersHigher = AllData[AllData.Latitude>UpperBound]
print(OutliersHigher)

LowerBound=float(MeanData-StdData)
print('Lower than ', LowerBound)
OutliersLower = AllData[AllData.Latitude<LowerBound]
print(OutliersLower)

print('Not Outliers')
OutliersNot = AllData[(AllData.Latitude>=LowerBound) & (AllData.Latitude<=UpperBound)]
print(OutliersNot)
              
              
              """)
        
    elif(num=="4e"):
        print(""" #Audit – Logging
import os
import logging
import uuid
import shutil
import time
############################################################
Base='C:/VKHCG'
############################################################
sCompanies=['01-Vermeulen','02-Krennwallner','03-Hillman','04-Clark']
sLayers=['01-Retrieve','02-Assess','03-Process','04-Transform','05-Organise','06-Report']
sLevels=['debug','info','warning','error']
for sCompany in sCompanies:
    sFileDir=Base + '/' + sCompany
    if not os.path.exists(sFileDir):
        os.makedirs(sFileDir)
    for sLayer in sLayers:
        log = logging.getLogger() # root logger
        for hdlr in log.handlers[:]: # remove all old handlers
            log.removeHandler(hdlr)
            
        sFileDir=Base + '/' + sCompany + '/' + sLayer + '/Logging'
        if os.path.exists(sFileDir):
          shutil.rmtree(sFileDir)
        time.sleep(2)
        if not os.path.exists(sFileDir):
            os.makedirs(sFileDir)
        skey=str(uuid.uuid4())
        sLogFile=Base + '/' + sCompany + '/' + sLayer + '/Logging/Logging_'+skey+'.log'
        #print('#'*20,skey)
        print('Set up:',sLogFile)
        logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=sLogFile,
            filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        logging.info('Practical Data Science is fun!.')
         
        for sLevel in sLevels:
          sApp='Apllication-'+ sCompany + '-' + sLayer + '-' + sLevel
          logger = logging.getLogger(sApp)
          if sLevel == 'debug':
              logger.debug('Practical Data Science logged a debugging message.')
          if sLevel == 'info':
              logger.info('Practical Data Science logged information message.')
          if sLevel == 'warning':
              logger.warning('Practical Data Science logged a warning message.')
          if sLevel == 'error':
              logger.error('Practical Data Science logged an error message.')


              
              
              """)
        
    elif(num=="5a"):
        print(""" #Program to retrieve different types of attributes
import pandas as pd

sFileName ='C:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print('Loading :',sFileName)
IP_DATA_ALL = pd.read_csv(sFileName, 
                          header=0,
                          low_memory=False, 
                          encoding="latin-1")

sFileDir= 'C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python'

print('Rows:', IP_DATA_ALL.shape[0])
print('Columns:', IP_DATA_ALL.shape[1])

print('### Raw Data Set ')
for i in range(0,len(IP_DATA_ALL.columns)):
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
    
print('### Fixed Data Set ')
IP_DATA_ALL_FIX=IP_DATA_ALL
for i in range(0,len(IP_DATA_ALL.columns)):
    cNameOld=IP_DATA_ALL_FIX.columns[i] + ' '
    cNameNew=cNameOld.strip().replace(" ", ".")
    IP_DATA_ALL_FIX.columns.values[i] = cNameNew
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
    
#print(IP_DATA_ALL_FIX.head())
print('Fixed Data Set with ID')
IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
IP_DATA_ALL_with_ID.index.names = ['RowID']
#print(IP_DATA_ALL_with_ID.head())

sFileName2='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
IP_DATA_ALL_with_ID.to_csv(sFileName2, index = True, encoding="latin-1")

print('### Done!!' )

              
              """)
        
    elif(num=="5b"):
        print(""" #Data Pattern
import pandas as pd
import string

sFileName = 'C:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print('Loading :',sFileName)

IP_DATA = pd.read_csv(sFileName,
                      header=0,
                      usecols=['Country','Latitude'],
                      low_memory=False,
                      encoding="latin-1")


IP_DATA['PatternCountry'] = ''
IP_DATA['PatternLatitude'] = ''

def Pattern(val):
    alpha = string.ascii_letters
    num = string.digits
    space = string.whitespace
    temp2 = []
    #temp = val
    
    for i in val :
        #print(i)
        if i in alpha:
            temp2.append("A")
        elif i in num:
            temp2.append("N")
        elif i in space:
            temp2.append("b")
        else:
            temp2.append("u")
        
    s = ''.join(str(x) for x in temp2)
    return s



for i in range(0,len(IP_DATA.axes[0])): 
    country = IP_DATA.Country.values[i] 
    latitude = IP_DATA.Latitude.values[i]
    
    country = str(country)
    latitude = str(latitude)
    
    IP_DATA.PatternCountry.values[i] = Pattern(country)
    IP_DATA.PatternLatitude.values[i] = Pattern(latitude)
        
        
IP_DATA

              
              
              
              """)
        
    elif(num=="5c"):
        print(""" #Loading IP_DATA_ALL
################################################################
import pandas as pd

sFileName='C:/VKHCG' + '/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
print('Loading :',sFileName)
IP_DATA_ALL = pd.read_csv(sFileName,
                          header=0,
                          low_memory=False, 
                          encoding="latin-1")
print('Rows:', IP_DATA_ALL.shape[0])
print('Columns:', IP_DATA_ALL.shape[1])

print('### Raw Data Set  ')
for i in range(0,len(IP_DATA_ALL.columns)):
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
    
print('### Fixed Data Set  ')
IP_DATA_ALL_FIX=IP_DATA_ALL
for i in range(0,len(IP_DATA_ALL.columns)):
    cNameOld=IP_DATA_ALL_FIX.columns[i] + ' '
    cNameNew=cNameOld.strip().replace(" ", ".")
    IP_DATA_ALL_FIX.columns.values[i] = cNameNew
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))

#print(IP_DATA_ALL_FIX.head())
print('Fixed Data Set with ID')
IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
IP_DATA_ALL_with_ID.index.names = ['RowID']
#print(IP_DATA_ALL_with_ID.head())

sFileName2='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
IP_DATA_ALL_with_ID.to_csv(sFileName2, index = True, encoding="latin-1")

print('### Done!!  ')

              
              
              """)
        
    elif(num=="6a"):
        print(""" #Horizontal style
import pandas as pd
import sqlite3 as sq

sDatabaseName = 'C:/VKHCG/99-DW/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)

sDatabaseName = 'C:/VKHCG/99-DW/datamart.db'
conn2 = sq.connect(sDatabaseName)

print('################')
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0 = pd.read_sql_query(sSQL, conn1)

print('################')
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT PersonID, Height, Weight, bmi, Indicator FROM [Dim-BMI]\
    WHERE Height > 1.5 and Indicator = 1\
    ORDER BY Height, Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)


DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)

sTable = 'Dim-BMI'

print('Storing :',sDatabaseName,'\n Table:',sTable)
#DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")


sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)

print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])

              
              """)
        
    elif(num=="6b"):
        print(""" #Vertical style
import pandas as pd
import sqlite3 as sq

sDatabaseName = 'C:/VKHCG/99-DW/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)

sDatabaseName = 'C:/VKHCG/99-DW/datamart.db'
conn2 = sq.connect(sDatabaseName)


sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0 = pd.read_sql_query(sSQL, conn1)

sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)


sSQL="SELECT Height,Weight, Indicator FROM [Dim-BMI];"
PersonFrame1 = pd.read_sql_query(sSQL, conn1)


DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)

sTable = 'Dim-BMI-Vertical'
print('Storing :',sDatabaseName,'\n Table:',sTable)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")


sTable = 'Dim-BMI-Vertical'
print('Loading :',sDatabaseName,' Table:',sTable)

sSQL="SELECT * FROM [Dim-BMI-Vertical];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)

print('################################')
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('################################')

             
              """)
    
    elif(num=="6c"):
        print(""" #Island style 
import pandas as pd
import sqlite3 as sq

sDatabaseName = 'C:/VKHCG/99-DW/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)

sDatabaseName = 'C:/VKHCG/99-DW/datamart.db'
conn2 = sq.connect(sDatabaseName)

sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)


sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT Height,Weight,Indicator FROM [Dim-BMI]\
    WHERE Indicator > 2 ORDER BY Height,Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)


DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)

sTable = 'Dim-BMI-Vertical'
print('Storing :',sDatabaseName,'\n Table:',sTable)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")


sTable = 'Dim-BMI-Vertical'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI-Vertical];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)


print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print()
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])

              
              """)
    
    elif(num=="6d"):
        print(""" #Secure Vault style
import pandas as pd
import sqlite3 as sq

sDatabaseName = 'C:/VKHCG/99-DW/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)

sDatabaseName = 'C:/VKHCG/99-DW/datamart.db'
conn2 = sq.connect(sDatabaseName)
 
sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)

sTable = 'Dim-BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL = "SELECT Height, Weight, Indicator, CASE Indicator\
        WHEN 1 THEN 'Pip'\
        WHEN 2 THEN 'Norman'\
        WHEN 3 THEN 'Grant'\
        ELSE 'Sam'\
        END AS Name\
        FROM [Dim-BMI] WHERE Indicator > 2 ORDER BY Height, Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)

DimPerson=PersonFrame1
DimPersonIndex=DimPerson.set_index(['Indicator'],inplace=False)

sTable = 'Dim-BMI-Secure'
print('Storing :',sDatabaseName,'\n Table:',sTable)
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")


sTable = 'Dim-BMI-Secure'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';"
PersonFrame2=pd.read_sql_query(sSQL, conn2)


print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print()
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])
print('Only Sam Data')
print(PersonFrame2.head())

              
              """)
    
    elif(num=="8a"):
        print(""" ##(CHANGE THE SLIP)## """*10)
        
    elif(num=="8b"):
        print(""" Simple Linear Regression

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-50:]
diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-50:]
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)
print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.axis('tight')
plt.title("Diabetes")
plt.xlabel("BMI")
plt.ylabel("Age")
plt.show()
              
              
              """)
    
    elif(num=="9a"):
        print(""" #9a.Vermeulen PLC
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

### Import Country Data
sFileName='C:/VKHCG/01-Vermeulen/02-Assess/01-EDS/02-Python/Assess-Network-Routing-Customer.csv'
print('Loading :',sFileName)
print('################################')
CustomerDataRaw=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
CustomerData=CustomerDataRaw.head(100)
print('Loaded Country:',CustomerData.columns.values)
print('################################')

print(CustomerData.head())
print(CustomerData.shape)

G=nx.Graph()
for i in range(CustomerData.shape[0]):
    for j in range(CustomerData.shape[0]):
        Node0=CustomerData['Customer_Country_Name'][i]
        Node1=CustomerData['Customer_Country_Name'][j]
        if Node0 != Node1:
            G.add_edge(Node0,Node1)
            
for i in range(CustomerData.shape[0]):
    Node0=CustomerData['Customer_Country_Name'][i]
    Node1=CustomerData['Customer_Place_Name'][i] + '('+ CustomerData['Customer_Country_Name'][i] + ')'
    Node2='('+ "{:.9f}".format(CustomerData['Customer_Latitude'][i]) + ')\
    ('+ "{:.9f}".format(CustomerData['Customer_Longitude'][i]) + ')'
    if Node0 != Node1:
        G.add_edge(Node0,Node1)
    if Node1 != Node2:
        G.add_edge(Node1,Node2)
 
print('Nodes:', G.number_of_nodes()) 
print('Edges:', G.number_of_edges()) 
 
sFileName='C:/VKHCG/01-Vermeulen/06-Report/01-EDS/02-Python/Report-Network-Routing-Customer.gml'
print('################################')
print('Storing :',sFileName)
nx.write_gml(G, sFileName) 


sFileName='C:/VKHCG/01-Vermeulen/06-Report/01-EDS/02-Python/Report-Network-Routing-Customer.png'
print('################################')
print('Storing Graph Image:',sFileName)

plt.figure(figsize=(25, 25))
pos=nx.spectral_layout(G,dim=2)
nx.draw_networkx_nodes(G,pos, node_color='k', node_size=10, alpha=0.8)
nx.draw_networkx_edges(G, pos,edge_color='r', arrows=False, style='dashed')
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif',font_color='b')
plt.axis('off')
plt.savefig(sFileName,dpi=600)
plt.show()
print('### Done!! ')
              
              """)
        
    elif(num=="9b"):
        print(""" #9b.Krennwallner AG 

##pip install folium
import sys
import os
import pandas as pd
from folium.plugins import FastMarkerCluster, HeatMap
from folium import Marker, Map
import webbrowser
################################################################
Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileName=Base+'/02-Krennwallner/01-Retrieve/01-EDS/02-Python/Retrieve_DE_Billboard_Locations.csv'
df = pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
df.fillna(value=0, inplace=True)
print(df.shape)
################################################################
t=0
for i in range(df.shape[0]):
    try:
        sLongitude=df["Longitude"][i]
        sLongitude=float(sLongitude)
    except Exception:
        sLongitude=float(0.0)
        
    try:
        sLatitude=df["Latitude"][i]
        sLatitude=float(sLatitude)
    except Exception:
        sLatitude=float(0.0)
        
    try:
        sDescription=df["Place_Name"][i] + ' (' + df["Country"][i]+')'
    except Exception:
        sDescription='VKHCG'
    
    if sLongitude != 0.0 and sLatitude != 0.0:
        DataClusterList=list([sLatitude, sLongitude])
        DataPointList=list([sLatitude, sLongitude, sDescription])
        t+=1
        if t==1:
            DataCluster=[DataClusterList]
            DataPoint=[DataPointList]
        else:
            DataCluster.append(DataClusterList)
            DataPoint.append(DataPointList)
data=DataCluster
pins=pd.DataFrame(DataPoint)
pins.columns = [ 'Latitude','Longitude','Description']
################################################################
stops_map1 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
marker_cluster = FastMarkerCluster(data).add_to(stops_map1)
sFileNameHtml=Base+'/02-Krennwallner/06-Report/01-EDS/02-Python/Billboard1.html'
stops_map1.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
stops_map2 = Map(location=[48.1459806, 11.4985484], zoom_start=5)
for name, row in pins.iloc[:100].iterrows():
    Marker([row["Latitude"],row["Longitude"]], popup=row["Description"]).add_to(stops_map2)
sFileNameHtml=Base+'/02-Krennwallner/06-Report/01-EDS/02-Python/Billboard2.html'
stops_map2.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
stops_heatmap = Map(location=[48.1459806, 11.4985484], zoom_start=5)
stops_heatmap.add_child(HeatMap([[row["Latitude"], row["Longitude"]] for name, row in 
pins.iloc[:100].iterrows()]))
sFileNameHtml=Base+'/02-Krennwallner/06-Report/01-EDS/02-Python/Billboard_heatmap.html'
stops_heatmap.save(sFileNameHtml)
webbrowser.open('file://' + os.path.realpath(sFileNameHtml))
################################################################
print('### Done!! ############################################')
################################################################
              
              """)

    elif(num=="10a"):
        print(""" #Build the time Hub, Link and Satellite
import sys
import os
from datetime import datetime
from datetime import timedelta
from pytz import timezone, all_timezones
import pandas as pd
import sqlite3 as sq
from pandas.io import sql
import uuid

pd.options.mode.chained_assignment = None
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
Company='01-Vermeulen'
InputDir='00-RawData'
InputFileName='VehicleData.csv'
################################################################
sDataBaseDir=Base + '/' + Company + '/03-Process/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataBaseDir + '/Hillman.db'
conn1 = sq.connect(sDatabaseName)
################################################################
sDataVaultDir=Base + '/88-DV'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
################################################################
sDatabaseName=sDataVaultDir + '/datavault.db'
conn2 = sq.connect(sDatabaseName)
################################################################
base = datetime(2018,1,1,0,0,0)
numUnits=10*365*24
################################################################
date_list = [base - timedelta(hours=x) for x in range(0, numUnits)]
t=0
for i in date_list:
    now_utc=i.replace(tzinfo=timezone('UTC')) 
    sDateTime=now_utc.strftime("%Y-%m-%d %H:%M:%S")  
    print(sDateTime)
    sDateTimeKey=sDateTime.replace(' ','-').replace(':','-')
    t+=1
    IDNumber=str(uuid.uuid4())
    TimeLine=[('ZoneBaseKey', ['UTC']),
             ('IDNumber', [IDNumber]),
             ('nDateTimeValue', [now_utc]),
             ('DateTimeValue', [sDateTime]),
             ('DateTimeKey', [sDateTimeKey])] 
    if t==1:
       TimeFrame = pd.DataFrame.from_dict(TimeLine) 
    else:
        TimeRow = pd.DataFrame.from_dict(TimeLine)
        TimeFrame = TimeFrame.append(TimeRow) 
################################################################
TimeHub=TimeFrame[['IDNumber','ZoneBaseKey','DateTimeKey','DateTimeValue']]
TimeHubIndex=TimeHub.set_index(['IDNumber'],inplace=False)
################################################################
TimeFrame.set_index(['IDNumber'],inplace=True)
################################################################
sTable = 'Process-Time'
print('Storing :',sDatabaseName,' Table:',sTable)
TimeHubIndex.to_sql(sTable, conn1, if_exists="replace")
################################################################
sTable = 'Hub-Time'
print('Storing :',sDatabaseName,' Table:',sTable)
TimeHubIndex.to_sql(sTable, conn2, if_exists="replace")
################################################################ 
active_timezones=all_timezones
z=0
for zone in active_timezones:    
    t=0
    for j in range(TimeFrame.shape[0]): 
        now_date=TimeFrame['nDateTimeValue'][j]
        DateTimeKey=TimeFrame['DateTimeKey'][j]
        now_utc=now_date.replace(tzinfo=timezone('UTC'))
        sDateTime=now_utc.strftime("%Y-%m-%d %H:%M:%S") 
        now_zone = now_utc.astimezone(timezone(zone)) 
        sZoneDateTime=now_zone.strftime("%Y-%m-%d %H:%M:%S")  
        print(sZoneDateTime)
        t+=1
        z+=1
        IDZoneNumber=str(uuid.uuid4())
        TimeZoneLine=[('ZoneBaseKey', ['UTC']),
                      ('IDZoneNumber', [IDZoneNumber]),
                      ('DateTimeKey', [DateTimeKey]),
                      ('UTCDateTimeValue', [sDateTime]),
                      ('Zone', [zone]),
                      ('DateTimeValue', [sZoneDateTime])] 
        if t==1:
           TimeZoneFrame = pd.DataFrame.from_dict(TimeZoneLine) 
        else:
            TimeZoneRow = pd.DataFrame.from_dict(TimeZoneLine)
            TimeZoneFrame = TimeZoneFrame.append(TimeZoneRow)
            
    TimeZoneFrameIndex=TimeZoneFrame.set_index(['IDZoneNumber'],inplace=False)
    sZone=zone.replace('/','-').replace(' ','')
    #############################################################  
    sTable = 'Process-Time-'+sZone
    print('Storing :',sDatabaseName,' Table:',sTable)
    TimeZoneFrameIndex.to_sql(sTable, conn1, if_exists="replace")
#################################################################
    #############################################################  
    sTable = 'Satellite-Time-'+sZone
    print('Storing :',sDatabaseName,' Table:',sTable)
    TimeZoneFrameIndex.to_sql(sTable, conn2, if_exists="replace")
#################################################################
print('################') 
print('Vacuum Databases')
sSQL="VACUUM;"
sql.execute(sSQL,conn1)
sql.execute(sSQL,conn2)
print('################') 
#################################################################
print('### Done!! ############################################')              
              
              """)
        
    elif(num=="10b"):
        print(""" ##(CHANGE THE SLIP)## """*10)
        
    elif(num=="10c"):
        print(""" 

################################################################
import sys
import os
import sqlite3 as sq
import quandl
import pandas as pd
################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
Company='04-Clark'
sInputFileName='00-RawData/VKHCG_Shares.csv'
sOutputFileName='Shares.csv'
################################################################
sDataBaseDir=Base + '/' + Company + '/03-Process/SQLite'
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir) 
################################################################
sFileDir1=Base + '/' + Company + '/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir1):
    os.makedirs(sFileDir1) 
################################################################
sFileDir2=Base + '/' + Company + '/02-Assess/01-EDS/02-Python'
if not os.path.exists(sFileDir2):
    os.makedirs(sFileDir2) 
################################################################
sFileDir3=Base + '/' + Company + '/03-Process/01-EDS/02-Python'
if not os.path.exists(sFileDir3):
    os.makedirs(sFileDir3) 
################################################################
sDatabaseName=sDataBaseDir + '/clark.db'
conn = sq.connect(sDatabaseName)
################################################################
### Import Share Names Data
################################################################
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
RawData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
RawData.drop_duplicates(subset=None, keep='first', inplace=True)
print('Rows   :',RawData.shape[0])
print('Columns:',RawData.shape[1])
print('################')   
################################################################
sFileName=sFileDir1 + '/Retrieve_' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
RawData.to_csv(sFileName, index = False)
print('################################')  
################################################################
sFileName=sFileDir2 + '/Assess_' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
RawData.to_csv(sFileName, index = False)
print('################################')  
################################################################
sFileName=sFileDir3 + '/Process_' + sOutputFileName
print('################################')
print('Storing :', sFileName)
print('################################')
RawData.to_csv(sFileName, index = False)
print('################################')
################################################################
### Import Shares Data Details
################################################################
nShares=RawData.shape[0]
nShares=6
for sShare in range(nShares):
    sShareName=str(RawData['Shares'][sShare])
    ShareData = quandl.get(sShareName)
    UnitsOwn=RawData['Units'][sShare]
    ShareData['UnitsOwn']=ShareData.apply(lambda row:(UnitsOwn),axis=1)
    ShareData['ShareCode']=ShareData.apply(lambda row:(sShareName),axis=1)
    print('################') 
    print('Share  :',sShareName) 
    print('Rows   :',ShareData.shape[0])
    print('Columns:',ShareData.shape[1])
    print('################')  
    #################################################################
    print('################')  
    sTable=str(RawData['sTable'][sShare])
    print('Storing :',sDatabaseName,' Table:',sTable)
    ShareData.to_sql(sTable, conn, if_exists="replace")
    print('################')  
    ################################################################
    sOutputFileName = sTable.replace("/","-") + '.csv'
    sFileName=sFileDir1 + '/Retrieve_' + sOutputFileName
    print('################################')
    print('Storing :', sFileName)
    print('################################')
    ShareData.to_csv(sFileName, index = False)
    print('################################')
    ################################################################
    sOutputFileName = sTable.replace("/","-") + '.csv'
    sFileName=sFileDir2 + '/Assess_' + sOutputFileName
    print('################################')
    print('Storing :', sFileName)
    print('################################')
    ShareData.to_csv(sFileName, index = False)
    print('################################')
    ################################################################
    sOutputFileName = sTable.replace("/","-") + '.csv'
    sFileName=sFileDir3 + '/Process_' + sOutputFileName
    print('################################')
    print('Storing :', sFileName)
    print('################################')
    ShareData.to_csv(sFileName, index = False)
    print('################################')
################################################################
################################################################
print('### Done!! ############################################')              
              
              """)
    else:
        print("Invalid Input")







