import numpy as np
import pandas as pd

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
import numpy as np
import pandas as pd

def load_matrix_from_excel(file_path, sheet_name=0):
    # Load the data from the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Replace non-numeric placeholders with `float('inf')` and convert all entries to floats
    df.replace({"-": float('inf'), "inf": float('inf')}, inplace=True)
    df = df.apply(pd.to_numeric, errors='coerce')
    
    # Fill any remaining non-numeric entries with `float('inf')`
    df.fillna(float('inf'), inplace=True)
    
    # Convert the DataFrame to a Numpy array
    matrix = df.to_numpy()
    return matrix

# Loading in Matrix
file_path = 'Diekstra Data.xlsx'
matrix = load_matrix_from_excel(file_path)
# file_path_1 = 'DiDataAcc.xlsx'
# acc_matrix = load_matrix_from_excel(file_path_1)import numpy as np
import pandas as pd

def load_matrix_from_excel(file_path, sheet_name=0):
    # Load the data from the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Replace non-numeric placeholders with `float('inf')` and convert all entries to floats
    df.replace({"-": float('inf'), "inf": float('inf')}, inplace=True)
    df = df.apply(pd.to_numeric, errors='coerce')
    
    # Fill any remaining non-numeric entries with `float('inf')`
    df.fillna(float('inf'), inplace=True)
    
    # Convert the DataFrame to a Numpy array
    matrix = df.to_numpy()
    return matrix

# Loading in Matrix
file_path = 'Diekstra Data.xlsx'
matrix = load_matrix_from_excel(file_path)
# file_path_1 = 'DiDataAcc.xlsx'
# acc_matrix = load_matrix_from_excel(file_path_1)

