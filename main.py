if __name__ == '__main__':
    from pipeline import paginate, normalized_data
    import pipeline.clean as pc
    
#list of dicts with scraped pages data,metadata and links
    pages = paginate()

#dict with data split into categories and DFs as values
    data_categories = normalized_data(pages)
    
#data cleaning
    
#print df.info() and df.head(2) for all dfs
    pc.key_info(data_categories)
    
#delete NaN columns and duplicate id from all dfs and check
    dfs_cl = pc.clean_nan_df(data_categories)
    dfs_cl = pc.deduplicate(dfs_cl)
    pc.key_info(dfs_cl)
    
#print df name and each column with the number of unique values
    pc.check_data(dfs_cl)
    