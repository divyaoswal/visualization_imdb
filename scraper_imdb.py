import csv
import bs4
import requests


def get_contents(year=2000, page_no=1):
	url = "http://www.imdb.com/search/title"
	payload = {
		'year': year,
		'title_type': 'feature',
		'sort': 'moviemeter',
		'page': page_no,
		'ref_': 'adv_prv'
	}
	data = requests.get(url, params=payload)
	soup = bs4.BeautifulSoup(data.text, "html.parser")
	contents = soup.find_all("div", class_="lister-item-content")
	return contents



def get_country(country_url):
	url = "http://www.imdb.com/"+country_url
	data = requests.get(url)
	soup1 = bs4.BeautifulSoup(data.text, "html.parser")
	country_arr = [val.text for val in soup1.select('a[href*=country_of_origin]')]
	return country_arr


if __name__ == "__main__":

	with open("mojo.csv", "w") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([
			"Movie_Name",
			"Country",
			"Rating",
			"Gross",
			"year"
		])
		for year in range(2000, 2017):
			for page in range(1,3):
				print("page {} year {}".format(page,year))
				contents = get_contents(year, page)
				if not contents:
					break
				for content in contents:
					link = content.find("h3", class_="lister-item-header").find('a')
					countries = get_country(link['href'])
					rating = content.find("div", class_="ratings-bar").find("strong").text
					gross = content.find("p", class_="sort-num_votes-visible")
					gross_value = None
					if("Gross" in gross.text):
						gross_value = gross.text.split("\n")[-2]
					writer.writerow(
						[ link.text, countries, rating, gross_value, year ]
					)





