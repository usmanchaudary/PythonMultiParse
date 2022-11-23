import pandas as pd
import sys
import json
import io
import matplotlib.pyplot as plt

#recieve and read env file 
file_path = sys.argv[1]
print(file_path)
tables = {}
result = {}
plots = {}
#with -> using. opening json file in read mode. 'f' would be range variable 
with open(file_path, 'r') as f:
  input_json = json.load(f)

#convert all tables to dataframes. and save them into tables dictionary.  
for key in input_json:
    #print(key)
    tables[key] = pd.DataFrame(input_json[key])


#you can access the input data like this.
#data = tabless['data'] # it would return the dataframe.



result['data'] = tables['data']   #for demo purpose

#creating charts
plt.bar(tables['data']['Analyte_Concentration__pg_mL_'], tables['data']['Calculated_Concentration__pg_mL_'], color ='maroon',
        width = 0.4)
#plt.show()
f = io.StringIO()
plt.savefig(f, format = "svg")
svg_value = f.getvalue()
plots['data_graph'] = svg_value
#save the resulting data into json as they are dataframe. i am assuming that result dictionary structure would look like this
# {key: dataframe}
for key in result:
    print(key)
    result[key] = result[key].to_json(orient ='records')
    #save it into a filepath. i.e write json file

result_plot = {}
result_plot['tables'] = result
result_plot['plots'] = plots
#arg2 would contain the outputfile
output_file = sys.argv[2]

with open(output_file, "w+") as outfile:  #using w+ mode to create file if it not exists.
        json.dump(result_plot, outfile)

print(result)