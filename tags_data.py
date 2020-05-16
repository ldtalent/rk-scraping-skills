from stackapi import StackAPI

def get_tags(parameter_list,count,sitename,maxpage=1,pagesize=50,page_no=1):
    try:
        SITE = StackAPI(sitename)
        SITE.max_pages = maxpage
        SITE.page_size = pagesize
        return SITE.fetch('tags',page=page_no )
    except:
        try:
            SITE = StackAPI(parameter_list[count])
            SITE.max_pages = maxpage
            SITE.page_size = pagesize
            return SITE.fetch('tags',page=page_no )
        except stackapi.StackAPIError as e:
            print(" Error URL: {}".format(e.url))
            print(" Error Code: {}".format(e.code))
            print(" Error Error: {}".format(e.error))
            print(" Error Message: {}".format(e.message))

            return 0



