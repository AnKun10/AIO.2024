def sales_convert(x, avg):
    if x > avg:
        return 'Good'
    elif x < avg:
        return 'Bad'
    else:
        return 'Average'
