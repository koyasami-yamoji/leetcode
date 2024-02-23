def domain_name(url: str):
	domain = url.replace('http://', '').replace('https://', '').replace('www.', '')
	domain = domain.split('.')
	return domain[0]




print(domain_name('https://youtube.co'))