# Naming Dictionary
name_mapping = {
    'A': 'Jamie',
    'B': 'Jamie (Right Intersection Facing Street Side)',
    'C': 'Daley (Immediant Entrance Street Side)',
    'D': 'Daley (Near Ridge Road)',
    'E': 'Jamie/Daley Intersection',
    'F': 'Jamie (Courtyard Entrance)',
    'G': 'Jamie Courtyard Intersection',
    'H': 'Hart (MCR Entrance)',
    'I': 'Hart Triangle',
    'J': 'Daley Courtyard',
    'K': 'Daley Courtyard (Near Trees)',
    'L': 'Ryburn (Laundry Entrance 1st Floor)',
    'M': 'Flowe (MCR Side)',
    'N': 'Ryburn (F Entrance)',
    'O': 'Ryburn (Laundry Entrance 2nd Floor)',
    'P': 'Hart (Courtyard Entrance)',
    'Q': 'Hart/Daley Intersection',
    'R': 'Davis (MCR Entrance)',
    'S': 'Daley/Ryburn Intersection',
    'T': 'Daley (Courtyard Entrance)',
    'U': 'Daley Courtyard (Near Trees)',
    'V': 'MCR Stairs (top)',
    'W': 'Railing Path',
    'X': 'Davis (Road)',
    'Y': 'Davis (Immediate Entrance)',
    'Z': 'Flowe (PCR)',
    'AA': 'Nummit ',
    'AB': 'Nummit (Long Path)',
    'AC': 'KSIG',
    'AD': 'BSC',
    'AE': 'Rusk',
    'AF': 'Patterson Court Intersection',
    'AG': 'Warner',
    'AH': 'Turner',
    'AI': 'SAE/Warner',
    'AJ': 'SPE/Fiji',
    'AK': 'Commons Lower',
    'AL': 'SPE',
    'AM': 'SAE',
    'AN': 'Fiji',
    'AO': 'Chinsey (Down Steps)',
    'AP': 'PhiDelt',
    'AQ': 'Connor',
    'AR': 'Chinsey (Gym Entrance)',
    'AS': 'F (Top Trashcan)',
    'AT': 'F (Main Courtyard)',
    'AU': 'F Basketball Court',
    'AV': 'Cross Country Trail Head',
    'AW': 'VAC',
    'AX': 'CInn',
    'AY': 'T&I',
    'AZ': 'Depot',
    'BA': 'CollegeStore',
    'BB': 'DCPC',
    'BC': 'Watson',
    'BD': 'WatsonSloanInt',
    'BE': 'Dana',
    'BF': 'Sloan',
    'BG': 'SloanChambersInt',
    'BH': 'ChambersS',
    'BI': 'LillyGallery',
    'BJ': 'Chambers',
    'BK': 'ChambersW',
    'BL': 'ChambersLawnInt',
    'BM': 'ChambersLawnIntB',
    'BN': 'PhilanthropicHall',
    'BO': 'EumeneanHall',
    'BP': 'ElmRow',
    'BQ': 'OakRow',
    'BR': 'Cunningham',
    'BS': 'CarnegieGH (changed to Carnegie House Entrance Facing Academic buildings)',
    'BT': 'Little (changed to Little Main Entrance)',
    'BU': 'Watts (changed to Watts Main entrance)',
    'BV': 'ChambersInt6',
    'BW': 'FlagPole',
    'BX': 'SittingSculpture',
    'BY': 'Sentelle (changed to Sentelle Main Entrance)',
    'BZ': 'FlagPoleR (Changed to Semicircle intersection by Belk, Watts and Cannon)',
    'CA': 'Cannon (changed to cannon front entrance)',
    'CB': 'South Side Chinsey Path Intersection',
    'CC': 'Spencer Wienstien/Chinsey',
    'CD': 'Triangle Between Tommy/SW',
    'CE': 'South Side Back Chinsey Lot',
    'CF': 'South Side Back Chinsey Dumpster',
    'CG': 'Campo Office',
    'CH': 'Tommy North Side',
    'CI': 'Spencer Wienstien Entrance',
    'CJ': 'Spencer Wienstien North',
    'CK': 'Spencer Wienstien Commons Intersection',
    'CL': 'Commons Lower',
    'CM': 'Commons Brick Replacement',
    'CN': 'North Side Rich Near Tree',
    'CO': 'Big Tree Near Rich Intersection',
    'CP': 'Rich Entrance North',
    'CQ': 'Tommy Rich Intersection',
    'CR': 'South East Tommy ',
    'CS': 'South Side Tommy Entrance',
    'CT': 'East Side, Rich lot Ciccle',
    'CU': 'West Rich Entrance',
    'CV': 'South Side Rich',
    'CW': 'South East Rich Intersection',
    'CX': 'East Most Rich Parkinglot Entrance',
    'CY': 'Commons South West Entrance',
    'CZ': 'Commons West Triangle North',
    'CA': 'Commons West Triangle South',
    'CB': 'Commons West Triangle East',
    'CC': 'Commons Triangles Intersection',
    'CD': 'Commons East Triangle West',
    'CE': 'Commons East Triangle North',
    'CF': 'Commons South Entrance Lower',
    'CG': 'Commons South Entrance Upper',
    'CH': 'Commons Lower West',
    'CI': 'Commons East Triangle South',
    'CJ': 'RLO',
    'CK': 'Old Laundry Room',
    'CL': 'RLO/Belk Intersection',
    'CM': 'Belk Base North Entrance',
    'CN': 'Belk North East',
    'CO': 'Belk North Entrence East',
    'CP': 'Belk North Entrance',
    'CQ': 'Belk Tree Commons Path',
    'CR': 'Belk Tree Rich',
    'CS': 'Belk North Entrance West',
    'CT': 'Belk West Entrance Immediate',
    'CU': 'Tommy/Rich lot to Health Center',
    'CV': 'Health Center',
    'CW': 'Back of Belk corner by Parking lot',
    'CX': 'Belk Basement Entrance (Parking Lot)',
    'CY': 'Watts back entrance',
    'CZ': 'Belk Entrance, Left Wing',
    'DA': 'Main Belk Entrance',
    'DB': 'Center of Belk intersection in front of Main Belk Entrance',
    'DC': 'Belk Entrance, Right Wing',
    'DD': 'Semicircle intersection by Belk, Watts and Cannon',
    'DE': 'Watts (Right intersection)',
    'DF': 'Watts Front Entrance',
    'DG': 'Watts (Left Intersection)',
    'DH': 'Watts (Back by Outside Area)',
    'DI': 'Little Back Entrance',
    'DJ': 'Little (Parking Lot Path)',
    'DK': 'Carnegie House (Entrance by Presidents House)',
    'DL': 'Parking Lot By Presidents House',
    'DM': 'Carnegie House Main Entrance',
    'DN': 'Carnegie House Entrance Facing Academic buildings',
    'DO': 'Little Main Entrance',
    'DP': 'Base Belk Entrance',
    'DQ': 'LuluBells Bottom of Stairs',
    'DR': 'LuluBells Top of Stairs',
    'DS': 'Watts Back Entrance',
    'DT': 'Cannon/ Sentelle (Back center intersection)',
    'DU': 'Sentelle Back Entrance',
    'DV': 'Duke Left Wing Entrance',
    'DW': 'Sentelle Main Entrance',
    'DX': 'Semicircle between Sentelle/Watts',
    'DY': 'Cannon/Sentelle (Front Center Intersection)',
    'DZ': 'Cannon Front Entrance',
    'EA': 'Wildcat',
    'EB': 'Baker Entrance',
    'EC': 'Tennis Courts',
    'ED': 'Track Corner',
    'EE': 'Bottom Labryinth',
    'EF': 'Top Labryinth',
    'EG': 'Hobart Park below Labryinth',
    'EH': 'White House',
    'EI': 'HR',
    'EJ': 'Jackson Court',
    'EK': 'School Side Jackson Court Entrance',
    'EL': 'Faculty Drive Right Corner',
    'EM': 'Faculty Drive Wall Corner',
    'EN': 'Right Side Wall Entrance',
    'EO': 'Back of Wall Entrance',
    'EP': 'Back Left Corner Wall',
    'EQ': 'Left Side Wall Entrance',
    'ER': 'Bottom Right Chambers 4-way',
    'ES': 'Top BR Chambers Wedge',
    'ET': 'Sculpture Garden',
    'EU': 'Right Side Chambers',
    'EV': 'Right BR Chambers Wedge',
    'EW': 'Wall',
    'EX': 'Wall Entrance',
    'EY': 'Top TR Wall Wedge',
    'EZ': 'Left TR Wall Wedge',
    'FA': 'Right TR Wall Wedge',
    'FB': 'Front Libs',
    'FC': 'Left TL Library Wedge',
    'FD': 'Right TL Library Wedge',
    'FE': 'Top TL Library Wedge',
    'FF': 'Top Libs 4-Way',
    'FG': 'Upper Left Duke Intersection',
    'FH': 'Front libs Chute',
    'FI': 'Back Libs Chute',
    'FJ': 'New Gym Entrance',
    'FK': 'Track/Libs/Duke Intersection',
    'FL': 'Track',
    'FM': 'Upper Union 4-way',
    'FN': 'Upper Right Side Duke',
    'FO': 'Lower Right Side Duke',
    'FP': 'Lower Right Side Duke Entrance',
    'FQ': 'Lower Union 4-Way',
    'FR': 'Duke Back Union Corner',
    'FS': 'Front Duke',
    'FT': 'Front Duke Entrance',
    'FU': 'Back Duke',
    'FV': 'Left Side Duke',
    'FW': 'Lower Left Duke Intersection',
    'FX': 'Baker Loopy',
    'FY': 'C Union',
    'FZ': 'A Union',
    'GA': 'Qdoba',
    'GB': 'Stowe Intersection',
    'GC': 'Qdoba Intersection',
    'GD': 'Side Baker',
    'GE': 'Union Qdoba side',
    'GF': 'Back Door Libs',
    'GG': 'Telephone',
    'GH': 'BL Track Intersection ',
    'GI': 'Olas/Pasas',
    'GJ': 'Commons Outdoor Seating',
}

