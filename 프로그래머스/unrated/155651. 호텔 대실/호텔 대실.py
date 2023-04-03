def solution(book_time):
    book_time.sort()
    endtime=[book_time[0][1]]
    
    for i in range(1,len(book_time)):
        endtime.sort()
        h,m = map(int,endtime[0].split(':'))
        if 50<=m<=59:   
            h += 1
            m -= 50
        else:
            m += 10
        bh,bm = map(int,book_time[i][0].split(':'))
        if (bh==h and bm>=m) or bh>h:
            endtime[0] = book_time[i][1]
        else:
            endtime.append(book_time[i][1])

    answer = len(endtime)
    return answer