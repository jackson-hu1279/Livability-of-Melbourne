import json 

chunk_size = 25000
file_num = 0
more = True

with open('twitter-melb.json', 'r', encoding = 'utf-8') as in_json_file:
    # skip the first line
    line = next(in_json_file)

    while more:
        i = 0
        file_num += 1
        with open('extracted-{0}.json'.format(file_num), 'w', encoding='utf-8') as out_json_file:
            print(file_num)
            print('{"docs": [', file=out_json_file)
            for line in in_json_file:
                i += 1
                # get rid of the comma at the end
                if i == chunk_size:
                    line = line[:-2]  
                    more = True
                    print(line, file=out_json_file)
                    break
                else:
                    more = False  
                print(line, file=out_json_file, end = '')
            
            # only 2.5 million tweets, the last extracted file will be empty 
            print(']}', file=out_json_file)


# with open('extracted.json', encoding='utf-8') as fp:
#     tweets = json.load(fp)
#     print(json.dumps(tweets, indent=True))




