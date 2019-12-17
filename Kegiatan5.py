def Filter(string, substr): 
    return [str for str in string if
             any(sub in str for sub in substr)] 
      
# Driver code 
string = ['Rangga Infotech', 'Abi Infokom', 'Agung Infokom', 'city2'] 
substr = ['Infokom'] 
print(Filter(string, substr)) 