if __name__ == '__main__':
    from pipeline import paginate, normalized_data
    import pipeline.clean as pc
    
#list of dicts with scraped pages data,metadata and links
    pages = paginate()

#dict with data split into categories and DFs as values
    data_categories = normalized_data(pages)
    
#data cleaning
    
#print df.info(), df.nunique() and df.head(2)
#for all dfs before cleaning
    print()
    print("Info summary about DataFrames before cleaning:")
    pc.key_info(data_categories)
#clean DataFrames    
    pc.clean_data(data_categories)
#print report about NaN values in DataFrames columns    
    print()
    print('NaN Report:\n')
    pc.nan_report(data_categories)
    
#print df.info(), nunique() and head(2) for all dfs
#after cleaning
    print()
    print("Info summary about DataFrames after cleaning:")
    pc.key_info(data_categories)
    
    