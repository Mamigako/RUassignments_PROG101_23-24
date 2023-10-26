def create_countries_dict(text_file):
    try:
        countries_dict= {}
        documents= open(text_file, "r")
        for line in documents:
            line= line.split(";")
            country= line[2].strip()
            full_name= line[1].split(",")
            first_name= full_name[1].strip()
            last_name= full_name[0].strip()
            name=[first_name, last_name]
            name= " ".join(name)
            rating= float(line[3])
            info= [name, rating]
            value= [info]
            if country not in countries_dict:
                countries_dict.update({country:value})
            else:
                countries_dict[country].append(info)

        return countries_dict
            
    except FileNotFoundError:
        return None


def countries_average_dict(countries_dict):
    countries_average_rate_dict= {}

    for counrty in countries_dict:
        rate_sum= 0.0
        number_of_players= len(countries_dict[counrty])
        
        for info_list in countries_dict[counrty]:
            indvidual_rate= info_list[1]
            rate_sum+= indvidual_rate
        
        average_rate= rate_sum / number_of_players
        value= [number_of_players, average_rate]

        countries_average_rate_dict.update({counrty:value})

    country_number_average_dict= dict(sorted(countries_average_rate_dict.items()))
    return country_number_average_dict


def print_by_country(country_number_average_dict, countries_dict):
    print("Enter filename: Players by country:\n-------------------")
    for country in country_number_average_dict:
        print(f"{country} ({country_number_average_dict[country][0]}) ({round(country_number_average_dict[country][1], 1)}):")
        for info_lis in countries_dict[country]:
            name= info_lis[0]
            rate= int(info_lis[1])
            print("{0:>40}{1:>10}".format(name,rate))


def main():
    text_file= input()
    counrties_dict= create_countries_dict(text_file)

    if counrties_dict != None:
        country_number_average_dict= countries_average_dict(counrties_dict)
        print_by_country(country_number_average_dict, counrties_dict)


if __name__ == "__main__":
    main()
