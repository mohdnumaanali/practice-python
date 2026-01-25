import re

def find_gov_urls(website):
    pattern = r"https://www\.[A-Za-z0-9.-]+\.gov"
    result = re.findall(pattern, website)
    return result

# Test cases
print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!"))  
# ['https://www.data.gov']

print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov."))  
# ['https://www.nps.gov', 'https://www.recreation.gov']

print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!"))  
# ['https://www.loc.gov']

print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!"))  
# [] 
