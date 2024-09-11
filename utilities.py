def tr_to_eng(df, column):

    tr_eng = {'İ': 'I', 'Ü': 'U', 'Ö': 'O', 'Ğ': 'G', 'Ş': 'S', 'Ç': 'C',
                'ü': 'u', 'ö': 'o', 'ğ': 'g', 'ş': 's', 'ç': 's'}
    
    for tr_char, en_char in tr_eng.items():
        df[column] = df[column].apply(lambda x: str(x).replace(tr_char, en_char))
