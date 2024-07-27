#create a month conversion dictionary
months = { 
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

print(months["january"]) # prints 1
print(months.get("january")) # prints 1
print(months.get("iwqejhfgwef", "value not found")) # prints value not found

print(months.keys()) # prints all the keys
print(months.values()) # prints all the values
print(months.items())   # prints all the keys and values
