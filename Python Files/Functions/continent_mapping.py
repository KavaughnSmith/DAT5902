def continent_mapping(x, df_column):
    continent_map = {
        'Afghanistan': 'Asia', 'Africa (UN)': 'Africa', 'Albania': 'Europe', 'Algeria': 'Africa', 'Angola': 'Africa', 'Antigua and Barbuda': 'North America',
        'Argentina': 'South America', 'Armenia': 'Asia', 'Aruba': 'North America', 'Australia': 'Oceania', 'Austria': 'Europe', 'Azerbaijan': 'Asia',
        'Bahamas': 'North America', 'Bahrain': 'Asia', 'Bangladesh': 'Asia', 'Barbados': 'North America', 'Belarus': 'Europe', 'Belgium': 'Europe',
        'Belize': 'North America', 'Benin': 'Africa', 'Bermuda': 'North America', 'Bhutan': 'Asia', 'Bolivia': 'South America', 'Bosnia and Herzegovina': 'Europe',
        'Botswana': 'Africa', 'Brazil': 'South America', 'Brunei': 'Asia', 'Bulgaria': 'Europe', 'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cambodia': 'Asia',
        'Cameroon': 'Africa', 'Canada': 'North America', 'Cape Verde': 'Africa', 'Cayman Islands': 'North America', 'Central African Republic': 'Africa',
        'Chad': 'Africa', 'Chile': 'South America', 'China': 'Asia', 'Colombia': 'South America', 'Comoros': 'Africa', 'Congo': 'Africa', 'Costa Rica': 'North America',
        "Cote d'Ivoire": 'Africa', 'Croatia': 'Europe', 'Curacao': 'North America', 'Cyprus': 'Asia', 'Czechia': 'Europe', 'Democratic Republic of Congo': 'Africa',
        'Denmark': 'Europe', 'Djibouti': 'Africa', 'Dominica': 'North America', 'Dominican Republic': 'North America', 'East Timor': 'Asia', 'Ecuador': 'South America',
        'Egypt': 'Africa', 'El Salvador': 'North America', 'Equatorial Guinea': 'Africa', 'Estonia': 'Europe', 'Eswatini': 'Africa', 'Ethiopia': 'Africa', 'Fiji': 'Oceania',
        'Finland': 'Europe', 'France': 'Europe', 'Gabon': 'Africa', 'Gambia': 'Africa', 'Georgia': 'Asia', 'Germany': 'Europe', 'Ghana': 'Africa', 'Greece': 'Europe',
        'Grenada': 'North America', 'Guatemala': 'North America', 'Guinea': 'Africa', 'Guinea-Bissau': 'Africa', 'Guyana': 'South America', 'Haiti': 'North America',
        'Honduras': 'North America', 'Hong Kong': 'Asia', 'Hungary': 'Europe', 'Iceland': 'Europe', 'India': 'Asia', 'Indonesia': 'Asia', 'Iran': 'Asia', 'Iraq': 'Asia',
        'Ireland': 'Europe', 'Israel': 'Asia', 'Italy': 'Europe', 'Jamaica': 'North America', 'Japan': 'Asia', 'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kenya': 'Africa',
        'Kiribati': 'Oceania', 'Kosovo': 'Europe', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 'Laos': 'Asia', 'Latvia': 'Europe', 'Lebanon': 'Asia', 'Lesotho': 'Africa',
        'Liberia': 'Africa', 'Libya': 'Africa', 'Lithuania': 'Europe', 'Luxembourg': 'Europe', 'Macao': 'Asia', 'Madagascar': 'Africa', 'Malawi': 'Africa', 'Malaysia': 'Asia',
        'Maldives': 'Asia', 'Mali': 'Africa', 'Malta': 'Europe', 'Marshall Islands': 'Oceania', 'Mauritania': 'Africa', 'Mauritius': 'Africa', 'Mexico': 'North America',
        'Micronesia (country)': 'Oceania', 'Moldova': 'Europe', 'Mongolia': 'Asia', 'Montenegro': 'Europe', 'Morocco': 'Africa', 'Mozambique': 'Africa', 'Myanmar': 'Asia',
        'Namibia': 'Africa', 'Nauru': 'Oceania', 'Nepal': 'Asia', 'Netherlands': 'Europe', 'New Zealand': 'Oceania', 'Nicaragua': 'North America', 'Niger': 'Africa',
        'Nigeria': 'Africa', 'North Macedonia': 'Europe', 'Norway': 'Europe', 'Oman': 'Asia', 'Pakistan': 'Asia', 'Palau': 'Oceania', 'Palestine': 'Asia',
        'Panama': 'North America', 'Papua New Guinea': 'Oceania', 'Paraguay': 'South America', 'Peru': 'South America', 'Philippines': 'Asia', 'Poland': 'Europe',
        'Portugal': 'Europe', 'Puerto Rico': 'North America', 'Qatar': 'Asia', 'Romania': 'Europe', 'Russia': 'Europe', 'Rwanda': 'Africa', 'Saint Kitts and Nevis': 'North America',
        'Saint Lucia': 'North America', 'Saint Vincent and the Grenadines': 'North America', 'Samoa': 'Oceania', 'San Marino': 'Europe', 'Sao Tome and Principe': 'Africa',
        'Saudi Arabia': 'Asia', 'Senegal': 'Africa', 'Serbia': 'Europe', 'Seychelles': 'Africa', 'Sierra Leone': 'Africa', 'Singapore': 'Asia',
        'Sint Maarten (Dutch part)': 'North America', 'Slovakia': 'Europe', 'Slovenia': 'Europe', 'Solomon Islands': 'Oceania', 'Somalia': 'Africa',
        'South Africa': 'Africa', 'South Korea': 'Asia', 'Spain': 'Europe', 'Sri Lanka': 'Asia', 'Sudan': 'Africa', 'Suriname': 'South America', 'Sweden': 'Europe',
        'Switzerland': 'Europe', 'Tajikistan': 'Asia', 'Tanzania': 'Africa', 'Thailand': 'Asia', 'Togo': 'Africa', 'Tonga': 'Oceania', 'Trinidad and Tobago': 'North America',
        'Tunisia': 'Africa', 'Turkey': 'Asia', 'Turkmenistan': 'Asia', 'Turks and Caicos Islands': 'North America', 'Tuvalu': 'Oceania', 'Uganda': 'Africa', 'Ukraine': 'Europe',
        'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe', 'United States': 'North America', 'Uruguay': 'South America', 'Uzbekistan': 'Asia', 'Vanuatu': 'Oceania',
        'Vietnam': 'Asia', 'World': 'World', 'Zambia': 'Africa', 'Zimbabwe': 'Africa'
    }

    # Create a new column 'Continent' based on the mapping
    df_column['Continent'] = df_column[x].map(continent_map)

    return df_column