location_to_coordinates = { 
   'Jamie': 'Latitude_35.5025795370159_Longitude_-80.8398994266764',
    'Jamie (Right Intersection Facing Street Side)': 'Latitude_35.5024709352551_Longitude_-80.8399784801042',
    'Daley (Immediant Entrance Street Side)': 'Latitude_35.5024065785868_Longitude_-80.8403292796899',
    'Daley (Near Ridge Road)': 'Latitude_35.5023301549762_Longitude_-80.8400871785674',
    'Jamie/Daley Intersection': 'Latitude_35.502534_Longitude_-80.840282',
    'Jamie (Courtyard Entrance)': 'Latitude_35.502684_Longitude_-80.840261',
    'Jamie Courtyard Intersection': 'Latitude_35.502725_Longitude_-80.84042',
    'Hart (MCR Entrance)': 'Latitude_35.50281_Longitude_-80.840948',
    'Hart Triangle': 'Latitude_35.50271_Longitude_-80.840959',
    'Daley Courtyard': 'Latitude_35.502464_Longitude_-80.840854',
    'Daley Courtyard (Near Trees)': 'Latitude_35.502484_Longitude_-80.84106',
    'Ryburn (Laundry Entrance 1st Floor)': 'Latitude_35.502237_Longitude_-80.841102',
    'Flowe (MCR Side)': 'Latitude_35.502614_Longitude_-80.841483',
    'Ryburn (F Entrance)': 'Latitude_35.502194_Longitude_-80.840727',
    'Ryburn (Laundry Entrance 2nd Floor)': 'Latitude_35.502307_Longitude_-80.841081',
    'Hart (Courtyard Entrance)': 'Latitude_35.50274_Longitude_-80.840564',
    'Hart/Daley Intersection': 'Latitude_35.502603_Longitude_-80.84062',
    'Davis (MCR Entrance)': 'Latitude_35.502887_Longitude_-80.841262',
    'Daley/Ryburn Intersection': 'Latitude_35.50234_Longitude_-80.840718',
    'Daley (Courtyard Entrance)': 'Latitude_35.502477_Longitude_-80.840672',
    'Daley Courtyard (Near Trees)': 'Latitude_35.502487_Longitude_-80.841047',
    'MCR Stairs (top)': 'Latitude_35.502751_Longitude_-80.841285',
    'Railing Path': 'Latitude_35.502888_Longitude_-80.84191',
    'Davis (Road)': 'Latitude_35.502999_Longitude_-80.841866',
    'Davis (Immediate Entrance)': 'Latitude_35.502967_Longitude_-80.841681',
    'Flowe (PCR)': 'Latitude_35.502714_Longitude_-80.841885',
    'Nummit ': 'Latitude_35.502934_Longitude_-80.842161',
    'Nummit (Long Path)': 'Latitude_35.502742_Longitude_-80.842284',
    'KSIG': 'Latitude_35.503433_Longitude_-80.842062',
    'BSC': 'Latitude_35.502563_Longitude_-80.842321',
    'Rusk': 'Latitude_35.502247_Longitude_-80.842585',
    'Patterson Court Intersection': 'Latitude_35.50319_Longitude_-80.843295',
    'Warner': 'Latitude_35.503746_Longitude_-80.842409',
    'Turner': 'Latitude_35.503908_Longitude_-80.842524',
    'SAE/Warner': 'Latitude_35.503804_Longitude_-80.842576',
    'SPE/Fiji': 'Latitude_35.503753_Longitude_-80.844134',
    'Commons Lower': 'Latitude_35.502894_Longitude_-80.844175',
    'SPE': 'Latitude_35.503536_Longitude_-80.844262',
    'SAE': 'Latitude_35.50393_Longitude_-80.842732',
    'Fiji': 'Latitude_35.503903_Longitude_-80.844033',
    'Chinsey (Down Steps)': 'Latitude_35.503422_Longitude_-80.844446',
    'PhiDelt': 'Latitude_35.504161_Longitude_-80.843123',
    'Connor': 'Latitude_35.504209_Longitude_-80.843807',
    'Chinsey (Gym Entrance)': 'Latitude_35.503719_Longitude_-80.844395',
    'F (Top Trashcan)': 'Latitude_35.501841_Longitude_-80.840482',
    'F (Main Courtyard)': 'Latitude_35.501684_Longitude_-80.84025',
    'F Basketball Court': 'Latitude_35.501389_Longitude_-80.839829',
    'Cross Country Trail Head': 'Latitude_35.500853_Longitude_-80.83997',
    'VAC': 'Latitude_35.501567_Longitude_-80.847637',
    'CInn': 'Latitude_35.5018034_Longitude_-80.8474006',
    'T&I': 'Latitude_35.5020398_Longitude_-80.8471642',
    'Depot': 'Latitude_35.5022762_Longitude_-80.8469278',
    'CollegeStore': 'Latitude_35.500053_Longitude_-80.848224',
    'DCPC': 'Latitude_35.5002894_Longitude_-80.8479876',
    'Watson': 'Latitude_35.499635_Longitude_-80.846634',
    'WatsonSloanInt': 'Latitude_35.499412_Longitude_-80.846327',
    'Dana': 'Latitude_35.499412_Longitude_-80.846762',
    'Sloan': 'Latitude_35.499221_Longitude_-80.845745',
    'SloanChambersInt': 'Latitude_35.499546_Longitude_-80.845624',
    'ChambersS': 'Latitude_35.499496_Longitude_-80.845377',
    'LillyGallery': 'Latitude_35.499905_Longitude_-80.844652',
    'Chambers': 'Latitude_35.500549_Longitude_-80.845041',
    'ChambersW': 'Latitude_35.500062_Longitude_-80.845476',
    'ChambersLawnInt': 'Latitude_35.5002984_Longitude_-80.8452396',
    'ChambersLawnIntB': 'Latitude_35.5005348_Longitude_-80.8450032',
    'PhilanthropicHall': 'Latitude_35.50039_Longitude_-80.847107',
    'EumeneanHall': 'Latitude_35.500463_Longitude_-80.847436',
    'ElmRow': 'Latitude_35.5006994_Longitude_-80.8471996',
    'OakRow': 'Latitude_35.5009358_Longitude_-80.8469632',
    'Cunningham': 'Latitude_35.501448_Longitude_-80.84626',
    'CarnegieGH (changed to Carnegie House Entrance Facing Academic buildings)': 'Latitude_35.5016844_Longitude_-80.8460236',
    'Little (changed to Little Main Entrance)': 'Latitude_35.501283_Longitude_-80.845687',
    'Watts (changed to Watts Main entrance)': 'Latitude_35.501163_Longitude_-80.845359',
    'ChambersInt6': 'Latitude_35.5013994_Longitude_-80.8451226',
    'FlagPole': 'Latitude_35.500655_Longitude_-80.844745',
    'SittingSculpture': 'Latitude_35.500665_Longitude_-80.844742',
    'Sentelle (changed to Sentelle Main Entrance)': 'Latitude_35.500786_Longitude_-80.844195',
    'FlagPoleR (Changed to Semicircle intersection by Belk, Watts and Cannon)': 'Latitude_35.5010224_Longitude_-80.8439586',
    'Cannon (changed to cannon front entrance)': 'Latitude_35.500914_Longitude_-80.844576',
    'South Side Chinsey Path Intersection': 'Latitude_35.503213_Longitude_-80.844643',
    'Spencer Wienstien/Chinsey': 'Latitude_35.503166_Longitude_-80.844524',
    'Triangle Between Tommy/SW': 'Latitude_35.503083_Longitude_-80.844589',
    'South Side Back Chinsey Lot': 'Latitude_35.503275_Longitude_-80.844826',
    'South Side Back Chinsey Dumpster': 'Latitude_35.503359_Longitude_-80.845002',
    'Campo Office': 'Latitude_35.503103_Longitude_-80.844911',
    'Tommy North Side': 'Latitude_35.503028_Longitude_-80.844754',
    'Spencer Wienstien Entrance': 'Latitude_35.503104_Longitude_-80.844395',
    'Spencer Wienstien North': 'Latitude_35.502963_Longitude_-80.844405',
    'Spencer Wienstien Commons Intersection': 'Latitude_35.502903_Longitude_-80.844174',
    'Commons Lower': 'Latitude_35.50262_Longitude_-80.844348',
    'Commons Brick Replacement': 'Latitude_35.502594_Longitude_-80.844308',
    'North Side Rich Near Tree': 'Latitude_35.502679_Longitude_-80.844454',
    'Big Tree Near Rich Intersection': 'Latitude_35.502584_Longitude_-80.844498',
    'Rich Entrance North': 'Latitude_35.502679_Longitude_-80.844651',
    'Tommy Rich Intersection': 'Latitude_35.502764_Longitude_-80.844853',
    'South East Tommy ': 'Latitude_35.502941_Longitude_-80.845101',
    'South Side Tommy Entrance': 'Latitude_35.502991_Longitude_-80.845185',
    'East Side, Rich lot Ciccle': 'Latitude_35.5026_Longitude_-80.84496',
    'West Rich Entrance': 'Latitude_35.502569_Longitude_-80.844848',
    'South Side Rich': 'Latitude_35.502275_Longitude_-80.844983',
    'South East Rich Intersection': 'Latitude_35.502276_Longitude_-80.844777',
    'East Most Rich Parkinglot Entrance': 'Latitude_35.502214_Longitude_-80.844894',
    'Commons South West Entrance': 'Latitude_35.502496_Longitude_-80.844078',
    'Commons West Triangle North': 'Latitude_35.502447_Longitude_-80.844229',
    'Commons West Triangle South': 'Latitude_35.502353_Longitude_-80.84436',
    'Commons West Triangle East': 'Latitude_35.50233_Longitude_-80.844219',
    'Commons Triangles Intersection': 'Latitude_35.502289_Longitude_-80.84419',
    'Commons East Triangle West': 'Latitude_35.50228_Longitude_-80.844159',
    'Commons East Triangle North': 'Latitude_35.502262_Longitude_-80.844039',
    'Commons South Entrance Lower': 'Latitude_35.502301_Longitude_-80.84394',
    'Commons South Entrance Upper': 'Latitude_35.502406_Longitude_-80.843936',
    'Commons Lower West': 'Latitude_35.502449_Longitude_-80.843559',
    'Commons East Triangle South': 'Latitude_35.50214_Longitude_-80.84412',
    'RLO': 'Latitude_35.501901_Longitude_-80.844159',
    'Old Laundry Room': 'Latitude_35.502001_Longitude_-80.844332',
    'RLO/Belk Intersection': 'Latitude_35.501724_Longitude_-80.844238',
    'Belk Base North Entrance': 'Latitude_35.501766_Longitude_-80.844343',
    'Belk North East': 'Latitude_35.501774_Longitude_-80.84443',
    'Belk North Entrence East': 'Latitude_35.501801_Longitude_-80.844567',
    'Belk North Entrance': 'Latitude_35.501811_Longitude_-80.844679',
    'Belk Tree Commons Path': 'Latitude_35.501901_Longitude_-80.844673',
    'Belk Tree Rich': 'Latitude_35.501921_Longitude_-80.844773',
    'Belk North Entrance West': 'Latitude_35.501848_Longitude_-80.844769',
    'Belk West Entrance Immediate': 'Latitude_35.501901_Longitude_-80.845024',
    'Tommy/Rich lot to Health Center': 'Latitude_35.502982_Longitude_-80.845573',
    'Health Center': 'Latitude_35.503301_Longitude_-80.846226',
    'Back of Belk corner by Parking lot': 'Latitude_35.501931_Longitude_-80.845072',
    'Belk Basement Entrance (Parking Lot)': 'Latitude_35.5017638827311_Longitude_-80.8450488497717',
    'Watts back entrance': 'Latitude_35.501512982309_Longitude_-80.8451788179285',
    'Belk Entrance, Left Wing': 'Latitude_35.5015928405306_Longitude_-80.8450111950389',
    'Main Belk Entrance': 'Latitude_35.5017143691533_Longitude_-80.8447008782386',
    'Center of Belk intersection in front of Main Belk Entrance': 'Latitude_35.5014739881424_Longitude_-80.8447683824299',
    'Belk Entrance, Right Wing': 'Latitude_35.5014935827135_Longitude_-80.8444989099654',
    'Semicircle intersection by Belk, Watts and Cannon': 'Latitude_35.5010702556087_Longitude_-80.8450333698556',
    'Watts (Right intersection)': 'Latitude_35.5011392667552_Longitude_-80.8452664612514',
    'Watts Front Entrance': 'Latitude_35.5011690708316_Longitude_-80.8453510020593',
    'Watts (Left Intersection)': 'Latitude_35.5012204103878_Longitude_-80.8454307421338',
    'Watts (Back by Outside Area)': 'Latitude_35.5014250238495_Longitude_-80.8453284897762',
    'Little Back Entrance': 'Latitude_35.501611318423_Longitude_-80.8455880668513',
    'Little (Parking Lot Path)': 'Latitude_35.5016721403483_Longitude_-80.8457035021755',
    'Carnegie House (Entrance by Presidents House)': 'Latitude_35.5017105317832_Longitude_-80.8461674097896',
    'Parking Lot By Presidents House': 'Latitude_35.5017702990221_Longitude_-80.8468883689228',
    'Carnegie House Main Entrance': 'Latitude_35.5016369481836_Longitude_-80.8463962665247',
    'Carnegie House Entrance Facing Academic buildings': 'Latitude_35.5014675895523_Longitude_-80.84627402744',
    'Little Main Entrance': 'Latitude_35.5016379318983_Longitude_-80.8455785851306',
    'Base Belk Entrance': 'Latitude_35.5015535184974_Longitude_-80.8443216311787',
    'LuluBells Bottom of Stairs': 'Latitude_35.5013584412258_Longitude_-80.8440702948185',
    'LuluBells Top of Stairs': 'Latitude_35.5013180112868_Longitude_-80.8440968349279',
    'Watts Back Entrance': 'Latitude_35.5012735932768_Longitude_-80.844399977843',
    'Cannon/ Sentelle (Back center intersection)': 'Latitude_35.5012109010957_Longitude_-80.8442013733491',
    'Sentelle Back Entrance': 'Latitude_35.501131033632_Longitude_-80.8439801585978',
    'Duke Left Wing Entrance': 'Latitude_35.5008985206657_Longitude_-80.8436917880076',
    'Sentelle Main Entrance': 'Latitude_35.500792_Longitude_-80.844187',
    'Semicircle between Sentelle/Watts': 'Latitude_35.5008588872868_Longitude_-80.8443726555953',
    'Cannon/Sentelle (Front Center Intersection)': 'Latitude_35.500846_Longitude_-80.844372',
    'Cannon Front Entrance': 'Latitude_35.500926_Longitude_-80.844574',
    'Wildcat': 'Latitude_35.499503_Longitude_-80.841678',
    'Baker Entrance': 'Latitude_35.499421_Longitude_-80.841216',
    'Tennis Courts': 'Latitude_35.499567_Longitude_-80.839904',
    'Track Corner': 'Latitude_35.499160195585_Longitude_-80.8439761722143',
    'Bottom Labryinth': 'Latitude_35.499396595585_Longitude_-80.8437397722143',
    'Top Labryinth': 'Latitude_35.499632995585_Longitude_-80.8435033722143',
    'Hobart Park below Labryinth': 'Latitude_35.4984386947706_Longitude_-80.8428940098045',
    'White House': 'Latitude_35.4986750947706_Longitude_-80.8426576098045',
    'HR': 'Latitude_35.4983589550816_Longitude_-80.8440281046666',
    'Jackson Court': 'Latitude_35.498356_Longitude_-80.843892',
    'School Side Jackson Court Entrance': 'Latitude_35.498622_Longitude_-80.844032',
    'Faculty Drive Right Corner': 'Latitude_35.4987782617766_Longitude_-80.8422000527822',
    'Faculty Drive Wall Corner': 'Latitude_35.4983822819078_Longitude_-80.8447196063772',
    'Right Side Wall Entrance': 'Latitude_35.4989454777518_Longitude_-80.8447199463865',
    'Back of Wall Entrance': 'Latitude_35.4988945083712_Longitude_-80.8449965044319',
    'Back Left Corner Wall': 'Latitude_35.4986518105894_Longitude_-80.8453709224566',
    'Left Side Wall Entrance': 'Latitude_35.4990964473536_Longitude_-80.8452108757483',
    'Bottom Right Chambers 4-way': 'Latitude_35.4994509331274_Longitude_-80.8451062864',
    'Top BR Chambers Wedge': 'Latitude_35.499749229493_Longitude_-80.844706686447',
    'Sculpture Garden': 'Latitude_35.499847_Longitude_-80.84448',
    'Right Side Chambers': 'Latitude_35.5000834_Longitude_-80.8442436',
    'Right BR Chambers Wedge': 'Latitude_35.5004452028574_Longitude_-80.8445196865667',
    'Wall': 'Latitude_35.4993950905301_Longitude_-80.8448323133271',
    'Wall Entrance': 'Latitude_35.4991542838842_Longitude_-80.8448804641088',
    'Top TR Wall Wedge': 'Latitude_35.4994790497382_Longitude_-80.8443832529783',
    'Left TR Wall Wedge': 'Latitude_35.499390165773_Longitude_-80.8446437278768',
    'Right TR Wall Wedge': 'Latitude_35.4992606994298_Longitude_-80.8444342431618',
    'Front Libs': 'Latitude_35.4998080386957_Longitude_-80.8442533021607',
    'Left TL Library Wedge': 'Latitude_35.5000300276589_Longitude_-80.8444518125181',
    'Right TL Library Wedge': 'Latitude_35.4998898139428_Longitude_-80.8442311483914',
    'Top TL Library Wedge': 'Latitude_35.5002105547133_Longitude_-80.8441398271134',
    'Top Libs 4-Way': 'Latitude_35.5003523450288_Longitude_-80.8440849151703',
    'Upper Left Duke Intersection': 'Latitude_35.5006825999997_Longitude_-80.8439085197175',
    'Front libs Chute': 'Latitude_35.5009189999997_Longitude_-80.8436721197175',
    'Back Libs Chute': 'Latitude_35.5011553999997_Longitude_-80.8434357197175',
    'New Gym Entrance': 'Latitude_35.500075_Longitude_-80.843163',
    'Track/Libs/Duke Intersection': 'Latitude_35.50037_Longitude_-80.843618',
    'Track': 'Latitude_35.500195989652_Longitude_-80.8429902936644',
    'Upper Union 4-way': 'Latitude_35.5004656740428_Longitude_-80.8432544937272',
    'Upper Right Side Duke': 'Latitude_35.5006199538085_Longitude_-80.8432917021685',
    'Lower Right Side Duke': 'Latitude_35.5008022160794_Longitude_-80.843055862134',
    'Lower Right Side Duke Entrance': 'Latitude_35.5008263848254_Longitude_-80.8431846500149',
    'Lower Union 4-Way': 'Latitude_35.5008893789005_Longitude_-80.8430484442081',
    'Duke Back Union Corner': 'Latitude_35.5008131481879_Longitude_-80.8431835430344',
    'Front Duke': 'Latitude_35.5010002220482_Longitude_-80.843340398713',
    'Front Duke Entrance': 'Latitude_35.5008203476045_Longitude_-80.8434504867965',
    'Back Duke': 'Latitude_35.5006332179451_Longitude_-80.8435451897586',
    'Left Side Duke': 'Latitude_35.5008723310648_Longitude_-80.8436850163635',
    'Lower Left Duke Intersection': 'Latitude_35.5010368189904_Longitude_-80.8436636336523',
    'Baker Loopy': 'Latitude_35.5011099624508_Longitude_-80.8430067554902',
    'C Union': 'Latitude_35.5006970478438_Longitude_-80.8427872788604',
    'A Union': 'Latitude_35.5003656526435_Longitude_-80.842302669073',
    'Qdoba': 'Latitude_35.500872_Longitude_-80.842008',
    'Stowe Intersection': 'Latitude_35.4987678557101_Longitude_-80.8421869094852',
    'Qdoba Intersection': 'Latitude_35.5009072200279_Longitude_-80.8420226354845',
    'Side Baker': 'Latitude_35.5011436200279_Longitude_-80.8417862354845',
    'Union Qdoba side': 'Latitude_35.500781_Longitude_-80.842591',
    'Back Door Libs': 'Latitude_35.499423_Longitude_-80.843775',
    'Telephone': 'Latitude_35.4989333093325_Longitude_-80.8439067756065',
    'BL Track Intersection ': 'Latitude_35.4991947842129_Longitude_-80.8438465135897',
    'Olas/Pasas': 'Latitude_35.501975_Longitude_-80.843152',
    'Commons Outdoor Seating': 'Latitude_35.502636_Longitude_-80.843816',

}

