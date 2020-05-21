from stackapi import StackAPI
import stackapi


# function to extract skills from API

def get_tags(parameter_list,count,sitename,maxpage,pagesize,page_no):
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



