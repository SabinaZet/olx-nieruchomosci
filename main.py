if __name__ == '__main__':
    import pipeline.request as pr
    import pipeline.transform as pt
    
    pages = pr.paginate()
    
    data = pt.cumulate_data(pages)
         
    separate_data = pt.data_separate(data)
    
    separate_dfs = pt.normalize_data(separate_data)
    pt.key_info(separate_dfs)
        
    dfs_no_nan = pt.clean_nan(separate_dfs)
    pt.key_info(dfs_no_nan)
    
    pt.check_data(dfs_no_nan)
    