def get_coordinates(location_name):
    # Check if the location name exists in the dictionary
    if location_name in location_to_coordinates:
        return location_to_coordinates[location_name]
    else:
        return "Coordinates not found for the given location."


# Function to get the index from a human-readable name
def get_index_from_name(name, reverse_mapping):
    if name in reverse_mapping:
        return get_index_from_code(reverse_mapping[name])
    else:
        raise ValueError(f"Name '{name}' not found in name mapping.")

def get_index_from_code(code):
    if len(code) == 1:
        return ord(code) - 65
    elif len(code) == 2:
        return (ord(code[0]) - 65) * 26 + (ord(code[1]) - 65) + 26
    return None


# Updated index mapping for two-letter codes
def get_index_from_code(code):
    if len(code) == 1:
        return ord(code) - 65
    elif len(code) == 2:
        return (ord(code[0]) - 65) * 26 + (ord(code[1]) - 65) + 26
    return None

def dijkstra(matrix, start_idx, end_idx, speed):
    num_nodes = len(matrix)
    visited = [False] * num_nodes
    distance = [float('inf')] * num_nodes
    distance[start_idx] = 0
    previous = [None] * num_nodes

    for _ in range(num_nodes):
        min_dist = float('inf')
        current_node = None
        for node in range(num_nodes):
            if not visited[node] and distance[node] < min_dist:
                min_dist = distance[node]
                current_node = node
        if current_node is None:
            break
        visited[current_node] = True
        for neighbor in range(num_nodes):
            if matrix[current_node][neighbor] != float('inf') and not visited[neighbor]:
                new_distance = distance[current_node] + matrix[current_node][neighbor]
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    previous[neighbor] = current_node
    
    path = []
    step = end_idx
    while step is not None:
        path.insert(0, step)
        step = previous[step]

    return distance[end_idx]*speed, path

