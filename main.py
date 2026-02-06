if __name__ == '__main__':
    import pipeline.request as pr
    import pipeline.transform as pt
    import pipeline.clean as pc
    
#list of dicts with scraped pages data,metadata and links
    pages = pr.paginate()

#dict with data split into categories and DFs as values
    data_categories = pt.normalized_data(pages)
    
#data cleaning
    
#print df.info() for all dfs
    pc.key_info(data_categories)
    
#delete NaN columns from all dfs
    dfs_no_nan = pc.clean_nan(data_categories)
    pc.key_info(dfs_no_nan)
    
#print df name and each column with the number of unique values
    pc.check_data(dfs_no_nan)
    