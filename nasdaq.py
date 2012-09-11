import csv, collections

def max_increase(prices):
	# pretty sure this could be done in O(n), this is O(n^2)
	inc = ({'stock_price_high':0},{'stock_price_low':1})
	incval=0
	for buy in range(len(prices)):
		for sell in range(buy, len(prices)):
			sellprice = float(prices[sell]['stock_price_high'])
			buyprice = float(prices[buy]['stock_price_low'])
			if sellprice - buyprice > incval:
				inc = (prices[sell], prices[buy])
				incval=sellprice-buyprice
	return inc

def main():
	for prefix in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		reader = csv.DictReader(open('data/NASDAQ/NASDAQ_daily_prices_%s.csv' % prefix))
		prices = collections.defaultdict(list)
		for row in reader:
			symbol = row['stock_symbol']
			prices[row['stock_symbol']].append(row)
		print 'Symbol\tBuy Date\tBuy Price\tSell Date\tSell Price\tGain'
		for symbol in sorted(prices.keys()):
			prices[symbol] = sorted(prices[symbol], key=lambda a:a['date'])
			increase = max_increase(prices[symbol])
			gain = float(increase[0]['stock_price_high'])/float(increase[1]['stock_price_low'])
			if gain > 10:
				print '%s\t%s\t%s\t\t%s\t%s\t\t%dx' % (symbol, increase[1]['date'], increase[1]['stock_price_low'], increase[0]['date'], increase[0]['stock_price_high'], gain)

if __name__ == '__main__':
	main()