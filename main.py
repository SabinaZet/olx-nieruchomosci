if __name__ == '__main__':
    import pipeline.request as pr
    import pipeline.transform as pt
    
    page1 = pt.split_response(pr.request())
    total = int(page1.get('metadata').get('total_elements'))
    
    pages_l = pr.pagination(total)
    pages = [pt.split_response(page) for page in pages_l]
    pages.insert(0, page1)
    
    data = pt.cumulate_data(pages)