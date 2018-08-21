def scrape():
    # Import Splinter and BeautifulSoup
    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd
    # Set the executable path and initialize the chrome browser in splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path)
    #print(browser)
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    slide_elem = news_soup.select_one('ul.item_list li.slide')

    slide_elem.find("div", class_='content_title')

    # Use the parent element to find the first a tag and save it as `news_title`
    news_title = slide_elem.find("div", class_='content_title')
    output_news_title = news_title.get_text()

    # Use the parent element to find the paragraph text
    list_text = slide_elem.find("div", class_='list_text')
    title = list_text.find("div", class_='content_title')
    title.get_text()
    teaser = list_text.find("div", class_='article_teaser_body')
    output_news_teaser= teaser.get_text()

    #########################

    #Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    #browser.visit(url)
    import requests
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    results = soup.find_all('div', class_="js-tweet-text-container")
    output_mars_weather = results[0].get_text().strip()


    #########################

    #Mars Fact
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Fields','Data']
    df.head()
    html_table = df.to_html()
    #print(html_table)

    #########################

    #Mars Hemispheres
    import urllib
    import urllib.request
    from bs4 import BeautifulSoup

    def make_soup(url):
        thepage = urllib.request.urlopen(url)
        soupdata = BeautifulSoup(thepage,"html.parser")
        return soupdata

    soup = make_soup("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    results = soup.find_all('a', class_="itemLink product-item")
    hemisphere_image_urls = []
    for result in results:
        title = {}
        title["title"]=result.h3.text.strip()
        hemisphere_image_urls.append(title)

    results=[]
    urls = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",\
            "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",\
        "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",\
        "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]
    for url in urls:
        soup = make_soup(url)
        result = soup.find('img', class_="wide-image")
        results.append("https://astrogeology.usgs.gov"+ result.get('src'))
    results

    counter = 0
    for item in hemisphere_image_urls:
            item["img_url"] = results[counter]
            counter += 1

    output = {}
    output["news_title"]=output_news_title
    output["news_teaser"]=output_news_teaser
    output["mars_weather"]=output_mars_weather
    output["hemisphere_image_urls"]=hemisphere_image_urls
    return(output)