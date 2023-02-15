library(jsonlite)
input_json <- fromJSON(readLines("input.json")) #would be coming from argument 1
d <- names(input_json)

for (key in d){
 str <- paste("tryCatch(",key, "<- input_json$",key,",","error = function (e)print(paste('error is: ',e)))",sep = '')
 print(str)
 eval(parse(text = str))
}