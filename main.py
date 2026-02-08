if __name__ == '__main__':
    from pipeline import paginate, normalized_data, key_info, nan_report, clean_data
    
#list of dicts with scraped pages data,metadata and links
    pages = paginate()

#dict with data split into categories and DFs as values
    data_categories = normalized_data(pages)
    
#data cleaning
    
#print df.info(), df.nunique() and df.head(2)
#for all dfs before cleaning
    print()
    print("Info summary about DataFrames before cleaning:")
    key_info(data_categories)
#clean DataFrames    
    clean_data(data_categories)
#print report about NaN values in DataFrames columns    
    print()
    print('NaN Report:\n')
    nan_report(data_categories)
    
#print df.info(), nunique() and head(2) for all dfs
#after cleaning
    print()
    print("Info summary about DataFrames after cleaning:")
    key_info(data_categories)
    
    