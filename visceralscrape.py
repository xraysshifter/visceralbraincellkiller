import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PIL import Image
import glob
import tkinter as tk
from tkinter import messagebox

bbase_phrases = ""
user_input = ""

def get_input():
	global bbase_phrases
	user_input = entry.get()
	confirm = messagebox.askyesno("Confirmation", "Are you sure you want to proceed?")
	if confirm:
		print("These will be sent to the spider:", user_input)
		bbase_phrases = user_input  # Update the bbase_phrases attribute of the spider instance
		window.destroy()
	else:
		entry.delete(0, tk.END)

custom_font = ("Nimbus", 20, "bold")
window = tk.Tk()
window.title("datasking")
entry = tk.Entry(window, width=20, font=custom_font)

# Create the Entry widget
entry = tk.Entry(window)
button = tk.Button(window, text="send these to the spider", font=custom_font, command=get_input)
entry.pack()
button.pack()

# Start the Tkinter event loop
window.mainloop()

class Visceral(scrapy.Spider):
    name = 'visceral'
    start_urls = ['https://www.google.com/imghp?hl=en&authuser=0&ogbl']

    def parse(self, response):
        base_phrases = bbase_phrases.split(',')
        for base_phrase in base_phrases:
            phrases = [base_phrase, base_phrase + 'pictures', 'photos of ' + base_phrase, base_phrase + 'image', 'image of' + base_phrase]
            for phrase in phrases:
                yield scrapy.FormRequest.from_response(
                    response,
                    formdata={'q': phrase},
                    callback=self.parse_results
                )
            print('s34rch1ng xd haha lol fuck yeah internet')

    def parse_results(self, response):
        image_urls = response.css('img::attr(src)').getall()[:200]
        for url in image_urls:
            yield {'image_urls': [url]}
        print('Images url:', image_urls)




settings = {
    'BOT_NAME': 'my_bot',
    'ROBOTSTXT_OBEY': False,
    'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1},
    'IMAGES_STORE': './img',
}



process = CrawlerProcess(settings)
process.crawl(Visceral)  # Pass the spider instance to the crawl method
process.start()
