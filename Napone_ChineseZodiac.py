# Enters the user its birthyear
UserZodiac = str(input("Enter Your Birth Year: "))

# Range of its Zodiac
Rat = {
    "1900", "1912", "1924", "1936", "1948", "1960", "1972", "1984", "1996", "2008", "2020"}
Ox = {
    "1901", "1913", "1925", "1937", "1949", "1961", "1973", "1985", "1997", "2009", "2021"}
Tiger = {
    "1902", "1914", "1926", "1938", "1950", "1962", "1974", "1986", "1998", "2010", "2022"}
Hare = {
    "1903", "1915", "1927", "1939", "1951", "1963", "1975", "1987", "1999", "2011", "2023"}
Dragon = {
    "1904", "1916", "1928", "1940", "1952", "1964", "1976", "1988", "2000", "2012", "2024"}
Snake = {
    "1905", "1917", "1929", "1941", "1953", "1965", "1977", "1989", "2001", "2013", "2025"}   
Horse = {
    "1906", "1918", "1930", "1942", "1954", "1966", "1978", "1990", "2002", "2014", "2026"}
Ram = {
    "1907", "1919", "1931", "1943", "1955", "1967", "1979", "1991", "2003", "2015", "2027"}
Monkey = {
    "1908", "1920", "1932", "1944", "1956", "1968", "1980", "1992", "2004", "2016", "2028"}
Rooster = {
    "1909", "1921", "1933", "1945", "1957", "1969", "1981", "1993", "2005", "2017", "2029"}
Dog = {
    "1910", "1922", "1934", "1946", "1958", "1970", "1982", "1994", "2006", "2018", "2030"}
Pig = {
    "1911", "1923", "1935", "1947", "1959", "1971", "1983", "1995", "2007", "2019", "2031"}

zod = "Your Zodiac Sign is"

if UserZodiac in Rat:
    print(zod, "Rat")
elif UserZodiac in Ox:
    print(zod, "Ox")
elif UserZodiac in Tiger:
    print(zod, "Tiger")
elif UserZodiac in Hare:
    print(zod, "Hare")
elif UserZodiac in Dragon:
    print(zod, "Dragon")
elif UserZodiac in Snake:
    print(zod, "Snake")
elif UserZodiac in Horse:
    print(zod, "Horse")
elif UserZodiac in Ram:
    print(zod, "Ram")
elif UserZodiac in Monkey:
    print(zod, "Monkey")
elif UserZodiac in Rooster:
    print(zod, "Rooster")
elif UserZodiac in Dog:
    print(zod, "Dog")
elif UserZodiac in Pig:
    print(zod, "Pig")
else:
    print("Invalid Year")
    # Jobert Napone Gwapo
