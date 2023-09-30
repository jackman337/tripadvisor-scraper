# tripadvisor-scraper
Scrape TripAdvisor website for reviews

Scrape reviews from TripAdvisor and output to text file.

User will need to build a remote webdriver (or just use requests library). I chose the remote webdriver using selenium so that I could build out a tool that would eventually be able to interact with websites (click, fill in forms, etc.)

schema is where the personalization comes from. div and span tags may change for different reviewed venues. Was the same for Florida Aquarium and Space Needle though.

<h2>Future Plans</h2>

Initially only wanted review text for a NLP project; however, will want more info on review such as date in order to track sentiment and other language features over time.
