def fao_global_averages(data, food):
    '''
    take the FAO food prices table and a specific food
    return a Series representing the average global price per year
    '''
    prices = data[data.Item == food]
    return prices.groupby('Year').Value.mean()    

def fao_pivot(data, food):
    '''
    take the FAO data and the name of a food
    return the pivot table where the rows are the countries,
    the columns are the years, and the values are the values
    '''
    foods = data[data.Item == food]
    return foods.pivot(index='Area', columns='Year', values='Value')