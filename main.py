from pipeline import paginate, normalized_data, key_info, nan_report, clean_data
import pipeline.storage as ps

def main(debug: bool = True):
    """Run whole process. If debug=True, prints out info
    about DataFrames before and after cleaning.
    
    Parameters
    ----------
    debug : bool
        print DataFrame info, head, NaN and
        nunique statistics
    """
    try:
#list of dicts with scraped pages data,metadata and links
        print("Fetching pages...")
        pages = paginate()

#dict with data split into categories and DFs as values
        print("Normalizing data...")
        data_categories = normalized_data(pages)
    
#data cleaning
        print("Cleaning data...")

#print df.info(), df.nunique() and df.head(2)
#for all dfs before cleaning
        if debug == True:
            print()
            print("Info summary about DataFrames before cleaning:")
            key_info(data_categories)
#clean DataFrames    
        clean_data(data_categories)
#print report about NaN values in DataFrames columns    
        if debug == True:
            print()
            print('NaN Report:\n')
            nan_report(data_categories)
        
#print df.info(), nunique() and head(2) for all dfs
#after cleaning
            print()
            print("Info summary about DataFrames after cleaning:")
            key_info(data_categories)
            
#save data to files
        print("Saving files...")
        ps.save_csv(data_categories)
        
        print('Pipeline finished successfully!')
        
    except Exception as e:
        print("Pipeline failed:", e)

    
if __name__ == '__main__':
    main(debug=False)
    
    