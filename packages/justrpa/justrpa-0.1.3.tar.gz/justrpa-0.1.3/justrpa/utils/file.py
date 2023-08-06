import os
import json
import pandas as pd
import xlsxwriter

def check_file_exists(target_filename:str, ignore_ext:bool=False)->bool:
    target_filename = os.path.abspath(target_filename)
    if ignore_ext==True:
        dir_name = os.path.dirname(target_filename)
        filename = os.path.splitext(target_filename)[0]
        for file in os.listdir(dir_name):
            current_filename = os.path.splitext(file)[0]
            if current_filename == filename:
                return True
        return False
    else:
        return os.path.isfile(target_filename)

def create_dir_for_file(filename):
    dir = os.path.dirname(filename)
    if os.path.isdir(dir)==False:
        os.makedirs(dir, exist_ok=True)

def detect_encoding(file_name:str)->str:
    with open(file_name, 'rb') as f:
        rawdata = f.read()
    encodings = ['utf-8','CP932', 'shift-jis', 'euc-jp', 'iso-2022-jp', 'iso-8859-1']
    for encoding in encodings:
        try:
            rawdata.decode(encoding)
            return encoding
        except:
            pass
    return 'utf-8'

def merge_csv_files(files:list, output_file:str, header_row=1, delete=True):
    print(f"Merging {len(files)} files to {output_file}")
    encoding = detect_encoding(files[0])
    with open(output_file, 'w', encoding=encoding) as outfile:
        for idx, fname in enumerate(files):
            with open(fname, 'r', encoding=encoding) as infile:
                for idy, line in enumerate(infile):
                    if idx<1 or idy >=header_row:
                        outfile.write(line)
    print(f"Merged {len(files)} files to {output_file}")
    if delete:
        for fname in files:
            os.remove(fname)
    return output_file

def load_json_file(file_dir:str, filename:str)->dict:
    dir_path = dir_path = os.getcwd()
    dir_path = os.path.join(dir_path, file_dir)
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r') as infile:
        return json.load(infile)

def save_json_file(result:dict, output_dir, filename:str):
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.getcwd()
    dir_path = os.path.join(dir_path, output_dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'w') as outfile:
        json.dump(result, outfile, indent=4)

def load_csv(file_name:str)->pd.DataFrame:
    encoding = detect_encoding(file_name)
    try:
        df = pd.read_csv(file_name, encoding=encoding)
    except pd.errors.EmptyDataError:
        print(f"{file_name} is empty csv.")
        df = pd.DataFrame()
    return df

def save_dfs_tabs(df_list, sheet_list, file_name):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')   
    for dataframe, sheet in zip(df_list, sheet_list):
        dataframe.to_excel(writer, sheet_name=sheet, startrow=0 , startcol=0, index=False)   
    writer.save()

def merge_csv_to_excel(csv_files, output_file, sheet_names=[]):
    dfs = [ load_csv(f) for f in csv_files if f != None]
    if len(sheet_names) == 0:
        sheet_names = [f"sheet{i}" for i in range(len(dfs))]
    save_dfs_tabs(dfs,sheet_names, output_file)
    return output_file