def find_path_with_names_and_coordinates(matrix, start_name, end_name, name_mapping, speed):
    reverse_mapping = {v: k for k, v in name_mapping.items()}
    start_idx = get_index_from_name(start_name, reverse_mapping)
    end_idx = get_index_from_name(end_name, reverse_mapping)
    distance, path_indices = dijkstra(matrix, start_idx, end_idx, speed)

    # Convert path indices back to names and get coordinates
    path_details = []
    for idx in path_indices:
        name = name_mapping.get(chr(65 + idx % 26), f"Unknown-{idx}")
        coordinates = get_coordinates(name)
        path_details.append((name, coordinates))

    return distance, path_details

def find_path_with_multiple_destinations(matrix, start_name, destination_names, name_mapping, speed):
    if not destination_names:
        return [], []

    reverse_mapping = {v: k for k, v in name_mapping.items()}
    current_name = start_name
    total_distance = 0
    complete_path_details = []

    while destination_names:
        current_idx = get_index_from_name(current_name, reverse_mapping)
        next_name = destination_names.pop(0)  # Get the next destination
        next_idx = get_index_from_name(next_name, reverse_mapping)
        
        distance, path_indices = dijkstra(matrix, current_idx, next_idx, speed)
        total_distance += distance
        
        # Convert path indices back to names and get coordinates
        path_details = []
        for idx in path_indices:
            name = name_mapping.get(chr(65 + idx % 26), f"Unknown-{idx}")
            coordinates = get_coordinates(name)
            path_details.append((name, coordinates))
        
        complete_path_details.append(path_details)
        current_name = next_name  # Move to the next start position

    return total_distance, complete_path_details

