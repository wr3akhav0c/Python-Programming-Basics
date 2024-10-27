processor_price = float(input()) * 1.57
price_video_card = float(input()) * 1.57
price_RAM_memory = float(input()) * 1.57

quantity_RAM_memory = int(input())
percent_discount = float(input())

processor_price_discount = processor_price - (processor_price * percent_discount)
price_video_card_discount = price_video_card - (price_video_card * percent_discount)

price_total = processor_price_discount + price_video_card_discount + (price_RAM_memory * quantity_RAM_memory)
print(f"Money needed - {price_total:.2f} leva.")