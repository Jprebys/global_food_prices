def fao_global_averages(data, food):
    '''
    take the FAO food prices table and a specific food
    return a Series representing the average global price per year
    '''
    prices = data[data.Item == food]
    return prices.groupby('Year').Value.mean()    