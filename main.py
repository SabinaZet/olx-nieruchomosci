if __name__ == '__main__':
    import pipeline.request as pr
    import pipeline.transform as pt
    
#list of dicts with scraped pages data,metadata and links
    pages = pr.paginate()
#list with only data values from all pages
    data = pt.cumulate_data(pages)
    
#dict with data split into categories(data_location,
#data_offer,data_photos itp) by FIELD_MAP
    separate_data = pt.data_separate(data)
    
#dict with categories as keys and flattened DataFrames as values
    separate_dfs = pt.normalize_data(separate_data)
    pt.key_info(separate_dfs)
    
#delete NaN columns from all dfs
    dfs_no_nan = pt.clean_nan(separate_dfs)
    pt.key_info(dfs_no_nan)
    
#print df name and each column with the number of unique values
    pt.check_data(dfs_no_nan)
    