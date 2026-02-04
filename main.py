if __name__ == '__main__':
    import pipeline.request as pr
    import pipeline.transform as pt
    
    page1 = pt.split_response(pr.request())
    total = int(page1.get('metadata').get('total_elements'))
    
    pages = pr.pagination(total)