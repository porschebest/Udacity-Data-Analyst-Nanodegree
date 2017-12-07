def check_duplicate(search_list):
    check_list = []
    count = 0
    for item in search_list:
        if item in check_list:
            count += 1
        else:
            check_list.append(item)
    return count

def continue_crawl(search_history,target_url):
    while len(search_history) < 25 :
        #   most recent article in the search_history is the target article -> False
        if(target_url in search_history):
            print('reach Philosophy')
            return False
        #   list is more than 25 urls -> False
        elif len(search_history) > 25:
            print('long route error')
            return False
        #   has a cycle in it -> False
        elif check_duplicate(search_history) != 0:
            print('loop detected')
            return False
        #   Else -> Continue
        else:
            print('continue')
            return True
continue_crawl(['https://en.wikipedia.org/wiki/Philosophy','https://en.wikipedia.org/wiki/Floating_point'],
                       'https://en.wikipedia.org/wiki/Philosophy')