@app.route('/api/find-path', methods=['POST'])
def get_data():
    data = request.get_json()  # Retrieve JSON data sent from the client
    
    if data.get('mid_point'):
        start = data.get('start')
        mid_point = data.get('mid_point')
        end = data.get('end')
        arr = [mid_point, end]
        distance, j_details = find_path_with_multiple_destinations(matrix, start, arr, name_mapping, 1)
    else:
        start = data.get('start')  # Extract the 'start' value from JSON data
        end = data.get('end')
        distance, j_details = find_path_with_names_and_coordinates(matrix, start, end, name_mapping, 1)
    
    result = {'distance': distance,'journey_details': j_details}
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

# Example usage
start = 1  # Jamie to Nummit 
destinations = [28] 
total_distance, journey_details = find_optimal_path(matrix, start, destinations, name_mapping, speed_factor=1)

print(f"Total Adjusted Time: {total_distance}")
print("Optimal Journey Order:")
for leg in journey_details:
    print(f"From {leg['start']} to {leg['end']}: Distance = {leg['distance']}, Path = {' -> '.join(leg['path'])}")
print("")

start = 1  # Jamie to Nummit/Chinsey Gym
destinations = [28,42] 
total_distance, journey_details = find_optimal_path(matrix, start, destinations, name_mapping, speed_factor=1)

print(f"Total Adjusted Time: {total_distance}")
print("Optimal Journey Order:")
for leg in journey_details:
    print(f"From {leg['start']} to {leg['end']}: Distance = {leg['distance']}, Path = {' -> '.join(leg['path'])}")
print("")

start = 1  # Jamie to Nummit/Chinsey Gym/Ksig
destinations = [28, 42, 26] 
total_distance, journey_details = find_optimal_path(matrix, start, destinations, name_mapping, speed_factor=1)

print(f"Total Adjusted Time: {total_distance}")
print("Optimal Journey Order:")
for leg in journey_details:
    print(f"From {leg['start']} to {leg['end']}: Distance = {leg['distance']}, Path = {' -> '.join(leg['path'])}")
print("")